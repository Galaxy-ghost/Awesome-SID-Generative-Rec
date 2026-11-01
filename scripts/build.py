#!/usr/bin/env python3
"""Build README.md, per-paper pages (pages/papers/<id>.md), llms.txt, and llms-full.txt,
or synchronize Table 1 columns from Table 1 in the survey paper (main.tex and supplementary.tex) (--sync-table1).
"""
import argparse
import os
import re
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
TECH_COLS = ["representation", "tokenization", "backbone", "tokenizer", "objective", "inference"]
COL_STAGES = ["Representation", "Tokenization", "Backbone", "Training", "Training", "Inference"]
PROB_MAP = {
    "Paradigms, Systems and Benchmarks": "psb",
    "I. Informativeness": "I",
    "II. Uniqueness and Validity": "II",
    "III. SID–Model Alignment": "III",
    "IV. Utility": "IV",
    "V. Efficiency": "V",
    "VI. Generalization": "VI",
}


def load_vocab(root: Path):
    return yaml.safe_load((root / "data/vocab.yaml").read_text(encoding="utf-8"))


def load_papers(root: Path):
    papers = []
    for p in sorted((root / "data/papers").glob("*.yaml")):
        papers.append(yaml.safe_load(p.read_text(encoding="utf-8")))
    return papers


def slugify_heading(title: str) -> str:
    return re.sub(r"[^a-z0-9 _-]", "", title.strip().lower()).replace(" ", "-")


def norm_tex(s: str) -> str:
    s = s.replace("$\\rightarrow$", "→").replace("$^\\dagger$", "†").replace("--", "–").replace("'", "’").replace("\\&", "&")
    return re.sub(r"\s+", " ", s).strip()


def na_to_dash(val: str) -> str:
    return " / ".join("–" if x == "n/a" else x for x in val.split(" / "))


def parse_table1_tex(paths) -> list:
    rows = []
    for p in paths:
        txt = Path(p).read_text(encoding="utf-8")
        for blk in re.findall(r"\\begin\{tabular\}.*?\\end\{tabular\}", txt, re.S):
            if "\\textbf{Representation}" not in blk:
                continue
            cur_prob = None
            for ln in blk.splitlines():
                m = re.search(r"\\rowcolor\{bandblue\}.*?\\textbf\{([^}]*)\}", ln)
                if m:
                    cur_prob = PROB_MAP[m.group(1).replace("--", "–")]
                    continue
                if "\\cite" not in ln or ln.count("&") != 7:
                    continue
                c = [x.strip() for x in ln.rstrip().rstrip("\\").split("&")]
                name = norm_tex(re.sub(r"~?\\cite\{[^}]*\}", "", c[0]))
                stage = "n/a"
                vals = {}
                for i, key in enumerate(TECH_COLS):
                    v = c[i + 2]
                    mm = re.match(r"\\cellcolor\{modgray\}\\textbf\{(.*)\}$", v)
                    if mm:
                        v = mm.group(1)
                        stage = COL_STAGES[i]
                    vals[key] = norm_tex(v)
                rows.append({"name": name, "venue": norm_tex(c[1]), "problem": cur_prob, "stage": stage, **vals})
    return rows


