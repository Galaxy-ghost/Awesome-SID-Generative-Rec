#!/usr/bin/env python3
"""Build README.md, per-paper pages (pages/papers/<id>.md), index pages (pages/index/), comparison tables (comparisons/),
guides/glossary.md, llms.txt, and llms-full.txt, plus the Chinese views README.zh.md, pages/zh/papers/, pages/zh/index/,
and guides/glossary.zh.md, or synchronize Table 1 columns from Table 1 in the survey paper (main.tex and supplementary.tex) (--sync-table1).
"""
import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote
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
    """GitHub heading anchor: lowercase, keep letters (including CJK), digits, spaces, '_' and '-'."""
    return re.sub(r"[^\w -]", "", title.strip().lower()).replace(" ", "-")


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
HEAT = [(1, "eef5fc"), (4, "d6e8fa"), (9, "bad8f7"), (16, "96c5f3")]
ALSO_BADGE_BG = "f1f5f9"
MODALITY_ROWS = [
    ("single", "Single-modal", "单模态", ("single-modal", "single-modal--cf")),
    ("multi", "Multimodal", "多模态", ("multimodal", "multimodal--cf")),
    ("other", "Other", "其他", ("other", "other--cf")),
]
MODALITY_BUCKETS = [
    (("single", False), "Single-modal", "单模态",
     "One content modality (`Text` or `Audio`), without `CF` in the tokenizer input.",
     "构码输入含单一内容模态（`Text` 或 `Audio`），未标 `CF`。"),
    (("single", True), "Single-modal + CF", "单模态 + 协同",
     "One content modality combined with collaborative filtering (`CF`) in the tokenizer input.",
     "构码输入含单一内容模态并融合协同过滤信号（`CF`）。"),
    (("multi", False), "Multimodal", "多模态",
     "Two or more content modalities (or `MM`), without `CF` in the tokenizer input.",
     "构码输入含两种及以上内容模态（或 `MM`），未标 `CF`。"),
    (("multi", True), "Multimodal + CF", "多模态 + 协同",
     "Two or more content modalities (or `MM`) combined with `CF` in the tokenizer input.",
     "构码输入含两种及以上内容模态（或 `MM`）并融合协同过滤信号（`CF`）。"),
    (("other", False), "Other", "其他",
     "Non-content tokenizer representations (such as spatial features alone), without `CF`.",
     "构码输入仅含非内容模态特征（如纯空间特征），未标 `CF`。"),
    (("other", True), "Other + CF", "其他 + 协同",
     "Pure collaborative (`CF`) or structured-attribute + `CF` representations without text, image, or audio.",
     "构码输入为纯协同信号（`CF`）或结构化属性加 `CF`，不含文本、图像或音频模态。"),
    (("unknown", None), "Unspecified Representation", "表征未明",
     "Table 1 `representation` is unreported (`–`) or records domain scope (`Multi-Dom`, `Cross-Dom`) without a modality override.",
     "Table 1 的 `representation` 未报告（`–`），或仅记录领域范围（`Multi-Dom`、`Cross-Dom`）且暂无模态覆盖字段。"),
    (("na", None), "Not Applicable", "不适用",
     "Diagnostic or non-method entries where tokenizer input representation does not apply (`n/a`).",
     "不涉及构码输入表征的诊断资源或非单一方法条目（`n/a`）。"),
]
AUX_SIGNAL_LIST = [
    ("Geo", "Geographic or spatial features in the representation.", "表征中包含地理或空间特征。"),
    ("Time", "Explicit interaction timestamps in the representation.", "表征中包含显式交互时间特征。"),
    ("SID", "Discrete Semantic IDs concatenated with dense representations.", "表征中拼接离散 SID（稠密与生成混合检索）。"),
]
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
    "stages_zh": {
        "Representation": "表征",
        "Tokenization": "编号",
        "Backbone": "骨干",
        "Training": "训练",
        "Inference": "推理",
    },
    "cols_zh": {
        "representation": "表征（Representation）",
        "tokenization": "编号（Tokenization）",
        "backbone": "生成骨干（Backbone）",
        "tokenizer": "编号器更新（Training）",
        "objective": "训练目标（Training）",
        "inference": "推理解码（Inference）",
    },
    "setup": ["数据集", "切分", "候选集", "可见性", "SID 规格", "推理预算", "结果来源"],
    "setup_title": "实验设置",
    "source": "出处",
    "levels": ["概览", "阅读笔记", "代码级精读"],
    "reading_level": "阅读级别",
    "card": {"Title": "题目", "Authors": "作者", "Venue": "发表", "Cell": "问题与阶段", "Links": "链接", "Reading level": "阅读级别"},
    "overview": "篇",
    "level_n": "第 {n} 级",
    "glance_title": "速览",
    "colon": "：",
    "on_this_page": "本页目录",
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
    "also_label": "补充",
    "links": {"Paper": "论文", "Code": "代码", "Code (third-party)": "代码（第三方）",
              "Matrix": "问题 × 阶段矩阵", "Stages": "按阶段索引", "Modality": "按模态索引"},
    "problems": {
        "psb": "范式、系统与基准",
        "I": "I. 信息量",
        "II": "II. 唯一性与合法性",
        "III": "III. SID 与模型对齐",
        "IV": "IV. 实用目标",
        "V": "V. 效率",
        "VI": "VI. 泛化",
    },
    "readme": {
        "badges": ("论文", "更新", "许可"),
        "intro": "围绕研究问题与五阶段流程组织的语义 ID（Semantic ID）生成式推荐论文索引与精读笔记。",
        "scope_title": "收录范围",
        "scope": "本仓库收录 {n} 篇语义 ID（Semantic ID，SID）生成式推荐论文。其中 {m} 篇按研究问题与主要改动的流程阶段放入矩阵，"
                 "其余 {k} 篇归入范式、系统与基准；将离散 SID 作为特征输入判别式或混合架构的工作一并收录。面向 POI 与本地生活场景的论文标有 `POI`，"
                 "汇总见 [POI 索引](pages/zh/index/poi.md)。",
        "start_title": "阅读导航",
        "start_head": ("阅读目标", "推荐入口"),
        "start": [("初次了解本方向", "[入门指南](guides/start-here.zh.md)"),
                  ("按研究问题定位论文", "[问题 × 阶段矩阵](#问题--阶段矩阵)"),
                  ("按流程阶段横向对比", "[按阶段索引](pages/zh/index/stages.md)"),
                  ("按构码输入模态检索", "[按构码输入模态索引](pages/zh/index/modality.md)"),
                  ("查找开源实现", "[有代码的论文](pages/zh/index/code.md)"),
                  ("供 LLM 与检索工具读取", "[llms.txt](llms.txt)（英文）")],
        "starter_title": "代表性必读论文",
        "starter_head": ("论文", "核心机制", "发表"),
        "matrix_title": "问题 × 阶段矩阵",
        "matrix_note": "主归类与综述 Table 1 一致；补充标签列出论文明确针对的其他研究问题或流程阶段。",
        "problem": "研究问题",
        "total": "合计",
        "click": "点击数字跳转至对应格子的论文列表；左段为主归类篇数（浅蓝越深篇数越多），右段 `+n` 为补充标签同时配对该问题与阶段的篇数。",
        "also_in_cell": "补充归入本格：",
        "modality_title": "构码输入模态",
        "modality_note": "按综述 Table 1 `representation` 列的构码输入内容模态与协同过滤（`CF`）信号分组；“协同”仅指构码输入含 `CF`，`A / B` 双分支配置分别计入各分支所在格。",
        "modality_head": ("内容模态", "未标 CF", "含协同（CF）"),
        "modality_unknown": "**表征未明**：[{n} 篇]({path}#{anchor})（`–`、`Multi-Dom`、`Cross-Dom` 或含未报告分支）。",
        "modality_na": "**不适用**：[{n} 篇]({path}#{anchor})（`n/a`）。",
        "modality_aux": "**附加信号**：{links}。",
        "legend_head": ("标记", "含义"),
        "glossary": "论文页与矩阵中的全部符号及缩写释义见 [术语表](guides/glossary.zh.md)。",
        "updates_title": "最近更新",
        "papers": "涉及论文：",
        "all_title": "全部论文",
        "contrib_title": "参与贡献",
        "contrib": "新增或修改 `data/papers/<id>.yaml` 后运行 `make build && make check`。双语维护规范见 [`CONTRIBUTING.zh.md`](CONTRIBUTING.zh.md)。",
    },
    "index": {
        "stages_title": "按阶段索引",
        "stages_intro": "下表按主要改动的流程阶段分组列出论文及其在综述 Table 1 中的对应取值。"
                        "范式、系统与基准类论文横跨多个阶段或提供评测基准，见 [README]({readme}#{anchor})。",
        "compare": "多维并排对比表（英文）：",
        "head": ("论文", "发表", "研究问题"),
        "cell": "问题 × 阶段",
        "code": "代码仓库",
        "pipeline": "五阶段配置",
        "code_title": "有代码的论文",
        "code_intro": "共 {n} 篇论文附有公开代码。`代码` 为作者官方仓库，`代码（第三方）` 为社区复现。",
        "poi_title": "POI 与本地生活论文",
        "poi_intro": "共 {n} 篇论文面向 POI、本地生活或地理空间推荐。加粗项标出各篇主要改动的流程阶段。",
        "modality_title": "按构码输入模态索引",
        "modality_intro": "本页按综述 Table 1 `representation` 列（或记录中的 `modality` 覆盖字段）所报告的构码输入内容模态与协同过滤（`CF`）信号分组列出论文。"
                          "此处的“协同”仅指构码输入中包含 `CF`，不代表生成骨干或训练目标中的协同信号。`A / B` 双分支配置分别列入各分支对应小节，各小节计不同论文数。",
        "rep_col": "表征（Representation）",
        "aux_col": "附加信号",
        "aux_title": "附加信号",
        "override": "（覆盖）",
    },
    "glossary": {
        "title": "术语表",
        "intro": "本页由 [`data/vocab.yaml`](../data/vocab.yaml) 自动生成，定义综述 Table 1、论文详情页与各索引页中的受控词表取值。",
        "symbols": "表内符号",
        "problems": "研究问题",
    },
    "legend": [
        ("`†`", "根据论文点名沿用的基座或配置推断得到。"),
        ("`A / B`", "包含两个分支或两种评测配置。"),
        ("`–`", "论文未报告。"),
        ("`n/a`", "不适用于该方法。"),
        ("**加粗**", "该论文主要改动的流程阶段。"),
        ("空白格", "该主分类下暂无论文。"),
        ("`warm`", "实验设置卡中的热启动过滤协议标签。"),
    ],
}
FLOW_IDS = ["R", "T", "B", "TR", "I"]
BASE_STYLE = "fill:#f8fafc,stroke:#cbd5e1"
MAIN_STYLE = "fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px"
ALSO_STYLE = "fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3"
LICENSE_ID = "CC0-1.0"  # SPDX id of LICENSE, shown in the README badge
BADGE_COLORS = {"papers": "d6e8fa", "updated": "d9ead3", "license": "e5dcef"}  # light shields.io backgrounds


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


