#!/usr/bin/env python3
"""Build README.md, per-paper pages (pages/papers/<id>.md), index pages (pages/index/), comparison tables (comparisons/),
guides/glossary.md, llms.txt, and llms-full.txt, or synchronize Table 1 columns from Table 1 in the survey paper (main.tex and supplementary.tex) (--sync-table1).
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
SETUP_KEYS = ["datasets", "split", "candidates", "visibility", "sid", "inference_budget", "results_from"]
SETUP_LABELS = ["Datasets", "Split", "Candidates", "Visibility", "SID", "Inference budget", "Results from"]
SECTIONS = ["1. Why This Paper Matters", "2. How It Works", "3. Experimental Findings", "4. Limitations & Critical Analysis"]
SECTIONS_ZH = ["1. 为什么重要", "2. 方法", "3. 实验发现", "4. 局限与分析"]
TOC_SHORT = {"1. Why This Paper Matters": "1. Why It Matters", "2. How It Works": "2. Method",
             "3. Experimental Findings": "3. Experiments", "4. Limitations & Critical Analysis": "4. Limitations",
             "5. Connections to Related Work": "5. Related Work"}
RELATED_TITLE = "5. Connections to Related Work"
LEVELS = ["Overview", "Reading Notes", "Annotated Deep Dive"]
GLANCE_KEYS = ["Key Findings", "Limitation"]
LEGEND = [  # (mark, meaning); the first four are the cell symbols listed in the glossary
    ("`†`", "Inferred from the configuration the paper names."),
    ("`A / B`", "Two branches or configurations."),
    ("`–`", "Not reported."),
    ("`n/a`", "Not applicable."),
    ("**Bold**", "The stage the paper mainly changes."),
    ("Empty cell", "No paper yet."),
    ("`warm`", "Protocol label in setup cards."),
]
ZH_LABELS = {
    "setup": ["数据集", "切分", "候选集", "可见性", "SID 规格", "推理预算", "结果来源"],
    "setup_title": "实验设置",
    "source": "出处",
    "levels": ["概览", "阅读笔记", "代码级精读"],
    "reading_level": "阅读级别",
    "on_this_page": "本页目录",
    "glance_title": "At a Glance",
    "glance_head": ("维度", "摘要"),
    "glance_rows": {
        "Research Problem": "研究问题",
        "Key Contribution": "核心贡献",
        "Modified Stage": "主要改动阶段",
        "Key Findings": "主要发现",
        "Limitation": "局限",
    },
    "related_title": "5. 相关工作",
    "relations": {
        "predecessor": "前序工作",
        "successor": "后续工作",
        "competitor": "同期对比",
        "alternative": "替代方案",
    },
    "view_cell": "查看同格全部论文",
    "no_single_stage": "无单一阶段",
    "links": {"Paper": "论文", "Code": "代码", "Code (third-party)": "代码（第三方）", "Matrix": "矩阵"},
    "problems": {
        "psb": "范式、系统与基准",
        "I": "I. 信息量",
        "II": "II. 唯一性与合法性",
        "III": "III. SID 与模型对齐",
        "IV": "IV. 实用目标",
        "V": "V. 效率",
        "VI": "VI. 泛化",
    },
    "legend": [
        ("`†`", "由论文点名的配置推断得到。"),
        ("`A / B`", "两个分支或两种配置。"),
        ("`–`", "原文未报告。"),
        ("`n/a`", "不适用。"),
        ("**加粗**", "该论文主要改动的阶段。"),
        ("空格", "主标签下暂无条目。"),
        ("`warm`", "条件卡中的协议标签。"),
    ],
}
FLOW_IDS = ["R", "T", "B", "TR", "I"]
MAIN_STYLE = "fill:#eaf2fb,stroke:#6b8fc7"


def title_of(rec: dict) -> str:
    t = re.sub(rf"^{re.escape(rec['name'])}(?:\s*:\s*|\s+)", "", rec["title"], flags=re.I).strip()
    return t[0].upper() + t[1:] if t else rec["name"]


def stage_values(rec: dict) -> list:
    return [rec["representation"], rec["tokenization"], rec["backbone"],
            f"{rec['tokenizer']} / {rec['objective']}", rec["inference"]]


def pipeline(rec: dict, sep: str = " → ") -> str:
    return sep.join(f"**`{v}`**" if s == rec["stage"] else f"`{v}`" for s, v in zip(STAGES, stage_values(rec)))


def mm_label(s: str) -> str:
    return '"' + str(s).replace('"', "#quot;") + '"'


def flow_chart(rec: dict) -> list:
    """Mermaid flowchart of the five stages; the stage the paper mainly changes gets the main style."""
    nodes = " --> ".join(f"{i}[{mm_label(f'{s}<br/>{v}')}]" for i, s, v in zip(FLOW_IDS, STAGES, stage_values(rec)))
    main = [f"    classDef main {MAIN_STYLE}", f"    class {FLOW_IDS[STAGES.index(rec['stage'])]} main"] if rec["stage"] in STAGES else []
    return ["```mermaid", "flowchart LR", f"    {nodes}", *main, "```"]


def related_chart(rec: dict, by_id: dict) -> str:
    """Mermaid graph from this paper to each related paper, labeled by relation; empty without related."""
    rel = rec.get("related", [])
    if not rel:
        return ""
    edges = [f"    P -->|{r['relation']}| {chr(65 + i)}[{mm_label(by_id[r['id']]['name'])}]" for i, r in enumerate(rel)]
    return "\n".join(["```mermaid", "flowchart LR", f"    P[{mm_label(rec['name'])}]", *edges, "```"])


def band(p: dict, zh: bool = False) -> str:
    if zh:
        return ZH_LABELS["problems"][p["value"]]
    return p["name"] if p["value"] == "psb" else f"{p['value']}. {p['name']}"


def stage_label(rec: dict, zh: bool = False) -> str:
    if rec["problem"] == "psb":
        return ZH_LABELS["no_single_stage"] if zh else "No single stage"
    return rec["stage"]


def cell_label(rec: dict, probs: dict, zh: bool = False) -> str:
    return band(probs["psb"], zh) if rec["problem"] == "psb" else f"{rec['problem']} × {rec['stage']}"


def code_links(rec: dict, zh: bool = False) -> list:
    return [(ZH_LABELS["links"][lab] if zh else lab, rec["links"][k])
            for k, lab in (("code", "Code"), ("code_third_party", "Code (third-party)")) if rec["links"].get(k)]


def link_line(rec: dict, extra=(), zh: bool = False) -> str:
    paper_lab = ZH_LABELS["links"]["Paper"] if zh else "Paper"
    return " · ".join([f"[{paper_lab}]({rec['links']['arxiv']})", *(f"[{l}]({u})" for l, u in code_links(rec, zh)), *extra])


def by_year(papers: list) -> list:
    return sorted(papers, key=lambda x: (x["year"], x["id"]))


def parse_notes(text: str, sections=SECTIONS) -> dict:
    """Split notes into the At a Glance lines, the standard sections, and the remaining text."""
    out = {"glance": {}, "sections": {}, "rest": [], "fences": [], "text": text}
    cur, fence = None, False
    for ln in text.splitlines():
        fm = re.match(r"^\s*```(\w*)", ln)
        hm = None if fence or fm else re.match(r"^(#{1,6})\s+(.+?)\s*$", ln)
        if fm:
            if not fence:
                out["fences"].append(fm.group(1))
            fence = not fence
        if hm:
            depth, title = len(hm.group(1)), hm.group(2)
            if depth == 2 and title == "At a Glance":
                cur = "glance"
                continue
            if depth == 3 and title in sections:
                cur = title
                out["sections"][title] = []
                continue
            if cur == "glance" or depth <= 3:
                cur = None
        if cur == "glance":
            gm = re.match(rf"^({'|'.join(GLANCE_KEYS)}):\s*(.+)$", ln)
            if gm:
                out["glance"][gm.group(1)] = gm.group(2).strip()
        elif cur:
            out["sections"][cur].append(ln)
        else:
            out["rest"].append(ln)
    out["sections"] = {k: "\n".join(v).strip() for k, v in out["sections"].items()}
    out["rest"] = "\n".join(out["rest"]).strip()
    return out


def reading_level(n, sections=SECTIONS) -> int:
    if not n:
        return 1
    has = lambda idx: all(sections[i] in n["sections"] for i in idx)
    if (has(range(4)) and "math" in n["fences"] and any(f != "math" for f in n["fences"])
            and re.search(r"^(Simplifications|简化说明)[：:]", n["text"], re.M)):
        return 3
    return 2 if has((0, 2, 3)) else 1


def short_links(text: str) -> str:
    """Show each URL as a short link: its #anchor as the label, or "link" without one."""
    def sub(m):
        url, tail = re.match(r"(.*?)([.,;:)]*)$", m.group(0)).groups()
        return f"[{url.partition('#')[2] or 'link'}]({url}){tail}"
    return re.sub(r"https?://\S+", sub, text)


