#!/usr/bin/env python3
"""Run end-to-end injection and workflow verification tests for the SID living review skeleton."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / 'scripts'
PACK_DIR = ROOT / 'pack'

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
import build as builder  # noqa: E402


def has_error_code(res, code):
    return any(code in err for err in res.get('errors', []))


def test_01_injection_a_metric_cell_mismatch():
    """Claude Injection A: tampering with value, cell_text, or column (Sports 2.8% as Beauty) is blocked."""
    # Subcase A1: change numeric value 2.1 -> 1.2
    res_a1 = builder.run_build(
        proposals={
            'metric_patches': [
                {'id': 'metric-hid-vae-beauty-collision-full', 'value': 1.2}
            ]
        },
        write_outputs=False,
    )
    # Subcase A2: change value, numeric_value, and cell_text to 1.2%
    res_a2 = builder.run_build(
        proposals={
            'metric_patches': [
                {
                    'id': 'metric-hid-vae-beauty-collision-full',
                    'value': 1.2,
                    'table_binding': {'numeric_value': 1.2, 'cell_text': '1.2%'},
                }
            ]
        },
        write_outputs=False,
    )
    # Subcase A3: copy Sports column value (2.8%, column_index=2, column_path=['Sports']) into amazon-beauty metric
    res_a3 = builder.run_build(
        proposals={
            'metric_patches': [
                {
                    'id': 'metric-hid-vae-beauty-collision-full',
                    'value': 2.8,
                    'table_binding': {
                        'column_index': 2,
                        'column_path': ['Sports'],
                        'numeric_value': 2.8,
                        'cell_text': '2.8%',
                    },
                }
            ]
        },
        write_outputs=False,
    )
    passed = (
        not res_a1['ok'] and has_error_code(res_a1, 'E_METRIC_CELL_MISMATCH')
        and not res_a2['ok'] and has_error_code(res_a2, 'E_METRIC_CELL_MISMATCH')
        and not res_a3['ok'] and has_error_code(res_a3, 'E_METRIC_CELL_MISMATCH')
    )
    return {
        'id': 'test_01_injection_A_metric_cell_mismatch',
        'passed': passed,
        'subcases': {
            'value_only_tamper_blocked': not res_a1['ok'] and has_error_code(res_a1, 'E_METRIC_CELL_MISMATCH'),
            'value_and_cell_text_tamper_blocked': not res_a2['ok'] and has_error_code(res_a2, 'E_METRIC_CELL_MISMATCH'),
            'wrong_column_sports_as_beauty_blocked': not res_a3['ok'] and has_error_code(res_a3, 'E_METRIC_CELL_MISMATCH'),
        },
        'sample_errors': res_a1['errors'] + res_a2['errors'] + res_a3['errors'],
    }


def test_02_injection_b_stage_change_and_dynamic_header():
    """Claude Injection B: unreviewed TransRec stage->Inference is blocked; reviewed change updates header & table."""
    res_unreviewed = builder.run_build(
        proposals={
            'record_patches': {
                'transrec': {'labels': {'stage': {'value': 'Inference'}}}
            }
        },
        write_outputs=False,
    )
    res_reviewed = builder.run_build(
        proposals={
            'record_patches': {
                'transrec': {'labels': {'stage': {'value': 'Inference'}}}
            },
            'rules_patches': {
                'problem_rows_patch': {
                    'transrec': {
                        'stage_change_review': {
                            'new_stage': 'Inference',
                            'reason': 'Fixture test for reviewed stage change to Inference',
                            'submitted_by': 'codex',
                            'reviewed_by': 'claude',
                        }
                    }
                }
            },
        },
        write_outputs=False,
    )
    p2_md = res_reviewed['staged_files']['problem-II.md']
    dist = res_reviewed['pack']['questions']['problem-II']['stage_distribution']
    summary_zh = res_reviewed['pack']['questions']['problem-II']['stage_summary_zh']
    passed = (
        not res_unreviewed['ok']
        and has_error_code(res_unreviewed, 'E_UNREVIEWED_STAGE_CHANGE')
        and res_reviewed['ok']
        and dist == {'Tokenization': 9, 'Inference': 1}
        and summary_zh == 'Tokenization 9 篇、Inference 1 篇'
        and 'Tokenization 9 篇、Inference 1 篇' in p2_md
    )
    return {
        'id': 'test_02_injection_B_stage_change_and_dynamic_header',
        'passed': passed,
        'unreviewed_blocked': not res_unreviewed['ok'] and has_error_code(res_unreviewed, 'E_UNREVIEWED_STAGE_CHANGE'),
        'reviewed_build_ok': res_reviewed['ok'],
        'reviewed_stage_distribution': dist,
        'reviewed_stage_summary_zh': summary_zh,
        'sample_errors': res_unreviewed['errors'],
    }


def test_03_injection_c_silent_removal_blocked():
    """Claude Injection C: changing CID problem II -> I without review is blocked by E_UNREVIEWED_REMOVAL."""
    res_unreviewed = builder.run_build(
        proposals={
            'record_patches': {
                'cid': {'labels': {'problem': {'value': 'I'}}}
            }
        },
        write_outputs=False,
    )
    res_reviewed = builder.run_build(
        proposals={
            'record_patches': {
                'cid': {'labels': {'problem': {'value': 'I'}}}
            },
            'rules_patches': {
                'field_bindings_replace': [
                    {
                        'claim_id': 'cid-problem',
                        'record_id': 'cid',
                        'field': 'problem',
                        'value': 'I',
                        'evidence_id': 'cid-design',
                        'subject': 'method',
                        'submitted_by': 'codex',
                        'reviewed_by': 'claude',
                    }
                ],
                'problem_II_membership_changes': [
                    {
                        'record_id': 'cid',
                        'action': 'remove',
                        'reason': 'Fixture test: reviewed reclassification from Problem II to Problem I',
                        'submitted_by': 'codex',
                        'reviewed_by': 'claude',
                        'date': '2026-10-30',
                    }
                ],
            },
        },
        write_outputs=False,
    )
    removals = res_reviewed['pack']['coverage']['removed_records_with_reason']
    passed = (
        not res_unreviewed['ok']
        and has_error_code(res_unreviewed, 'E_UNREVIEWED_REMOVAL')
        and res_reviewed['ok']
        and res_reviewed['pack']['coverage']['problem_II_records'] == 9
        and len(removals) == 1 and removals[0]['record_id'] == 'cid'
    )
    return {
        'id': 'test_03_injection_C_silent_removal_blocked',
        'passed': passed,
        'unreviewed_removal_blocked': not res_unreviewed['ok'] and has_error_code(res_unreviewed, 'E_UNREVIEWED_REMOVAL'),
        'reviewed_removal_build_ok': res_reviewed['ok'],
        'reviewed_problem_II_count': res_reviewed['pack']['coverage']['problem_II_records'],
        'removed_records_with_reason': removals,
        'sample_errors': res_unreviewed['errors'],
    }



def test_04_injection_d_first_time_baseline_subject_misread():
    """Claude Injection D: first-time misread setting subject='method' on baseline quote is blocked generically."""
    # Case D1: OneLoc first-time misread (no prior R-KM adjudication, subject='method' on oneloc-baseline)
    res_oneloc = builder.run_build(
        proposals={
            'record_patches': {
                'oneloc': {'labels': {'tokenization': {'value': 'RQ-VAE'}}}
            },
            'adjudications_patch': [
                {
                    'id': 'decision-poi-oneloc',
                    'accepted': {
                        'problem': 'III',
                        'stage': 'Tokenization',
                        'representation': 'Text+CF+Geo',
                        'tokenization': 'RQ-VAE',
                        'backbone': 'Enc-Dec',
                        'tokenizer_training': '2-Stage',
                        'objective': 'Multi-task NTP',
                        'inference': 'Beam',
                        'in_table1': True,
                    },
                }
            ],
            'evidence_patches': {
                'oneloc-baseline': {'subject': 'method'}
            },
            'rules_patches': {
                'field_bindings_replace': [
                    {
                        'claim_id': 'oneloc-tokenization',
                        'record_id': 'oneloc',
                        'field': 'tokenization',
                        'value': 'RQ-VAE',
                        'evidence_id': 'oneloc-baseline',
                        'subject': 'method',
                        'negative_evidence_ids': [],
                        'submitted_by': 'codex',
                        'reviewed_by': 'claude',
                    }
                ]
            },
        },
        write_outputs=False,
    )

    # Case D2: Non-OneLoc paper (CARD) first-time misread attributing VQ-Rec OPQ from Baselines section (#S4.I1.i5.p1.1)
    res_card = builder.run_build(
        proposals={
            'record_patches': {
                'card': {'labels': {'tokenization': {'value': 'OPQ'}}}
            },
            'evidence_patches': {
                'card-baseline': {'subject': 'method'}
            },
            'rules_patches': {
                'field_bindings_replace': [
                    {
                        'claim_id': 'card-tokenization',
                        'record_id': 'card',
                        'field': 'tokenization',
                        'value': 'OPQ',
                        'evidence_id': 'card-baseline',
                        'subject': 'method',
                        'negative_evidence_ids': [],
                        'submitted_by': 'codex',
                        'reviewed_by': 'claude',
                    }
                ]
            },
        },
        write_outputs=False,
    )

    passed = (
        not res_oneloc['ok'] and has_error_code(res_oneloc, 'E_SUBJECT_REVIEW_REQUIRED')
        and not res_card['ok'] and has_error_code(res_card, 'E_SUBJECT_REVIEW_REQUIRED')
    )
    return {
        'id': 'test_04_injection_D_first_time_baseline_subject_misread',
        'passed': passed,
        'oneloc_first_time_misread_blocked': (
            not res_oneloc['ok'] and has_error_code(res_oneloc, 'E_SUBJECT_REVIEW_REQUIRED')
        ),
        'non_oneloc_card_misread_blocked': (
            not res_card['ok'] and has_error_code(res_card, 'E_SUBJECT_REVIEW_REQUIRED')
        ),
        'sample_errors': res_oneloc['errors'] + res_card['errors'],
    }


def test_05_generic_admission_before_and_after():
    """Verify generic admission workflow before/after without any paper-specific code branch."""
    # Simulate pre-admission state for gwhere (in_table1=False, problem=None, reviewed expected_record_ids=9)
    expected_9 = [
        rid for rid in ['adasid', 'card', 'cid', 'diger', 'gwhere', 'hid-vae', 'psi', 'quasid', 'r3-vae', 'transrec']
        if rid != 'gwhere'
    ]
    res_before = builder.run_build(
        proposals={
            'record_patches': {
                'gwhere': {
                    'in_table1': False,
                    'labels': {'problem': {'value': 'pending', 'status': 'unverified', 'source': 'missing'}},
                }
            },
            'adjudications_patch': [
                {'id': 'decision-poi-gwhere', 'status': 'pending'}
            ],
            'rules_patches': {
                'problem_II_expected_record_ids': expected_9,
                'problem_rows_patch': {'gwhere': None},
                'field_bindings_replace': [
                    {
                        'claim_id': 'gwhere-problem',
                        'record_id': 'gwhere',
                        'field': 'problem',
                        'value': 'pending',
                        'evidence_id': 'gwhere-design',
                        'subject': 'method',
                        'submitted_by': 'codex',
                        'reviewed_by': 'claude',
                    }
                ],
            },
        },
        write_outputs=False,
    )
    res_after = builder.run_build(write_outputs=False)
    passed = (
        res_before['ok']
        and res_before['pack']['coverage']['problem_II_records'] == 9
        and res_before['pack']['coverage']['poi_records_in_problem_II'] == 0
        and res_after['ok']
        and res_after['pack']['coverage']['problem_II_records'] == 10
        and res_after['pack']['coverage']['poi_records_in_problem_II'] == 1
    )
    return {
        'id': 'test_05_generic_admission_before_and_after',
        'passed': passed,
        'before_problem_II_count': res_before['pack']['coverage']['problem_II_records'],
        'before_poi_in_problem_II': res_before['pack']['coverage']['poi_records_in_problem_II'],
        'after_problem_II_count': res_after['pack']['coverage']['problem_II_records'],
        'after_poi_in_problem_II': res_after['pack']['coverage']['poi_records_in_problem_II'],
    }


def test_06_protocol_and_grade_gates_and_determinism():
    """Verify protocol isolation for unknown resolver, constraint-1 upgrade gate, unsupported_question, and byte-identical build."""
    res_grade = builder.run_build(
        proposals={'rules_patches': {'constraint_status': 'Reported'}},
        write_outputs=False,
    )
    res_unknown_q = builder.run_build(requested_question='question-does-not-exist', write_outputs=False)

    with tempfile.TemporaryDirectory(prefix='sid-det-1-') as d1, tempfile.TemporaryDirectory(prefix='sid-det-2-') as d2:
        p1, p2 = Path(d1), Path(d2)
        b1 = builder.run_build(out_dir=p1, write_outputs=True)
        b2 = builder.run_build(out_dir=p2, write_outputs=True)
        hashes_1 = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p1.iterdir()) if f.is_file()}
        hashes_2 = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(p2.iterdir()) if f.is_file()}

    tc = b1['pack']['questions']['trie-collisions']
    comp_groups = tc['comparable_metric_groups']
    isolated = tc['non_comparable_metrics']
    passed = (
        not res_grade['ok'] and has_error_code(res_grade, 'E_GRADE_UPGRADE')
        and res_unknown_q['pack']['status'] == 'unsupported_question'
        and b1['ok'] and b2['ok']
        and hashes_1 == hashes_2
        and len(comp_groups) == 1 and len(comp_groups[0]['rows']) == 4
        and len(isolated) == 2 and all(m['resolver'] == 'unknown' for m in isolated)
    )
    return {
        'id': 'test_06_protocol_and_grade_gates_and_determinism',
        'passed': passed,
        'unreviewed_grade_upgrade_blocked': not res_grade['ok'] and has_error_code(res_grade, 'E_GRADE_UPGRADE'),
        'unsupported_question_status': res_unknown_q['pack']['status'],
        'comparable_group_row_count': len(comp_groups[0]['rows']) if comp_groups else 0,
        'isolated_unknown_resolver_count': len(isolated),
        'double_build_hashes_identical': hashes_1 == hashes_2,
        'artifact_sha256': hashes_1,
    }


def test_07_readme_and_paper_page_interfaces():
    """Verify Stage 1 interfaces for awesome-lint README generation and labml.ai-style single-paper pages."""
    records = builder.load_records(ROOT / 'data' / 'papers')
    evidence = json.loads((ROOT / 'data' / 'evidence.json').read_text(encoding='utf-8'))
    metrics = json.loads((ROOT / 'data' / 'metrics.json').read_text(encoding='utf-8'))
    rules = json.loads((ROOT / 'data' / 'rules.json').read_text(encoding='utf-8'))

    pilot_ids = ['tiger', 'rpg', 'oneloc']
    pilot_pages = {
        pid: builder.render_paper_page_skeleton(
            records[pid], evidence, metrics, all_records=records, rules=rules
        )
        for pid in pilot_ids
    }
    required_markers = [
        '<!-- BEGIN GENERATED: taxonomy-positioning -->',
        '<!-- BEGIN NARRATIVE: equations-and-variables -->',
        '<!-- BEGIN NARRATIVE: code-walkthrough -->',
        '<!-- BEGIN GENERATED: source-evidence -->',
        '<!-- BEGIN GENERATED: protocol-results -->',
        '<!-- BEGIN GENERATED: limitations-and-links -->',
    ]
    pages_ok = all(
        all(marker in page for marker in required_markers)
        for page in pilot_pages.values()
    )
    res = builder.run_build(write_outputs=False)
    awesome_gate = next(
        (g for g in res['gates'] if g['gate'] == 'awesome_readme_interface_check'),
        {'ok': False},
    )
    priv_gate = next(
        (g for g in res['gates'] if g['gate'] == 'no_private_paths_check'),
        {'ok': False},
    )
    passed = bool(pages_ok and awesome_gate['ok'] and priv_gate['ok'])
    return {
        'id': 'test_07_readme_and_paper_page_interfaces',
        'passed': passed,
        'awesome_readme_gate_ok': awesome_gate['ok'],
        'no_private_paths_gate_ok': priv_gate['ok'],
        'pilot_paper_pages_ok': pages_ok,
        'pilot_ids_checked': pilot_ids,
    }


def main():
    tests = [
        test_01_injection_a_metric_cell_mismatch(),
        test_02_injection_b_stage_change_and_dynamic_header(),
        test_03_injection_c_silent_removal_blocked(),
        test_04_injection_d_first_time_baseline_subject_misread(),
        test_05_generic_admission_before_and_after(),
        test_06_protocol_and_grade_gates_and_determinism(),
        test_07_readme_and_paper_page_interfaces(),
    ]
    passed = sum(1 for t in tests if t['passed'])
    report = {
        'passed': passed,
        'total': len(tests),
        'all_passed': passed == len(tests),
        'tests': tests,
    }
    PACK_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PACK_DIR / 'workflow-results.json'
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for t in tests:
        status = 'PASS' if t['passed'] else 'FAIL'
        print(f"[{status}] {t['id']}")
    print(f"Workflows: {passed}/{len(tests)} passed -> {out_path}")
    return 0 if passed == len(tests) else 1


if __name__ == '__main__':
    raise SystemExit(main())