def flow_chart(rec: dict, zh: bool = False) -> list:
    """Mermaid flowchart of the five stages; primary stage gets light blue fill, secondary stages get dashed borders."""
    s_disp = lambda s: f"{ZH_LABELS['stages_zh'][s]} {s}" if zh else s
    nodes = " --> ".join(f"{i}[{mm_label(f'{s_disp(s)}<br/>{v}')}]" for i, s, v in zip(FLOW_IDS, STAGES, stage_values(rec)))
    styles = [f"    classDef base {BASE_STYLE}", f"    class {','.join(FLOW_IDS)} base"]
    also_stages = [s for s in STAGES if s != rec["stage"] and any(a.get("stage") == s for a in rec.get("also", []))]
    if also_stages:
        styles += [f"    classDef also {ALSO_STYLE}", f"    class {','.join(FLOW_IDS[STAGES.index(s)] for s in also_stages)} also"]
    if rec["stage"] in STAGES:
        styles += [f"    classDef main {MAIN_STYLE}", f"    class {FLOW_IDS[STAGES.index(rec['stage'])]} main"]
    return ["```mermaid", "flowchart LR", f"    {nodes}", *styles, "```"]


def format_also_item(item: dict, probs: dict, zh: bool = False, code_wrap: bool = True) -> str:
    w = (lambda s: f"`{s}`") if code_wrap else str
    pr, stg = item.get("problem"), item.get("stage")
    p_txt = w(band(probs[pr], zh)) if pr else ""
    s_txt = w(f"{ZH_LABELS['stages_zh'][stg]}（{stg}）" if zh else stg) if stg else ""
    if p_txt and s_txt:
        return f"{p_txt} × {s_txt}"
    return p_txt or s_txt