def sync_table1(root: Path, tex_paths: list):
    rows = parse_table1_tex(tex_paths)
    by_name = {}
    for p in sorted((root / "data/papers").glob("*.yaml")):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        by_name[d["name"]] = (p, d)
    missing = [r["name"] for r in rows if r["name"] not in by_name]
    if missing:
        for nm in missing:
            print(f"ERROR: row in tex missing from data/papers/: {nm}", file=sys.stderr)
        sys.exit(1)
    seen = set()
    for r in rows:
        seen.add(r["name"])
        p, d = by_name[r["name"]]
        d["venue"] = r["venue"]
        d["problem"] = r["problem"]
        d["stage"] = r["stage"]
        for k in TECH_COLS:
            if na_to_dash(str(d.get(k, ""))) != r[k]:
                d[k] = r[k]
        p.write_text(yaml.dump(d, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    for nm in sorted(set(by_name) - seen):
        print(f"WARNING: record {nm} not found in Table 1 tex; kept.", file=sys.stderr)
    print(f"Synchronized {len(rows)} rows from {[str(x) for x in tex_paths]} into data/papers/*.yaml.")


STAGES = ["Representation", "Tokenization", "Backbone", "Training", "Inference"]
HEAT = [(1, "c6dbef"), (4, "6baed6"), (9, "2171b5"), (16, "08306b")]


def title_of(rec: dict) -> str:
    t = re.sub(rf"^{re.escape(rec['name'])}(?:\s*:\s*|\s+)", "", rec["title"], flags=re.I).strip()
    return t[0].upper() + t[1:] if t else rec["name"]


def pipeline(rec: dict, sep: str = " → ") -> str:
    vals = [rec["representation"], rec["tokenization"], rec["backbone"],
            f"{rec['tokenizer']} / {rec['objective']}", rec["inference"]]
    return sep.join(f"**`{v}`**" if s == rec["stage"] else f"`{v}`" for s, v in zip(STAGES, vals))


def format_item(rec: dict) -> str:
    t = title_of(rec)
    code = f" · [Code]({rec['links']['code']})" if rec["links"].get("code") else ""
    poi = " · `POI`" if rec.get("poi") else ""
    return (f"- [{rec['name']}]({rec['links']['arxiv']}) - {t}{'' if t[-1] in '.?!' else '.'} "
            f"{rec['authors']}, {rec['venue']}{poi} · [Page](pages/papers/{rec['id']}.md){code}. {pipeline(rec)}.")


def heat(n: int, anchor: str) -> str:
    color = [c for lo, c in HEAT if n >= lo][-1] if n else ""
    return f"[![{n}](https://img.shields.io/badge/{n}-{color}?style=for-the-badge)](#{anchor})" if n else "·"


def align(rows: list) -> list:
    cells = [[c.strip() for c in r.strip("|").split(" | ")] for r in rows]
    w = [max(len(r[i]) for r in cells) for i in range(len(cells[0]))]
    mid = [c == ":-:" for c in cells[1]]
    pad = lambda c, i: (c[0] + c[1:-1].ljust(w[i] - 2, "-") + c[-1]) if set(c) <= set(":-") else c.center(w[i]) if mid[i] else c.ljust(w[i])
    return ["| " + " | ".join(pad(c, i) for i, c in enumerate(r)) + " |" for r in cells]


def build_readme(vocab: dict, papers: list) -> str:
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    psb = next(p for p in vocab["problem"] if p["value"] == "psb")
    ordered = sorted(papers, key=lambda x: (x["year"], x["id"]))
    cell = {(p["value"], s): [r for r in ordered if (r["problem"], r["stage"]) == (p["value"], s)] for p in problems for s in STAGES}
    psb_list = [r for r in ordered if r["problem"] == "psb"]
    band = lambda p: f"{p['value']}. {p['name']}"
    table = [f"| Problem | {' | '.join(STAGES)} | Total |", "| :-- |" + " :-: |" * (len(STAGES) + 1)]
    for p in problems:
        counts = [len(cell[(p["value"], s)]) for s in STAGES]
        anchors = [slugify_heading(f"{p['value']} × {s}") for s in STAGES]
        table.append(f"| **{p['value']}.** {p['name']} | " + " | ".join(map(heat, counts, anchors)) + f" | **{sum(counts)}** |")
    totals = [sum(len(cell[(p["value"], s)]) for p in problems) for s in STAGES]
    table.append("| **Total** | " + " | ".join(f"**{t}**" for t in totals) + f" | **{sum(totals)}** |")
    lines = [
        "<!--lint disable awesome-github-->",
        "# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        f"> {len(papers)} papers on generative recommendation with Semantic IDs, sorted by the problem each paper fixes (rows) and the pipeline stage it changes (columns).",
        "",
        *align(table),
        "",
        "Click a count to jump to its papers; darker means more papers, `·` means none yet. "
        f"Another {len(psb_list)} papers on {psb['name'].lower()} are listed first. "
        "Every entry links to a generated page with its Table 1 specification, architecture diagram where one exists, and notes; "
        "[TIGER](pages/papers/tiger.md), [RPG](pages/papers/rpg.md) and [OneLoc](pages/papers/oneloc.md) carry annotated walkthroughs. "
        "One YAML record per paper lives in [`data/papers/`](data/papers/); [`llms.txt`](llms.txt) and [`llms-full.txt`](llms-full.txt) are the machine-readable views.",
        "",
        "## Contents",
        "",
        f"- [{psb['name']}](#{slugify_heading(psb['name'])})",
        *[f"- [{band(p)}](#{slugify_heading(band(p))})" for p in problems],
        "",
    ]
    lines += [f"## {psb['name']}", "", f"> {psb['description']}", "", *map(format_item, psb_list), ""]
    for p in problems:
        lines += [f"## {band(p)}", "", f"> {p['description']}", ""]
        for s in STAGES:
            if cell[(p["value"], s)]:
                lines += [f"### {p['value']} × {s}", "", *map(format_item, cell[(p["value"], s)]), ""]
    lines += ["## Contributing", "", "Add one YAML record and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).", ""]
    return "\n".join(lines)


def build_paper_page(rec: dict, vocab: dict, all_papers: list, root: Path) -> str:
    prob = next(e for e in vocab["problem"] if e["value"] == rec["problem"])
    psb = rec["problem"] == "psb"
    band = prob["name"] if psb else f"{rec['problem']}. {prob['name']}"
    code = f" · [Code]({rec['links']['code']})" if rec["links"].get("code") else ""
    defs = {c: {e["value"]: e.get("description") for e in vocab.get(c, [])} for c in TECH_COLS}
    anchor = slugify_heading(band if psb else f"{rec['problem']} × {rec['stage']}")
    lines = [
        f"# {rec['name']}", "",
        f"*{title_of(rec)}* — {rec['authors']}, {rec['venue']}" + (" · `POI`" if rec.get("poi") else ""), "",
        f"[arXiv]({rec['links']['arxiv']}){code} · [Record](../../data/papers/{rec['id']}.yaml) · [← Catalog](../../README.md#{anchor})", "",
        f"> {rec['summary'].strip()}", "",
        f"| {'Group' if psb else 'Problem it fixes'} | Stage it changes |", "| :-- | :-- |",
        f"| **{band}**: {prob['description']} | " + ("No single stage" if psb else f"**{rec['stage']}**") + " |", "",
        "## Pipeline", "",
        f"| {' | '.join(STAGES)} |", "|" + " :-: |" * len(STAGES),
        f"| {pipeline(rec, ' | ')} |", "",
        *[f"- `{rec[c]}`: {defs[c][rec[c]]}" for c in TECH_COLS if defs[c].get(rec[c])], "",
    ]
    image = root / "architectures" / f"{rec['id']}.png"
    if image.is_file():
        lines += ["## Architecture", "", f"![{rec['name']} architecture diagram](../../architectures/{image.name})", ""]
    if rec.get("evidence"):
        lines += ["## Evidence", "", *[f"- **`{ev['field']}`** ({ev['where']}): {ev['quote']}" for ev in rec["evidence"]], ""]
    note_file = root / "notes" / f"{rec['id']}.md"
    if note_file.exists():
        lines += [note_file.read_text(encoding="utf-8").strip(), ""]
    peers = [p for p in sorted(all_papers, key=lambda x: (x["year"], x["id"]))
             if (p["problem"], p["stage"]) == (rec["problem"], rec["stage"]) and p["id"] != rec["id"]]
    if peers:
        where = band if psb else f"{rec['problem']} × {rec['stage']}"
        lines += [f"## Same cell: {where} ({len(peers)} more)", "", "| Paper | Venue | Pipeline |", "| :-- | :-- | :-- |",
                  *[f"| [{p['name']}]({p['id']}.md) | {p['venue']} | {pipeline(p)} |" for p in peers], ""]
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
    ap.add_argument("--sync-table1", type=Path, nargs="*", help="Sync from PATH(s), or TABLE1 when omitted")
    args = ap.parse_args()

    if args.sync_table1 is not None:
        paths = args.sync_table1 or [Path(x) for x in os.environ.get("TABLE1", "").split()]
        if not paths or any(not p.is_file() for p in paths):
            ap.error("--sync-table1 requires existing PATH(s) or TABLE1 source file(s)")
        sync_table1(args.root, paths)
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
