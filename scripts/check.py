#!/usr/bin/env python3
"""Validate all paper records and generated views:
1. Schema & vocabulary compliance (schema/paper.schema.json + data/vocab.yaml + 3 hard content rules)
2. Global uniqueness (file stem, id, name, links.arxiv)
3. Table 1 cell-by-cell round-trip against Table1_扩展版.md
4. Relative Markdown links and anchors across README.md, CONTRIBUTING.md, schema/README.md, notes/, pages/
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path
import yaml
from build import ROOT, TECH_COLS, parse_table1_md, slugify_heading

FORBIDDEN_STAMP_KEYS = {"status", "label_status", "verified_by", "review_stamp", "evidence_grade", "claim_kind"}


def check_schema_and_vocab(root: Path, schema: dict, vocab: dict, errors: list) -> dict:
    req_keys = set(schema["required"])
    allowed_keys = set(schema["properties"].keys())
    id_pat = re.compile(schema["properties"]["id"]["pattern"])
    ev_item_schema = schema["properties"]["evidence"]["items"]
    ev_req = set(ev_item_schema["required"])
    ev_fields = allowed_keys - {"evidence"}

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
        if not isinstance(links, dict) or set(links.keys()) != {"arxiv", "code"}:
            errors.append(f"[schema] {p.name}: links must contain exactly 'arxiv' and 'code'")
        elif not isinstance(links.get("arxiv"), str) or not links["arxiv"].startswith("http"):
            errors.append(f"[schema] {p.name}: links.arxiv must be a non-empty URL")

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
                    if not isinstance(item, dict) or set(item.keys()) != ev_req:
                        errors.append(f"[schema] {p.name}: evidence[{idx}] must have keys {sorted(ev_req)}")
                    elif item.get("field") not in ev_fields:
                        errors.append(f"[schema] {p.name}: evidence[{idx}].field={item.get('field')!r} invalid")

        records[rec["id"]] = rec
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


def check_table1_roundtrip(records: dict, table1_path: Path, errors: list):
    if not table1_path.exists():
        errors.append(f"[table1] source file not found: {table1_path}")
        return
    rows = parse_table1_md(table1_path)
    by_name = {r["name"]: r for r in records.values()}
    if len(rows) != len(records):
        errors.append(f"[table1] row count mismatch: Table 1 has {len(rows)}, repo has {len(records)}")

    for r in rows:
        nm = r["name"]
        if nm not in by_name:
            errors.append(f"[table1] row {nm!r} in Table 1 missing from data/papers/")
            continue
        rec = by_name[nm]
        for field in ["authors", "year", "venue", "problem", "stage", *TECH_COLS]:
            if rec[field] != r[field]:
                errors.append(
                    f"[table1] cell mismatch for {nm} / {field}: repo={rec[field]!r} vs table1={r[field]!r}"
                )
        if r["url"] and rec["links"]["arxiv"] != r["url"]:
            errors.append(
                f"[table1] URL mismatch for {nm}: repo={rec['links']['arxiv']!r} vs table1={r['url']!r}"
            )


def check_links_and_content_rules(root: Path, vocab: dict, errors: list):
    md_files = [
        root / "README.md",
        root / "CONTRIBUTING.md",
        root / "schema/README.md",
        *sorted((root / "notes").glob("*.md")),
        *sorted((root / "pages/papers").glob("*.md")),
    ]
    if (root / "pack/constraint-1.md").exists() or (root / "pages/constraint-1.md").exists():
        errors.append("[content-rule-2] constraint-1 page must not exist")

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
        if mf.parent.name == "notes":
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

    link_pat = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for mf in md_files:
        if not mf.exists():
            continue
        txt = mf.read_text(encoding="utf-8")
        for m in link_pat.finditer(txt):
            target = m.group(1).strip()
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


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--table1", type=Path, default=os.environ.get("TABLE1"), help="External Table 1 source (or TABLE1)")
    args = ap.parse_args()

    schema = json.loads((args.root / "schema/paper.schema.json").read_text(encoding="utf-8"))
    vocab = yaml.safe_load((args.root / "data/vocab.yaml").read_text(encoding="utf-8"))
    errors = []

    records = check_schema_and_vocab(args.root, schema, vocab, errors)
    check_uniqueness(records, errors)
    if args.table1 is not None:
        check_table1_roundtrip(records, args.table1, errors)
    else:
        print("SKIP: external Table 1 round-trip (supply --table1 PATH or TABLE1).")
    check_links_and_content_rules(args.root, vocab, errors)

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s) found.", file=sys.stderr)
        sys.exit(1)

    print(
        f"OK: {len(records)} records passed schema, vocab, uniqueness, "
        f"relative link checks."
        + (f" Table 1 round-trip ({len(records) * 8} cells) passed." if args.table1 is not None else "")
    )


if __name__ == "__main__":
    main()