def rep_modality_map(vocab: dict) -> dict:
    return {e["value"]: e["modality"] for e in vocab["representation"]}


def paper_modality(rec: dict, rmap: dict) -> tuple:
    """Return (deduplicated list of (content, cf) buckets, auxiliary signal list, overridden bool)."""
    v_branches = rmap[rec["representation"]]
    signals = list(dict.fromkeys(sig for b in v_branches for sig in b.get("signals", [])))
    if "modality" in rec:
        ov = rec["modality"] if isinstance(rec["modality"], list) else [rec["modality"]]
        buckets = list(dict.fromkeys((b["content"], b["cf"]) for b in ov))
        return buckets, signals, True
    buckets = list(dict.fromkeys((b["content"], b["cf"]) for b in v_branches))
    return buckets, signals, False


def modality_label(bucket: tuple, zh: bool = False) -> str:
    for key, en_name, zh_name, *_ in MODALITY_BUCKETS:
        if key == bucket:
            if key == ("unknown", None):
                return "表征未明" if zh else "Unspecified"
            return zh_name if zh else en_name
    return str(bucket)


def modality_summary_en(rec: dict, rmap: dict) -> str:
    buckets, signals, _ = paper_modality(rec, rmap)
    base = " / ".join(modality_label(b, zh=False) for b in buckets)
    return f"{base} ({', '.join(signals)})" if signals else base


def build_modality_table(papers: list, rmap: dict, mod_path: str, zh: bool = False) -> list:
    """Render the 3x2 modality summary table plus the three lines below it (unknown, n/a, auxiliary signals)."""
    R = ZH_LABELS["readme"]
    ordered = by_year(papers)
    bucket_papers = {key: [] for key, *_ in MODALITY_BUCKETS}
    sig_papers = {sig: [] for sig, *_ in AUX_SIGNAL_LIST}
    for r in ordered:
        buckets, signals, _ = paper_modality(r, rmap)
        for b in buckets:
            bucket_papers[b].append(r)
        for s in signals:
            sig_papers[s].append(r)
    b_meta = {key: (en_n, zh_n) for key, en_n, zh_n, *_ in MODALITY_BUCKETS}
    cell_link = lambda key: (
        f"[{b_meta[key][1 if zh else 0]}{'（' if zh else ' ('}{len(bucket_papers[key])}{'）' if zh else ')'}]"
        f"({mod_path}#{slugify_heading(b_meta[key][1 if zh else 0])})"
    )
    head = R["modality_head"] if zh else ("Content Modality", "No CF tagged", "With CF")
    rows = [f"| {head[0]} | {head[1]} | {head[2]} |", "| :-- | :-- | :-- |"]
    for c_key, en_row, zh_row, _ in MODALITY_ROWS:
        r_label = f"**{zh_row}**" if zh else f"**{en_row}**"
        rows.append(f"| {r_label} | {cell_link((c_key, False))} | {cell_link((c_key, True))} |")
    unk_title = b_meta[("unknown", None)][1 if zh else 0]
    na_title = b_meta[("na", None)][1 if zh else 0]
    unk_n, na_n = len(bucket_papers[("unknown", None)]), len(bucket_papers[("na", None)])
    aux_links = " · ".join(
        f"[`{sig}`{'（' if zh else ' ('}{len(sig_papers[sig])}{'）' if zh else ')'}]({mod_path}#{slugify_heading(sig)})"
        for sig, *_ in AUX_SIGNAL_LIST
    )
    if zh:
        foot = [
            R["modality_unknown"].format(n=unk_n, path=mod_path, anchor=slugify_heading(unk_title)), "",
            R["modality_na"].format(n=na_n, path=mod_path, anchor=slugify_heading(na_title)), "",
            R["modality_aux"].format(links=aux_links),
        ]
    else:
        foot = [
            f"**Unspecified representation**: [{unk_n} papers]({mod_path}#{slugify_heading(unk_title)}) (`–`, `Multi-Dom`, `Cross-Dom`, or an unreported branch).", "",
            f"**Not applicable**: [{na_n} paper{'s' if na_n != 1 else ''}]({mod_path}#{slugify_heading(na_title)}) (`n/a`).", "",
            f"**Auxiliary signals**: {aux_links}.",
        ]
    return [*align(rows), "", *foot]


def related_chart(rec: dict, by_id: dict, zh: bool = False) -> str:
    """Mermaid graph from this paper to each related paper, labeled by relation; empty without related."""
    rel = rec.get("related", [])
    if not rel:
        return ""
    rel_lab = (lambda r: ZH_LABELS["relations"][r]) if zh else (lambda r: r)
    ids = [chr(65 + i) for i in range(len(rel))]
    edges = [f"    P -->|{mm_label(rel_lab(r['relation']))}| {ids[i]}[{mm_label(by_id[r['id']]['name'])}]" for i, r in enumerate(rel)]
    styles = [f"    classDef main {MAIN_STYLE}", f"    classDef peer {BASE_STYLE}",
              "    class P main", f"    class {','.join(ids)} peer"]
    return "\n".join(["```mermaid", "flowchart LR", f"    P[{mm_label(rec['name'])}]", *edges, *styles, "```"])


def band(p: dict, zh: bool = False) -> str:
    if zh:
        return ZH_LABELS["problems"][p["value"]]
    return p["name"] if p["value"] == "psb" else f"{p['value']}. {p['name']}"


