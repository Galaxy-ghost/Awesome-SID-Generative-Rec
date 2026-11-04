#!/usr/bin/env python3
"""Validate all paper records and generated views:
1. Schema & vocabulary compliance (schema/paper.schema.json + data/vocab.yaml + modality grouping rules + bilingual descriptions + 3 hard content rules)
2. Global uniqueness (file stem, id, name, links.arxiv)
3. Table 1 cell-by-cell round-trip (including bold primary column vs changes) against Table 1 in the survey paper (main.tex and supplementary.tex)
4. Relative Markdown links, reference definitions, and anchors across README.md, README.zh.md, CONTRIBUTING.md,
   CONTRIBUTING.zh.md, schema/README.md, notes/, notes/zh/, pages/papers/, pages/zh/papers/, pages/index/,
   pages/zh/index/, guides/, comparisons/
5. data/updates.yaml entries (date, change, change_zh, papers)
6. No constraint-*.md or tension-*.md file anywhere in the repository
7. Bilingual pairing & Chinese sync: hand-maintained pairs (via data/i18n.yaml) plus generated bilingual views
   (READMEs, paper cards and 5-stage diagrams, modality/domain indexes, and glossaries)
"""
import argparse
import hashlib
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import yaml
from build import (
    COL_STAGES,
    ROOT,
    SETUP_KEYS,
    TECH_COLS,
    na_to_dash,
    parse_table1_tex,
    slugify_heading,
)

QUOTE_RE = re.compile(r'"([^"\n]*\s[^"\n]*)"')  # double-quoted text with at least two words
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")
FENCE_RE = re.compile(r"^\s*```.*?^\s*```", re.S | re.M)
CJK_RE = re.compile(r"[\u4e00-\u9fff]")

FORBIDDEN_STAMP_KEYS = {"status", "label_status", "verified_by", "review_stamp", "evidence_grade", "claim_kind"}
RELATIONS = {"predecessor", "successor", "competitor", "alternative"}
VALID_GROUP_RULES = {
    "branch_content_exact",
    "branch_content_single_excluding",
    "branch_content_multi_or_any",
    "all_branches_no_content",
    "union_exact",
    "union_with_other",
    "union_contains",
}
VOCAB_LIST_SECTIONS = ["problem", "stage", *TECH_COLS, "modality", "domain", "settings"]