def setup_card(rec: dict, folded: bool = False, zh: bool = False) -> str:
    """Setup card; folded wraps the entire card in a collapsible <details> block."""
    st, sw = rec.get("setup"), rec.get("setup_where", {})
    if not st:
        return ""
    labels = ZH_LABELS["setup"] if zh else SETUP_LABELS
    title = ZH_LABELS["setup_title"] if zh else "Experimental setup"
    src_lab = ZH_LABELS["source"] if zh else "Source"
    pairs = list(zip(SETUP_KEYS, labels))
    if not folded:
        return f"**{title}**\n\n" + "\n".join(
            f"- **{lab}**: {st[k]}" + (f"\n  - {src_lab}: {sw[k]}" if sw.get(k) else "") for k, lab in pairs)
    items = "\n".join(
        f"- **{lab}**: {st[k]}" + (f"\n  - {src_lab}: {short_links(sw[k])}" if sw.get(k) else "") for k, lab in pairs)
    return f"<details>\n<summary>{title}</summary>\n\n{items}\n\n</details>"


def build_paper_page(rec: dict, vocab: dict, by_id: dict, n, root: Path, zh: bool = False) -> str:
    probs = {e["value"]: e for e in vocab["problem"]}
    prob = probs[rec["problem"]]
    anchor = slugify_heading(cell_label(rec, probs))
    sections = SECTIONS_ZH if zh else SECTIONS
    level = reading_level(n, sections)
    defs = {c: {e["value"]: e.get("description") for e in vocab.get(c, [])} for c in TECH_COLS}
    
    if zh:
        glance_rows_map = ZH_LABELS["glance_rows"]
        glance = [
            (glance_rows_map["Research Problem"], f"{band(prob, True)}: {prob['description']}"),
            (glance_rows_map["Key Contribution"], rec.get("tldr_zh") or rec.get("tldr")),
            (glance_rows_map["Modified Stage"], stage_label(rec, True)),
        ]
        for k in GLANCE_KEYS:
            val = (n or {}).get("glance", {}).get(k)
            if val:
                glance.append((glance_rows_map[k], val))
        table_headers = ZH_LABELS["glance_head"]
    else:
        glance = [
            ("Research Problem", f"{band(prob)}: {prob['description']}"),
            ("Key Contribution", rec.get("tldr")),
            ("Modified Stage", stage_label(rec)),
            *((k, (n or {}).get("glance", {}).get(k)) for k in GLANCE_KEYS),
        ]
        table_headers = ("Aspect", "Summary")

    rows = [f"| {a} | {v.strip().replace('|', chr(92) + '|')} |" for a, v in glance if v]
    
    tldr_text = (rec.get("tldr_zh") if zh else rec.get("tldr")) or ""
    tldr_block = ["> [!NOTE]", f"> {tldr_text}"] if tldr_text else []
    
    glance_block = ["\n".join([f"| {table_headers[0]} | {table_headers[1]} |", "| :-- | :-- |", *rows])] if rows else []
    
    blocks = [("TL;DR", tldr_block)] if tldr_block else []
    blocks += [("At a Glance" if not zh else ZH_LABELS["glance_title"], glance_block)] if glance_block else []
    
    image = root / "architectures" / f"{rec['id']}.png"
    setup_card_str = setup_card(rec, folded=True, zh=zh)
    inserts = {
        sections[1]: f"![{rec['name']} architecture diagram](../../architectures/{image.name})" if image.is_file() else "",
        sections[2]: setup_card_str,
    }
    for t in sections:
        parts = [p for p in (inserts.get(t), (n or {}).get("sections", {}).get(t)) if p]
        blocks += [(t, parts)] if parts else []
    blocks += [(None, [n["rest"]])] if n and n["rest"] else []
    
    rel_title = ZH_LABELS["related_title"] if zh else RELATED_TITLE
    rel_rels = ZH_LABELS["relations"]
    rel_view_all = ZH_LABELS["view_cell"]
    rel_matrix_link = f"../../README.zh.md#{anchor}" if zh else f"../../README.md#{anchor}"
    
    rel_items = []
    for r in rec.get("related", []):
        rel_type = rel_rels.get(r['relation'], r['relation'].capitalize())
        target_name = by_id[r['id']]['name']
        target_file = f"{r['id']}.md"
        note = r['note']
        where = r['where']
        rel_items.append(f"- **{rel_type}** · [{target_name}]({target_file}): {note}\n  - Source: {where}")
    rel_str = "\n".join(rel_items)
    
    blocks.append((rel_title, [p for p in (related_chart(rec, by_id), rel_str, f"[{rel_view_all}]({rel_matrix_link})") if p]))
    
    tags = [band(prob, zh), stage_label(rec, zh)] + (["POI"] if rec.get("poi") else [])
    
    toc_links = []
    for t, _ in blocks:
        if not t:
            continue
        short_t = TOC_SHORT.get(t, t) if not zh else t
        toc_links.append(f"[{short_t}](#{slugify_heading(t)})")
    toc = " · ".join(toc_links)
    
    vals = dict.fromkeys(f"- `{rec[c]}`: {defs[c][rec[c]]}" for c in TECH_COLS if defs[c].get(rec[c]))
    
    switch_link = f"[中文](../zh/papers/{rec['id']}.md)" if not zh else f"[English](../../papers/{rec['id']}.md)"
    matrix_link = f"[Matrix](../../README.md#{anchor})" if not zh else f"[矩阵](../../../README.zh.md#{anchor})"
    
    line1_links = link_line(rec, [matrix_link, switch_link], zh=zh)
    
    level_name = LEVELS[level - 1] if not zh else ZH_LABELS["levels"][level - 1]
    level_label_str = ZH_LABELS["reading_level"] if zh else "Reading level"
    on_this_page_str = ZH_LABELS["on_this_page"] if zh else "On this page"
    
    lines = [
        f"# {rec['name']}", "",
        f"*{title_of(rec)}* — {rec['authors']} · {rec['venue']}", "",
        " · ".join(f"`{t}`" for t in tags) + " · " + line1_links, "",
        f"{level_label_str}: {level_name} (Level {level}) · {on_this_page_str}: {toc}", "",
        *flow_chart(rec), "",
        *vals, "",
    ]
    for t, parts in blocks:
        lines += ([f"### {t}", ""] if t else []) + [x for p in parts for x in (p, "")]
    return "\n".join(lines)