def stage_label(rec: dict, zh: bool = False) -> str:
    if rec["problem"] == "psb":
        return ZH_LABELS["no_single_stage"] if zh else "No single stage"
    if zh:
        return f"{ZH_LABELS['stages_zh'][rec['stage']]}（{rec['stage']}）"
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
    """Setup card; folded wraps the card in a collapsed <details> block with short source links."""
    st, sw = rec.get("setup"), rec.get("setup_where", {})
    if not st:
        return ""
    labels = ZH_LABELS["setup"] if zh else SETUP_LABELS
    title = ZH_LABELS["setup_title"] if zh else "Experimental setup"
    src = f"{ZH_LABELS['source']}{ZH_LABELS['colon']}" if zh else "Source: "
    colon = ZH_LABELS["colon"] if zh else ": "
    fmt = short_links if folded else str
    items = "\n".join(f"- **{lab}**{colon}{st[k]}" + (f"\n  - {src}{fmt(sw[k])}" if sw.get(k) else "")
                      for k, lab in zip(SETUP_KEYS, labels))
    return f"<details>\n<summary>{title}</summary>\n\n{items}\n\n</details>" if folded else f"**{title}**\n\n{items}"


def build_paper_page(rec: dict, vocab: dict, by_id: dict, n, root: Path, zh: bool = False) -> str:
    Z = ZH_LABELS
    up = "../../../" if zh else "../../"
    readme = f"{up}README.zh.md" if zh else f"{up}README.md"
    probs = {e["value"]: e for e in vocab["problem"]}
    prob = probs[rec["problem"]]
    anchor = slugify_heading(cell_label(rec, probs, zh))
    sections = SECTIONS_ZH if zh else SECTIONS
    level = reading_level(n, sections)
    desc_key = "description_zh" if zh else "description"
    defs = {c: {e["value"]: e.get(desc_key) or e.get("description") for e in vocab.get(c, [])} for c in TECH_COLS}
    tldr = ((rec.get("tldr_zh") if zh else rec.get("tldr")) or "").strip()
    prob_desc = prob.get("description_zh") if zh else prob["description"]
    glance = [("Research Problem", f"{band(prob, zh)}{Z['colon'] if zh else ': '}{prob_desc}"), ("Key Contribution", tldr),
              ("Modified Stage", stage_label(rec, zh)), *((k, (n or {}).get("glance", {}).get(k)) for k in GLANCE_KEYS)]
    head = Z["glance_head"] if zh else ("Aspect", "Summary")
    rows = [f"| {Z['glance_rows'][a] if zh else a} | {v.strip().replace('|', chr(92) + '|')} |" for a, v in glance if v]
    colon = Z["colon"] if zh else ": "
    blocks = [("TL;DR", [f"> [!NOTE]\n> {tldr}"])] if tldr else []
    blocks += [(Z["glance_title"] if zh else "At a Glance", ["\n".join([f"| {head[0]} | {head[1]} |", "| :-- | :-- |", *rows])])] if rows else []
    image = root / "architectures" / f"{rec['id']}.png"
    inserts = {sections[1]: f"![{rec['name']} architecture diagram]({up}architectures/{image.name})" if image.is_file() else "",
               sections[2]: setup_card(rec, folded=True, zh=zh)}
    for t in sections:
        parts = [p for p in (inserts.get(t), (n or {}).get("sections", {}).get(t)) if p]
        blocks += [(t, parts)] if parts else []
    blocks += [(None, [n["rest"]])] if n and n["rest"] else []
    rel_lab = (lambda r: Z["relations"][r]) if zh else (lambda r: r.capitalize())
    src_lab = Z["source"] if zh else "Source"
    rel = "\n".join(f"- **{rel_lab(r['relation'])}** · [{by_id[r['id']]['name']}]({r['id']}.md): {r['note']}"
                    f"\n  - {src_lab}{colon}{short_links(r['where'])}" for r in rec.get("related", []))
    view = Z["view_cell"] if zh else "View all papers in this cell"
    blocks.append((Z["related_title"] if zh else RELATED_TITLE,
                   [p for p in (related_chart(rec, by_id, zh=zh), rel, f"[{view}]({readme}#{anchor})") if p]))
    tags = [band(prob, zh), stage_label(rec, zh)] + (["POI"] if rec.get("poi") else [])
    cell_str = " · ".join(f"`{t}`" for t in tags)
    if rec.get("also"):
        sep = "；" if zh else "; "
        also_prefix = f" — {Z['also_label']}：" if zh else " — Also: "
        cell_str += also_prefix + sep.join(format_also_item(a, probs, zh=zh, code_wrap=True) for a in rec["also"])
    toc = " · ".join(f"[{t if zh else TOC_SHORT.get(t, t)}](#{slugify_heading(t)})" for t, _ in blocks if t)
    vals = dict.fromkeys(
        f"- `{rec[c]}`{colon}{defs[c][rec[c]]}"
        for c in TECH_COLS
        if rec[c] not in ("n/a", "–") and defs[c].get(rec[c])
    )
    nav_bar = (
        f"[← {Z['links']['Matrix']}]({readme}#{anchor}) · [{Z['links']['Stages']}](../index/stages.md) · "
        f"[{Z['links']['Modality']}](../index/modality.md) · [English](../../papers/{rec['id']}.md) | 中文"
        if zh else
        f"[← Problem × Stage Matrix]({readme}#{anchor}) · [Papers by Stage](../index/stages.md) · "
        f"[Papers by Modality](../index/modality.md) · English | [中文](../zh/papers/{rec['id']}.md)"
    )
    level_name = (Z["levels"] if zh else LEVELS)[level - 1]
    level_text = f"{level_name}（{Z['level_n'].format(n=level)}）" if zh else f"{level_name} (Level {level})"
    card = [("Title", f"*{title_of(rec)}*"), ("Authors", rec["authors"]), ("Venue", rec["venue"]),
            ("Cell", cell_str), ("Links", link_line(rec, zh=zh)),
            ("Reading level", level_text)]
    lab = lambda k: Z["card"][k] if zh else ("Problem × Stage" if k == "Cell" else k)
    rows = [f"| **{lab(k)}** | {v.replace('|', chr(92) + '|')} |" for k, v in card]
    lines = [
        f"# {rec['name']}", "",
        nav_bar, "",
        rows[0], "| :-- | :-- |", *rows[1:], "",
        f"**{Z['on_this_page'] if zh else 'On this page'}**{colon}{toc}", "",
        *flow_chart(rec, zh=zh), "",
        *([*vals, ""] if vals else []),
    ]
    for i, (t, parts) in enumerate(blocks):
        lines += (["---", ""] if i else []) + ([f"### {t}", ""] if t else []) + [x for p in parts for x in (p, "")]
    return "\n".join(lines)