def check_schema_and_vocab(root: Path, schema: dict, vocab: dict, errors: list) -> dict:
    req_keys = set(schema["required"])
    allowed_keys = set(schema["properties"].keys())
    id_pat = re.compile(schema["properties"]["id"]["pattern"])
    ev_item_schema = schema["properties"]["evidence"]["items"]
    ev_req = set(ev_item_schema["required"])
    ev_keys = list(ev_item_schema["properties"].keys())
    ev_one_of = [r["required"][0] for r in ev_item_schema["anyOf"]]
    ev_fields = allowed_keys - {
        "changes", "modality", "modality_open", "modality_where", "note",
        "domain", "settings", "evidence", "tldr", "tldr_zh", "setup", "related", "setup_where",
    }

    for sec in VOCAB_LIST_SECTIONS:
        items = vocab.get(sec)
        if not isinstance(items, list) or not items:
            errors.append(f"[vocab] data/vocab.yaml: missing or empty section {sec!r}")
            continue
        for e in items:
            if not e.get("value") or not e.get("description") or not e.get("description_zh"):
                errors.append(f"[vocab] data/vocab.yaml ({sec}={e.get('value')!r}): requires value, description, and description_zh")
            if sec in ("domain", "settings"):
                nzh = e.get("name_zh", "")
                if not isinstance(nzh, str) or not nzh.strip() or not CJK_RE.search(nzh):
                    errors.append(f"[vocab] data/vocab.yaml ({sec}={e.get('value')!r}): requires Chinese name_zh")
            if sec == "domain":
                cat = e.get("category", "")
                cat_zh = e.get("category_zh", "")
                if not isinstance(cat, str) or not cat.strip() or not isinstance(cat_zh, str) or not CJK_RE.search(cat_zh):
                    errors.append(f"[vocab] data/vocab.yaml (domain={e.get('value')!r}): requires category and Chinese category_zh")
            if sec == "modality" and not isinstance(e.get("is_content"), bool):
                errors.append(f"[vocab] data/vocab.yaml (modality={e.get('value')!r}): requires boolean is_content")

    vocab_sets = {
        sec: {e["value"] for e in vocab.get(sec, []) if isinstance(e, dict) and "value" in e}
        for sec in VOCAB_LIST_SECTIONS
    }

    mgroups = vocab.get("modality_groups")
    if not isinstance(mgroups, list) or not mgroups:
        errors.append("[vocab] data/vocab.yaml: missing or empty modality_groups")
    else:
        for gi, g in enumerate(mgroups):
            req_g = {"value", "aspect", "aspect_zh", "name", "name_zh", "rule", "description", "description_zh"}
            if not isinstance(g, dict) or not (req_g <= set(g.keys())):
                errors.append(f"[vocab] data/vocab.yaml modality_groups[{gi}]: missing required keys {sorted(req_g)}")
                continue
            if not CJK_RE.search(str(g.get("aspect_zh", ""))) or not CJK_RE.search(str(g.get("name_zh", ""))):
                errors.append(f"[vocab] data/vocab.yaml modality_groups[{gi}] ({g.get('value')!r}): aspect_zh and name_zh must contain Chinese")
            rule = g.get("rule")
            if rule not in VALID_GROUP_RULES:
                errors.append(f"[vocab] data/vocab.yaml modality_groups[{gi}] ({g.get('value')!r}): invalid rule {rule!r}")
            if "target" in g and g["target"] not in vocab_sets["modality"]:
                errors.append(f"[vocab] data/vocab.yaml modality_groups[{gi}]: target={g['target']!r} not in modality vocab")
            for k_list in ("exclude", "include_any", "exclude_all_only"):
                if k_list in g:
                    vals = g[k_list]
                    if not isinstance(vals, list) or not vals or any(x not in vocab_sets["modality"] for x in vals):
                        errors.append(f"[vocab] data/vocab.yaml modality_groups[{gi}]: invalid {k_list}={vals!r}")

    records = {}
    for p in sorted((root / "data/papers").glob("*.yaml")):
        rec = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(rec, dict):
            errors.append(f"[schema] {p.name}: root is not a mapping")
            continue
        keys = set(rec.keys())
        for fk in keys & FORBIDDEN_STAMP_KEYS:
            errors.append(f"[content-rule-3] {p.name}: forbidden review-stamp field '{fk}'")
        missing = req_keys - keys
        extra = keys - allowed_keys
        if missing:
            errors.append(f"[schema] {p.name}: missing required fields {sorted(missing)}")
        if extra:
            errors.append(f"[schema] {p.name}: unknown fields {sorted(extra)}")
        if p.stem != rec.get("id"):
            errors.append(f"[schema] {p.name}: file stem '{p.stem}' != id '{rec.get('id')}'")
        if not id_pat.match(str(rec.get("id", ""))):
            errors.append(f"[schema] {p.name}: invalid id pattern '{rec.get('id')}'")
        if not isinstance(rec.get("year"), int) or rec.get("year", 0) < 1990:
            errors.append(f"[schema] {p.name}: invalid year '{rec.get('year')}'")
        if not isinstance(rec.get("poi"), bool):
            errors.append(f"[schema] {p.name}: poi must be boolean")

        links = rec.get("links", {})
        if not isinstance(links, dict) or not ({"arxiv", "code"} <= set(links.keys()) <= {"arxiv", "code", "code_third_party"}):
            errors.append(f"[schema] {p.name}: links must contain 'arxiv' and 'code' (and optionally 'code_third_party')")
        else:
            if not isinstance(links.get("arxiv"), str) or not links["arxiv"].startswith("http"):
                errors.append(f"[schema] {p.name}: links.arxiv must be a non-empty URL")
            if links.get("code") is not None and (not isinstance(links["code"], str) or not links["code"].startswith("http")):
                errors.append(f"[schema] {p.name}: links.code must be a URL or null")
            if "code_third_party" in links and (not isinstance(links["code_third_party"], str) or not links["code_third_party"].startswith("http")):
                errors.append(f"[schema] {p.name}: links.code_third_party must be a non-empty URL")

        for vk in ("problem", "stage", *TECH_COLS):
            val = rec.get(vk)
            if val not in vocab_sets[vk]:
                errors.append(f"[vocab] {p.name}: {vk}={val!r} not in data/vocab.yaml")

        if rec.get("problem") == "psb" and rec.get("stage") != "n/a":
            errors.append(f"[vocab] {p.name}: problem=psb requires stage=n/a")
        if rec.get("problem") != "psb" and rec.get("stage") == "n/a":
            errors.append(f"[vocab] {p.name}: problem={rec.get('problem')} cannot have stage=n/a")

        # 1. Validate changes
        ch = rec.get("changes")
        if not isinstance(ch, dict) or set(ch.keys()) != set(TECH_COLS):
            errors.append(f"[changes] {p.name}: changes must be a mapping with exact keys {TECH_COLS}")
        else:
            prim_cols = []
            for col in TECH_COLS:
                cv = ch[col]
                if cv == "primary":
                    prim_cols.append(col)
                elif cv == "none":
                    continue
                elif isinstance(cv, dict):
                    if set(cv.keys()) != {"value", "quote", "where"} or cv.get("value") != "other":
                        errors.append(f"[changes] {p.name}: changes.{col} object must have exact keys value='other', quote, where")
                    elif any(not isinstance(cv[k], str) or not cv[k].strip() for k in ("quote", "where")):
                        errors.append(f"[changes] {p.name}: changes.{col} quote and where must be non-empty strings")
                else:
                    errors.append(f"[changes] {p.name}: invalid changes.{col}={cv!r}")
            if rec.get("problem") == "psb":
                if prim_cols:
                    errors.append(f"[changes] {p.name}: problem=psb cannot have primary in changes (found {prim_cols})")
            else:
                if len(prim_cols) != 1:
                    errors.append(f"[changes] {p.name}: non-psb record must have exactly 1 primary in changes (found {prim_cols})")
                else:
                    pcol = prim_cols[0]
                    expected_stage = COL_STAGES[TECH_COLS.index(pcol)]
                    if expected_stage != rec.get("stage"):
                        errors.append(
                            f"[changes] {p.name}: primary column {pcol!r} maps to stage {expected_stage!r}, "
                            f"but record stage is {rec.get('stage')!r}"
                        )

        # 2. Validate modality, modality_open, modality_where, note
        mod = rec.get("modality")
        if isinstance(mod, list):
            if not mod:
                errors.append(f"[modality] {p.name}: modality list cannot be empty")
            else:
                if len(mod) != len(set(mod)):
                    errors.append(f"[modality] {p.name}: duplicate values in modality={mod!r}")
                for mv in mod:
                    if mv not in vocab_sets["modality"]:
                        errors.append(f"[modality] {p.name}: modality value {mv!r} not in data/vocab.yaml")
        elif isinstance(mod, dict):
            if not mod:
                errors.append(f"[modality] {p.name}: modality dict cannot be empty")
            else:
                non_empty_branches = 0
                for br, bvals in mod.items():
                    if not isinstance(br, str) or not br.strip():
                        errors.append(f"[modality] {p.name}: invalid branch key {br!r}")
                    if not isinstance(bvals, list):
                        errors.append(f"[modality] {p.name}: modality[{br!r}] must be a list")
                        continue
                    if bvals:
                        non_empty_branches += 1
                    if len(bvals) != len(set(bvals)):
                        errors.append(f"[modality] {p.name}: duplicate values in modality[{br!r}]={bvals!r}")
                    for mv in bvals:
                        if mv not in vocab_sets["modality"]:
                            errors.append(f"[modality] {p.name}: modality[{br!r}] value {mv!r} not in data/vocab.yaml")
                if non_empty_branches == 0:
                    errors.append(f"[modality] {p.name}: modality dict must have at least one non-empty branch")
        else:
            errors.append(f"[modality] {p.name}: modality must be a non-empty list or branch mapping")

        if "modality_open" in rec:
            mo = rec["modality_open"]
            if not isinstance(mo, list) or not mo or any(not isinstance(x, str) or not x.strip() for x in mo):
                errors.append(f"[modality] {p.name}: modality_open must be a non-empty list of non-empty strings")

        if "modality_where" in rec:
            mw = rec["modality_where"]
            if not isinstance(mw, dict) or set(mw.keys()) != {"quote", "where"} or any(
                not isinstance(mw[k], str) or not mw[k].strip() for k in ("quote", "where")
            ):
                errors.append(f"[modality] {p.name}: modality_where must have non-empty quote and where")

        if "note" in rec:
            if not isinstance(rec["note"], str) or not rec["note"].strip():
                errors.append(f"[modality] {p.name}: note must be a non-empty string")

        # 3. Validate domain
        dom = rec.get("domain")
        if not isinstance(dom, list) or not dom:
            errors.append(f"[domain] {p.name}: domain must be a non-empty list")
        else:
            if len(dom) != len(set(dom)):
                errors.append(f"[domain] {p.name}: duplicate values in domain={dom!r}")
            for dv in dom:
                if dv not in vocab_sets["domain"]:
                    errors.append(f"[domain] {p.name}: domain value {dv!r} not in data/vocab.yaml")

        # 4. Validate settings
        stgs = rec.get("settings")
        if not isinstance(stgs, list):
            errors.append(f"[settings] {p.name}: settings must be a list")
        else:
            seen_stgs = set()
            for si, sitem in enumerate(stgs):
                if not isinstance(sitem, dict):
                    errors.append(f"[settings] {p.name}: settings[{si}] must be an object")
                    continue
                sval = sitem.get("value")
                if sval not in vocab_sets["settings"]:
                    errors.append(f"[settings] {p.name}: settings[{si}].value={sval!r} not in data/vocab.yaml")
                if sval == "cold-start":
                    if set(sitem.keys()) != {"value", "scope", "quote", "where"}:
                        errors.append(f"[settings] {p.name}: cold-start settings[{si}] must have exact keys value, scope, quote, where")
                        continue
                    if sitem.get("scope") not in ("user", "item"):
                        errors.append(f"[settings] {p.name}: cold-start settings[{si}].scope={sitem.get('scope')!r} must be 'user' or 'item'")
                else:
                    if set(sitem.keys()) != {"value", "quote", "where"}:
                        errors.append(f"[settings] {p.name}: settings[{si}] ({sval!r}) must have exact keys value, quote, where")
                        continue
                if any(not isinstance(sitem.get(k), str) or not sitem[k].strip() for k in ("quote", "where")):
                    errors.append(f"[settings] {p.name}: settings[{si}] quote and where must be non-empty strings")
                pair_key = (sval, sitem.get("scope"))
                if pair_key in seen_stgs:
                    errors.append(f"[settings] {p.name}: duplicate settings entry {pair_key!r}")
                seen_stgs.add(pair_key)

        if "evidence" in rec:
            if not isinstance(rec["evidence"], list):
                errors.append(f"[schema] {p.name}: evidence must be a list")
            else:
                for idx, item in enumerate(rec["evidence"]):
                    if not isinstance(item, dict) or not ev_req <= set(item) or set(item) - set(ev_keys) \
                            or not set(item) & set(ev_one_of):
                        errors.append(f"[schema] {p.name}: evidence[{idx}] must have {sorted(ev_req)}, at least one of "
                                      f"{ev_one_of}, and no other keys")
                    elif any(not isinstance(v, str) or not v.strip() for v in item.values()):
                        errors.append(f"[schema] {p.name}: evidence[{idx}] values must be non-empty strings")
                    elif item.get("field") not in ev_fields:
                        errors.append(f"[schema] {p.name}: evidence[{idx}].field={item.get('field')!r} invalid")

        for tk in ("tldr", "tldr_zh"):
            if tk in rec and (not isinstance(rec[tk], str) or not rec[tk].strip()):
                errors.append(f"[schema] {p.name}: {tk} must be a non-empty string")

        if "setup" in rec:
            st = rec["setup"]
            if not isinstance(st, dict) or list(st.keys()) != SETUP_KEYS:
                errors.append(f"[schema] {p.name}: setup must have exact ordered keys {SETUP_KEYS}")
            elif any(not isinstance(v, str) or not v.strip() for v in st.values()):
                errors.append(f"[schema] {p.name}: all setup values must be non-empty strings")

        if "setup_where" in rec:
            if "setup" not in rec:
                errors.append(f"[schema] {p.name}: setup_where can only appear with setup")
            sw = rec["setup_where"]
            if not isinstance(sw, dict) or set(sw.keys()) != set(SETUP_KEYS):
                errors.append(f"[schema] {p.name}: setup_where must have keys {SETUP_KEYS}")
            elif any(not isinstance(v, str) or not v.strip() for v in sw.values()):
                errors.append(f"[schema] {p.name}: all setup_where values must be non-empty strings")

        records[rec["id"]] = rec

    for pid, rec in records.items():
        if "related" not in rec:
            continue
        rel = rec["related"]
        if not isinstance(rel, list) or not (1 <= len(rel) <= 5):
            errors.append(f"[schema] {pid}.yaml: related must be a list of 1–5 items")
            continue
        seen_rel = set()
        for idx, item in enumerate(rel):
            if not isinstance(item, dict) or set(item.keys()) != {"id", "relation", "note", "where"}:
                errors.append(f"[schema] {pid}.yaml: related[{idx}] must have exact keys id, relation, note, where")
                continue
            if any(not isinstance(v, str) or not v.strip() for v in item.values()):
                errors.append(f"[schema] {pid}.yaml: related[{idx}] values must be non-empty strings")
                continue
            if item["relation"] not in RELATIONS:
                errors.append(f"[schema] {pid}.yaml: related[{idx}].relation={item['relation']!r} invalid")
            rid = item["id"]
            if rid == pid or rid not in records:
                errors.append(f"[schema] {pid}.yaml: related[{idx}].id={rid!r} must be another existing record id")
            if rid in seen_rel:
                errors.append(f"[schema] {pid}.yaml: duplicate related id {rid!r}")
            seen_rel.add(rid)

    return records


