#!/usr/bin/env python3
"""Build README.md, per-paper pages (pages/papers/<id>.md), llms.txt, and llms-full.txt,
or synchronize Table 1 columns from Table1_扩展版.md (--sync-table1).
"""
import argparse
import os
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
TECH_COLS = ["representation", "tokenization", "backbone", "tokenizer", "objective", "inference"]
STAGE_MAP = [
    (2, "Representation", "representation"),
    (3, "Tokenization", "tokenization"),
    (4, "Backbone", "backbone"),
    (5, "Tokenizer", "tokenizer"),
    (6, "Objective", "objective"),
    (7, "Inference", "inference"),
]


def load_vocab(root: Path):
    return yaml.safe_load((root / "data/vocab.yaml").read_text(encoding="utf-8"))


def load_papers(root: Path):
    papers = []
    for p in sorted((root / "data/papers").glob("*.yaml")):
        papers.append(yaml.safe_load(p.read_text(encoding="utf-8")))
    return papers


def slugify_heading(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    return re.sub(r"\s+", "-", s.strip())


def parse_table1_md(md_path: Path):
    lines = md_path.read_text(encoding="utf-8").splitlines()
    start = lines.index("## Table 1")
    tlines = []
    for ln in lines[start + 1:]:
        if ln.startswith("|"):
            tlines.append(ln)
        elif tlines:
            break
    prob_map = {
        "Paradigms, Systems and Benchmarks": "psb",
        "I. Informativeness": "I",
        "II. Uniqueness and Validity": "II",
        "III. SID–Model Alignment": "III",
        "IV. Utility": "IV",
        "V. Efficiency": "V",
        "VI. Generalization": "VI",
    }
    cur_prob = None
    rows = []
    for ln in tlines[2:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(c == "" for c in cells[1:]):
            cur_prob = prob_map[cells[0].strip("*")]
            continue
        m = re.match(
            r"^(★‡\s+|★\s+)?(?:\[([^\]]+)\]\(([^\)]+)\)|([A-Za-z0-9_.-]+))\s*(?:\(([^\)]+)\))?(（基线）)?$",
            cells[0],
        )
        _, lname, url, pname, cit, _ = m.groups()
        name = lname or pname
        authors = re.sub(r",\s*\d{4}[a-z]?$", "", cit or "").strip()
        ym = re.search(r"(\d{4})", cit or "")
        year = int(ym.group(1)) if ym else 2000 + int(re.search(r"’(\d{2})\b", cells[1]).group(1))
        stage = "n/a"
        vals = {}
        for idx, st_name, key in STAGE_MAP:
            v = cells[idx]
            if v.startswith("**") and v.endswith("**"):
                v = v[2:-2].strip()
                stage = "Training" if st_name in ("Tokenizer", "Objective") else st_name
            vals[key] = v
        rows.append({
            "name": name,
            "authors": authors,
            "year": year,
            "venue": cells[1],
            "url": url,
            "problem": cur_prob,
            "stage": stage,
            **vals,
        })
    return rows


def sync_table1(root: Path, md_path: Path):
    rows = parse_table1_md(md_path)
    by_name, by_id, retained = {}, {}, set()
    for p in sorted((root / "data/papers").glob("*.yaml")):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        by_name[d["name"]] = (p, d)
        by_id[d["id"]] = (p, d)
    for r in rows:
        pid = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
        if r["name"] in by_name:
            p, d = by_name[r["name"]]
        elif pid in by_id:
            p, d = by_id[pid]
        else:
            p = root / "data/papers" / f"{pid}.yaml"
            d = {
                "id": pid,
                "title": r["name"],
                "links": {"arxiv": r["url"] or "", "code": None},
                "poi": ("Geo" in r["representation"]) or ("Geo" in r["tokenization"]),
                "summary": f"{r['name']} ({r['venue']}): {r['stage']}-stage method.",
            }
        d["name"] = r["name"]
        d["authors"] = r["authors"]
        d["year"] = r["year"]
        d["venue"] = r["venue"]
        if r["url"]:
            d["links"]["arxiv"] = r["url"]
        d["problem"] = r["problem"]
        d["stage"] = r["stage"]
        for k in TECH_COLS:
            d[k] = r[k]
        p.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
        retained.add(p)
    for p in sorted((root / "data/papers").glob("*.yaml")):
        if p not in retained:
            p.unlink()
    print(f"Synchronized {len(rows)} rows from {md_path} into data/papers/*.yaml.")


def format_item(rec: dict) -> str:
    summary = rec["summary"].strip().rstrip(".")
    summary = re.sub(r"\[([^\]]+)\]", r"(\1)", summary)
    summary = summary[0].upper() + summary[1:] if summary else "Method in Semantic ID generative recommendation"
    code_part = f", [Code]({rec['links']['code']})" if rec["links"].get("code") else ""
    poi_part = " `POI`" if rec.get("poi") else ""
    note_part = " (`Notes`)" if (ROOT / "notes" / f"{rec['id']}.md").exists() else ""
    spec = (
        f"`Rep: {rec['representation']}` · `Tok: {rec['tokenization']}` · "
        f"`Backbone: {rec['backbone']}` · `Train: {rec['tokenizer']} / {rec['objective']}` · "
        f"`Inf: {rec['inference']}`"
    )
    return (
        f"- [{rec['name']}: {rec['title']}]({rec['links']['arxiv']}) - "
        f"{rec['authors']} ({rec['venue']}{poi_part}, [Page](pages/papers/{rec['id']}.md){code_part}){note_part}. "
        f"{spec}. {summary}."
    )


def align_table(rows: list) -> list:
    widths = [max(len(r[c]) for r in rows) for c in range(len(rows[0]))]
    out = []
    for idx, r in enumerate(rows):
        if idx == 1:
            cells = ["-" * w for w in widths]
        else:
            cells = [r[c].ljust(widths[c]) for c in range(len(r))]
        out.append("| " + " | ".join(cells) + " |")
    return out


def build_readme(vocab: dict, papers: list) -> str:
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    stages = [s["value"] for s in vocab["stage"] if s["value"] != "n/a"]
    psb_name = next(p["name"] for p in vocab["problem"] if p["value"] == "psb")

    by_cell = {(p["value"], s): [] for p in problems for s in stages}
    psb_list = []
    for rec in sorted(papers, key=lambda x: (x["year"], x["id"])):
        if rec["problem"] == "psb":
            psb_list.append(rec)
        else:
            by_cell[(rec["problem"], rec["stage"])].append(rec)

    lines = [
        "<!--lint disable awesome-github-->",
        "# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        f"> A curated, taxonomy-driven living repository of {len(papers)} papers on Semantic ID-based Generative Recommendation, organized by a Problem x Stage matrix.",
        "",
        "Each paper is stored as a single declarative record in [`data/papers/`](data/papers/) validated against [`schema/paper.schema.json`](schema/paper.schema.json) and [`data/vocab.yaml`](data/vocab.yaml), with per-paper technical pages in [`pages/papers/`](pages/papers/) (including labml-style annotated deep dives for [`TIGER`](pages/papers/tiger.md), [`RPG`](pages/papers/rpg.md), and [`OneLoc`](pages/papers/oneloc.md)) and machine-readable indices in [`llms.txt`](llms.txt) and [`llms-full.txt`](llms-full.txt).",
        "",
        "## Contents",
        "",
        "- [Problem x Stage Matrix](#problem-x-stage-matrix)",
        f"- [{psb_name}](#{slugify_heading(psb_name)})",
    ]
    for p in problems:
        sec_title = f"{p['value']}. {p['name']}"
        lines.append(f"- [{sec_title}](#{slugify_heading(sec_title)})")
    lines += [
        "",
        "## Problem x Stage Matrix",
        "",
        "Click any cell in the 6 Problems x 5 Stages matrix to jump to the corresponding subsection below:",
        "",
    ]
    t_rows = [
        ["Problem / Stage", *stages, "Total"],
        ["---", *["---" for _ in stages], "---"],
    ]
    for p in problems:
        row_cells = []
        row_total = 0
        for s in stages:
            cnt = len(by_cell[(p["value"], s)])
            row_total += cnt
            sub_anchor = slugify_heading(f"{p['value']} {s}")
            row_cells.append(f"[{cnt}](#{sub_anchor})" if cnt else "0")
        sec_title = f"{p['value']}. {p['name']}"
        t_rows.append([f"**{sec_title}**", *row_cells, f"**{row_total}**"])
    lines += align_table(t_rows)
    lines += [
        "",
        f"## {psb_name}",
        "",
        f"_{next(p['description'] for p in vocab['problem'] if p['value'] == 'psb')}_",
        "",
    ]
    for rec in psb_list:
        lines.append(format_item(rec))
    lines.append("")

    for p in problems:
        sec_title = f"{p['value']}. {p['name']}"
        lines += [
            f"## {sec_title}",
            "",
            f"_{p['description']}_",
            "",
        ]
        for s in stages:
            cell_papers = by_cell[(p["value"], s)]
            if not cell_papers:
                continue
            lines += [f"### {p['value']} {s}", ""]
            for rec in cell_papers:
                lines.append(format_item(rec))
            lines.append("")

    lines += [
        "## Contributing",
        "",
        "See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the two-step workflow: add one `data/papers/<id>.yaml` record and run `make build && make check`.",
        "",
    ]
    return "\n".join(lines)


def build_paper_page(rec: dict, vocab: dict, all_papers: list, root: Path) -> str:
    prob_map = {e["value"]: e for e in vocab["problem"]}
    stage_map = {e["value"]: e for e in vocab["stage"]}
    col_desc = {
        c: {e["value"]: e.get("description", "") for e in vocab.get(c, [])}
        for c in TECH_COLS
    }
    p_info = prob_map[rec["problem"]]
    s_info = stage_map[rec["stage"]]
    prob_label = p_info["name"] if rec["problem"] == "psb" else f"{rec['problem']}. {p_info['name']}"
    code_str = f"[`{rec['links']['code']}`]({rec['links']['code']})" if rec["links"].get("code") else "Not reported"

    lines = [
        f"# {rec['name']}: {rec['title']}",
        "",
        f"[Back to Catalog](../../README.md) · [Paper (`{rec['links']['arxiv']}`)]({rec['links']['arxiv']}) · [Source Record (`data/papers/{rec['id']}.yaml`)](../../data/papers/{rec['id']}.yaml)",
        "",
        f"> **Summary**: {rec['summary']}",
        "",
        "## Taxonomy & Table 1 Specification",
        "",
        "| Field | Value | Vocabulary Definition |",
        "| :--- | :--- | :--- |",
        f"| **Authors & Year** | {rec['authors']} ({rec['year']}) | Published / posted in `{rec['venue']}` |",
        f"| **Problem Band** | `{prob_label}` | {p_info.get('description', '')} |",
        f"| **Primary Stage** | `{rec['stage']}` | {s_info.get('description', '')} |",
        f"| **Representation** | `{rec['representation']}` | {col_desc['representation'].get(rec['representation'], 'See Table 1 notation in data/vocab.yaml.')} |",
        f"| **Tokenization** | `{rec['tokenization']}` | {col_desc['tokenization'].get(rec['tokenization'], 'See Table 1 notation in data/vocab.yaml.')} |",
        f"| **Backbone** | `{rec['backbone']}` | {col_desc['backbone'].get(rec['backbone'], 'See Table 1 notation in data/vocab.yaml.')} |",
        f"| **Tokenizer Training** | `{rec['tokenizer']}` | {col_desc['tokenizer'].get(rec['tokenizer'], 'See Table 1 notation in data/vocab.yaml.')} |",
        f"| **Training Objective** | `{rec['objective']}` | {col_desc['objective'].get(rec['objective'], 'See Table 1 notation in data/vocab.yaml.')} |",
        f"| **Inference Decoding** | `{rec['inference']}` | {col_desc['inference'].get(rec['inference'], 'See Table 1 notation in data/vocab.yaml.')} |",
        f"| **POI / Local-Life** | `{str(rec['poi']).lower()}` | Point-of-interest / geographic recommendation indicator |",
        f"| **Code Repository** | {code_str} | Official or public implementation link |",
        "",
    ]

    image = root / "architectures" / f"{rec['id']}.png"
    if image.is_file():
        lines += ["## Architecture", "", f"![{rec['name']} architecture diagram](../../architectures/{image.name})", ""]

    if rec.get("evidence"):
        lines += ["## Verbatim Evidence & Rationale", ""]
        for ev in rec["evidence"]:
            lines.append(f"- **`{ev['field']}`** ({ev['where']}): {ev['quote']}")
        lines.append("")

    note_file = root / "notes" / f"{rec['id']}.md"
    if note_file.exists():
        lines += [note_file.read_text(encoding="utf-8").strip(), ""]

    peers = [
        p for p in sorted(all_papers, key=lambda x: (x["year"], x["id"]))
        if p["problem"] == rec["problem"] and p["stage"] == rec["stage"] and p["id"] != rec["id"]
    ]
    if peers:
        lines += [
            f"## Peer Methods in `{prob_label}` × `{rec['stage']}` ({len(peers)} peers)",
            "",
            "| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |",
            "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        ]
        for pr in peers:
            lines.append(
                f"| [{pr['name']}]({pr['id']}.md) | {pr['venue']} | `{pr['representation']}` | "
                f"`{pr['tokenization']}` | `{pr['backbone']}` | `{pr['tokenizer']}` | "
                f"`{pr['objective']}` | `{pr['inference']}` |"
            )
        lines.append("")
    return "\n".join(lines)


def build_llms(vocab: dict, papers: list, root: Path):
    prob_map = {e["value"]: e["name"] for e in vocab["problem"]}
    lines = [
        "# Awesome Semantic ID Generative Recommendation",
        "",
        f"> Declarative knowledge base of {len(papers)} papers on Semantic ID-based Generative Recommendation organized by a 6 Problems x 5 Stages matrix.",
        "",
        "## Core Files",
        "- [README.md](README.md): Problem x Stage matrix and full awesome-list catalog.",
        "- [data/vocab.yaml](data/vocab.yaml): Controlled vocabulary for problems, stages, and all 6 Table 1 technical columns.",
        "- [schema/paper.schema.json](schema/paper.schema.json): Single-source JSON Schema for `data/papers/<id>.yaml`.",
        "",
        f"## Papers Index ({len(papers)} records)",
    ]
    for rec in sorted(papers, key=lambda x: x["id"]):
        p_label = prob_map[rec["problem"]] if rec["problem"] == "psb" else f"{rec['problem']}. {prob_map[rec['problem']]}"
        lines.append(
            f"- [{rec['name']}](pages/papers/{rec['id']}.md) ({rec['venue']}): "
            f"[{p_label} | {rec['stage']}] Rep={rec['representation']}, Tok={rec['tokenization']}, "
            f"Backbone={rec['backbone']}, Train={rec['tokenizer']}/{rec['objective']}, Inf={rec['inference']}. "
            f"{rec['summary']}"
        )
    (root / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    full = list(lines) + ["", "## Paper Notes", ""]
    for np in sorted((root / "notes").glob("*.md")):
        full += [f"### Note: {np.stem}", "", np.read_text(encoding="utf-8").strip(), ""]
    (root / "llms-full.txt").write_text("\n".join(full) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--sync-table1", type=Path, nargs="?", const=True, help="Sync from PATH, or TABLE1 when omitted")
    args = ap.parse_args()

    if args.sync_table1 is not None:
        table1 = os.environ.get("TABLE1") if args.sync_table1 is True else args.sync_table1
        if not table1 or not Path(table1).is_file():
            ap.error("--sync-table1 requires an existing PATH or TABLE1 source file")
        sync_table1(args.root, Path(table1))
        return

    vocab = load_vocab(args.root)
    papers = load_papers(args.root)
    (args.root / "README.md").write_text(build_readme(vocab, papers), encoding="utf-8")

    pages_dir = args.root / "pages/papers"
    pages_dir.mkdir(parents=True, exist_ok=True)
    for existing in pages_dir.glob("*.md"):
        existing.unlink()
    for rec in papers:
        (pages_dir / f"{rec['id']}.md").write_text(
            build_paper_page(rec, vocab, papers, args.root), encoding="utf-8"
        )
    build_llms(vocab, papers, args.root)
    print(f"Built README.md, {len(papers)} paper pages in pages/papers/, llms.txt, and llms-full.txt.")


if __name__ == "__main__":
    main()