def heat(n: int, also_n: int, anchor: str) -> str:
    if not n and not also_n:
        return ""
    if n and also_n:
        color = [c for lo, c in HEAT if n >= lo][-1]
        return f"[![{n} (+{also_n})](https://img.shields.io/badge/{n}-%2B{also_n}-{ALSO_BADGE_BG}?style=for-the-badge&labelColor={color})](#{anchor})"
    if n:
        color = [c for lo, c in HEAT if n >= lo][-1]
        return f"[![{n}](https://img.shields.io/badge/{n}-{color}?style=for-the-badge)](#{anchor})"
    return f"[![+{also_n}](https://img.shields.io/badge/%2B{also_n}-{ALSO_BADGE_BG}?style=for-the-badge)](#{anchor})"


def align(rows: list) -> list:
    cells = [[c.strip() for c in r.strip("|").split(" | ")] for r in rows]
    w = [max(len(r[i]) for r in cells) for i in range(len(cells[0]))]
    mid = [c == ":-:" for c in cells[1]]
    pad = lambda c, i: (c[0] + c[1:-1].ljust(w[i] - 2, "-") + c[-1]) if c and set(c) <= set(":-") else c.center(w[i]) if mid[i] else c.ljust(w[i])
    return ["| " + " | ".join(pad(c, i) for i, c in enumerate(r)) + " |" for r in cells]


def ref(rec: dict) -> str:
    """Reference-style link to the paper page; awesome-lint requires absolute URLs in inline list links."""
    return f"[{rec['name']}][{'' if rec['name'].lower() == rec['id'] else rec['id']}]"


def format_item(rec: dict, zh: bool = False) -> str:
    first = f"- {ref(rec)} - {rec['venue']}" + (" · `POI`" if rec.get("poi") else "")
    tldr = ((rec.get("tldr_zh") if zh else rec.get("tldr")) or "").strip()
    return "<br>\n  ".join([first, *[x for x in (tldr, link_line(rec, zh=zh)) if x]])


def shield(label: str, value: str, color: str) -> str:
    esc = lambda x: quote(str(x).replace("-", "--").replace("_", "__").replace(" ", "_"))
    return f"https://img.shields.io/badge/{esc(label)}-{esc(value)}-{color}"


def stage_overview(papers: list, zh: bool = False) -> list:
    """Mermaid chart of the five stages, each node with the number of papers that mainly change it."""
    unit = f" {ZH_LABELS['overview']}" if zh else " papers"
    s_disp = lambda s: f"{ZH_LABELS['stages_zh'][s]} {s}" if zh else s
    counts = {s: sum(r["stage"] == s for r in papers) for s in STAGES}
    nodes = " --> ".join(f"{i}[{mm_label(f'{s_disp(s)}<br/>{counts[s]}{unit}')}]" for i, s in zip(FLOW_IDS, STAGES))
    styles = [f"    classDef stage {BASE_STYLE}", f"    class {','.join(FLOW_IDS)} stage"]
    return ["```mermaid", "flowchart LR", f"    {nodes}", *styles, "```"]


def readme_head(papers: list, updates: list, zh: bool = False) -> list:
    """Centered title, one-line description, light badges, language switch, and the five-stage overview."""
    R = ZH_LABELS["readme"]
    labels = R["badges"] if zh else ("papers", "updated", "license")
    latest = max((u["date"] for u in updates), default="")
    badges = [(labels[0], len(papers), "papers", "#" + slugify_heading(R["all_title"] if zh else "All Papers")),
              (labels[1], latest, "updated", "#" + slugify_heading(R["updates_title"] if zh else "Recent Updates")),
              (labels[2], LICENSE_ID, "license", "LICENSE")]
    intro = R["intro"] if zh else ("Papers and annotated deep dives on Semantic ID generative recommendation, "
                                   "indexed by research problem and pipeline stage.")
    return ['<div align="center">', "",
            "# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)", "",
            intro, "",
            " ".join(f"[![{l}]({shield(l, v, BADGE_COLORS[k])})]({href})" for l, v, k, href in badges), "",
            "[English](README.md) | 中文" if zh else "English | [中文](README.zh.md)", "",
            "</div>", "", *stage_overview(papers, zh)]