def check_uniqueness(records: dict, errors: list):
    seen_names = {}
    seen_arxiv = {}
    for pid, rec in records.items():
        nm = rec["name"]
        ax = rec["links"]["arxiv"]
        if nm in seen_names:
            errors.append(f"[uniqueness] duplicate name {nm!r} in {pid} and {seen_names[nm]}")
        seen_names[nm] = pid
        if ax in seen_arxiv:
            errors.append(f"[uniqueness] duplicate links.arxiv {ax!r} in {pid} and {seen_arxiv[ax]}")
        seen_arxiv[ax] = pid


def check_table1_roundtrip(records: dict, table1_paths: list, errors: list):
    for p in table1_paths:
        if not p.exists():
            errors.append(f"[table1] source file not found: {p}")
            return
    rows = parse_table1_tex(table1_paths)
    by_name = {r["name"]: r for r in records.values()}
    if len(rows) != len(records):
        errors.append(f"[table1] row count mismatch: Table 1 has {len(rows)}, repo has {len(records)}")

    seen = set()
    for r in rows:
        nm = r["name"]
        if nm in seen:
            errors.append(f"[table1] duplicate row {nm!r} in Table 1 tex")
            continue
        seen.add(nm)
        if nm not in by_name:
            errors.append(f"[table1] row {nm!r} in Table 1 missing from data/papers/")
            continue
        rec = by_name[nm]
        for field in ["name", "venue", "problem", "stage"]:
            if rec[field] != r[field]:
                errors.append(f"[table1] cell mismatch for {nm} / {field}: repo={rec[field]!r} vs table1={r[field]!r}")
        for col in TECH_COLS:
            repo_val = na_to_dash(rec[col])
            if repo_val != r[col]:
                errors.append(f"[table1] cell mismatch for {nm} / {col}: repo={rec[col]!r} ({repo_val!r}) vs table1={r[col]!r}")
        ch = rec.get("changes", {})
        prim_cols = [c for c in TECH_COLS if ch.get(c) == "primary"]
        repo_prim = prim_cols[0] if len(prim_cols) == 1 else None
        if repo_prim != r.get("primary_col"):
            errors.append(
                f"[table1] primary bold cell mismatch for {nm}: changes primary={repo_prim!r} vs tex bold={r.get('primary_col')!r}"
            )
    for nm in sorted(set(by_name) - seen):
        errors.append(f"[table1] repo record {nm!r} missing from Table 1 tex")