def heat(n: int, anchor: str) -> str:
    color = [c for lo, c in HEAT if n >= lo][-1] if n else ""
    return f"[![{n}](https://img.shields.io/badge/{n}-{color}?style=for-the-badge)](#{anchor})" if n else ""


def align(rows: list) -> list:
    cells = [[c.strip() for c in r.strip("|").split(" | ")] for r in rows]
    w = [max(len(r[i]) for r in cells) for i in range(len(cells[0]))]
    mid = [c == ":-:" for c in cells[1]]
    pad = lambda c, i: (c[0] + c[1:-1].ljust(w[i] - 2, "-") + c[-1]) if c and set(c) <= set(":-") else c.center(w[i]) if mid[i] else c.ljust(w[i])
    return ["| " + " | ".join(pad(c, i) for i, c in enumerate(r)) + " |" for r in cells]


def ref(rec: dict) -> str:
    """Reference-style link to the paper page; awesome-lint requires absolute URLs in inline list links."""
    return f"[{rec['name']}][{'' if rec['name'].lower() == rec['id'] else rec['id']}]"


def format_item(rec: dict) -> str:
    first = f"- {ref(rec)} - {rec['venue']}" + (" · `POI`" if rec.get("poi") else "")
    return "<br>\n  ".join([first, *[x for x in ((rec.get("tldr") or "").strip(), link_line(rec)) if x]])