def build_readme(vocab: dict, papers: list, by_id: dict, levels: dict, updates: list, zh: bool = False) -> str:
    R = ZH_LABELS["readme"]
    rmap = rep_modality_map(vocab)
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    psb = next(p for p in vocab["problem"] if p["value"] == "psb")
    ordered = by_year(papers)
    cell = {(p["value"], s): [r for r in ordered if (r["problem"], r["stage"]) == (p["value"], s)] for p in problems for s in STAGES}
    also_cell = {
        (p["value"], s): [r for r in ordered if any((a.get("problem"), a.get("stage")) == (p["value"], s) for a in r.get("also", []))]
        for p in problems for s in STAGES
    }
    psb_list = [r for r in ordered if r["problem"] == "psb"]
    pname = lambda p: ZH_LABELS["problems"][p["value"]].split(". ", 1)[1] if zh else p["name"]
    pdesc = lambda p: p.get("description_zh") if zh else p["description"]
    table = [f"| {R['problem'] if zh else 'Problem'} | {' | '.join(STAGES)} | {R['total'] if zh else 'Total'} |",
             "| :-- |" + " :-: |" * (len(STAGES) + 1)]
    for p in problems:
        counts = [len(cell[(p["value"], s)]) for s in STAGES]
        also_counts = [len(also_cell[(p["value"], s)]) for s in STAGES]
        anchors = [slugify_heading(f"{p['value']} × {s}") for s in STAGES]
        table.append(f"| **{p['value']}.** {pname(p)} | " + " | ".join(map(heat, counts, also_counts, anchors)) + f" | **{sum(counts)}** |")
    totals = [sum(len(cell[(p["value"], s)]) for p in problems) for s in STAGES]
    table.append(f"| **{R['total'] if zh else 'Total'}** | " + " | ".join(f"**{t}**" for t in totals) + f" | **{sum(totals)}** |")
    starters = [r for r in ordered if levels[r["id"]] == 3]
    tl = lambda r: ((r.get("tldr_zh") if zh else r.get("tldr")) or "").strip()
    two = lambda head, rows: align([f"| {' | '.join(head)} |", "|" + " :-- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]])
    n, m, k = len(papers), sum(totals), len(psb_list)
    if zh:
        top = [
            f"## {R['scope_title']}", "", R["scope"].format(n=n, m=m, k=k), "",
            f"## {R['start_title']}", "", *two(R["start_head"], R["start"]), "",
            f"## {R['starter_title']}", ""]
    else:
        top = ["## Scope", "",
               f"This repository indexes {n} papers on generative recommendation with Semantic IDs (SIDs). "
               f"The matrix organizes {m} of them by research problem and primary modified stage, while {k} cover {psb['name'].lower()}. "
               "Approaches that feed discrete SIDs into discriminative or hybrid architectures are included alongside autoregressive and parallel generators. "
               "POI and local-life papers carry a `POI` tag and are collected in the [POI index](pages/index/poi.md).", "",
               "## Where to Start", "",
               *two(("Goal", "Entry point"), [
                   ("New to the topic", "[Start Here](guides/start-here.md)"),
                   ("Locate papers by research problem", "[Problem × Stage Matrix](#problem--stage-matrix)"),
                   ("Compare methods within one stage", "[Papers by Stage](pages/index/stages.md)"),
                   ("Browse by tokenizer input modality", "[Papers by Modality](pages/index/modality.md)"),
                   ("Find open-source implementations", "[Papers with Code](pages/index/code.md)"),
                   ("Feed LLMs and search tools", "[llms.txt](llms.txt)")]), "",
               "## Starter Papers", ""]
    uchange = lambda u: (u.get("change_zh") or u["change"]).strip() if zh else u["change"].strip()
    mod_path = "pages/zh/index/modality.md" if zh else "pages/index/modality.md"
    matrix_note = R["matrix_note"] if zh else (
        "Primary placement follows the survey's Table 1; additional tags list other problems or stages the paper explicitly targets."
    )
    mod_note = R["modality_note"] if zh else (
        "Grouped by the content modality and collaborative filtering (`CF`) signal in the survey's Table 1 `representation` column; "
        "`CF` here refers only to the tokenizer input, and `A / B` dual-branch configurations appear in each branch's cell."
    )
    lines = [
        "<!--lint disable awesome-github-->",
        *readme_head(papers, updates, zh), "",
        *top,
        *two(R["starter_head"] if zh else ("Paper", "Core mechanism", "Venue"),
             [(ref(r), tl(r).replace("|", "\\|"), r["venue"]) for r in starters]), "",
        f"## {R['matrix_title'] if zh else 'Problem × Stage Matrix'}", "",
        matrix_note, "",
        *align(table), "",
        R["click"] if zh else (
            "Click a badge to jump to its papers; the left count is primary placements (darker light-blue indicates more papers) "
            "and `+n` counts papers with a paired secondary tag in that cell."
        ), "",
        *align([f"| {' | '.join(R['legend_head'] if zh else ('Mark', 'Meaning'))} |", "| :-- | :-- |",
                *[f"| {mk} | {t} |" for mk, t in (ZH_LABELS["legend"] if zh else LEGEND)]]), "",
        R["glossary"] if zh else "The [glossary](guides/glossary.md) defines every symbol and column value used across the paper pages.", "",
        f"## {R['modality_title'] if zh else 'Tokenizer Input Modality'}", "",
        mod_note, "",
        *build_modality_table(papers, rmap, mod_path, zh=zh), "",
        f"## {R['updates_title'] if zh else 'Recent Updates'}", "",
        *[f"- {u['date']}: {uchange(u)}" + ((f"{R['papers']}{'、'.join(ref(by_id[x]) for x in u['papers'])}。" if zh else
                                             f" Papers: {', '.join(ref(by_id[x]) for x in u['papers'])}.") if u["papers"] else "")
          for u in sorted(updates, key=lambda u: u["date"], reverse=True)], "",
        f"## {R['all_title'] if zh else 'All Papers'}", "",
        *[f"- [{band(p, zh)}][]" for p in [psb, *problems]], "",
        f"## {band(psb, zh)}", "", f"> {pdesc(psb)}", "", *(format_item(r, zh) for r in psb_list), "",
    ]
    for p in problems:
        lines += [f"## {band(p, zh)}", "", f"> {pdesc(p)}", ""]
        for s in STAGES:
            prim = cell[(p["value"], s)]
            sec = also_cell[(p["value"], s)]
            if prim or sec:
                lines += [f"### {p['value']} × {s}", ""]
                if prim:
                    lines += [*(format_item(r, zh) for r in prim), ""]
                if sec:
                    also_line = (
                        f"{R['also_in_cell']}{'、'.join(ref(r) for r in sec)}。"
                        if zh else
                        f"Also in this cell: {', '.join(ref(r) for r in sec)}."
                    )
                    lines += [also_line, ""]
    page_dir = "pages/zh/papers" if zh else "pages/papers"
    lines += [f"## {R['contrib_title'] if zh else 'Contributing'}", "",
              R["contrib"] if zh else "Add or update `data/papers/<id>.yaml` and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).", "",
              *[f"[{band(p, zh).lower()}]: #{slugify_heading(band(p, zh))}" for p in [psb, *problems]],
              *[f"[{r['id']}]: {page_dir}/{r['id']}.md" for r in sorted(papers, key=lambda x: x["id"])], ""]
    return "\n".join(lines)


def build_indexes(vocab: dict, papers: list, zh: bool = False) -> dict:
    X = ZH_LABELS["index"]
    up = "../../../" if zh else "../../"
    probs = {e["value"]: e for e in vocab["problem"]}
    ordered = by_year(papers)
    link = lambda r: f"[{r['name']}](../papers/{r['id']}.md)"
    table = lambda head, rows: [f"| {' | '.join(head)} |", "|" + " :-- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]]
    readme = f"{up}README.zh.md" if zh else f"{up}README.md"
    psb_anchor = slugify_heading(band(probs["psb"], zh))
    head = X["head"] if zh else ("Paper", "Venue", "Problem")
    cell_h = X["cell"] if zh else "Problem × Stage"
    compare = " · ".join(f"[{t}]({up}comparisons/{f}.md)" for f, t, *_ in COMPARISONS)
    switch = lambda f: f"[English](../../index/{f}) | 中文" if zh else f"English | [中文](../zh/index/{f})"
    stages = [f"# {X['stages_title'] if zh else 'Papers by Stage'}", "", switch("stages.md"), "",
              X["stages_intro"].format(readme=readme, anchor=psb_anchor) if zh else
              "Each table groups papers by the pipeline stage they primarily modify, alongside that stage's Table 1 value. "
              f"Papers under {probs['psb']['name'].lower()} span multiple stages or provide benchmarks; see the [README]({readme}#{psb_anchor}).", "",
              (X["compare"] if zh else "Side-by-side comparison tables: ") + compare, ""]
    for s in STAGES:
        s_head = f"{ZH_LABELS['stages_zh'][s]}（{s}）" if zh else s
        rows = [[link(r), r["venue"], band(probs[r["problem"]], zh),
                 f"`{r['tokenizer']} / {r['objective']}`" if s == "Training" else f"`{r[s.lower()]}`"]
                for r in ordered if r["stage"] == s]
        stages += [f"## {s_head}", "", *table([*head, s_head], rows), ""]
    coded = [r for r in ordered if code_links(r)]
    code = [f"# {X['code_title'] if zh else 'Papers with Code'}", "", switch("code.md"), "",
            X["code_intro"].format(n=len(coded)) if zh else
            f"{len(coded)} papers link to public code. `Code` marks an official author repository; `Code (third-party)` marks a community implementation.", "",
            *table([head[0], head[1], cell_h, X["code"] if zh else "Code"],
                   [[link(r), r["venue"], cell_label(r, probs, zh), " · ".join(f"[{l}]({u})" for l, u in code_links(r, zh))]
                    for r in coded]), ""]
    poi = [r for r in ordered if r.get("poi")]
    poi_page = [f"# {X['poi_title'] if zh else 'POI and Local-Life Papers'}", "", switch("poi.md"), "",
                X["poi_intro"].format(n=len(poi)) if zh else
                f"{len(poi)} papers target POI, local-life, or spatial recommendation. Bold marks the stage each paper primarily modifies.", "",
                *table([head[0], head[1], cell_h, X["pipeline"] if zh else "Pipeline"],
                       [[link(r), r["venue"], cell_label(r, probs, zh), pipeline(r)] for r in poi]), ""]
    rmap = rep_modality_map(vocab)
    bucket_papers = {key: [] for key, *_ in MODALITY_BUCKETS}
    sig_papers = {sig: [] for sig, *_ in AUX_SIGNAL_LIST}
    paper_mod_info = {}
    for r in ordered:
        buckets, signals, overridden = paper_modality(r, rmap)
        paper_mod_info[r["id"]] = (buckets, signals, overridden)
        for b in buckets:
            bucket_papers[b].append(r)
        for s in signals:
            sig_papers[s].append(r)
    rep_cell = lambda r: (
        f"`{r['representation']}`{X['override'] if zh else ' *(override)*'}"
        if paper_mod_info[r["id"]][2] else f"`{r['representation']}`"
    )
    aux_cell = lambda r: " · ".join(f"`{s}`" for s in paper_mod_info[r["id"]][1]) or "–"
    mod_cols = [head[0], head[1], cell_h, X["rep_col"] if zh else "Representation", X["aux_col"] if zh else "Auxiliary"]
    mod_page = [
        f"# {X['modality_title'] if zh else 'Papers by Tokenizer Input Modality'}", "",
        switch("modality.md"), "",
        X["modality_intro"] if zh else (
            "Papers grouped by the content modality and collaborative filtering (`CF`) signal reported in the survey's Table 1 "
            "`representation` column (or paper-level `modality` override where recorded). Collaborative signal here refers only "
            "to `CF` in the tokenizer input, not to collaborative supervision in the generator backbone or training objective. "
            "Dual-branch `A / B` configurations appear in each branch's section, with distinct papers counted per section."
        ), "",
        *build_modality_table(papers, rmap, "", zh=zh), "",
    ]
    for key, en_name, zh_name, en_desc, zh_desc in MODALITY_BUCKETS:
        sec_title = zh_name if zh else en_name
        sec_desc = zh_desc if zh else en_desc
        rows = [[link(r), r["venue"], cell_label(r, probs, zh), rep_cell(r), aux_cell(r)] for r in bucket_papers[key]]
        mod_page += [f"## {sec_title}", "", f"> {sec_desc}", "", *table(mod_cols, rows), ""]
    mod_page += [f"## {X['aux_title'] if zh else 'Auxiliary Signals'}", ""]
    for sig, en_sdesc, zh_sdesc in AUX_SIGNAL_LIST:
        rows = [[link(r), r["venue"], cell_label(r, probs, zh), rep_cell(r), aux_cell(r)] for r in sig_papers[sig]]
        mod_page += [f"### {sig}", "", f"> {zh_sdesc if zh else en_sdesc}", "", *table(mod_cols, rows), ""]
    return {"stages.md": "\n".join(stages), "code.md": "\n".join(code), "poi.md": "\n".join(poi_page), "modality.md": "\n".join(mod_page)}


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


def build_glossary(vocab: dict, zh: bool = False) -> str:
    G = ZH_LABELS["glossary"]
    colon = "：" if zh else ": "
    entry = lambda v, d: f"- `{v}`{colon}{d}" if d else f"- `{v}`"
    pname = lambda p: band(p, True).split(". ", 1)[-1] + "。" if zh else p["name"] + "."
    pdesc = lambda p: p.get("description_zh") if zh else p["description"]
    desc_key = "description_zh" if zh else "description"
    lines = [f"# {G['title'] if zh else 'Glossary'}", "",
             "[English](glossary.md) | 中文" if zh else "English | [中文](glossary.zh.md)", "",
             G["intro"] if zh else "This page is generated from [`data/vocab.yaml`](../data/vocab.yaml). "
             "It defines the controlled vocabulary values used in Table 1, the paper pages, and the indexes.", "",
             f"## {G['symbols'] if zh else 'Symbols'}", "", *[f"- {m}{colon}{t}" for m, t in (ZH_LABELS["legend"] if zh else LEGEND)[:4]], "",
             f"## {G['problems'] if zh else 'Problems'}", "",
             *[entry(p["value"], f"**{pname(p)}** {pdesc(p)}") for p in vocab["problem"]], ""]
    for c, s in zip(TECH_COLS, COL_STAGES):
        head = ZH_LABELS["cols_zh"][c] if zh else (c.capitalize() + ("" if s == c.capitalize() else f" ({s})"))
        lines += [f"## {head}", "", *[entry(e["value"], e.get(desc_key) or e.get("description")) for e in vocab[c]], ""]
    return "\n".join(lines)


def llm_fields(rec: dict, probs: dict, rmap: dict) -> list:
    f = [f"Problem: {band(probs[rec['problem']])}", f"Stage: {stage_label(rec)}"]
    if rec.get("also"):
        f.append("Also: " + "; ".join(format_also_item(a, probs, zh=False, code_wrap=False) for a in rec["also"]))
    f += [f"Modality: {modality_summary_en(rec, rmap)}",
          "; ".join(f"{c.capitalize()}: {rec[c]}" for c in TECH_COLS)]
    f += [f"TL;DR: {rec['tldr'].strip()}"] if rec.get("tldr") else []
    f += [f"[{l}]({u})" for l, u in code_links(rec)]
    return f + [f"Setup card: {'yes' if rec.get('setup') else 'no'}", f"Relations: {len(rec.get('related', []))}"]


def build_llms(vocab: dict, papers: list, notes: dict) -> tuple:
    probs = {e["value"]: e for e in vocab["problem"]}
    rmap = rep_modality_map(vocab)
    ordered = sorted(papers, key=lambda x: x["id"])
    head = [
        "# Awesome Semantic ID Generative Recommendation", "",
        f"> {len(papers)} papers on generative recommendation with Semantic IDs (SIDs), organized by research problem "
        "and primary modified pipeline stage.", "",
        "## Core Files", "",
        "- [README.md](README.md): Problem × Stage matrix, tokenizer input modality table, and the full list of papers.",
        "- [guides/glossary.md](guides/glossary.md): Definitions of every problem and Table 1 value.",
        "- [pages/index/stages.md](pages/index/stages.md): Papers grouped by the stage they mainly change.",
        "- [pages/index/modality.md](pages/index/modality.md): Papers grouped by tokenizer input modality and collaborative signal.",
        "- [pages/index/code.md](pages/index/code.md): Papers that link to code.",
        "- [pages/index/poi.md](pages/index/poi.md): Papers on POI and local-life recommendation.",
        "- [data/vocab.yaml](data/vocab.yaml): Controlled vocabulary for problems, stages, and the six Table 1 columns.",
        "- [schema/paper.schema.json](schema/paper.schema.json): JSON Schema for `data/papers/<id>.yaml`.", "",
    ]
    short = head + [f"## Papers ({len(papers)} records)", ""] + [
        f"- [{r['name']}](pages/papers/{r['id']}.md) · {r['venue']} · " + " · ".join(llm_fields(r, probs, rmap)) for r in ordered]
    full = list(head)
    for r in ordered:
        full += [f"## {r['name']}", "", f"- Page: pages/papers/{r['id']}.md", f"- Venue: {r['venue']}",
                 *[f"- {x}" for x in llm_fields(r, probs, rmap)], ""]
        if r.get("also"):
            full += [
                "### Additional tags", "",
                *[f"- {format_also_item(a, probs, zh=False, code_wrap=False)} — \"{a['quote']}\" ({a['where']})"
                  for a in r["also"]],
                "",
            ]
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
    read_notes = lambda d, sec: {p.stem: parse_notes(p.read_text(encoding="utf-8"), sec) for p in sorted((root / d).glob("*.md"))}
    notes, notes_zh = read_notes("notes", SECTIONS), read_notes("notes/zh", SECTIONS_ZH)
    levels = {r["id"]: reading_level(notes.get(r["id"])) for r in papers}
    updates = yaml.safe_load((root / "data/updates.yaml").read_text(encoding="utf-8")) or []
    outputs = {
        "pages/papers": {f"{r['id']}.md": build_paper_page(r, vocab, by_id, notes.get(r["id"]), root) for r in papers},
        "pages/zh/papers": {f"{r['id']}.md": build_paper_page(r, vocab, by_id, notes_zh.get(r["id"]), root, zh=True) for r in papers},
        "pages/index": build_indexes(vocab, papers),
        "pages/zh/index": build_indexes(vocab, papers, zh=True),
        "comparisons": build_comparisons(papers, by_id),
    }
    for sub, files in outputs.items():
        out = root / sub
        out.mkdir(parents=True, exist_ok=True)
        for existing in out.glob("*.md"):
            existing.unlink()
        for name, text in files.items():
            (out / name).write_text(text, encoding="utf-8")
    (root / "guides").mkdir(exist_ok=True)
    singles = {
        "README.md": build_readme(vocab, papers, by_id, levels, updates),
        "README.zh.md": build_readme(vocab, papers, by_id, levels, updates, zh=True),
        "guides/glossary.md": build_glossary(vocab),
        "guides/glossary.zh.md": build_glossary(vocab, zh=True),
    }
    singles["llms.txt"], singles["llms-full.txt"] = build_llms(vocab, papers, notes)
    for name, text in singles.items():
        (root / name).write_text(text, encoding="utf-8")
    print(f"Built README.md, README.zh.md, {len(papers)} paper pages in English and Chinese, 4 index pages in English and Chinese, "
          "3 comparison tables, guides/glossary.md, guides/glossary.zh.md, llms.txt, and llms-full.txt.")


if __name__ == "__main__":
    main()