def check_links_and_content_rules(root: Path, vocab: dict, errors: list):
    md_files = [
        root / "README.md",
        root / "README.zh.md",
        root / "CONTRIBUTING.md",
        root / "CONTRIBUTING.zh.md",
        root / "schema/README.md",
        *sorted((root / "notes").glob("*.md")),
        *sorted((root / "notes/zh").glob("*.md")),
        *sorted((root / "pages/papers").glob("*.md")),
        *sorted((root / "pages/zh/papers").glob("*.md")),
        *sorted((root / "pages/index").glob("*.md")),
        *sorted((root / "pages/zh/index").glob("*.md")),
        *sorted((root / "guides").glob("*.md")),
        *sorted((root / "comparisons").glob("*.md")),
    ]
    for d, subdirs, files in os.walk(root):
        subdirs[:] = [x for x in subdirs if x not in (".git", "node_modules")]
        for f in files:
            if f.endswith(".md") and f.startswith(("constraint-", "tension-")):
                errors.append(f"[content-rule-2] forbidden page {(Path(d) / f).relative_to(root)}")

    wrong_names = ["Information Loss", "Collision & Invalidity", "Alignment Gap", "Single-Point Utility"]

    headings_cache = {}
    for mf in md_files:
        if not mf.exists():
            errors.append(f"[links] expected Markdown file missing: {mf}")
            continue
        txt = mf.read_text(encoding="utf-8")
        for wn in wrong_names:
            if wn in txt:
                errors.append(f"[content-rule-1] forbidden non-vocab problem name {wn!r} found in {mf.relative_to(root)}")
        if mf.parent in (root / "notes", root / "notes/zh"):
            # GitHub math: Markdown eats \| \{ \, inside $...$ and $$...$$, and rejects \operatorname.
            # Use ```math blocks and $`...`$ inline; write \gt / \lt inline.
            if "\\operatorname" in txt or "$$" in txt or re.search(r"(?<!`)\$(?!`)", txt) \
                    or any(c in m for m in re.findall(r"\$`(.*?)`\$", txt) for c in "<>"):
                errors.append(f"[math] {mf.relative_to(root)}: use ```math / $`...`$, no \\operatorname, \\gt/\\lt inline")
        anchors = set()
        for line in txt.splitlines():
            hm = re.match(r"^#{1,6}\s+(.+)$", line.strip())
            if hm:
                h_clean = re.sub(r"\s*\[!\[.*$", "", hm.group(1)).strip()
                anchors.add(slugify_heading(h_clean))
        headings_cache[mf.resolve()] = anchors

    link_pat = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)|^\[[^\]]+\]:\s*(\S+)", re.M)
    for mf in md_files:
        if not mf.exists():
            continue
        txt = mf.read_text(encoding="utf-8")
        for m in link_pat.finditer(txt):
            target = (m.group(1) or m.group(2)).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            path_part, _, anchor = target.partition("#")
            target_file = (mf.parent / path_part).resolve() if path_part else mf.resolve()
            if not target_file.exists():
                errors.append(f"[links] broken relative link in {mf.relative_to(root)}: {target}")
                continue
            if anchor and target_file in headings_cache:
                if anchor not in headings_cache[target_file]:
                    errors.append(f"[links] broken anchor in {mf.relative_to(root)}: #{anchor}")


