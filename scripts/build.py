#!/usr/bin/env python3
"""Deterministic fail-closed build for the SID living review skeleton."""
import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data'
SCRIPTS_DIR = ROOT / 'scripts'
TEMPLATES_DIR = ROOT / 'templates'
DEFAULT_OUT_DIR = ROOT / 'pack'

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
import validate as schema_validator  # noqa: E402
import verify_sources as source_verifier  # noqa: E402


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_records(records_dir):
    records = {}
    for p in sorted(records_dir.glob('*.yaml')):
        rec = yaml.safe_load(p.read_text(encoding='utf-8'))
        records[rec['id']] = rec
    return records


def apply_proposals(records, adjudications, rules, evidence, metrics, proposals):
    """Apply generic declarative overlays for testing or pre-admission review without paper-specific branches."""
    if not proposals:
        return records, adjudications, rules, evidence, metrics
    records = json.loads(json.dumps(records))
    adjudications = json.loads(json.dumps(adjudications))
    rules = json.loads(json.dumps(rules))
    evidence = json.loads(json.dumps(evidence))
    metrics = json.loads(json.dumps(metrics))

    for rid, patch in (proposals.get('record_patches') or {}).items():
        if rid not in records:
            continue
        rec = records[rid]
        if 'in_table1' in patch:
            rec['in_table1'] = patch['in_table1']
        for lkey, lval in (patch.get('labels') or {}).items():
            if isinstance(lval, dict):
                rec['labels'].setdefault(lkey, {}).update(lval)
            else:
                rec['labels'].setdefault(lkey, {})['value'] = lval

    for eid, epatch in (proposals.get('evidence_patches') or {}).items():
        if eid in evidence:
            evidence[eid].update(epatch)
        else:
            evidence[eid] = epatch

    for mpatch in (proposals.get('metric_patches') or []):
        mid = mpatch.get('id')
        matched = False
        for m in metrics:
            if m.get('id') == mid:
                for k, v in mpatch.items():
                    if k == 'table_binding' and isinstance(v, dict):
                        m.setdefault('table_binding', {}).update(v)
                    else:
                        m[k] = v
                matched = True
        if not matched:
            metrics.append(mpatch)

    if 'rules_patches' in proposals:
        rpatch = proposals['rules_patches']
        if 'constraint_status' in rpatch:
            rules['constraint']['status'] = rpatch['constraint_status']
        if 'registered_crossed_controls' in rpatch:
            rules['constraint']['registered_crossed_controls'] = rpatch['registered_crossed_controls']
        for fb in (rpatch.get('field_bindings_add') or []):
            rules['field_bindings'].append(fb)
        for fb_override in (rpatch.get('field_bindings_replace') or []):
            cid = fb_override.get('claim_id')
            for idx, existing in enumerate(rules['field_bindings']):
                if existing.get('claim_id') == cid:
                    rules['field_bindings'][idx] = fb_override
                    break
            else:
                rules['field_bindings'].append(fb_override)
        for rid, prow_patch in (rpatch.get('problem_rows_patch') or {}).items():
            if prow_patch is None:
                rules['problem_rows'].pop(rid, None)
            else:
                rules['problem_rows'].setdefault(rid, {}).update(prow_patch)
        if 'problem_II_membership_changes' in rpatch:
            rules['questions']['problem-II']['membership_changes'] = rpatch['problem_II_membership_changes']
        if 'problem_II_expected_record_ids' in rpatch:
            rules['questions']['problem-II']['expected_record_ids'] = rpatch['problem_II_expected_record_ids']

    if 'adjudications_replace' in proposals:
        adjudications = proposals['adjudications_replace']
    elif 'adjudications_patch' in proposals:
        for apatch in proposals['adjudications_patch']:
            aid = apatch.get('id')
            for idx, existing in enumerate(adjudications):
                if existing.get('id') == aid:
                    adjudications[idx].update(apatch)
                    break
            else:
                adjudications.append(apatch)

    return records, adjudications, rules, evidence, metrics


def check_renderer_lint(records):
    """Ensure zero paper IDs or method names appear as string literals in build.py."""
    source_code = Path(__file__).read_text(encoding='utf-8')
    tree = ast.parse(source_code)
    forbidden_ids = {rid for rid in records}
    forbidden_names = {rec.get('name', '') for rec in records.values() if rec.get('name')}
    violations = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            val = node.value.strip()
            if val in forbidden_ids or val in forbidden_names:
                violations.append({'lineno': getattr(node, 'lineno', 0), 'literal': val})
    return {
        'gate': 'renderer_lint_check',
        'ok': len(violations) == 0,
        'errors': [
            f"E_RENDERER_HARDCODED_ID: string literal '{v['literal']}' at line {v['lineno']}"
            for v in violations
        ],
    }


def check_schema(records):
    schema = json.loads((ROOT / 'schema' / 'paper.schema.json').read_text(encoding='utf-8'))
    vocab = yaml.safe_load((DATA_DIR / 'vocab.yaml').read_text(encoding='utf-8'))
    allowed = {field: {e['value'] for e in entries} for field, entries in vocab.items()}
    errors = []
    for rid, rec in sorted(records.items()):
        for cat, loc, msg in schema_validator.schema_errors(rec, schema, schema, '$'):
            errors.append(f'{rid} [{cat}] {loc}: {msg}')
        for cat, loc, msg in schema_validator.record_errors(rec, rid, allowed):
            errors.append(f'{rid} [{cat}] {loc}: {msg}')
    return {
        'gate': 'schema_check',
        'ok': len(errors) == 0,
        'record_count': len(records),
        'errors': [f'E_SCHEMA: {e}' for e in errors],
    }