def build_readme(vocab: dict, papers: list, by_id: dict, levels: dict, updates: list) -> str:
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    psb = next(p for p in vocab["problem"] if p["value"] == "psb")
    ordered = by_year(papers)
    cell = {(p["value"], s): [r for r in ordered if (r["problem"], r["stage"]) == (p["value"], s)] for p in problems for s in STAGES}
    psb_list = [r for r in ordered if r["problem"] == "psb"]
    table = [f"| Problem | {' | '.join(STAGES)} | Total |", "| :-- |" + " :-: |" * (len(STAGES) + 1)]
    for p in problems:
        counts = [len(cell[(p["value"], s)]) for s in STAGES]
        anchors = [slugify_heading(f"{p['value']} × {s}") for s in STAGES]
        table.append(f"| **{p['value']}.** {p['name']} | " + " | ".join(map(heat, counts, anchors)) + f" | **{sum(counts)}** |")
    totals = [sum(len(cell[(p["value"], s)]) for p in problems) for s in STAGES]
    table.append("| **Total** | " + " | ".join(f"**{t}**" for t in totals) + f" | **{sum(totals)}** |")
    starters = [r for r in ordered if levels[r["id"]] == 3]
    lines = [
        "<!--lint disable awesome-github-->",
        "# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)", "",
        "## Scope", "",
        f"This list collects {len(papers)} papers on generative recommendation with Semantic IDs (SIDs). "
        f"The matrix places {sum(totals)} of them by the problem each paper fixes and the pipeline stage it mainly changes. "
        f"The other {len(psb_list)} are {psb['name'].lower()}. It also includes methods that use SIDs as features. "
        "Papers on POI and local-life recommendation carry a `POI` tag and are listed in the [POI index](pages/index/poi.md).", "",
        "## Where to Start", "",
        "- New to the topic: [Start Here](guides/start-here.md)",
        "- Looking for research problems: [Problem × Stage Matrix](#problem--stage-matrix)",
        "- Choosing a method by stage: [Papers by Stage](pages/index/stages.md)",
        "- Looking for code: [Papers with Code](pages/index/code.md)",
        "- LLMs and tools: [llms.txt](llms.txt)", "",
        "## Starter Papers", "",
        *[f"- {ref(r)}" + (f" - {r['tldr'].strip()}" if r.get("tldr") else "") for r in starters], "",
        "## Problem × Stage Matrix", "",
        *align(table), "",
        "Click a count to jump to its papers; darker means more papers.", "",
        *align(["| Mark | Meaning |", "| :-- | :-- |", *[f"| {m} | {t} |" for m, t in LEGEND]]), "",
        "The [glossary](guides/glossary.md) defines every value in the paper pages.", "",
        "## Recent Updates", "",
        *[f"- {u['date']}: {u['change'].strip()}" + (f" Papers: {', '.join(ref(by_id[x]) for x in u['papers'])}." if u["papers"] else "")
          for u in sorted(updates, key=lambda u: u["date"], reverse=True)], "",
        "## All Papers", "",
        *[f"- [{band(p)}][]" for p in [psb, *problems]], "",
        f"## {band(psb)}", "", f"> {psb['description']}", "", *map(format_item, psb_list), "",
    ]
    for p in problems:
        lines += [f"## {band(p)}", "", f"> {p['description']}", ""]
        for s in STAGES:
            if cell[(p["value"], s)]:
                lines += [f"### {p['value']} × {s}", "", *map(format_item, cell[(p["value"], s)]), ""]
    lines += ["## Contributing", "", "Add one YAML record and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).", "",
              *[f"[{band(p).lower()}]: #{slugify_heading(band(p))}" for p in [psb, *problems]],
              *[f"[{r['id']}]: pages/papers/{r['id']}.md" for r in sorted(papers, key=lambda x: x["id"])], ""]
    return "\n".join(lines)