def body_text(txt: str) -> str:
    """Text outside fenced blocks and inline code, where quotations are written."""
    return re.sub(r"`[^`\n]*`", "", FENCE_RE.sub("", txt))


def parse_section_blocks(txt: str) -> list:
    """Split a Markdown document into (depth_tuple, slug_stack, prose_outside_fences) per heading section."""
    sections = []
    stack = []  # list of (depth, slug)
    cur_lines = []
    fence = False

    def flush():
        prose = re.sub(r"\s+", " ", "\n".join(cur_lines)).strip()
        if stack or prose:
            path = "/" + "/".join(s for _, s in stack) if stack else "/"
            depths = tuple(d for d, _ in stack)
            digest = hashlib.sha256(prose.encode("utf-8")).hexdigest()[:16]
            sections.append((depths, path, digest))

    for ln in txt.splitlines():
        if re.match(r"^\s*```", ln):
            fence = not fence
            continue
        if fence:
            continue
        hm = re.match(r"^(#{1,6})\s+(.+?)\s*$", ln)
        if hm:
            flush()
            cur_lines = []
            depth = len(hm.group(1))
            slug = slugify_heading(hm.group(2))
            while stack and stack[-1][0] >= depth:
                stack.pop()
            stack.append((depth, slug))
        else:
            cur_lines.append(ln)
    flush()
    return sections