def check_adjudications(records, adjudications):
    errors = []
    for adj in adjudications:
        aid = adj.get('id', '<unknown>')
        rid = adj.get('record_id')
        status = adj.get('status')
        sub = adj.get('submitted_by')
        rev = adj.get('reviewed_by')
        if status in ('accepted', 'adjudicated'):
            if not sub or not rev or sub == rev:
                errors.append(
                    f'E_UNREVIEWED_ADJUDICATION: {aid} ({rid}) requires independent submitted_by != reviewed_by'
                )
            if rid not in records:
                errors.append(f'E_ADJUDICATION_MISSING_RECORD: {aid} references missing record {rid}')
                continue
            rec = records[rid]
            for fkey, expected_val in (adj.get('accepted') or {}).items():
                lkey = 'tokenizer' if fkey == 'tokenizer_training' else fkey
                actual_val = rec.get('in_table1') if lkey == 'in_table1' else rec['labels'][lkey]['value']
                if actual_val != expected_val:
                    errors.append(
                        f'E_KNOWN_FACT: record {rid}.{lkey}={actual_val!r} contradicts accepted adjudication '
                        f'{aid} ({expected_val!r})'
                    )
    return {
        'gate': 'adjudication_consistency_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def check_evidence(evidence, source_verification, evidence_bytes):
    errors = []
    if source_verification.get('evidence_sha256') != digest(evidence_bytes):
        errors.append('E_EVIDENCE_RECEIPT_STALE: source-verification.json evidence_sha256 does not match evidence.json')
    anchor_map = {c['id']: c for c in source_verification.get('checks', [])}
    for eid in sorted(evidence):
        c = anchor_map.get(eid)
        if not c or not c.get('ok'):
            errors.append(f'E_SOURCE_ANCHOR_FAILED: evidence anchor {eid} failed source verification')
    return {
        'gate': 'evidence_check',
        'ok': len(errors) == 0,
        'passed': source_verification.get('passed', 0),
        'total': source_verification.get('total', 0),
        'errors': errors,
    }


def check_subject_and_field_bindings(records, rules, evidence, source_verification):
    errors = []
    anchor_map = {c['id']: c for c in source_verification.get('checks', [])}
    for fb in rules.get('field_bindings', []):
        cid = fb.get('claim_id', '<unnamed>')
        rid = fb.get('record_id')
        field = fb.get('field')
        expected_val = fb.get('value')
        ev_id = fb.get('evidence_id')
        sub = fb.get('submitted_by')
        rev = fb.get('reviewed_by')
        if not sub or not rev or sub == rev:
            errors.append(f'E_UNREVIEWED_BINDING: {cid} requires independent submitted_by != reviewed_by')
        if rid not in records:
            errors.append(f'E_BINDING_MISSING_RECORD: {cid} references unknown record {rid}')
            continue
        rec = records[rid]
        actual_val = rec.get('in_table1') if field == 'in_table1' else rec['labels'][field]['value']
        if actual_val != expected_val:
            errors.append(
                f'E_KNOWN_FACT: record {rid}.{field}={actual_val!r} does not match bound value {expected_val!r} ({cid})'
            )
        ev = evidence.get(ev_id)
        if not ev:
            errors.append(f'E_MISSING_EVIDENCE: {cid} references unknown evidence_id {ev_id}')
            continue
        if ev.get('record_id') != rid:
            errors.append(
                f'E_SUBJECT_BINDING: {cid} binds record {rid} to evidence {ev_id} owned by {ev.get("record_id")!r}'
            )
        if ev.get('subject') != 'method':
            errors.append(
                f'E_SUBJECT_BINDING: {cid} binds {rid}.{field} to non-method evidence {ev_id} (subject={ev.get("subject")!r})'
            )
        if ev_id in (fb.get('negative_evidence_ids') or []):
            errors.append(
                f'E_SUBJECT_BINDING: {cid} binds {rid}.{field} to negative baseline evidence {ev_id}'
            )
        anchor = anchor_map.get(ev_id, {})
        heur = anchor.get('subject_heuristics') or {}
        if heur.get('needs_subject_review') and not fb.get('subject_review_override_approved'):
            errors.append(
                f'E_SUBJECT_REVIEW_REQUIRED: {cid} ({rid}.{field}) cites {ev_id} inside a baseline/comparison '
                f'section or competing-method sentence (section_path={anchor.get("section_path")}, '
                f'competing_subject={heur.get("competing_sentence_subject")!r})'
            )
    return {
        'gate': 'subject_and_field_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def check_metrics(metrics, rules, evidence, source_verification):
    errors = []
    vocab = rules.get('protocol_vocab') or {}
    header_tokens_map = vocab.get('dataset_header_tokens') or {}
    anchor_map = {c['id']: c for c in source_verification.get('checks', [])}

    for m in metrics:
        mid = m.get('id', '<unnamed-metric>')
        for pfield in ('dataset', 'split', 'level', 'resolver', 'metric'):
            val = m.get(pfield)
            allowed = vocab.get(pfield) or []
            if val not in allowed:
                errors.append(f'E_PROTOCOL_VOCAB: {mid}.{pfield}={val!r} not in controlled vocab {allowed}')
        sub = m.get('submitted_by')
        rev = m.get('reviewed_by')
        if not sub or not rev or sub == rev:
            errors.append(f'E_UNREVIEWED_METRIC: {mid} requires independent submitted_by != reviewed_by')

        tb = m.get('table_binding')
        if not isinstance(tb, dict):
            errors.append(f'E_METRIC_CELL_MISMATCH: {mid} is missing table_binding')
            continue

        res = source_verifier.verify_table_binding(m, evidence, anchor_map)
        if not res['ok']:
            failed_keys = [k for k, v in res['checks'].items() if not v]
            errors.append(
                f'E_METRIC_CELL_MISMATCH: {mid} failed table cell verification {failed_keys} '
                f'(expected cell={res["expected_cell_text"]!r} at row={res["row_label"]!r}, '
                f'col={res["column_path"]!r}; observed cell={res["observed_cell_text"]!r}, '
                f'observed header={res["observed_header_path"]!r})'
            )

        ds = m.get('dataset')
        expected_tokens = header_tokens_map.get(ds) or []
        col_path = tb.get('column_path') or []
        if expected_tokens and not any(tok in col_path for tok in expected_tokens):
            errors.append(
                f'E_METRIC_CELL_MISMATCH: {mid} dataset={ds!r} does not match table column_path={col_path!r}'
            )

    return {
        'gate': 'metric_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def query_problem_ii(records):
    return sorted(
        [
            rec for rec in records.values()
            if rec.get('in_table1') is True and rec['labels']['problem']['value'] == 'II'
        ],
        key=lambda r: r['id'],
    )


def check_query_membership_and_rows(records, rules, evidence):
    errors = []
    qspec = rules['questions']['problem-II']
    expected_ids = set(qspec.get('expected_record_ids') or [])
    matched_records = query_problem_ii(records)
    actual_ids = {r['id'] for r in matched_records}

    changes = qspec.get('membership_changes') or []
    reviewed_adds = {}
    reviewed_removals = {}
    for ch in changes:
        rid = ch.get('record_id')
        act = ch.get('action')
        sub = ch.get('submitted_by')
        rev = ch.get('reviewed_by')
        reason = ch.get('reason')
        if rid and act in ('add', 'remove') and reason and sub and rev and sub != rev:
            if act == 'add':
                reviewed_adds[rid] = ch
            else:
                reviewed_removals[rid] = ch
        else:
            errors.append(f'E_INVALID_MEMBERSHIP_CHANGE: malformed or unreviewed membership_change {ch}')

    added_ids = sorted(actual_ids - expected_ids)
    removed_ids = sorted(expected_ids - actual_ids)

    for rid in added_ids:
        if rid not in reviewed_adds:
            errors.append(
                f'E_UNREVIEWED_ROW: record {rid} entered problem-II query without reviewed membership_changes entry'
            )
    for rid in removed_ids:
        if rid not in reviewed_removals:
            errors.append(
                f'E_UNREVIEWED_REMOVAL: record {rid} disappeared from problem-II query without reviewed '
                f'membership_changes removal entry'
            )

    problem_rows = rules.get('problem_rows') or {}
    for rec in matched_records:
        rid = rec['id']
        row = problem_rows.get(rid)
        if not row:
            errors.append(f'E_UNREVIEWED_ROW: record {rid} is in problem-II query but has no reviewed problem_rows entry')
            continue
        sub = row.get('submitted_by')
        rev = row.get('reviewed_by')
        if not sub or not rev or sub == rev:
            errors.append(f'E_UNREVIEWED_ROW: problem_rows[{rid}] requires independent submitted_by != reviewed_by')
        ev_id = row.get('evidence_id')
        if not ev_id or ev_id not in evidence:
            errors.append(f'E_UNREVIEWED_ROW: problem_rows[{rid}] is missing valid evidence_id')
        actual_stage = rec['labels']['stage']['value']
        expected_stage = row.get('expected_stage')
        if actual_stage != expected_stage:
            srev = row.get('stage_change_review') or {}
            if (
                srev.get('new_stage') != actual_stage
                or not srev.get('reason')
                or not srev.get('submitted_by')
                or not srev.get('reviewed_by')
                or srev.get('submitted_by') == srev.get('reviewed_by')
            ):
                errors.append(
                    f'E_UNREVIEWED_STAGE_CHANGE: record {rid} stage changed from {expected_stage!r} to '
                    f'{actual_stage!r} without reviewed stage_change_review in problem_rows[{rid}]'
                )

    return {
        'gate': 'query_membership_and_row_check',
        'ok': len(errors) == 0,
        'matched_count': len(matched_records),
        'added_ids': added_ids,
        'removed_ids': removed_ids,
        'reviewed_removals': [reviewed_removals[rid] for rid in removed_ids if rid in reviewed_removals],
        'reviewed_adds': [reviewed_adds[rid] for rid in added_ids if rid in reviewed_adds],
        'errors': errors,
    }


def check_constraint(rules, evidence):
    errors = []
    c = rules.get('constraint') or {}
    status = c.get('status')
    req_spec = c.get('upgrade_requirements_spec') or {}
    req_controls = set(req_spec.get('required_controls') or [])
    controls = c.get('registered_crossed_controls') or []

    if status != 'Open':
        valid_controls = []
        for ctrl in controls:
            sub = ctrl.get('submitted_by')
            rev = ctrl.get('reviewed_by')
            ev_id = ctrl.get('evidence_id')
            satisfied = set(ctrl.get('controls_satisfied') or [])
            if (
                ctrl.get('design') == req_spec.get('required_design')
                and req_controls.issubset(satisfied)
                and ev_id in evidence
                and sub and rev and sub != rev
            ):
                valid_controls.append(ctrl)
        if not valid_controls:
            errors.append(
                f'E_GRADE_UPGRADE: constraint-1 status cannot be upgraded from Open to {status!r} '
                f'without a reviewed 2x2 crossed-control entry satisfying {sorted(req_controls)}'
            )

    for obs in c.get('observations', []):
        for ev_id in obs.get('evidence', []):
            if ev_id not in evidence:
                errors.append(f'E_MISSING_EVIDENCE: constraint observation {obs.get("id")} references {ev_id}')

    return {
        'gate': 'constraint_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def group_metrics_by_protocol(metrics):
    """Group metrics only when dataset, split, level, metric, unit, and known/not_applicable resolver match."""
    comparable_groups = {}
    isolated = []
    for m in metrics:
        resolver = m.get('resolver')
        if resolver in (None, '', 'unknown'):
            isolated.append({
                'metric_id': m['id'],
                'record_id': m['record_id'],
                'method_variant': m['method_variant'],
                'metric': m['metric'],
                'value': m['value'],
                'unit': m['unit'],
                'dataset': m['dataset'],
                'split': m['split'],
                'level': m['level'],
                'resolver': resolver,
                'table_binding': m['table_binding'],
                'reason_not_grouped': 'resolver is unknown (post-collision item resolution protocol unspecified)',
            })
            continue
        key = (m['dataset'], m['split'], m['level'], resolver, m['metric'], m['unit'])
        comparable_groups.setdefault(key, []).append(m)

    grouped_list = []
    for key, items in sorted(comparable_groups.items()):
        ds, split, level, resolver, mname, unit = key
        grouped_list.append({
            'protocol_key': {
                'dataset': ds,
                'split': split,
                'level': level,
                'resolver': resolver,
                'metric': mname,
                'unit': unit,
            },
            'comparable': True,
            'rows': [
                {
                    'metric_id': x['id'],
                    'record_id': x['record_id'],
                    'method_variant': x['method_variant'],
                    'value': x['value'],
                    'unit': x['unit'],
                    'cell_text': x['table_binding']['cell_text'],
                    'table_id': x['table_binding']['table_id'],
                    'table_element_id': x['table_binding']['table_element_id'],
                    'row_label': x['table_binding']['row_label'],
                    'column_path': x['table_binding']['column_path'],
                    'source_version': x['table_binding']['source_version'],
                }
                for x in items
            ],
        })
    return grouped_list, isolated


def compute_stage_distribution(records_list):
    counts = Counter(r['labels']['stage']['value'] for r in records_list)
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    summary_zh = '、'.join(f'{stage} {cnt} 篇' for stage, cnt in ordered)
    return dict(ordered), summary_zh


def build_answer_pack(records, adjudications, rules, evidence, metrics, gates, query_gate, requested_question=None):
    all_records = sorted(records.values(), key=lambda r: r['id'])
    table1_records = [r for r in all_records if r.get('in_table1') is True]
    prob2_records = query_problem_ii(records)
    stage_dist, stage_summary_zh = compute_stage_distribution(prob2_records)
    comparable_groups, isolated_metrics = group_metrics_by_protocol(metrics)
    poi_ids = {
        a['record_id']
        for a in adjudications
        if a.get('domain') == 'POI' and a.get('status') in ('accepted', 'adjudicated')
    }
    poi_in_prob2 = [r['id'] for r in prob2_records if r['id'] in poi_ids or r.get('domain') == 'POI']

    active_rules = []
    for dr in rules.get('decision_rules', []):
        trig = dr.get('trigger')
        if trig == 'any_poi_in_problem_II' and not poi_in_prob2:
            continue
        active_rules.append(dr)

    problem_ii_rows = []
    for rec in prob2_records:
        rid = rec['id']
        prow = rules['problem_rows'][rid]
        ev_id = prow['evidence_id']
        ev = evidence[ev_id]
        dom = 'POI' if (rid in poi_ids or rec.get('domain') == 'POI') else 'General'
        problem_ii_rows.append({
            'record_id': rid,
            'name': rec['name'],
            'citation': rec['citation'],
            'domain': dom,
            'stage': rec['labels']['stage']['value'],
            'tokenization': rec['labels']['tokenization']['value'],
            'inference': rec['labels']['inference']['value'],
            'subproblem': prow['subproblem'],
            'mechanism': prow['mechanism'],
            'grade': prow['grade'],
            'evidence_id': ev_id,
            'source_version': ev['version'],
            'element_id': ev['element_id'],
            'quote': ev['quote'],
        })

    supported_qids = list(rules.get('question_ids') or [])
    question_lookup_status = 'ok'
    if requested_question and requested_question not in supported_qids:
        question_lookup_status = 'unsupported_question'

    return {
        'schema_version': rules.get('schema_version', '2.0'),
        'status': question_lookup_status,
        'requested_question': requested_question,
        'supported_questions': supported_qids,
        'coverage': {
            'total_records': len(all_records),
            'table1_records': len(table1_records),
            'problem_II_records': len(prob2_records),
            'poi_records_total': sum(1 for r in all_records if r['id'] in poi_ids or r.get('domain') == 'POI'),
            'poi_records_in_problem_II': len(poi_in_prob2),
            'problem_II_stage_distribution': stage_dist,
            'problem_II_stage_summary_zh': stage_summary_zh,
            'added_records_with_reason': query_gate.get('reviewed_adds', []),
            'removed_records_with_reason': query_gate.get('reviewed_removals', []),
        },
        'gates': gates,
        'questions': {
            'problem-II': {
                'id': 'problem-II',
                'title': rules['questions']['problem-II']['title'],
                'count': len(prob2_records),
                'stage_distribution': stage_dist,
                'stage_summary_zh': stage_summary_zh,
                'rows': problem_ii_rows,
                'scope_boundary_notes': rules['questions']['problem-II'].get('scope_boundary_notes', []),
                'added_records_with_reason': query_gate.get('reviewed_adds', []),
                'removed_records_with_reason': query_gate.get('reviewed_removals', []),
            },
            'constraint-1': rules['constraint'],
            'trie-collisions': {
                'id': 'trie-collisions',
                'title': rules['questions']['trie-collisions']['title'],
                'decision_rules': active_rules,
                'comparable_metric_groups': comparable_groups,
                'non_comparable_metrics': isolated_metrics,
            },
        },
        'adjudications_count': len(adjudications),
        'field_bindings': {
            fb['claim_id']: {
                'record_id': fb['record_id'],
                'field': fb['field'],
                'value': fb['value'],
                'evidence_id': fb['evidence_id'],
                'review_state': fb.get('review_state', 'reviewed'),
            }
            for fb in rules.get('field_bindings', [])
        },
    }


def render_pages(pack, evidence):
    cov = pack['coverage']
    p2 = pack['questions']['problem-II']
    c1 = pack['questions']['constraint-1']
    tc = pack['questions']['trie-collisions']

    readme_lines = [
        '# SID 生成式推荐：确定性核验骨架（Living Review Skeleton）',
        '',
        '## 覆盖回执（Coverage Receipt）',
        f'- 仓库有效记录总数：`{cov["total_records"]}` 篇（其中 `in_table1: true` 共 `{cov["table1_records"]}` 篇，POI 领域共 `{cov["poi_records_total"]}` 篇）',
        f'- Problem II 主表收录：`{cov["problem_II_records"]}` 篇（阶段分布：`{cov["problem_II_stage_summary_zh"]}`；含 POI 论文 `{cov["poi_records_in_problem_II"]}` 篇）',
        f'- 裁决档案条目数：`{pack["adjudications_count"]}` 条（全部通过 `submitted_by != reviewed_by` 独立复核与字段一致性校验）',
        '',
        '## 核心页面与机器可读产物',
        '- [Problem II：静态码本崩塌与前缀碰撞](problem-II.md)',
        '- [牵制 1：码位依赖 ↔ 生成因子分解](constraint-1.md)',
        '- [回答页：Trie 能消除出词表 ID，但不能消除同码碰撞](answer-trie-collisions.md)',
        '- [answer-pack.json](answer-pack.json)：供检索与智能体消费的结构化答案包',
        '- [effective-records.jsonl](effective-records.jsonl)：全量有效论文记录快照',
    ]

    p2_lines = [
        f'# {p2["title"]}',
        '',
        f'当前 `problem: II` 且 `in_table1: true` 共 **{p2["count"]}** 篇（阶段分布：**{p2["stage_summary_zh"]}**）。',
        '',
        '| 方法 | 引文 | 领域 | 阶段 | 分词器 | 推理约束 | 子问题 | 核心机制 | 证据等级 | 原文锚点 |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |',
    ]
    for r in p2['rows']:
        dom = r['domain'] or 'General'
        p2_lines.append(
            f'| `{r["name"]}` (`{r["record_id"]}`) | {r["citation"]} | {dom} | {r["stage"]} | '
            f'`{r["tokenization"]}` | `{r["inference"]}` | {r["subproblem"]} | {r["mechanism"]} | '
            f'{r["grade"]} | `{r["source_version"]}#{r["element_id"]}` |'
        )
    if p2['removed_records_with_reason']:
        p2_lines.extend(['', '## 已复核移出记录（Reviewed Removals）'])
        for rm in p2['removed_records_with_reason']:
            p2_lines.append(
                f'- `{rm["record_id"]}`：{rm["reason"]}（提交：`{rm["submitted_by"]}`，复核：`{rm["reviewed_by"]}`）'
            )
    if p2['scope_boundary_notes']:
        p2_lines.extend(['', '## 范围边界说明（Scope Boundary Notes）'])
        for note in p2['scope_boundary_notes']:
            p2_lines.append(f'- `{note["record_id"]}`：{note["reason"]}（裁决日期：`{note["date"]}`）')

    c1_lines = [
        f'# 牵制 1：{c1["title"]}（总状态：`{c1["status"]}`）',
        '',
        f'- **核心命题**：{c1["claim"]}',
        f'- **分层状态说明**：{c1["status_source"]["summary"]}',
        f'- **维持 `{c1["status"]}` 的原因**：{c1["why_open"]}',
        f'- **升级门禁条件**：{c1["upgrade_requirement"]}',
        '',
        '## 已核验单侧与局部证据（Reported Observations）',
        '| 编号 | 来源 | 机制方向 | 等级 | 原文元素锚点 | 摘要 |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for obs in c1['observations']:
        src_label = f'`{obs["record_id"]}`' if obs.get('record_id') else obs.get('external_paper', 'external')
        ev_locs = ', '.join(
            f'`{evidence[eid]["version"]}#{evidence[eid]["element_id"]}`'
            for eid in obs['evidence']
        )
        c1_lines.append(
            f'| `{obs["id"]}` | {src_label} | {obs["direction"]} | `{obs["grade"]}` | {ev_locs} | {obs["summary"]} |'
        )

    tc_lines = [
        f'# {tc["title"]}',
        '',
        '## 条件化决策规则（Decision Rules）',
        '| 规则 ID | 适用条件 | 处置建议 | 证据等级 | 原文锚点 | 边界说明 |',
        '| --- | --- | --- | --- | --- | --- |',
    ]
    for dr in tc['decision_rules']:
        ev_str = ', '.join(
            f'`{evidence[eid]["version"]}#{evidence[eid]["element_id"]}`'
            for eid in dr.get('evidence', [])
        ) or '无（纯流水线接口推断）'
        tc_lines.append(
            f'| `{dr["id"]}` | {dr["condition"]} | {dr["claim"]} | `{dr["grade"]}` | {ev_str} | {dr["boundary_note"]} |'
        )

    tc_lines.extend(['', '## 协议对齐的同桶可比指标（Comparable Metric Groups）'])
    for grp in tc['comparable_metric_groups']:
        pk = grp['protocol_key']
        tc_lines.extend([
            '',
            f'### 协议桶：`dataset={pk["dataset"]}, split={pk["split"]}, level={pk["level"]}, '
            f'resolver={pk["resolver"]}, metric={pk["metric"]}`',
            '| 记录 | 变体 | 数值 | 原文单元格 | 表格坐标 | 原文版本 |',
            '| --- | --- | --- | --- | --- | --- |',
        ])
        for row in grp['rows']:
            col_str = ' / '.join(row['column_path'])
            tc_lines.append(
                f'| `{row["record_id"]}` | `{row["method_variant"]}` | `{row["value"]}{row["unit"]}` | '
                f'`{row["cell_text"]}` | `{row["table_id"]} ({row["table_element_id"]}) [{row["row_label"]}, {col_str}]` | '
                f'`{row["source_version"]}` |'
            )

    tc_lines.extend([
        '',
        '## 协议不完备或不可混排的独立指标（Isolated Non-Comparable Metrics）',
        '| 记录 | 变体 | 指标与数值 | 协议五元组 | 原文单元格与坐标 | 禁止混排原因 |',
        '| --- | --- | --- | --- | --- | --- |',
    ])
    for m in tc['non_comparable_metrics']:
        tb = m['table_binding']
        col_str = ' / '.join(tb['column_path'])
        proto_str = f'ds={m["dataset"]}, split={m["split"]}, level={m["level"]}, resolver={m["resolver"]}'
        tc_lines.append(
            f'| `{m["record_id"]}` | `{m["method_variant"]}` | `{m["metric"]}={m["value"]} ({m["unit"]})` | '
            f'`{proto_str}` | `{tb["cell_text"]}` (`{tb["table_id"]} #{tb["table_element_id"]} [{tb["row_label"]}, {col_str}]`) | '
            f'{m["reason_not_grouped"]} |'
        )

    return {
        'README.md': '\n'.join(readme_lines) + '\n',
        'problem-II.md': '\n'.join(p2_lines) + '\n',
        'constraint-1.md': '\n'.join(c1_lines) + '\n',
        'answer-trie-collisions.md': '\n'.join(tc_lines) + '\n',
    }


def format_label_val(val):
    if isinstance(val, list):
        return ' / '.join(str(v) for v in val)
    return str(val)


def github_slug(heading_text):
    slug = heading_text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug.strip())
    return slug


def record_primary_url(rec, repo_base_url):
    ext = rec.get('external') or {}
    if ext.get('arxiv'):
        return f"https://arxiv.org/abs/{ext['arxiv']}"
    if ext.get('doi'):
        return f"https://doi.org/{ext['doi']}"
    if ext.get('url'):
        return ext['url']
    return f"{repo_base_url}/data/papers/{rec['id']}.yaml"


def render_awesome_readme(pack, records, evidence, spec=None):
    """Deterministically generate an awesome-lint compliant README from structured records."""
    spec = spec or json.loads((TEMPLATES_DIR / 'readme-spec.json').read_text(encoding='utf-8'))
    title = spec['title']
    badge_img = spec['badge_image']
    badge_link = spec['badge_link']
    tagline = spec['tagline']
    repo_base = spec['repository_base_url'].rstrip('/')

    sections = spec['sections']
    lines = [
        f'# {title} [![Awesome]({badge_img})]({badge_link})',
        '',
        tagline,
        '',
        '## Contents',
        '',
    ]
    for sec in sections:
        lines.append(f"- [{sec['heading']}](#{github_slug(sec['heading'])})")

    seen_urls = set()
    table1_recs = sorted(
        [r for r in records.values() if r.get('in_table1') is True],
        key=lambda r: ((r.get('external') or {}).get('year') or 0, r['id']),
    )

    for sec in sections:
        lines.extend(['', f"## {sec['heading']}", ''])
        if 'filter_record_type' in sec:
            matched = [r for r in table1_recs if r.get('record_type') == sec['filter_record_type']]
        else:
            prob = sec['filter_problem']
            matched = [
                r for r in table1_recs
                if r.get('record_type') == 'method' and r['labels']['problem']['value'] == prob
            ]
        for rec in matched:
            rid = rec['id']
            name = rec['name']
            url = record_primary_url(rec, repo_base)
            if url in seen_urls:
                url = f'{url}#record-{rid}'
            seen_urls.add(url)
            stage = format_label_val(rec['labels']['stage']['value'])
            tok = format_label_val(rec['labels']['tokenization']['value'])
            bb = format_label_val(rec['labels']['backbone']['value'])
            obj = format_label_val(rec['labels']['objective']['value'])
            venue = (rec.get('external') or {}).get('venue') or rec.get('citation', '')
            if rec.get('record_type') == 'paradigm-system-benchmark':
                desc = (
                    f'Paradigm, system, or benchmark entry ({venue}) using `{tok}` tokenization '
                    f'and `{bb}` backbone with `{obj}` objective.'
                )
            else:
                desc = (
                    f'Addresses Problem {rec["labels"]["problem"]["value"]} at the {stage} stage ({venue}) '
                    f'via `{tok}` tokenization, `{bb}` backbone, and `{obj}` objective.'
                )
            lines.append(f'- [{name}]({url}) - {desc}')

    lines.extend([
        '',
        '## Contributing',
        '',
        f'Contributions follow the deterministic verification gates in [contributing.md]({repo_base}/schema/README.md).',
    ])
    return '\n'.join(lines) + '\n'


def check_awesome_readme_contract(readme_text):
    """Validate local awesome-lint structural rules on the generated awesome README."""
    errors = []
    lines = readme_text.splitlines()
    if not lines or not re.match(
        r'^# [A-Z][^\n]+ \[!\[Awesome\]\(https://awesome\.re/badge(?:-flat2?)?\.svg\)\]'
        r'\((?:https://awesome\.re|https://github\.com/sindresorhus/awesome)\)$',
        lines[0],
    ):
        errors.append('E_AWESOME_LINT: first line must be H1 Title Case with canonical Awesome badge')

    h1_count = sum(1 for ln in lines if ln.startswith('# '))
    if h1_count != 1:
        errors.append(f'E_AWESOME_LINT: expected exactly 1 H1 heading, found {h1_count}')

    h2_headings = [ln[3:].strip() for ln in lines if ln.startswith('## ')]
    if not h2_headings or h2_headings[0] != 'Contents':
        errors.append('E_AWESOME_LINT: first H2 section must be Contents')

    for h2 in h2_headings:
        if h2.lower() in ('license', 'licence'):
            errors.append('E_AWESOME_LINT: forbidden License section in README')

    item_re = re.compile(r'^- \[([^\]]+)\]\(([^)]+)\) - (.+)$')
    seen_main_urls = set()
    in_contents = False
    for idx, ln in enumerate(lines, 1):
        if ln.startswith('## '):
            in_contents = (ln.strip() == '## Contents')
            continue
        if in_contents or not ln.startswith('- '):
            continue
        m = item_re.match(ln)
        if not m:
            errors.append(f'E_AWESOME_LINT: line {idx} violates `- [Name](url) - Description.` format')
            continue
        name, url, desc = m.group(1), m.group(2), m.group(3)
        if not url.startswith('https://'):
            errors.append(f'E_AWESOME_LINT: line {idx} main link must be an absolute https:// URL ({url!r})')
        if url in seen_main_urls:
            errors.append(f'E_AWESOME_LINT: duplicate main link URL {url!r} at line {idx}')
        seen_main_urls.add(url)
        if not desc[0].isupper():
            errors.append(f'E_AWESOME_LINT: line {idx} description must start with uppercase character')
        if not desc.endswith('.'):
            errors.append(f'E_AWESOME_LINT: line {idx} description must end with a period')
        if desc.lower().startswith(name.lower()):
            after = desc[len(name):]
            if not after or re.match(r'^[\s.,!?:-]', after):
                errors.append(f'E_AWESOME_LINT: line {idx} description repeats item name {name!r}')

    return {
        'gate': 'awesome_readme_interface_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def render_paper_page_skeleton(record, evidence, metrics, all_records=None, rules=None, narrative_blocks=None):
    """Render an Annotated Deep Learning Papers (labml.ai) style single-paper page from structured records."""
    tmpl = (TEMPLATES_DIR / 'paper-page.md.tmpl').read_text(encoding='utf-8')
    rid = record['id']
    narrative_blocks = narrative_blocks or {}
    all_records = all_records or {rid: record}
    rules = rules or {}

    labels = record.get('labels') or {}
    tax_lines = [
        '## 1. Problem and Stage Positioning',
        '',
        '| Field | Value | Status | Source Location | Note |',
        '| --- | --- | --- | --- | --- |',
    ]
    for fkey in ('problem', 'stage', 'representation', 'tokenization', 'backbone', 'tokenizer', 'objective', 'inference'):
        cell = labels.get(fkey) or {}
        val = format_label_val(cell.get('value', '–'))
        if cell.get('inferred'):
            val = f'{val} (inferred)'
        status = cell.get('status', 'unverified')
        src = cell.get('source', 'missing')
        note = (cell.get('note') or '–').replace('|', '\\|')
        tax_lines.append(f'| `{fkey}` | `{val}` | `{status}` | `{src}` | {note} |')

    rec_ev = [
        (eid, ev) for eid, ev in sorted(evidence.items())
        if ev.get('record_id') == rid and ev.get('subject') == 'method'
    ]
    ev_lines = [
        '| Evidence ID | Pinned Version | HTML Element | Verbatim Quote | Quote SHA256 |',
        '| --- | --- | --- | --- | --- |',
    ]
    if rec_ev:
        for eid, ev in rec_ev:
            q = ev['quote'].replace('|', '\\|')
            ev_lines.append(
                f'| `{eid}` | `{ev["version"]}` | `{ev["element_id"]}` | "{q}" | `{ev["quote_sha256"][:16]}...` |'
            )
    else:
        ev_lines.append('| `none-pinned-yet` | `–` | `–` | Label positions recorded in Section 1; sentence anchor pending Stage 2. | `–` |')

    rec_metrics = [m for m in metrics if m.get('record_id') == rid]
    comp_groups, isolated = group_metrics_by_protocol(rec_metrics)
    res_lines = []
    if comp_groups:
        res_lines.extend([
            '### Comparable Protocol-Aligned Metrics',
            '',
            '| Variant | Dataset / Split / Level / Resolver | Metric | Value | Table Cell Coordinate | Source Version |',
            '| --- | --- | --- | --- | --- | --- |',
        ])
        for grp in comp_groups:
            pk = grp['protocol_key']
            pstr = f'{pk["dataset"]} / {pk["split"]} / {pk["level"]} / {pk["resolver"]}'
            for row in grp['rows']:
                cstr = ' / '.join(row['column_path'])
                res_lines.append(
                    f'| `{row["method_variant"]}` | `{pstr}` | `{pk["metric"]}` | `{row["value"]}{row["unit"]}` | '
                    f'`{row["table_id"]} #{row["table_element_id"]} [{row["row_label"]}, {cstr}]` | `{row["source_version"]}` |'
                )
    if isolated:
        if res_lines:
            res_lines.append('')
        res_lines.extend([
            '### Isolated Non-Comparable Metrics (Incomplete Protocol)',
            '',
            '| Variant | Metric | Value | Protocol Tuple | Isolation Reason |',
            '| --- | --- | --- | --- | --- |',
        ])
        for m in isolated:
            pstr = f'ds={m["dataset"]}, split={m["split"]}, level={m["level"]}, resolver={m["resolver"]}'
            res_lines.append(
                f'| `{m["method_variant"]}` | `{m["metric"]}` | `{m["value"]}{m["unit"]}` | `{pstr}` | {m["reason_not_grouped"]} |'
            )
    if not res_lines:
        res_lines.append('No table-bound numeric metrics registered for this record yet; protocol comparison pending.')

    prob_val = (labels.get('problem') or {}).get('value')
    stage_val = (labels.get('stage') or {}).get('value')
    peers = sorted(
        r['id'] for r in all_records.values()
        if r['id'] != rid
        and r.get('in_table1') is True
        and (r.get('labels', {}).get('problem') or {}).get('value') == prob_val
        and (r.get('labels', {}).get('stage') or {}).get('value') == stage_val
    )
    c1_obs = [
        obs['id'] for obs in (rules.get('constraint') or {}).get('observations', [])
        if obs.get('record_id') == rid
    ]
    lim_lines = [
        f'- **Same `(Problem {prob_val}, {stage_val})` cell peers ({len(peers)})**: '
        + (', '.join(f'`{p}`' for p in peers[:12]) if peers else 'none'),
        f'- **Cross-stage tension observations**: '
        + (', '.join(f'`{oid}`' for oid in c1_obs) if c1_obs else 'none registered in `constraint-1`'),
    ]

    default_eq_block = (
        'Core intuition, key mathematical formulation, and variable-by-variable symbol definitions:\n\n'
        '| Symbol | Domain / Shape | Meaning in Paper | Reference Code Variable |\n'
        '| --- | --- | --- | --- |\n'
        '| `$\\mathbf{z}_i$` | `$\\mathbb{R}^d$` | Continuous item representation before quantization | `item_emb` |\n'
        '| `$c_{i,\\ell}$` | `$\\{1,\\dots,K\\}$` | Discrete code index at hierarchy level `$\\ell$` | `sem_ids[:, l]` |'
    )
    default_code_block = (
        '| Paper Section / Equation | Method Step | Reference Implementation Path | Pinning Anchor (`data-expect`) |\n'
        '| --- | --- | --- | --- |\n'
        f'| `{format_label_val((labels.get("tokenization") or {}).get("source", "missing"))}` | '
        f'Tokenization (`{format_label_val((labels.get("tokenization") or {}).get("value", "–"))}`) | '
        '`pending-stage2-walkthrough` | `pending-stage2-anchor` |'
    )
    default_lim_notes = 'Method-specific scope conditions and failure modes to be expanded in Stage 2 synthesis.'

    venue = (record.get('external') or {}).get('venue') or '–'
    primary_url = record_primary_url(record, 'https://github.com/milkshakeforreal/Awesome-SID-Generative-Rec/blob/living-review')
    return tmpl.format(
        name=record.get('name', rid),
        id=rid,
        citation=record.get('citation') or '–',
        venue=venue,
        primary_url=primary_url,
        generated_taxonomy_positioning='\n'.join(tax_lines),
        narrative_equations_and_variables=narrative_blocks.get('equations_and_variables', default_eq_block),
        narrative_code_walkthrough=narrative_blocks.get('code_walkthrough', default_code_block),
        generated_source_evidence='\n'.join(ev_lines),
        generated_protocol_results='\n'.join(res_lines),
        generated_limitations_and_links='\n'.join(lim_lines),
        narrative_limitations_notes=narrative_blocks.get('limitations_notes', default_lim_notes),
    )


def check_no_private_paths(staged_files):
    """Ensure zero private host paths or local agent cache paths appear in repo code, data, or staged outputs."""
    errors = []
    private_re = re.compile(r'(\.cc-' + r'switch|/' + r'home/|/' + r'Users/|~/' + r'\.cc-' + r'switch)')
    scan_paths = (
        list(SCRIPTS_DIR.glob('*.py'))
        + list(DATA_DIR.glob('*.json'))
        + list(DATA_DIR.glob('*.yaml'))
        + list((ROOT / 'schema').glob('*'))
        + list(TEMPLATES_DIR.glob('*'))
    )
    for p in sorted(scan_paths):
        if p.is_file():
            txt = p.read_text(encoding='utf-8', errors='ignore')
            m = private_re.search(txt)
            if m:
                errors.append(f'E_PRIVATE_PATH_LEAK: {p.relative_to(ROOT)} contains private path token {m.group(0)!r}')
    for fname, txt in sorted(staged_files.items()):
        m = private_re.search(txt)
        if m:
            errors.append(f'E_PRIVATE_PATH_LEAK: staged {fname} contains private path token {m.group(0)!r}')
    return {
        'gate': 'no_private_paths_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def check_relative_links(staged_files):
    errors = []
    link_re = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
    available = set(staged_files.keys())
    for fname, content in staged_files.items():
        if not fname.endswith('.md'):
            continue
        for m in link_re.finditer(content):
            target = m.group(1).split('#', 1)[0].strip()
            if not target or '://' in target or target.startswith('mailto:'):
                continue
            if target not in available:
                errors.append(f'E_BROKEN_RELATIVE_LINK: {fname} links to missing target {target!r}')
    return {
        'gate': 'relative_link_check',
        'ok': len(errors) == 0,
        'errors': errors,
    }


def run_build(out_dir=DEFAULT_OUT_DIR, proposals=None, requested_question=None, write_outputs=True):
    records_dir = DATA_DIR / 'papers'
    records = load_records(records_dir)
    adjudications = json.loads((DATA_DIR / 'adjudications.json').read_text(encoding='utf-8'))
    rules = json.loads((DATA_DIR / 'rules.json').read_text(encoding='utf-8'))
    evidence_bytes = (DATA_DIR / 'evidence.json').read_bytes()
    evidence = json.loads(evidence_bytes.decode('utf-8'))
    metrics = json.loads((DATA_DIR / 'metrics.json').read_text(encoding='utf-8'))
    source_verification = json.loads((DATA_DIR / 'source-verification.json').read_text(encoding='utf-8'))

    records, adjudications, rules, evidence, metrics = apply_proposals(
        records, adjudications, rules, evidence, metrics, proposals
    )

    g_lint = check_renderer_lint(records)
    g_schema = check_schema(records)
    g_adj = check_adjudications(records, adjudications)
    g_ev = check_evidence(evidence, source_verification, evidence_bytes)
    g_subj = check_subject_and_field_bindings(records, rules, evidence, source_verification)
    g_met = check_metrics(metrics, rules, evidence, source_verification)
    g_query = check_query_membership_and_rows(records, rules, evidence)
    g_con = check_constraint(rules, evidence)

    gates = [g_lint, g_schema, g_adj, g_ev, g_subj, g_met, g_query, g_con]
    pack = build_answer_pack(records, adjudications, rules, evidence, metrics, gates, g_query, requested_question)
    pages = render_pages(pack, evidence)
    awesome_readme = render_awesome_readme(pack, records, evidence)

    eff_lines = [
        json.dumps(records[rid], ensure_ascii=False, sort_keys=True)
        for rid in sorted(records)
    ]
    staged = dict(pages)
    staged['readme-awesome.md'] = awesome_readme
    staged['effective-records.jsonl'] = '\n'.join(eff_lines) + '\n'
    staged['answer-pack.json'] = ''

    g_awesome = check_awesome_readme_contract(awesome_readme)
    g_links = check_relative_links(staged)
    g_priv = check_no_private_paths(staged)
    gates.extend([g_awesome, g_links, g_priv])

    all_errors = [err for g in gates for err in g.get('errors', [])]
    ok = len(all_errors) == 0
    pack['gates'] = gates
    pack['build_ok'] = ok
    pack['errors'] = all_errors
    staged['answer-pack.json'] = json.dumps(pack, ensure_ascii=False, indent=2) + '\n'

    if ok and write_outputs:
        out_dir.mkdir(parents=True, exist_ok=True)
        for fname, text in staged.items():
            (out_dir / fname).write_text(text, encoding='utf-8')

    return {
        'ok': ok,
        'errors': all_errors,
        'gates': gates,
        'pack': pack,
        'staged_files': staged,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-dir', type=Path, default=DEFAULT_OUT_DIR)
    ap.add_argument('--proposals', type=Path, help='optional JSON overlay for testing workflows')
    ap.add_argument('--question', type=str, help='optional question ID to query')
    args = ap.parse_args()

    proposals = json.loads(args.proposals.read_text(encoding='utf-8')) if args.proposals else None
    res = run_build(out_dir=args.out_dir, proposals=proposals, requested_question=args.question, write_outputs=True)
    if not res['ok']:
        print(f"Build FAILED with {len(res['errors'])} error(s):", file=sys.stderr)
        for err in res['errors']:
            print(f'  - {err}', file=sys.stderr)
        return 1
    cov = res['pack']['coverage']
    print(
        f"Build OK -> {args.out_dir} | records={cov['total_records']} | "
        f"table1={cov['table1_records']} | problem_II={cov['problem_II_records']} "
        f"({cov['problem_II_stage_summary_zh']})"
    )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