def build_indexes(vocab: dict, papers: list) -> dict:
    probs = {e["value"]: e for e in vocab["problem"]}
    ordered = by_year(papers)
    link = lambda r: f"[{r['name']}](../papers/{r['id']}.md)"
    table = lambda head, rows: [f"| {' | '.join(head)} |", "|" + " :-- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]]
    stages = ["# Papers by Stage", "",
              "Each table lists the papers whose main change sits in one stage, with that stage's Table 1 value. "
              f"Papers on {probs['psb']['name'].lower()} change no single stage; the "
              f"[README](../../README.md#{slugify_heading(probs['psb']['name'])}) lists them.", "",
              "Side-by-side tables: " + " · ".join(f"[{t}](../../comparisons/{f}.md)" for f, t, *_ in COMPARISONS), ""]
    for s in STAGES:
        rows = [[link(r), r["venue"], band(probs[r["problem"]]),
                 f"`{r['tokenizer']} / {r['objective']}`" if s == "Training" else f"`{r[s.lower()]}`"]
                for r in ordered if r["stage"] == s]
        stages += [f"## {s}", "", *table(["Paper", "Venue", "Problem", s], rows), ""]
    coded = [r for r in ordered if code_links(r)]
    code = ["# Papers with Code", "",
            f"{len(coded)} papers link to code. `Code` is the authors' repository; `Code (third-party)` is an implementation by others.", "",
            *table(["Paper", "Venue", "Problem × Stage", "Code"],
                   [[link(r), r["venue"], cell_label(r, probs), " · ".join(f"[{l}]({u})" for l, u in code_links(r))] for r in coded]), ""]
    poi = [r for r in ordered if r.get("poi")]
    poi_page = ["# POI and Local-Life Papers", "",
                f"{len(poi)} papers target POI, local-life, or spatial recommendation. Bold marks the stage each paper mainly changes.", "",
                *table(["Paper", "Venue", "Problem × Stage", "Pipeline"], [[link(r), r["venue"], cell_label(r, probs), pipeline(r)] for r in poi]), ""]
    return {"stages.md": "\n".join(stages), "code.md": "\n".join(code), "poi.md": "\n".join(poi_page)}


COMPARISONS = [  # (file, title, intro, sort keys, [(header, record key or setup.<key>)])
    ("tokenizer", "Tokenizer", "How each paper builds its Semantic IDs.", ["tokenization"],
     [("Information Source", "representation"), ("Quantization", "tokenization"),
      ("SID Length, Codebook, Collisions", "setup.sid"), ("Tokenizer Update", "tokenizer")]),
    ("training", "Training", "How each paper trains its tokenizer and generator.", ["tokenizer", "objective"], [("Tokenizer Update", "tokenizer"), ("Objective", "objective")]),
    ("inference", "Inference", "How each paper generates Semantic IDs at inference.", ["inference"],
     [("Backbone", "backbone"), ("Decoding", "inference"), ("Search Budget", "setup.inference_budget"),
      ("Visibility", "setup.visibility")]),
]


def cell_text(s: str) -> str:
    return re.sub(r"\s+", " ", str(s)).strip().replace("|", "\\|")


def build_comparisons(papers: list, by_id: dict) -> dict:
    link = lambda r: f"[{r['name']}](../pages/papers/{r['id']}.md)"
    val = lambda r, k: cell_text((r.get("setup") or {}).get(k[6:], "no card yet")) if k.startswith("setup.") else f"`{cell_text(r[k])}`"
    rel = lambda r: "; ".join(f"{x['relation'].capitalize()}: {link(by_id[x['id']])}" for x in r.get("related", [])) or "–"
    out = {}
    for f, title, intro, keys, cols in COMPARISONS:
        rows = sorted(papers, key=lambda r: [r[k].lower() for k in keys] + [r["name"].lower()])
        head = ["Paper", *(h for h, _ in cols), "Related"]
        table = [f"| {' | '.join(head)} |", "|" + " :-- |" * len(head),
                 *[f"| {' | '.join([link(r), *(val(r, k) for _, k in cols), rel(r)])} |" for r in rows]]
        out[f"{f}.md"] = "\n".join([f"# {title} Comparison", "", f"{intro} Values are Table 1 entries defined in the "
                                    "[glossary](../guides/glossary.md); setup text is quoted from each paper's setup card.", "",
                                    *table, ""])
    return out


def build_glossary(vocab: dict) -> str:
    entry = lambda v, d: f"- `{v}`: {d}" if d else f"- `{v}`"
    lines = ["# Glossary", "",
             "This page is generated from [`data/vocab.yaml`](../data/vocab.yaml). "
             "It defines the values in Table 1, the paper pages, and the indexes.", "",
             "## Symbols", "", *[f"- {m}: {t}" for m, t in LEGEND[:4]], "",
             "## Problems", "", *[entry(p["value"], f"**{p['name']}.** {p['description']}") for p in vocab["problem"]], ""]
    for c, s in zip(TECH_COLS, COL_STAGES):
        head = c.capitalize() + ("" if s == c.capitalize() else f" ({s})")
        lines += [f"## {head}", "", *[entry(e["value"], e.get("description")) for e in vocab[c]], ""]
    return "\n".join(lines)


def llm_fields(rec: dict, probs: dict) -> list:
    f = [f"Problem: {band(probs[rec['problem']])}", f"Stage: {stage_label(rec)}",
         "; ".join(f"{c.capitalize()}: {rec[c]}" for c in TECH_COLS)]
    f += [f"TL;DR: {rec['tldr'].strip()}"] if rec.get("tldr") else []
    f += [f"[{l}]({u})" for l, u in code_links(rec)]
    return f + [f"Setup card: {'yes' if rec.get('setup') else 'no'}", f"Relations: {len(rec.get('related', []))}"]


def build_llms(vocab: dict, papers: list, notes: dict) -> tuple:
    probs = {e["value"]: e for e in vocab["problem"]}
    ordered = sorted(papers, key=lambda x: x["id"])
    head = [
        "# Awesome Semantic ID Generative Recommendation", "",
        f"> {len(papers)} papers on generative recommendation with Semantic IDs (SIDs), each placed by the problem it fixes "
        "and the pipeline stage it mainly changes.", "",
        "## Core Files", "",
        "- [README.md](README.md): Problem × Stage matrix and the full list of papers.",
        "- [guides/glossary.md](guides/glossary.md): Definitions of every problem and Table 1 value.",
        "- [pages/index/stages.md](pages/index/stages.md): Papers grouped by the stage they mainly change.",
        "- [pages/index/code.md](pages/index/code.md): Papers that link to code.",
        "- [pages/index/poi.md](pages/index/poi.md): Papers on POI and local-life recommendation.",
        "- [data/vocab.yaml](data/vocab.yaml): Controlled vocabulary for problems, stages, and the six Table 1 columns.",
        "- [schema/paper.schema.json](schema/paper.schema.json): JSON Schema for `data/papers/<id>.yaml`.", "",
    ]
    short = head + [f"## Papers ({len(papers)} records)", ""] + [
        f"- [{r['name']}](pages/papers/{r['id']}.md) · {r['venue']} · " + " · ".join(llm_fields(r, probs)) for r in ordered]
    full = list(head)
    for r in ordered:
        full += [f"## {r['name']}", "", f"- Page: pages/papers/{r['id']}.md", f"- Venue: {r['venue']}",
                 *[f"- {x}" for x in llm_fields(r, probs)], ""]
        if r.get("setup"):
            full += ["### Setup card", "", setup_card(r).split("\n\n", 1)[1], ""]
        if r.get("related"):
            full += ["### Related", "", *[f"- id: {x['id']}; relation: {x['relation']}; note: {x['note']}; where: {x['where']}"
                                         for x in r["related"]], ""]
        if r["id"] in notes:
            full += ["### Notes", "", notes[r["id"]]["text"].strip(), ""]
    return "\n".join(short) + "\n", "\n".join(full) + "\n"


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

    root = args.root
    vocab, papers = load_vocab(root), load_papers(root)
    by_id = {r["id"]: r for r in papers}
    notes = {p.stem: parse_notes(p.read_text(encoding="utf-8")) for p in sorted((root / "notes").glob("*.md"))}
    levels = {r["id"]: reading_level(notes.get(r["id"])) for r in papers}
    updates = yaml.safe_load((root / "data/updates.yaml").read_text(encoding="utf-8")) or []
    (root / "README.md").write_text(build_readme(vocab, papers, by_id, levels, updates), encoding="utf-8")
    for sub, files in (("pages/papers", {f"{r['id']}.md": build_paper_page(r, vocab, by_id, notes.get(r["id"]), root) for r in papers}),
                       ("pages/index", build_indexes(vocab, papers)), ("comparisons", build_comparisons(papers, by_id))):
        out = root / sub
        out.mkdir(parents=True, exist_ok=True)
        for existing in out.glob("*.md"):
            existing.unlink()
        for name, text in files.items():
            (out / name).write_text(text, encoding="utf-8")
    (root / "guides").mkdir(exist_ok=True)
    (root / "guides/glossary.md").write_text(build_glossary(vocab), encoding="utf-8")
    short, full = build_llms(vocab, papers, notes)
    (root / "llms.txt").write_text(short, encoding="utf-8")
    (root / "llms-full.txt").write_text(full, encoding="utf-8")
    print(f"Built README.md, {len(papers)} paper pages, 3 index pages, 3 comparison tables, guides/glossary.md, llms.txt, and llms-full.txt.")


if __name__ == "__main__":
    main()