def bilingual_pairs(root: Path) -> list:
    """Return ordered list of (rel_key, en_path, zh_path) for all hand-maintained bilingual Markdown pairs."""
    pairs = [
        ("CONTRIBUTING.md", root / "CONTRIBUTING.md", root / "CONTRIBUTING.zh.md"),
        ("guides/start-here.md", root / "guides/start-here.md", root / "guides/start-here.zh.md"),
    ]
    for ep in sorted((root / "notes").glob("*.md")):
        pairs.append((f"notes/{ep.name}", ep, root / "notes/zh" / ep.name))
    return pairs


def check_generated_bilingual_views(root: Path, records: dict, errors: list):
    """Verify structural and content parity across generated English and Chinese READMEs, indexes, paper pages, and glossaries."""
    r_en_path, r_zh_path = root / "README.md", root / "README.zh.md"
    if r_en_path.exists() and r_zh_path.exists():
        r_en = r_en_path.read_text(encoding="utf-8")
        r_zh = r_zh_path.read_text(encoding="utf-8")
        for h_prefix in ("## ", "### "):
            c_en = len(re.findall(rf"^{h_prefix}", r_en, re.M))
            c_zh = len(re.findall(rf"^{h_prefix}", r_zh, re.M))
            if c_en != c_zh:
                errors.append(f"[sync-gen] README.zh.md has {c_zh} '{h_prefix.strip()}' headings, README.md has {c_en}")
        sum_en = re.findall(r"<summary>(.*?)</summary>", r_en)
        sum_zh = re.findall(r"<summary>(.*?)</summary>", r_zh)
        if len(sum_en) != len(sum_zh):
            errors.append(f"[sync-gen] README <details> summary count differs (en={len(sum_en)}, zh={len(sum_zh)})")
        for s_e, s_z in zip(sum_en, sum_zh):
            if not CJK_RE.search(s_z) or "篇" not in s_z:
                errors.append(f"[sync-gen] README.zh.md <summary> must be in Chinese: {s_z!r}")
            if re.findall(r"\d+", s_e) != re.findall(r"\d+", s_z):
                errors.append(f"[sync-gen] README <summary> paper count mismatch: {s_e!r} vs {s_z!r}")
        for sym in ("●", "○"):
            if r_en.count(sym) != r_zh.count(sym):
                errors.append(f"[sync-gen] README {sym!r} count mismatch: en={r_en.count(sym)} vs zh={r_zh.count(sym)}")

    expected_svgs = ("taxonomy.svg", "taxonomy.zh.svg")
    for svg_name in expected_svgs:
        sp = root / "assets/figures" / svg_name
        if not sp.exists():
            errors.append(f"[figures] missing generated SVG figure assets/figures/{svg_name}")
            continue
        svg_txt = sp.read_text(encoding="utf-8")
        try:
            ET.fromstring(svg_txt)
        except ET.ParseError as exc:
            errors.append(f"[figures] malformed XML in assets/figures/{svg_name}: {exc}")
        if svg_name.endswith(".zh.svg") and not CJK_RE.search(svg_txt):
            errors.append(f"[figures] Chinese SVG assets/figures/{svg_name} contains no Chinese text")

    en_idx_files = sorted(p.name for p in (root / "pages/index").glob("*.md"))
    zh_idx_files = sorted(p.name for p in (root / "pages/zh/index").glob("*.md"))
    if en_idx_files != zh_idx_files or "modality.md" not in en_idx_files or "domain.md" not in en_idx_files:
        errors.append(f"[sync-gen] index file mismatch: en={en_idx_files} vs zh={zh_idx_files}")
    else:
        for fn in en_idx_files:
            t_en = (root / "pages/index" / fn).read_text(encoding="utf-8")
            t_zh = (root / "pages/zh/index" / fn).read_text(encoding="utf-8")
            h2_en = re.findall(r"^##\s+(.+)$", t_en, re.M)
            h2_zh = re.findall(r"^##\s+(.+)$", t_zh, re.M)
            if len(h2_en) != len(h2_zh):
                errors.append(f"[sync-gen] pages/zh/index/{fn}: {len(h2_zh)} H2 sections vs {len(h2_en)} in English")
            if fn in ("modality.md", "domain.md"):
                for hz in h2_zh:
                    if not CJK_RE.search(hz):
                        errors.append(f"[sync-gen] pages/zh/index/{fn}: H2 group heading {hz!r} must use Chinese")
            rows_en = len(re.findall(r"^\| \[", t_en, re.M))
            rows_zh = len(re.findall(r"^\| \[", t_zh, re.M))
            if rows_en != rows_zh:
                errors.append(f"[sync-gen] pages/zh/index/{fn}: table row count {rows_zh} != English {rows_en}")

    for pid in sorted(records):
        p_en = root / "pages/papers" / f"{pid}.md"
        p_zh = root / "pages/zh/papers" / f"{pid}.md"
        if not p_en.exists() or not p_zh.exists():
            errors.append(f"[sync-gen] missing generated paper page pair for {pid}")
            continue
        t_en = p_en.read_text(encoding="utf-8")
        t_zh = p_zh.read_text(encoding="utf-8")
        for sym in ("●", "○"):
            if t_en.count(sym) != t_zh.count(sym):
                errors.append(f"[sync-gen] {pid}.md {sym!r} count mismatch: en={t_en.count(sym)} vs zh={t_zh.count(sym)}")
        for dup_row in ("| Key Contribution |", "| Modified Stage |", "| 核心贡献 |", "| 主要改动阶段 |"):
            if dup_row in t_en or dup_row in t_zh:
                errors.append(f"[sync-gen] {pid}.md still contains duplicate At a Glance row {dup_row!r}")

    for llm_fn in ("llms.txt", "llms-full.txt"):
        lp = root / llm_fn
        if lp.exists() and CJK_RE.search(lp.read_text(encoding="utf-8")):
            errors.append(f"[llms] {llm_fn} must be English-only (found CJK characters)")


