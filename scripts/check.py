#!/usr/bin/env python3
"""Validate all paper records and generated views:
1. Schema & vocabulary compliance (schema/paper.schema.json + data/vocab.yaml + 3 hard content rules)
2. Global uniqueness (file stem, id, name, links.arxiv)
3. Table 1 cell-by-cell round-trip against Table 1 in the survey paper (main.tex and supplementary.tex)
4. Relative Markdown links, reference definitions, and anchors across README.md, README.zh.md, CONTRIBUTING.md,
   schema/README.md, notes/, notes/zh/, pages/papers/, pages/zh/papers/, pages/index/, pages/zh/index/, guides/,
   comparisons/
6. No constraint-*.md or tension-*.md file anywhere in the repository
5. data/updates.yaml entries (date, change, papers)
7. Chinese notes sync: notes/<id>.md and notes/zh/<id>.md exist in pairs, with the same number of ### and #### headings,
   every English quotation verbatim, and every English number
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path
import yaml
from build import ROOT, SETUP_KEYS, TECH_COLS, na_to_dash, parse_table1_tex, slugify_heading

QUOTE_RE = re.compile(r'"([^"\n]*\s[^"\n]*)"')  # double-quoted text with at least two words
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")
FENCE_RE = re.compile(r"^\s*```.*?^\s*```", re.S | re.M)

FORBIDDEN_STAMP_KEYS = {"status", "label_status", "verified_by", "review_stamp", "evidence_grade", "claim_kind"}
RELATIONS = {"predecessor", "successor", "competitor", "alternative"}


def check_schema_and_vocab(root: Path, schema: dict, vocab: dict, errors: list) -> dict:
    req_keys = set(schema["required"])
    allowed_keys = set(schema["properties"].keys())
    id_pat = re.compile(schema["properties"]["id"]["pattern"])
    ev_item_schema = schema["properties"]["evidence"]["items"]
    ev_req = set(ev_item_schema["required"])
    ev_keys = list(ev_item_schema["properties"].keys())
    ev_one_of = [r["required"][0] for r in ev_item_schema["anyOf"]]
    ev_fields = allowed_keys - {"evidence", "tldr", "tldr_zh", "setup", "related", "setup_where"}

    vocab_sets = {
        "problem": {e["value"] for e in vocab["problem"]},
        "stage": {e["value"] for e in vocab["stage"]},
        **{c: {e["value"] for e in vocab.get(c, [])} for c in TECH_COLS},
    }

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

        for vk, vset in vocab_sets.items():
            val = rec.get(vk)
            if val not in vset:
                errors.append(f"[vocab] {p.name}: {vk}={val!r} not in data/vocab.yaml")

        if rec.get("problem") == "psb" and rec.get("stage") != "n/a":
            errors.append(f"[vocab] {p.name}: problem=psb requires stage=n/a")
        if rec.get("problem") != "psb" and rec.get("stage") == "n/a":
            errors.append(f"[vocab] {p.name}: problem={rec.get('problem')} cannot have stage=n/a")

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
    for nm in sorted(set(by_name) - seen):
        errors.append(f"[table1] repo record {nm!r} missing from Table 1 tex")


def check_links_and_content_rules(root: Path, vocab: dict, errors: list):
    md_files = [
        root / "README.md",
        root / "README.zh.md",
        root / "CONTRIBUTING.md",
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

    valid_prob_names = {e["name"] for e in vocab["problem"]}
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


def check_zh_notes(root: Path, errors: list):
    """Each English note has a Chinese note that mirrors it: heading counts, verbatim quotations, and numbers."""
    for ep in sorted((root / "notes").glob("*.md")):
        if not (root / "notes/zh" / ep.name).exists():
            errors.append(f"[sync] notes/{ep.name}: no Chinese note notes/zh/{ep.name}")
    for zp in sorted((root / "notes/zh").glob("*.md")):
        ep = root / "notes" / zp.name
        name = f"notes/zh/{zp.name}"
        if not ep.exists():
            errors.append(f"[sync] {name}: no English note notes/{zp.name}")
            continue
        en, zh = ep.read_text(encoding="utf-8"), zp.read_text(encoding="utf-8")
        for depth in ("###", "####"):
            count = lambda t: len(re.findall(rf"^{depth}\s", FENCE_RE.sub("", t), re.M))
            if count(en) != count(zh):
                errors.append(f"[sync] {name}: {count(zh)} '{depth}' headings, English has {count(en)}")
        for q in dict.fromkeys(QUOTE_RE.findall(body_text(en))):
            if q not in body_text(zh):
                errors.append(f"[sync] {name}: missing quotation \"{q[:60]}\"")
        zh_nums = set(NUMBER_RE.findall(zh))
        missing = [x for x in dict.fromkeys(NUMBER_RE.findall(en)) if x not in zh_nums]
        if missing:
            errors.append(f"[sync] {name}: missing numbers {missing}")


def check_updates(root: Path, records: dict, errors: list):
    p = root / "data/updates.yaml"
    ups = yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None
    if not isinstance(ups, list):
        errors.append("[updates] data/updates.yaml must exist and be a list")
        return
    for i, u in enumerate(ups):
        if not isinstance(u, dict) or set(u) != {"date", "change", "papers"}:
            errors.append(f"[updates] entry {i} must have exactly the keys date, change, papers")
            continue
        if not isinstance(u["date"], str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", u["date"]):
            errors.append(f"[updates] entry {i}: date must be a 'YYYY-MM-DD' string")
        if not isinstance(u["change"], str) or not u["change"].strip():
            errors.append(f"[updates] entry {i}: change must be a non-empty string")
        if not isinstance(u["papers"], list) or any(x not in records for x in u["papers"]):
            errors.append(f"[updates] entry {i}: papers must be a list of existing record ids")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--table1", type=Path, nargs="+", help="External Table 1 source(s) (or TABLE1)")
    args = ap.parse_args()

    schema = json.loads((args.root / "schema/paper.schema.json").read_text(encoding="utf-8"))
    vocab = yaml.safe_load((args.root / "data/vocab.yaml").read_text(encoding="utf-8"))
    errors = []

    records = check_schema_and_vocab(args.root, schema, vocab, errors)
    check_uniqueness(records, errors)
    table1_paths = args.table1 or [Path(x) for x in os.environ.get("TABLE1", "").split()]
    if table1_paths:
        check_table1_roundtrip(records, table1_paths, errors)
    else:
        print("SKIP: external Table 1 round-trip (supply --table1 PATH... or TABLE1).")
    check_links_and_content_rules(args.root, vocab, errors)
    check_updates(args.root, records, errors)
    check_zh_notes(args.root, errors)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s) found.", file=sys.stderr)
        sys.exit(1)

    print(
        f"OK: {len(records)} records passed schema, vocab, uniqueness, "
        f"relative link, updates, and Chinese notes sync checks."
        + (f" Table 1 round-trip ({len(records) * 8} cells) passed." if table1_paths else "")
    )


if __name__ == "__main__":
    main()