def check_bilingual_sync(root: Path, errors: list, write_i18n: bool = False):
    """Verify bilingual Markdown pairs (structure, quotations, numbers, and @deepseek-ai/dsh section hashes)."""
    for zp in sorted((root / "notes/zh").glob("*.md")):
        if not (root / "notes" / zp.name).exists():
            errors.append(f"[sync] notes/zh/{zp.name}: no English note notes/{zp.name}")

    computed_i18n = {}
    for rel_key, ep, zp in bilingual_pairs(root):
        if not ep.exists():
            errors.append(f"[sync] {rel_key}: missing English file")
            continue
        if not zp.exists():
            errors.append(f"[sync] {rel_key}: missing paired Chinese file {zp.relative_to(root)}")
            continue
        en, zh = ep.read_text(encoding="utf-8"), zp.read_text(encoding="utf-8")
        zh_name = str(zp.relative_to(root))

        for depth in ("###", "####"):
            count = lambda t: len(re.findall(rf"^{depth}\s", FENCE_RE.sub("", t), re.M))
            if count(en) != count(zh):
                errors.append(f"[sync] {zh_name}: {count(zh)} '{depth}' headings, English has {count(en)}")

        if rel_key.startswith("notes/"):
            for q in dict.fromkeys(QUOTE_RE.findall(body_text(en))):
                if q not in body_text(zh):
                    errors.append(f"[sync] {zh_name}: missing quotation \"{q[:60]}\"")
            zh_nums = set(NUMBER_RE.findall(zh))
            missing = [x for x in dict.fromkeys(NUMBER_RE.findall(en)) if x not in zh_nums]
            if missing:
                errors.append(f"[sync] {zh_name}: missing numbers {missing}")

        en_secs = parse_section_blocks(en)
        zh_secs = parse_section_blocks(zh)
        if [d for d, _, _ in en_secs] != [d for d, _, _ in zh_secs]:
            errors.append(f"[i18n] {rel_key}: heading hierarchy mismatch between English ({len(en_secs)} sections) "
                          f"and Chinese ({len(zh_secs)} sections)")
            continue
        computed_i18n[rel_key] = {
            path: {"en": en_hash, "zh": zh_hash}
            for (_, path, en_hash), (_, _, zh_hash) in zip(en_secs, zh_secs)
        }

    i18n_path = root / "data/i18n.yaml"
    if write_i18n:
        header = (
            "# Bilingual-pair consistency record (modeled on @deepseek-ai/dsh *.i18n.yaml):\n"
            "# per paired Markdown document and heading section path, a 16-hex SHA-256 hash of its\n"
            "# English and Chinese prose blocks outside fenced code blocks.\n"
            "# After editing either side, update its counterpart and re-record with:\n"
            "#   python3 scripts/check.py --write-i18n\n\n"
        )
        i18n_path.write_text(header + yaml.dump(computed_i18n, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
        print(f"Recorded bilingual section hashes for {len(computed_i18n)} document pairs into data/i18n.yaml.")
        return

    if not i18n_path.exists():
        errors.append("[i18n] data/i18n.yaml missing; run `python3 scripts/check.py --write-i18n`")
        return
    recorded = yaml.safe_load(i18n_path.read_text(encoding="utf-8")) or {}
    for rel_key, sec_map in computed_i18n.items():
        rec_map = recorded.get(rel_key)
        if not isinstance(rec_map, dict):
            errors.append(f"[i18n] {rel_key}: missing from data/i18n.yaml (run `python3 scripts/check.py --write-i18n`)")
            continue
        if list(rec_map.keys()) != list(sec_map.keys()):
            errors.append(f"[i18n] {rel_key}: section keys out of sync with data/i18n.yaml (run `python3 scripts/check.py --write-i18n`)")
            continue
        for sec_path, hashes in sec_map.items():
            rec_h = rec_map.get(sec_path, {})
            if rec_h.get("en") != hashes["en"] or rec_h.get("zh") != hashes["zh"]:
                changed = [lang for lang in ("en", "zh") if rec_h.get(lang) != hashes[lang]]
                errors.append(f"[i18n] {rel_key} ({sec_path}): {','.join(changed)} prose changed since last bilingual pairing record "
                              "(update counterpart and run `python3 scripts/check.py --write-i18n`)")


def check_updates(root: Path, records: dict, errors: list):
    p = root / "data/updates.yaml"
    ups = yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None
    if not isinstance(ups, list):
        errors.append("[updates] data/updates.yaml must exist and be a list")
        return
    for i, u in enumerate(ups):
        if not isinstance(u, dict) or set(u) != {"date", "change", "change_zh", "papers"}:
            errors.append(f"[updates] entry {i} must have exactly the keys date, change, change_zh, papers")
            continue
        if not isinstance(u["date"], str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", u["date"]):
            errors.append(f"[updates] entry {i}: date must be a 'YYYY-MM-DD' string")
        for ck in ("change", "change_zh"):
            if not isinstance(u[ck], str) or not u[ck].strip():
                errors.append(f"[updates] entry {i}: {ck} must be a non-empty string")
        if not isinstance(u["papers"], list) or any(x not in records for x in u["papers"]):
            errors.append(f"[updates] entry {i}: papers must be a list of existing record ids")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--table1", type=Path, nargs="+", help="External Table 1 source(s) (or TABLE1)")
    ap.add_argument("--write-i18n", action="store_true", help="Record bilingual section hashes in data/i18n.yaml")
    args = ap.parse_args()

    schema = json.loads((args.root / "schema/paper.schema.json").read_text(encoding="utf-8"))
    vocab = yaml.safe_load((args.root / "data/vocab.yaml").read_text(encoding="utf-8"))
    errors = []

    records = check_schema_and_vocab(args.root, schema, vocab, errors)
    check_uniqueness(records, errors)
    table1_paths = args.table1 or [Path(x) for x in os.environ.get("TABLE1", "").split()]
    if table1_paths:
        check_table1_roundtrip(records, table1_paths, errors)
    elif not args.write_i18n:
        print("SKIP: external Table 1 round-trip (supply --table1 PATH... or TABLE1).")
    check_bilingual_sync(args.root, errors, write_i18n=args.write_i18n)
    if args.write_i18n and not errors:
        return
    check_generated_bilingual_views(args.root, records, errors)
    check_links_and_content_rules(args.root, vocab, errors)
    check_updates(args.root, records, errors)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s) found.", file=sys.stderr)
        sys.exit(1)

    print(
        f"OK: {len(records)} records passed schema, vocab, uniqueness, "
        f"relative link, updates, and bilingual pairing (data/i18n.yaml) checks."
        + (f" Table 1 round-trip ({len(records) * 8} cells) passed." if table1_paths else "")
    )


if __name__ == "__main__":
    main()
