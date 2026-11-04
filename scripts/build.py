#!/usr/bin/env python3
"""Build README.md, per-paper pages (pages/papers/<id>.md), index pages (pages/index/), comparison tables (comparisons/),
guides/glossary.md, llms.txt, and llms-full.txt, plus the Chinese views README.zh.md, pages/zh/papers/, pages/zh/index/,
and guides/glossary.zh.md, or synchronize Table 1 columns from Table 1 in the survey paper (main.tex and supplementary.tex) (--sync-table1).
"""
import argparse
from collections import Counter
import html
import math
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote
import yaml

ROOT = Path(__file__).resolve().parent.parent
TECH_COLS = ["representation", "tokenization", "backbone", "tokenizer", "objective", "inference"]
COL_STAGES = ["Representation", "Tokenization", "Backbone", "Training", "Training", "Inference"]
COL_HEADERS_EN = {
    "representation": "Representation",
    "tokenization": "Tokenization",
    "backbone": "Backbone",
    "tokenizer": "Tokenizer",
    "objective": "Objective",
    "inference": "Inference",
}
COL_HEADERS_ZH = {
    "representation": "物品表示",
    "tokenization": "构码",
    "backbone": "生成骨干",
    "tokenizer": "编号器更新",
    "objective": "训练目标",
    "inference": "推理",
}
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
                primary_col = None
                vals = {}
                for i, key in enumerate(TECH_COLS):
                    v = c[i + 2]
                    mm = re.match(r"\\cellcolor\{modgray\}\\textbf\{(.*)\}$", v)
                    if mm:
                        v = mm.group(1)
                        stage = COL_STAGES[i]
                        primary_col = key
                    vals[key] = norm_tex(v)
                rows.append({
                    "name": name,
                    "venue": norm_tex(c[1]),
                    "problem": cur_prob,
                    "stage": stage,
                    "primary_col": primary_col,
                    **vals,
                })
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
LEGEND = [  # (mark, meaning); the first six are the symbols listed in the glossary
    ("`†`", "Inferred from the configuration the paper names."),
    ("`A / B`", "Two branches or configurations."),
    ("`–`", "Not reported."),
    ("`n/a`", "Not applicable."),
    ("`●` / `○`", "Primary Table 1 cell (`●`) and additional column with a new mechanism (`○`)."),
    ("**Bold**", "The stage the paper mainly changes."),
    ("Empty cell", "No paper yet."),
    ("`warm`", "Protocol label in setup cards."),
]
ZH_LABELS = {
    "stages_zh": {
        "Representation": "物品表示",
        "Tokenization": "构码",
        "Backbone": "生成骨干",
        "Training": "训练",
        "Inference": "推理",
    },
    "cols_zh": {
        "representation": "物品表示（Representation）",
        "tokenization": "构码（Tokenization）",
        "backbone": "生成骨干（Backbone）",
        "tokenizer": "编号器更新（Training）",
        "objective": "训练目标（Training）",
        "inference": "推理（Inference）",
    },
    "setup": ["数据集", "切分", "候选集", "可见性", "SID 规格", "推理预算", "结果来源"],
    "setup_title": "实验设置",
    "source": "出处",
    "levels": ["概览", "阅读笔记", "代码级精读"],
    "reading_level": "阅读级别",
    "card": {
        "Title": "题目",
        "Authors": "作者",
        "Venue": "发表",
        "Cell": "问题与阶段",
        "Changes": "改动",
        "SID inputs": "构码输入",
        "Domain": "领域",
        "Settings": "特殊设置",
        "Links": "链接",
        "Reading level": "阅读级别",
    },
    "scope_zh": {"user": "用户", "item": "物品"},
    "overview": "篇",
    "level_n": "第 {n} 级",
    "glance_title": "速览",
    "colon": "：",
    "on_this_page": "本页目录",
    "glance_head": ("维度", "摘要"),
    "glance_rows": {
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
    "links": {
        "Paper": "论文",
        "Code": "代码",
        "Code (third-party)": "代码（第三方）",
        "Matrix": "问题 × 阶段矩阵",
        "Stages": "按阶段索引",
        "Modality": "按模态找论文",
        "Domain": "按领域找论文",
    },
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
        "toc": (
            "[问题 × 阶段矩阵](#问题--阶段矩阵) · [每篇改了什么](#每篇改了什么) · "
            "[按模态找论文](#按模态找论文) · [按领域找论文](#按领域找论文) · "
            "[全部论文](#全部论文) · [参与贡献](#参与贡献)"
        ),
        "scope_title": "收录范围",
        "scope": "本仓库收录 {n} 篇语义 ID（Semantic ID，简称 SID，即把每个物品编码为一串离散码字、由序列模型逐位生成下一物品）生成式推荐论文："
                 "其中 {m} 篇方法论文按研究问题与主改阶段归入下方矩阵，{k} 篇为综述、系统与基准（本地生活场景论文另见 [POI 索引](pages/zh/index/poi.md)）。"
                 "下图按 arXiv 首次挂出月份统计每季度新增论文数。",
        "start_title": "阅读导航",
        "start_note": "按你的查找目的，从下表选择对应入口：",
        "start_head": ("我想……", "去哪里看"),
        "start": [
            ("刚接触 Semantic ID，了解基本流程并从代表作读起", "[入门指南](guides/start-here.zh.md)"),
            ("找解决某类问题的方法（如码字冲突、表征对齐、推理效率）", "[问题 × 阶段矩阵](#问题--阶段矩阵)"),
            ("看一篇论文具体改了五阶段流程中的哪些地方", "[每篇改了什么](#每篇改了什么)"),
            ("在同一个流程阶段内横向对比不同方法", "[按阶段索引](pages/zh/index/stages.md)"),
            ("找用多模态内容或协同过滤（CF）信号构码的论文", "[按模态找论文](pages/zh/index/modality.md)"),
            ("找某个业务领域的论文（如电商、本地生活 POI、短视频）", "[按领域找论文](pages/zh/index/domain.md)"),
            ("找公开了开源代码的论文", "[有代码的论文](pages/zh/index/code.md)"),
            ("让大模型或检索工具直接读取这个仓库", "[llms.txt](llms.txt)（英文）"),
        ],
        "starter_title": "代表性必读论文",
        "starter_note": "初读建议先看下表三篇代表作，分别对应标准五阶段流程、工业界本地生活扩展与长 ID 并行生成：",
        "starter_head": ("论文", "核心机制", "发表"),
        "matrix_title": "问题 × 阶段矩阵",
        "matrix_note": "下表行是六类研究问题，列是论文主要改动的五个流程阶段；点击格内数字可跳到对应论文列表。",
        "legend_note": "表中与论文页常用的标记和缩写含义如下（完整定义见 [术语表](guides/glossary.zh.md)）：",
        "problem": "研究问题",
        "total": "合计",
        "changes_title": "每篇改了什么",
        "changes_fig_note": "下图中，行是论文主要改动的阶段列（●），列是同一篇论文同时改动的其他阶段列（○）。",
        "changes_legend": "下表按研究问题折叠：● 标综述 Table 1 主改动列，○ 标同时改动的其他列（训练拆为“编号器更新”即码本如何随生成器更新、“训练目标”即生成器损失函数），空白格表示沿用常规做法。",
        "changes_method": "方法",
        "modality_title": "按模态找论文",
        "modality_fig_note": "下图展示各时期在构码阶段仅用文本（`Text`）、融合多模态内容（`Multimodal`）或引入用户交互协同过滤信号（`With CF`）的论文占比。",
        "modality_note": "下表按构码输入信号的四个维度分组列出论文入口（内容组按分支判定，协同与上下文组按全部分支合并判定，一篇可入多组）：",
        "modality_head": ("方面", "分组"),
        "domain_title": "按领域找论文",
        "domain_note": "下表将评测数据集归入四类业务场景，组内按论文数从多到少排列（跨领域论文同时列入各对应领域）：",
        "domain_head": ("类别", "领域"),
        "legend_head": ("标记", "含义"),
        "updates_title": "最近更新",
        "updates_note": "按日期倒序记录仓库内容增补与综述 Table 1 同步情况：",
        "papers": "涉及论文：",
        "all_title": "全部论文",
        "all_note": "按研究问题分带与主要改动阶段排列的完整论文列表（每篇含一句话核心机制、论文与代码链接）：",
        "back_to_top": "[↑ 回到顶部](#awesome-semantic-id-generative-recommendation)",
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
        "modality_title": "按模态找论文",
        "modality_intro": "本页按输入 SID 编号器的信息类型分组列出论文（分组规则定义于 `data/vocab.yaml`）。"
                          "内容方面按各构码分支分别判定，协同与上下文方面按全部分支合起来判定；同一篇论文可进入多个分组，各节列出完整的构码分支值与应用领域。",
        "domain_title": "按领域找论文",
        "domain_intro": "本页按实验数据集所属的业务领域分组列出论文；涉及多个领域的论文同时列入各对应小节。下图按论文数从多到少展示各领域的收录规模：",
        "domain_nav_note": "点击下表中的领域名称可直接跳到对应小节：",
        "sid_inputs_col": "构码输入",
        "domain_col": "领域",
        "empty_group": "当前暂无论文归入本组。",
    },
    "glossary": {
        "title": "术语表",
        "intro": "本页由 [`data/vocab.yaml`](../data/vocab.yaml) 自动生成，定义综述 Table 1、论文详情页与各索引页中的受控词表取值。",
        "symbols": "表内符号",
        "problems": "研究问题",
        "modality": "构码输入模态（SID Inputs）",
        "domain": "应用领域（Domain）",
        "settings": "特殊实验设置（Settings）",
    },
    "legend": [
        ("`†`", "根据论文点名沿用的基座或配置推断得到。"),
        ("`A / B`", "包含两个分支或两种评测配置。"),
        ("`–`", "论文未报告。"),
        ("`n/a`", "不适用于该方法。"),
        ("`●` / `○`", "综述 Table 1 主改动列（`●`）与新增具体机制的其他列（`○`）。"),
        ("**加粗**", "该论文主要改动的流程阶段。"),
        ("空白格", "该主分类下暂无论文。"),
        ("`warm`", "实验设置卡中的热启动过滤协议标签。"),
    ],
}
FLOW_IDS = ["R", "T", "B", "TR", "I"]
BASE_STYLE = "fill:#f8fafc,stroke:#cbd5e1"
MAIN_STYLE = "fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px"
OTHER_STYLE = "fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3"
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


def change_kind(val) -> str:
    if val == "primary":
        return "primary"
    if isinstance(val, dict) and val.get("value") == "other":
        return "other"
    return "none"


def change_dot(val) -> str:
    k = change_kind(val)
    return "● " if k == "primary" else ("○ " if k == "other" else "")


def flow_chart(rec: dict, zh: bool = False) -> list:
    """Mermaid flowchart of the five stages; primary stage gets light-blue fill, stages with ○ get dashed borders."""
    ch = rec["changes"]
    s_disp = lambda s: f"{ZH_LABELS['stages_zh'][s]} {s}" if zh else s
    tok_lbl = COL_HEADERS_ZH["tokenizer"] if zh else "Tokenizer"
    obj_lbl = COL_HEADERS_ZH["objective"] if zh else "Objective"
    node_texts = [
        f"{s_disp('Representation')}<br/>{change_dot(ch['representation'])}{rec['representation']}",
        f"{s_disp('Tokenization')}<br/>{change_dot(ch['tokenization'])}{rec['tokenization']}",
        f"{s_disp('Backbone')}<br/>{change_dot(ch['backbone'])}{rec['backbone']}",
        f"{s_disp('Training')}<br/>{tok_lbl}: {change_dot(ch['tokenizer'])}{rec['tokenizer']}"
        f"<br/>{obj_lbl}: {change_dot(ch['objective'])}{rec['objective']}",
        f"{s_disp('Inference')}<br/>{change_dot(ch['inference'])}{rec['inference']}",
    ]
    nodes = " --> ".join(f"{fid}[{mm_label(txt)}]" for fid, txt in zip(FLOW_IDS, node_texts))
    stage_cols = [
        ["representation"],
        ["tokenization"],
        ["backbone"],
        ["tokenizer", "objective"],
        ["inference"],
    ]
    main_ids = [fid for fid, cols in zip(FLOW_IDS, stage_cols) if any(change_kind(ch[c]) == "primary" for c in cols)]
    other_ids = [
        fid for fid, cols in zip(FLOW_IDS, stage_cols)
        if fid not in main_ids and any(change_kind(ch[c]) == "other" for c in cols)
    ]
    styles = [f"    classDef base {BASE_STYLE}", f"    class {','.join(FLOW_IDS)} base"]
    if other_ids:
        styles += [f"    classDef other {OTHER_STYLE}", f"    class {','.join(other_ids)} other"]
    if main_ids:
        styles += [f"    classDef main {MAIN_STYLE}", f"    class {','.join(main_ids)} main"]
    return ["```mermaid", "flowchart LR", f"    {nodes}", *styles, "```"]


def format_changes_inline(rec: dict, zh: bool = False, sep: str = " · ", empty: str = "–") -> str:
    headers = COL_HEADERS_ZH if zh else COL_HEADERS_EN
    ch = rec["changes"]
    items = []
    for c in TECH_COLS:
        dot = change_dot(ch[c])
        if dot:
            items.append(f"{dot}{headers[c]}")
    return sep.join(items) if items else empty


def format_modality(rec: dict, code_wrap: bool = True) -> str:
    w = (lambda s: f"`{s}`") if code_wrap else str
    m = rec["modality"]
    if isinstance(m, dict):
        sep = " · " if code_wrap else "; "
        return sep.join(f"{br}: " + (" + ".join(w(x) for x in vals) if vals else "–") for br, vals in m.items())
    return " + ".join(w(x) for x in m)


def domain_zh_map(vocab: dict) -> dict:
    return {e["value"]: e["name_zh"] for e in vocab["domain"]}


def settings_zh_map(vocab: dict) -> dict:
    return {e["value"]: e["name_zh"] for e in vocab["settings"]}


def format_domain(rec: dict, dom_zh: dict, zh: bool = False, code_wrap: bool = True) -> str:
    w = (lambda s: f"`{s}`") if code_wrap else str
    sep = " · " if code_wrap else ", "
    return sep.join(w(dom_zh[d] if zh else d) for d in rec["domain"])


def format_settings(rec: dict, set_zh: dict, zh: bool = False, code_wrap: bool = True, empty: str = "") -> str:
    if not rec.get("settings"):
        return empty
    w = (lambda s: f"`{s}`") if code_wrap else str
    sep = " · " if code_wrap else ", "
    parts = []
    for s in rec["settings"]:
        if zh:
            lbl = (
                f"{set_zh[s['value']]}（{ZH_LABELS['scope_zh'][s['scope']]}）"
                if "scope" in s else set_zh[s["value"]]
            )
        else:
            lbl = f"{s['value']} ({s['scope']})" if "scope" in s else s["value"]
        parts.append(w(lbl))
    return sep.join(parts)


def content_modality_set(vocab: dict) -> set:
    return {e["value"] for e in vocab["modality"] if e.get("is_content")}


def match_modality_group(rec: dict, group: dict, content_set: set) -> bool:
    """Evaluate a declarative grouping rule from data/vocab.yaml against a paper's modality field."""
    m = rec["modality"]
    branches = list(m.values()) if isinstance(m, dict) else [m]
    union = {x for b in branches for x in b}
    b_contents = [set(b) & content_set for b in branches]
    rule = group["rule"]
    if rule == "branch_content_exact":
        return any(bc == {group["target"]} for bc in b_contents)
    if rule == "branch_content_single_excluding":
        excl = set(group["exclude"])
        return any(len(bc) == 1 and not (bc <= excl) for bc in b_contents)
    if rule == "branch_content_multi_or_any":
        inc = set(group["include_any"])
        return any(len(bc) >= 2 or bool(bc & inc) for bc in b_contents)
    if rule == "all_branches_no_content":
        excl = set(group.get("exclude", ()))
        excl_only = set(group.get("exclude_all_only", ()))
        return (
            all(len(bc) == 0 for bc in b_contents)
            and not (union & excl)
            and (not excl_only or not (union <= excl_only))
        )
    if rule == "union_exact":
        return union == {group["target"]}
    if rule == "union_with_other":
        return group["target"] in union and len(union) > 1
    if rule == "union_contains":
        return group["target"] in union
    raise ValueError(f"Unsupported modality_groups rule in data/vocab.yaml: {rule!r}")


def group_papers_by_modality(papers: list, vocab: dict) -> dict:
    cset = content_modality_set(vocab)
    ordered = by_year(papers)
    return {
        g["value"]: [r for r in ordered if match_modality_group(r, g, cset)]
        for g in vocab["modality_groups"]
    }


def ordered_domains(papers: list, vocab: dict) -> list:
    """Return [(domain_entry, papers_in_domain), ...] ordered by descending paper count, keeping unknown last."""
    ordered = by_year(papers)
    buckets = []
    for idx, entry in enumerate(vocab["domain"]):
        val = entry["value"]
        members = [r for r in ordered if val in r["domain"]]
        is_unk = val.startswith("unknown")
        buckets.append((is_unk, -len(members), idx, entry, members))
    buckets.sort(key=lambda x: (x[0], x[1], x[2]))
    return [(entry, members) for _, _, _, entry, members in buckets]


def format_group_entry(label: str, count: int, target_path: str, zh: bool = False) -> str:
    """Link to target_path#anchor with paper count; zero-paper groups render plain text with no link."""
    disp = f"{label}（{count}）" if zh else f"{label} ({count})"
    if count == 0:
        return disp
    anchor = slugify_heading(label)
    prefix = f"{target_path}#{anchor}" if target_path else f"#{anchor}"
    return f"[{disp}]({prefix})"


def build_modality_nav(papers: list, vocab: dict, mod_path: str, zh: bool = False) -> list:
    R = ZH_LABELS["readme"]
    grouped = group_papers_by_modality(papers, vocab)
    aspects = []
    seen_aspects = {}
    for g in vocab["modality_groups"]:
        asp = g["aspect_zh"] if zh else g["aspect"]
        if asp not in seen_aspects:
            seen_aspects[asp] = []
            aspects.append(asp)
        label = g["name_zh"] if zh else g["name"]
        seen_aspects[asp].append(format_group_entry(label, len(grouped[g["value"]]), mod_path, zh=zh))
    head = R["modality_head"] if zh else ("Aspect", "Groups")
    rows = [f"| {head[0]} | {head[1]} |", "| :--- | :--- |"]
    for asp in aspects:
        rows.append(f"| **{asp}** | {' · '.join(seen_aspects[asp])} |")
    return rows


def build_domain_nav(papers: list, vocab: dict, dom_path: str, zh: bool = False) -> list:
    R = ZH_LABELS["readme"]
    dom_buckets = ordered_domains(papers, vocab)
    categories = []
    seen_categories = {}
    for g in vocab["domain"]:
        cat = g["category_zh"] if zh else g["category"]
        if cat not in seen_categories:
            seen_categories[cat] = []
            categories.append(cat)
    categories.sort(key=lambda c: ("Other" in c or "其他" in c))
    for e, members in dom_buckets:
        cat = e["category_zh"] if zh else e["category"]
        label = e["name_zh"] if zh else e["value"]
        seen_categories[cat].append(format_group_entry(label, len(members), dom_path, zh=zh))
    head = R["domain_head"] if zh else ("Category", "Domains")
    rows = [f"| {head[0]} | {head[1]} |", "| :--- | :--- |"]
    for cat in categories:
        rows.append(f"| **{cat}** | {' · '.join(seen_categories[cat])} |")
    return rows


SVG_BG = "#fcfcfb"
SVG_TEXT = "#0b0b0b"
SVG_MUTED = "#52514e"
SVG_GRID = "#e4e3df"
SVG_BLUE = "#5B9BD5"
SVG_ORANGE = "#EE8866"
SVG_TEAL = "#44BB99"
SVG_HEAT_STEPS = ("#eef5fc", "#d6e8fa", "#bad8f7", "#96c5f3", "#6da7ec")
SVG_FONT_EN = '-apple-system, "Segoe UI", Helvetica, Arial, sans-serif'
SVG_FONT_ZH = '-apple-system, "Segoe UI", "PingFang SC", "Noto Sans CJK SC", Helvetica, Arial, sans-serif'
ARXIV_YM_RE = re.compile(r"(?:abs/|pdf/)?(\d{2})(\d{2})\.\d+")


def svg_esc(text: str) -> str:
    return html.escape(str(text), quote=True)


def svg_wrap(width: int, height: int, title: str, body: list, zh: bool = False) -> str:
    font = SVG_FONT_ZH if zh else SVG_FONT_EN
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        f'role="img" aria-label="{svg_esc(title)}" font-family=\'{font}\'>',
        f'  <rect x="0" y="0" width="{width}" height="{height}" rx="8" fill="{SVG_BG}"/>',
        *body,
        "</svg>",
        "",
    ]
    return "\n".join(lines)


def paper_quarter(rec: dict) -> tuple[int, int]:
    arxiv = (rec.get("links") or {}).get("arxiv") or ""
    m = ARXIV_YM_RE.search(arxiv)
    if m:
        yy, mm = int(m.group(1)), int(m.group(2))
        if 1 <= mm <= 12:
            return 2000 + yy, (mm - 1) // 3 + 1
    return int(rec["year"]), 4


def heat_cell_fill(val: int) -> str:
    if val <= 0:
        return SVG_BG
    if val <= 3:
        return SVG_HEAT_STEPS[0]
    if val <= 7:
        return SVG_HEAT_STEPS[1]
    if val <= 15:
        return SVG_HEAT_STEPS[2]
    if val <= 25:
        return SVG_HEAT_STEPS[3]
    return SVG_HEAT_STEPS[4]


def render_figure_block(fig_meta: dict, rel_svg_path: str, zh: bool = False) -> list:
    summary = "数据" if zh else "Data"
    return [
        f"![{fig_meta['alt']}]({rel_svg_path})",
        "",
        "<details>",
        f"<summary>{summary}</summary>",
        "",
        *fig_meta["table"],
        "",
        "</details>",
    ]


def build_figures(vocab: dict, papers: list) -> tuple[dict, dict]:
    """Return (svg_files_dict, figure_meta_dict) for both English and Chinese."""
    svg_files = {}
    meta = {"en": {}, "zh": {}}
    n_total = len(papers)

    # 1. Quarterly new papers (by first arXiv posting month; fallback to year Q4)
    q_counts = Counter(paper_quarter(r) for r in papers)
    min_y, min_q = min(q_counts)
    max_y, max_q = max(q_counts)
    quarters = []
    cy, cq = min_y, min_q
    while (cy, cq) <= (max_y, max_q):
        quarters.append((cy, cq, q_counts.get((cy, cq), 0)))
        cq += 1
        if cq > 4:
            cy += 1
            cq = 1

    for zh in (False, True):
        lang = "zh" if zh else "en"
        fname = "papers-by-quarter.zh.svg" if zh else "papers-by-quarter.svg"
        W, H = 760, 304
        x0, x1 = 56, 724
        y0, y1 = 86, 240
        y_max = 35
        title = (
            f"每季度新增论文数（{min_y} Q{min_q} – {max_y} Q{max_q}，N = {n_total}）"
            if zh else
            f"New Papers per Quarter ({min_y} Q{min_q} – {max_y} Q{max_q}, N = {n_total})"
        )
        subtitle = (
            "按 arXiv 首次提交月份统计；1 篇无 arXiv 链接的论文计入 2026 Q4"
            if zh else
            "Grouped by first arXiv posting month; 1 non-arXiv paper placed in 2026 Q4"
        )
        body = [
            f'  <text x="32" y="38" font-size="15" font-weight="600" fill="{SVG_TEXT}">{svg_esc(title)}</text>',
            f'  <text x="32" y="58" font-size="12" fill="{SVG_MUTED}">{svg_esc(subtitle)}</text>',
        ]
        for tick in range(0, y_max + 1, 5):
            ty = y1 - (tick / y_max) * (y1 - y0)
            body.append(f'  <line x1="{x0}" y1="{ty:.1f}" x2="{x1}" y2="{ty:.1f}" stroke="{SVG_GRID}" stroke-width="1"/>')
            body.append(
                f'  <text x="{x0 - 10}" y="{ty + 4:.1f}" font-size="11" fill="{SVG_MUTED}" text-anchor="end">{tick}</text>'
            )
        pts = []
        num_q = len(quarters)
        for i, (qy, qq, cnt) in enumerate(quarters):
            px = x0 + i * (x1 - x0) / max(1, num_q - 1)
            py = y1 - (cnt / y_max) * (y1 - y0)
            pts.append((px, py, qy, qq, cnt))
            body.append(f'  <line x1="{px:.1f}" y1="{y1}" x2="{px:.1f}" y2="{y1 + 5}" stroke="{SVG_GRID}" stroke-width="1"/>')
            body.append(
                f'  <text x="{px:.1f}" y="{y1 + 19}" font-size="11" fill="{SVG_MUTED}" text-anchor="middle">Q{qq}</text>'
            )
            if i == 0 or qq == 1:
                body.append(
                    f'  <text x="{px:.1f}" y="{y1 + 36}" font-size="11" font-weight="600" fill="{SVG_TEXT}" text-anchor="middle">{qy}</text>'
                )
        poly_pts = " ".join(f"{px:.1f},{py:.1f}" for px, py, *_ in pts)
        body.append(
            f'  <polyline fill="none" stroke="{SVG_BLUE}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" points="{poly_pts}"/>'
        )
        for px, py, _, _, cnt in pts:
            body.append(
                f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{SVG_BLUE}" stroke="{SVG_BG}" stroke-width="2"/>'
            )
            body.append(
                f'  <text x="{px:.1f}" y="{py - 9:.1f}" font-size="10.5" fill="{SVG_MUTED}" text-anchor="middle">{cnt}</text>'
            )
        svg_files[fname] = svg_wrap(W, H, title, body, zh=zh)
        t_head = "| 季度 | 新增论文数 |" if zh else "| Quarter | New Papers |"
        t_rows = [t_head, "| :--- | :--- |", *[f"| {qy} Q{qq} | {cnt} |" for qy, qq, cnt in quarters]]
        y2023 = sum(cnt for qy, _, cnt in quarters if qy == 2023)
        y2024 = sum(cnt for qy, _, cnt in quarters if qy == 2024)
        y2025 = sum(cnt for qy, _, cnt in quarters if qy == 2025)
        y2026 = sum(cnt for qy, _, cnt in quarters if qy == 2026)
        peak = max(cnt for *_, cnt in quarters)
        alt = (
            f"2022 Q4 至 2026 Q4 每季度新增 SID 生成式推荐论文数（共 {n_total} 篇），由 2022 Q4 的 1 篇、2023 年的 {y2023} 篇、"
            f"2024 年的 {y2024} 篇增长至 2025 年的 {y2025} 篇与 2026 年的 {y2026} 篇（单季峰值 {peak} 篇）。"
            if zh else
            f"Quarterly new SID generative recommendation papers from 2022 Q4 to 2026 Q4 (N = {n_total}), rising from 1 paper in 2022 Q4, "
            f"{y2023} in 2023, and {y2024} in 2024 to {y2025} in 2025 and {y2026} in 2026 (peaking at {peak} per quarter)."
        )
        meta[lang]["quarter"] = {"alt": alt, "table": t_rows}

    # 2. 6x6 Stage Co-modification Heatmap (non-psb papers)
    non_psb = [r for r in papers if r["problem"] != "psb"]
    n_non_psb = len(non_psb)
    prim_counts = {c: 0 for c in TECH_COLS}
    co_matrix = {(r_col, c_col): 0 for r_col in TECH_COLS for c_col in TECH_COLS}
    for r in non_psb:
        ch = r["changes"]
        prim_cols = [c for c in TECH_COLS if change_kind(ch.get(c)) == "primary"]
        for pc in prim_cols:
            prim_counts[pc] += 1
            for oc in TECH_COLS:
                if oc != pc and change_kind(ch.get(oc)) == "other":
                    co_matrix[(pc, oc)] += 1

    for zh in (False, True):
        lang = "zh" if zh else "en"
        fname = "stage-cochanges.zh.svg" if zh else "stage-cochanges.svg"
        W, H = 760, 384
        x0, y0 = 204, 108
        cell_w, cell_h = 88, 38
        col_labels = [COL_HEADERS_ZH[c] if zh else COL_HEADERS_EN[c] for c in TECH_COLS]
        title = (
            f"主改列与协同改动列共现热力图（N = {n_non_psb}，不含“范式、系统与基准”）"
            if zh else
            f"Primary vs. Co-Modified Columns (N = {n_non_psb}; Paradigms, Systems and Benchmarks excluded)"
        )
        subtitle = (
            "行 = 表 1 主改列（●，括号内为主改论文数）；列 = 同一篇论文同步改动的其他列（○）"
            if zh else
            "Row = primary column (●, n = papers); column = another column changed in the same paper (○)"
        )
        corner_note = "主改列 (●) ↓ · 协同改 (○) →" if zh else "Primary (●) ↓ · Co-modified (○) →"
        body = [
            f'  <text x="32" y="38" font-size="15" font-weight="600" fill="{SVG_TEXT}">{svg_esc(title)}</text>',
            f'  <text x="32" y="58" font-size="12" fill="{SVG_MUTED}">{svg_esc(subtitle)}</text>',
            f'  <text x="{x0 - 12}" y="{y0 - 14}" font-size="11" fill="{SVG_MUTED}" text-anchor="end">{svg_esc(corner_note)}</text>',
        ]
        for j, c_label in enumerate(col_labels):
            cx = x0 + (j + 0.5) * cell_w
            body.append(
                f'  <text x="{cx:.1f}" y="{y0 - 14}" font-size="11.5" font-weight="600" fill="{SVG_TEXT}" text-anchor="middle">{svg_esc(c_label)}</text>'
            )
        for i, r_col in enumerate(TECH_COLS):
            ry = y0 + i * cell_h
            r_label = f"{col_labels[i]} (n={prim_counts[r_col]})"
            body.append(
                f'  <text x="{x0 - 12}" y="{ry + cell_h / 2 + 4:.1f}" font-size="11.5" font-weight="600" fill="{SVG_TEXT}" text-anchor="end">{svg_esc(r_label)}</text>'
            )
            for j, c_col in enumerate(TECH_COLS):
                cx = x0 + j * cell_w
                val = co_matrix[(r_col, c_col)]
                fill = SVG_BG if i == j else heat_cell_fill(val)
                body.append(
                    f'  <rect x="{cx}" y="{ry}" width="{cell_w}" height="{cell_h}" fill="{fill}" stroke="{SVG_GRID}" stroke-width="1"/>'
                )
                if i != j:
                    fw = "600" if val > 0 else "400"
                    body.append(
                        f'  <text x="{cx + cell_w / 2:.1f}" y="{ry + cell_h / 2 + 4:.1f}" font-size="12" font-weight="{fw}" fill="{SVG_TEXT}" text-anchor="middle">{val}</text>'
                    )
        # Scale legend at bottom
        scale_y = y0 + 6 * cell_h + 16
        scale_label = "篇数色阶：" if zh else "Paper count:"
        body.append(
            f'  <text x="{x0}" y="{scale_y + 11}" font-size="11" fill="{SVG_MUTED}">{svg_esc(scale_label)}</text>'
        )
        bins = [("0", SVG_BG), ("1–3", SVG_HEAT_STEPS[0]), ("4–7", SVG_HEAT_STEPS[1]),
                ("8–15", SVG_HEAT_STEPS[2]), ("16–25", SVG_HEAT_STEPS[3]), ("26+", SVG_HEAT_STEPS[4])]
        sx = x0 + (62 if zh else 76)
        for b_text, b_fill in bins:
            body.append(
                f'  <rect x="{sx}" y="{scale_y}" width="14" height="14" fill="{b_fill}" stroke="{SVG_GRID}" stroke-width="1"/>'
            )
            body.append(
                f'  <text x="{sx + 19}" y="{scale_y + 11}" font-size="11" fill="{SVG_MUTED}">{svg_esc(b_text)}</text>'
            )
            sx += 19 + len(b_text) * 7 + 16
        svg_files[fname] = svg_wrap(W, H, title, body, zh=zh)
        first_col = "主改列 (●) \\ 协同改 (○)" if zh else "Primary (●) \\ Co-modified (○)"
        t_rows = [
            f"| {first_col} | {' | '.join(col_labels)} |",
            "|" + " :--- |" * (len(TECH_COLS) + 1),
        ]
        for i, r_col in enumerate(TECH_COLS):
            r_label = f"{col_labels[i]} (n={prim_counts[r_col]})"
            cells = ["–" if i == j else str(co_matrix[(r_col, c_col)]) for j, c_col in enumerate(TECH_COLS)]
            t_rows.append(f"| {r_label} | {' | '.join(cells)} |")
        tok_obj = co_matrix[("tokenization", "objective")]
        tok_bb = co_matrix[("tokenization", "backbone")]
        tok_inf = co_matrix[("tokenization", "inference")]
        bb_obj = co_matrix[("backbone", "objective")]
        alt = (
            f"{n_non_psb} 篇论文（不含“范式、系统与基准”）的 6×6 阶段共同改动热力图：主改构码的 {prim_counts['tokenization']} 篇中，"
            f"同时改训练目标的 {tok_obj} 篇、改生成骨干的 {tok_bb} 篇、改推理的 {tok_inf} 篇；主改生成骨干的 {prim_counts['backbone']} 篇中，"
            f"同时改训练目标的 {bb_obj} 篇。"
            if zh else
            f"6x6 co-modification heatmap over {n_non_psb} papers (excluding Paradigms, Systems and Benchmarks): of the {prim_counts['tokenization']} papers "
            f"whose primary change is Tokenization, {tok_obj} also change Objective, {tok_bb} Backbone, and {tok_inf} Inference; of the "
            f"{prim_counts['backbone']} primary Backbone papers, {bb_obj} also change Objective."
        )
        meta[lang]["cochanges"] = {"alt": alt, "table": t_rows}

    # 3. Modality share by year (years with < 5 papers merged into adjacent year)
    grouped_mod = group_papers_by_modality(papers, vocab)
    mod_ids = {g_key: {r["id"] for r in members} for g_key, members in grouped_mod.items()}
    raw_years = sorted(Counter(int(r["year"]) for r in papers).items())
    year_buckets = []
    for y, cnt in raw_years:
        if not year_buckets:
            year_buckets.append([y])
        elif sum(1 for r in papers if int(r["year"]) in year_buckets[-1]) < 5 or cnt < 5:
            year_buckets[-1].append(y)
        else:
            year_buckets.append([y])

    series_defs = [
        ("Text", "Text", "文本", SVG_BLUE),
        ("Multimodal", "Multimodal", "多模态", SVG_ORANGE),
        ("With CF", "With CF", "含协同信号", SVG_TEAL),
    ]
    bucket_stats = []
    for ys in year_buckets:
        y_set = set(ys)
        b_papers = [r for r in papers if int(r["year"]) in y_set]
        b_total = len(b_papers)
        label = f"{ys[0]}–{ys[-1]}" if len(ys) > 1 else str(ys[0])
        sub_en = f"(n = {b_total}, incl. {sum(1 for r in b_papers if int(r['year']) == ys[0])} in {ys[0]})" if len(ys) > 1 else f"(n = {b_total})"
        sub_zh = f"（n = {b_total}，含 {ys[0]} 年 {sum(1 for r in b_papers if int(r['year']) == ys[0])} 篇）" if len(ys) > 1 else f"（n = {b_total}）"
        s_vals = {}
        for s_key, *_ in series_defs:
            c = sum(1 for r in b_papers if r["id"] in mod_ids[s_key])
            s_vals[s_key] = (c, (c / b_total * 100.0) if b_total else 0.0)
        bucket_stats.append({"label": label, "sub_en": sub_en, "sub_zh": sub_zh, "total": b_total, "vals": s_vals})

    for zh in (False, True):
        lang = "zh" if zh else "en"
        fname = "modality-by-year.zh.svg" if zh else "modality-by-year.svg"
        W, H = 760, 310
        x0, x1 = 64, 536
        y0, y1 = 86, 246
        y_max = 80.0
        title = (
            f"各时期不同 SID 词表输入模态的论文占比（N = {n_total}）"
            if zh else
            f"Share of Papers by SID Tokenizer Input Modality over Time (N = {n_total})"
        )
        subtitle = (
            "占当期论文总数的百分比（单篇可归入多组；2023 年仅 3 篇，并入 2023–2024）"
            if zh else
            "Percentage of papers per period (multi-label; 2023 has 3 papers and is merged into 2023–2024)"
        )
        body = [
            f'  <text x="32" y="38" font-size="15" font-weight="600" fill="{SVG_TEXT}">{svg_esc(title)}</text>',
            f'  <text x="32" y="58" font-size="12" fill="{SVG_MUTED}">{svg_esc(subtitle)}</text>',
        ]
        for tick in (0, 20, 40, 60, 80):
            ty = y1 - (tick / y_max) * (y1 - y0)
            body.append(f'  <line x1="{x0}" y1="{ty:.1f}" x2="{x1}" y2="{ty:.1f}" stroke="{SVG_GRID}" stroke-width="1"/>')
            body.append(
                f'  <text x="{x0 - 10}" y="{ty + 4:.1f}" font-size="11" fill="{SVG_MUTED}" text-anchor="end">{tick}%</text>'
            )
        nb = len(bucket_stats)
        x_pad = 36
        xs = [x0 + x_pad + i * (x1 - x0 - 2 * x_pad) / max(1, nb - 1) for i in range(nb)]
        for bx, b in zip(xs, bucket_stats):
            body.append(f'  <line x1="{bx:.1f}" y1="{y1}" x2="{bx:.1f}" y2="{y1 + 5}" stroke="{SVG_GRID}" stroke-width="1"/>')
            body.append(
                f'  <text x="{bx:.1f}" y="{y1 + 20}" font-size="11.5" font-weight="600" fill="{SVG_TEXT}" text-anchor="middle">{svg_esc(b["label"])}</text>'
            )
            sub_txt = b["sub_zh"] if zh else b["sub_en"]
            body.append(
                f'  <text x="{bx:.1f}" y="{y1 + 36}" font-size="11" fill="{SVG_MUTED}" text-anchor="middle">{svg_esc(sub_txt)}</text>'
            )

        end_labels = []
        for s_key, name_en, name_zh, color in series_defs:
            s_name = name_zh if zh else name_en
            s_pts = []
            for i, (bx, b) in enumerate(zip(xs, bucket_stats)):
                cnt, pct = b["vals"][s_key]
                py = y1 - (pct / y_max) * (y1 - y0)
                s_pts.append((bx, py, cnt, pct, i))
            poly = " ".join(f"{px:.1f},{py:.1f}" for px, py, *_ in s_pts)
            body.append(
                f'  <polyline fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" points="{poly}"/>'
            )
            for px, py, cnt, pct, i in s_pts:
                body.append(
                    f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{color}" stroke="{SVG_BG}" stroke-width="2"/>'
                )
                if i < nb - 1:
                    dy = -9 if pct > 5 else -8
                    body.append(
                        f'  <text x="{px:.1f}" y="{py + dy:.1f}" font-size="10.5" fill="{SVG_MUTED}" text-anchor="middle">{pct:.1f}%</text>'
                    )
            last_x, last_y, last_cnt, last_pct, _ = s_pts[-1]
            end_labels.append({
                "x": last_x,
                "y": last_y,
                "label_y": last_y,
                "color": color,
                "text": f"{s_name} · {last_pct:.1f}% ({last_cnt})",
            })

        # Ensure direct end-of-line labels have at least 22px vertical separation
        end_labels.sort(key=lambda d: d["y"])
        min_gap = 22.0
        for idx in range(1, len(end_labels)):
            if end_labels[idx]["label_y"] - end_labels[idx - 1]["label_y"] < min_gap:
                mid = 0.5 * (end_labels[idx]["y"] + end_labels[idx - 1]["y"])
                end_labels[idx - 1]["label_y"] = mid - 0.5 * min_gap
                end_labels[idx]["label_y"] = mid + 0.5 * min_gap
        for el in end_labels:
            lx = el["x"]
            ly = el["label_y"]
            body.append(
                f'  <line x1="{lx + 6:.1f}" y1="{el["y"]:.1f}" x2="{x1 + 14:.1f}" y2="{ly:.1f}" stroke="{SVG_GRID}" stroke-width="1"/>'
            )
            body.append(
                f'  <circle cx="{x1 + 22:.1f}" cy="{ly:.1f}" r="3.5" fill="{el["color"]}"/>'
            )
            body.append(
                f'  <text x="{x1 + 31:.1f}" y="{ly + 4:.1f}" font-size="11.5" font-weight="600" fill="{SVG_TEXT}">{svg_esc(el["text"])}</text>'
            )

        svg_files[fname] = svg_wrap(W, H, title, body, zh=zh)
        t_head = (
            "| 时期 | 论文总数 | 文本 (Text) | 多模态 (Multimodal) | 含协同信号 (With CF) |"
            if zh else
            "| Period | Total Papers | Text | Multimodal | With CF |"
        )
        t_rows = [t_head, "| :--- | :--- | :--- | :--- | :--- |"]
        for b in bucket_stats:
            tc, tp = b["vals"]["Text"]
            mc, mp = b["vals"]["Multimodal"]
            cc, cp = b["vals"]["With CF"]
            p_lbl = f"{b['label']} {b['sub_zh'] if zh else b['sub_en']}"
            t_rows.append(f"| {p_lbl} | {b['total']} | {tc} ({tp:.1f}%) | {mc} ({mp:.1f}%) | {cc} ({cp:.1f}%) |")
        b0, b1, b2 = bucket_stats[0], bucket_stats[1], bucket_stats[2]
        alt = (
            f"{b0['label']}（n = {b0['total']}）、{b1['label']}（n = {b1['total']}）与 {b2['label']}（n = {b2['total']}）各时期 SID 词表输入模态占比："
            f"文本由 {b0['vals']['Text'][1]:.1f}% 变化至 {b2['vals']['Text'][1]:.1f}%，多模态由 {b0['vals']['Multimodal'][1]:.1f}% 升至 "
            f"{b1['vals']['Multimodal'][1]:.1f}% 与 {b2['vals']['Multimodal'][1]:.1f}%，含协同信号由 {b0['vals']['With CF'][1]:.1f}% "
            f"升至 {b1['vals']['With CF'][1]:.1f}% 与 {b2['vals']['With CF'][1]:.1f}%。"
            if zh else
            f"Share of papers by SID tokenizer input modality across {b0['label']} (n = {b0['total']}), {b1['label']} (n = {b1['total']}), "
            f"and {b2['label']} (n = {b2['total']}): Text stays at {b0['vals']['Text'][1]:.1f}%–{b2['vals']['Text'][1]:.1f}%, Multimodal rises "
            f"from {b0['vals']['Multimodal'][1]:.1f}% to {b1['vals']['Multimodal'][1]:.1f}% and {b2['vals']['Multimodal'][1]:.1f}%, and With CF "
            f"goes from {b0['vals']['With CF'][1]:.1f}% to {b1['vals']['With CF'][1]:.1f}% and {b2['vals']['With CF'][1]:.1f}%."
        )
        meta[lang]["modality"] = {"alt": alt, "table": t_rows}

    # 4. Domain distribution Cleveland dot plot
    dom_buckets = ordered_domains(papers, vocab)
    for zh in (False, True):
        lang = "zh" if zh else "en"
        fname = "domain-distribution.zh.svg" if zh else "domain-distribution.svg"
        num_d = len(dom_buckets)
        row_h = 22
        y_start = 94
        y_end = y_start + (num_d - 1) * row_h
        W, H = 760, y_end + 56
        x0, x1 = 196, 716
        x_max = 160.0
        title = (
            f"各评测领域的论文分布（N = {n_total}）"
            if zh else
            f"Papers per Evaluation Domain (N = {n_total})"
        )
        subtitle = (
            "按评测数据集所属业务领域统计的克利夫兰点图（跨领域论文计入各对应领域）"
            if zh else
            "Cleveland dot plot of dataset domains (multi-domain papers counted in each applicable domain)"
        )
        body = [
            f'  <text x="32" y="38" font-size="15" font-weight="600" fill="{SVG_TEXT}">{svg_esc(title)}</text>',
            f'  <text x="32" y="58" font-size="12" fill="{SVG_MUTED}">{svg_esc(subtitle)}</text>',
        ]
        for tick in range(0, 161, 40):
            tx = x0 + (tick / x_max) * (x1 - x0)
            body.append(
                f'  <line x1="{tx:.1f}" y1="{y_start - 12}" x2="{tx:.1f}" y2="{y_end + 10}" stroke="{SVG_GRID}" stroke-width="1"/>'
            )
            body.append(
                f'  <text x="{tx:.1f}" y="{y_end + 26}" font-size="11" fill="{SVG_MUTED}" text-anchor="middle">{tick}</text>'
            )
        for i, (entry, members) in enumerate(dom_buckets):
            ry = y_start + i * row_h
            cnt = len(members)
            d_label = entry["name_zh"] if zh else entry["value"]
            cx = x0 + (cnt / x_max) * (x1 - x0)
            body.append(f'  <line x1="{x0}" y1="{ry}" x2="{x1}" y2="{ry}" stroke="{SVG_GRID}" stroke-width="1"/>')
            body.append(
                f'  <text x="{x0 - 12}" y="{ry + 4}" font-size="11.5" fill="{SVG_TEXT}" text-anchor="end">{svg_esc(d_label)}</text>'
            )
            body.append(
                f'  <circle cx="{cx:.1f}" cy="{ry}" r="4" fill="{SVG_BLUE}" stroke="{SVG_BG}" stroke-width="2"/>'
            )
            body.append(
                f'  <text x="{cx + 9:.1f}" y="{ry + 4}" font-size="11" fill="{SVG_TEXT}">{cnt}</text>'
            )
        svg_files[fname] = svg_wrap(W, H, title, body, zh=zh)
        t_head = "| 领域 | 类别 | 论文数 |" if zh else "| Domain | Category | Papers |"
        t_rows = [t_head, "| :--- | :--- | :--- |"]
        for entry, members in dom_buckets:
            d_lbl = entry["name_zh"] if zh else entry["value"]
            c_lbl = entry["category_zh"] if zh else entry["category"]
            t_rows.append(f"| {d_lbl} | {c_lbl} | {len(members)} |")
        top4 = [(e["name_zh"] if zh else e["value"], len(m)) for e, m in dom_buckets[:4]]
        alt = (
            f"{num_d} 个评测业务领域的论文数量克利夫兰点图（共 {n_total} 篇）："
            f"{top4[0][0]}以 {top4[0][1]} 篇居首，其次为{top4[1][0]}（{top4[1][1]} 篇）、"
            f"{top4[2][0]}（{top4[2][1]} 篇）与{top4[3][0]}（{top4[3][1]} 篇）。"
            if zh else
            f"Cleveland dot plot of paper counts across {num_d} evaluation domains (N = {n_total}): "
            f"{top4[0][0]} leads with {top4[0][1]} papers, followed by {top4[1][0]} ({top4[1][1]}), "
            f"{top4[2][0]} ({top4[2][1]}), and {top4[3][0]} ({top4[3][1]})."
        )
        meta[lang]["domain"] = {"alt": alt, "table": t_rows}

    return svg_files, meta


def build_changes_section(vocab: dict, cell: dict, psb_list: list, cochanges_fig: dict, zh: bool = False) -> list:
    """Render 'What Each Paper Changes' with 1-sentence legend, co-change heatmap figure, and 7 collapsed <details> tables."""
    R = ZH_LABELS["readme"]
    probs = {e["value"]: e for e in vocab["problem"]}
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    psb = probs["psb"]
    page_dir = "pages/zh/papers" if zh else "pages/papers"
    col_heads = [COL_HEADERS_ZH[c] if zh else COL_HEADERS_EN[c] for c in TECH_COLS]
    head_row = [R["changes_method"] if zh else "Method", *col_heads]

    fig_note = R["changes_fig_note"] if zh else (
        "In the heatmap below, each row is the column a paper mainly modifies (●) and each column is another stage it modifies at the same time (○)."
    )
    legend = R["changes_legend"] if zh else (
        "In the tables below, ● marks the primary Table 1 column, ○ marks co-modified columns "
        "(`Tokenizer` = how codebook parameters are updated during generator training; `Objective` = generator training loss), "
        "and blank cells use standard choices."
    )
    svg_rel = "assets/figures/stage-cochanges.zh.svg" if zh else "assets/figures/stage-cochanges.svg"
    out = [
        f"## {R['changes_title'] if zh else 'What Each Paper Changes'}", "",
        fig_note, "",
        *render_figure_block(cochanges_fig, svg_rel, zh=zh), "",
        legend, "",
    ]

    bands = [
        *((p, [r for s in STAGES for r in cell[(p["value"], s)]]) for p in problems),
        (psb, psb_list),
    ]
    for p, band_papers in bands:
        cnt = len(band_papers)
        cnt_str = f"{cnt} 篇" if zh else f"{cnt} paper{'s' if cnt != 1 else ''}"
        summary = f"{band(p, zh)} · {cnt_str}"
        t_rows = [
            f"| {' | '.join(head_row)} |",
            "|" + " :--- |" * len(head_row),
        ]
        for r in band_papers:
            m_link = f"[{r['name']}]({page_dir}/{r['id']}.md)"
            ch_cells = []
            for c in TECH_COLS:
                dot = change_dot(r["changes"][c])
                val = cell_text(r[c])
                ch_cells.append(f"{dot}`{val}`" if dot else "")
            t_rows.append(f"| {' | '.join([m_link, *ch_cells])} |")
        out += [
            "<details>",
            f"<summary>{summary}</summary>",
            "",
            *t_rows,
            "",
            "</details>",
            "",
        ]
    return out


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
    dom_zh = domain_zh_map(vocab)
    set_zh = settings_zh_map(vocab)
    anchor = slugify_heading(cell_label(rec, probs, zh))
    sections = SECTIONS_ZH if zh else SECTIONS
    level = reading_level(n, sections)
    desc_key = "description_zh" if zh else "description"
    defs = {c: {e["value"]: e.get(desc_key) or e.get("description") for e in vocab.get(c, [])} for c in TECH_COLS}
    tldr = ((rec.get("tldr_zh") if zh else rec.get("tldr")) or "").strip()
    glance = [(k, (n or {}).get("glance", {}).get(k)) for k in GLANCE_KEYS]
    head = Z["glance_head"] if zh else ("Aspect", "Summary")
    glance_rows = [f"| {Z['glance_rows'][a] if zh else a} | {v.strip().replace('|', chr(92) + '|')} |" for a, v in glance if v]
    colon = Z["colon"] if zh else ": "
    blocks = [("TL;DR", [f"> [!NOTE]\n> {tldr}"])] if tldr else []
    blocks += [(Z["glance_title"] if zh else "At a Glance", ["\n".join([f"| {head[0]} | {head[1]} |", "| :-- | :-- |", *glance_rows])])] if glance_rows else []
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
    toc = " · ".join(f"[{t if zh else TOC_SHORT.get(t, t)}](#{slugify_heading(t)})" for t, _ in blocks if t)
    vals = dict.fromkeys(
        f"- `{rec[c]}`{colon}{defs[c][rec[c]]}"
        for c in TECH_COLS
        if rec[c] not in ("n/a", "–") and defs[c].get(rec[c])
    )
    nav_bar = (
        f"[← {Z['links']['Matrix']}]({readme}#{anchor}) · [{Z['links']['Stages']}](../index/stages.md) · "
        f"[{Z['links']['Modality']}](../index/modality.md) · [{Z['links']['Domain']}](../index/domain.md) · "
        f"[English](../../papers/{rec['id']}.md) | 中文"
        if zh else
        f"[← Problem × Stage Matrix]({readme}#{anchor}) · [Papers by Stage](../index/stages.md) · "
        f"[Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · "
        f"English | [中文](../zh/papers/{rec['id']}.md)"
    )
    level_name = (Z["levels"] if zh else LEVELS)[level - 1]
    level_text = f"{level_name}（{Z['level_n'].format(n=level)}）" if zh else f"{level_name} (Level {level})"
    settings_str = format_settings(rec, set_zh, zh=zh, code_wrap=True)
    card = [
        ("Title", f"*{title_of(rec)}*"),
        ("Authors", rec["authors"]),
        ("Venue", rec["venue"]),
        ("Cell", cell_str),
        ("Changes", format_changes_inline(rec, zh=zh)),
        ("SID inputs", format_modality(rec, code_wrap=True)),
        ("Domain", format_domain(rec, dom_zh, zh=zh, code_wrap=True)),
        *([("Settings", settings_str)] if settings_str else []),
        ("Links", link_line(rec, zh=zh)),
        ("Reading level", level_text),
    ]
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


def heat(n: int, anchor: str) -> str:
    if not n:
        return ""
    color = [c for lo, c in HEAT if n >= lo][-1]
    return f"[![{n}](https://img.shields.io/badge/{n}-{color}?style=for-the-badge)](#{anchor})"


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
    """Centered title, one-line description, light badges, language switch, TOC line, and the five-stage overview."""
    R = ZH_LABELS["readme"]
    labels = R["badges"] if zh else ("papers", "updated", "license")
    latest = max((u["date"] for u in updates), default="")
    badges = [(labels[0], len(papers), "papers", "#" + slugify_heading(R["all_title"] if zh else "All Papers")),
              (labels[1], latest, "updated", "#" + slugify_heading(R["updates_title"] if zh else "Recent Updates")),
              (labels[2], LICENSE_ID, "license", "LICENSE")]
    intro = R["intro"] if zh else ("Papers and annotated deep dives on Semantic ID generative recommendation, "
                                   "indexed by research problem and pipeline stage.")
    toc = R["toc"] if zh else (
        "[Problem × Stage Matrix](#problem--stage-matrix) · [What Each Paper Changes](#what-each-paper-changes) · "
        "[Papers by Modality](#papers-by-modality) · [Papers by Domain](#papers-by-domain) · "
        "[All Papers](#all-papers) · [Contributing](#contributing)"
    )
    return ['<div align="center">', "",
            "# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)", "",
            intro, "",
            " ".join(f"[![{l}]({shield(l, v, BADGE_COLORS[k])})]({href})" for l, v, k, href in badges), "",
            "[English](README.md) | 中文" if zh else "English | [中文](README.zh.md)", "",
            toc, "",
            "</div>", "", *stage_overview(papers, zh)]


def build_readme(vocab: dict, papers: list, by_id: dict, levels: dict, updates: list, fig_meta: dict, zh: bool = False) -> str:
    R = ZH_LABELS["readme"]
    lang = "zh" if zh else "en"
    figs = fig_meta[lang]
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    psb = next(p for p in vocab["problem"] if p["value"] == "psb")
    ordered = by_year(papers)
    cell = {(p["value"], s): [r for r in ordered if (r["problem"], r["stage"]) == (p["value"], s)] for p in problems for s in STAGES}
    psb_list = [r for r in ordered if r["problem"] == "psb"]
    pname = lambda p: ZH_LABELS["problems"][p["value"]].split(". ", 1)[1] if zh else p["name"]
    pdesc = lambda p: p.get("description_zh") if zh else p["description"]
    table = [f"| {R['problem'] if zh else 'Problem'} | {' | '.join(STAGES)} | {R['total'] if zh else 'Total'} |",
             "| :-- |" + " :-: |" * (len(STAGES) + 1)]
    for p in problems:
        counts = [len(cell[(p["value"], s)]) for s in STAGES]
        anchors = [slugify_heading(f"{p['value']} × {s}") for s in STAGES]
        table.append(f"| **{p['value']}.** {pname(p)} | " + " | ".join(map(heat, counts, anchors)) + f" | **{sum(counts)}** |")
    totals = [sum(len(cell[(p["value"], s)]) for p in problems) for s in STAGES]
    table.append(f"| **{R['total'] if zh else 'Total'}** | " + " | ".join(f"**{t}**" for t in totals) + f" | **{sum(totals)}** |")
    starters = [r for r in ordered if levels[r["id"]] == 3]
    tl = lambda r: ((r.get("tldr_zh") if zh else r.get("tldr")) or "").strip()
    two = lambda head, rows: align([f"| {' | '.join(head)} |", "|" + " :-- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]])
    n, m, k = len(papers), sum(totals), len(psb_list)
    q_svg = "assets/figures/papers-by-quarter.zh.svg" if zh else "assets/figures/papers-by-quarter.svg"
    mod_svg = "assets/figures/modality-by-year.zh.svg" if zh else "assets/figures/modality-by-year.svg"
    if zh:
        top = [
            f"## {R['scope_title']}", "",
            R["scope"].format(n=n, m=m, k=k), "",
            *render_figure_block(figs["quarter"], q_svg, zh=True), "",
            f"## {R['start_title']}", "",
            R["start_note"], "",
            *two(R["start_head"], R["start"]), "",
            f"## {R['starter_title']}", "",
            R["starter_note"], "",
        ]
    else:
        top = [
            "## Scope", "",
            f"This repository indexes {n} papers on Semantic ID (SID) generative recommendation—where each item is represented as a short tuple "
            f"of discrete codes so a sequence model can generate the next item token by token ({m} method papers in the matrix below, plus {k} "
            f"on {psb['name'].lower()}; [POI / local-life index](pages/index/poi.md)). The chart below tracks quarterly paper volume by first arXiv posting date.", "",
            *render_figure_block(figs["quarter"], q_svg, zh=False), "",
            "## Where to Start", "",
            "Pick an entry point below based on what you want to look up:", "",
            *two(("I want to...", "Where to go"), [
                ("Understand how Semantic IDs work and which papers to read first", "[Start Here](guides/start-here.md)"),
                ("Find methods for a specific research problem (e.g., collisions, alignment, efficiency)", "[Problem × Stage Matrix](#problem--stage-matrix)"),
                ("See which pipeline stages a paper modifies", "[What Each Paper Changes](#what-each-paper-changes)"),
                ("Compare methods side by side within one pipeline stage", "[Papers by Stage](pages/index/stages.md)"),
                ("Find papers that tokenize multimodal content or collaborative filtering (CF) signals", "[Papers by Modality](pages/index/modality.md)"),
                ("Find papers in a specific domain (e.g., e-commerce, POI, short video)", "[Papers by Domain](pages/index/domain.md)"),
                ("Find papers with open-source code", "[Papers with Code](pages/index/code.md)"),
                ("Feed this repository to an LLM or search tool", "[llms.txt](llms.txt)"),
            ]), "",
            "## Starter Papers", "",
            "Read these three papers first for the standard five-stage pipeline, industrial local-life extension, and parallel long-ID generation:", "",
        ]
    uchange = lambda u: (u.get("change_zh") or u["change"]).strip() if zh else u["change"].strip()
    mod_path = "pages/zh/index/modality.md" if zh else "pages/index/modality.md"
    dom_path = "pages/zh/index/domain.md" if zh else "pages/index/domain.md"
    matrix_note = R["matrix_note"] if zh else (
        "Rows are the six research problems and columns are the five pipeline stages each paper primarily modifies; "
        "click any count badge to jump to that paper list."
    )
    legend_note = R["legend_note"] if zh else (
        "Common symbols and abbreviations used across tables and paper cards (full definitions in the [glossary](guides/glossary.md)):"
    )
    mod_fig_note = R["modality_fig_note"] if zh else (
        "The chart below shows the yearly share of papers whose SID tokenizer uses item text only (`Text`), "
        "multimodal content (`Multimodal`), or collaborative filtering signals from user–item interactions (`With CF`)."
    )
    mod_note = R["modality_note"] if zh else (
        "Each row below groups papers by one aspect of tokenizer input signals (content per branch, collaborative and context across branches; multi-label):"
    )
    dom_note = R["domain_note"] if zh else (
        "Each row groups evaluation domains into one business category, ordered by paper count within each category (multi-domain papers appear in each matching domain):"
    )
    updates_note = R["updates_note"] if zh else "Recent additions and Table 1 synchronization logs in reverse chronological order:"
    all_note = R["all_note"] if zh else (
        "Full paper list organized by research problem and primary modified stage (each entry includes a one-sentence summary and paper/code links):"
    )
    back_top = R["back_to_top"] if zh else "[↑ Back to top](#awesome-semantic-id-generative-recommendation)"
    lines = [
        "<!--lint disable awesome-github table-pipe-alignment double-link-->",
        *readme_head(papers, updates, zh), "",
        *top,
        *two(R["starter_head"] if zh else ("Paper", "Core mechanism", "Venue"),
             [(ref(r), tl(r).replace("|", "\\|"), r["venue"]) for r in starters]), "",
        f"## {R['matrix_title'] if zh else 'Problem × Stage Matrix'}", "",
        matrix_note, "",
        *align(table), "",
        legend_note, "",
        *align([f"| {' | '.join(R['legend_head'] if zh else ('Mark', 'Meaning'))} |", "| :-- | :-- |",
                *[f"| {mk} | {t} |" for mk, t in (ZH_LABELS["legend"] if zh else LEGEND)]]), "",
        *build_changes_section(vocab, cell, psb_list, figs["cochanges"], zh=zh),
        back_top, "",
        f"## {R['modality_title'] if zh else 'Papers by Modality'}", "",
        mod_fig_note, "",
        *render_figure_block(figs["modality"], mod_svg, zh=zh), "",
        mod_note, "",
        *build_modality_nav(papers, vocab, mod_path, zh=zh), "",
        f"## {R['domain_title'] if zh else 'Papers by Domain'}", "",
        dom_note, "",
        *build_domain_nav(papers, vocab, dom_path, zh=zh), "",
        f"## {R['updates_title'] if zh else 'Recent Updates'}", "",
        updates_note, "",
        *[f"- {u['date']}: {uchange(u)}" + ((f"{R['papers']}{'、'.join(ref(by_id[x]) for x in u['papers'])}。" if zh else
                                             f" Papers: {', '.join(ref(by_id[x]) for x in u['papers'])}.") if u["papers"] else "")
          for u in sorted(updates, key=lambda u: u["date"], reverse=True)], "",
        f"## {R['all_title'] if zh else 'All Papers'}", "",
        all_note, "",
        *[f"- [{band(p, zh)}][]" for p in [psb, *problems]], "",
        f"## {band(psb, zh)}", "", f"> {pdesc(psb)}", "", *(format_item(r, zh) for r in psb_list), "",
        back_top, "",
    ]
    for p in problems:
        lines += [f"## {band(p, zh)}", "", f"> {pdesc(p)}", ""]
        for s in STAGES:
            prim = cell[(p["value"], s)]
            if prim:
                lines += [f"### {p['value']} × {s}", "", *(format_item(r, zh) for r in prim), ""]
        lines += [back_top, ""]
    page_dir = "pages/zh/papers" if zh else "pages/papers"
    lines += [
        f"## {R['contrib_title'] if zh else 'Contributing'}", "",
        R["contrib"] if zh else "Add or update `data/papers/<id>.yaml` and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).", "",
        *[f"[{band(p, zh).lower()}]: #{slugify_heading(band(p, zh))}" for p in [psb, *problems]],
        *[f"[{r['id']}]: {page_dir}/{r['id']}.md" for r in sorted(papers, key=lambda x: x["id"])], "",
    ]
    return "\n".join(lines)


def build_indexes(vocab: dict, papers: list, fig_meta: dict, zh: bool = False) -> dict:
    X = ZH_LABELS["index"]
    R = ZH_LABELS["readme"]
    lang = "zh" if zh else "en"
    figs = fig_meta[lang]
    up = "../../../" if zh else "../../"
    probs = {e["value"]: e for e in vocab["problem"]}
    dom_zh = domain_zh_map(vocab)
    ordered = by_year(papers)
    link = lambda r: f"[{r['name']}](../papers/{r['id']}.md)"
    table = lambda head, rows: [f"| {' | '.join(head)} |", "|" + " :-- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]]
    readme = f"{up}README.zh.md" if zh else f"{up}README.md"
    psb_anchor = slugify_heading(band(probs["psb"], zh))
    head = X["head"] if zh else ("Paper", "Venue", "Problem")
    cell_h = X["cell"] if zh else "Problem × Stage"
    compare = " · ".join(f"[{t}]({up}comparisons/{f}.md)" for f, t, *_ in COMPARISONS)
    switch = lambda f: f"[English](../../index/{f}) | 中文" if zh else f"English | [中文](../zh/index/{f})"

    stages = [
        f"# {X['stages_title'] if zh else 'Papers by Stage'}", "", switch("stages.md"), "",
        X["stages_intro"].format(readme=readme, anchor=psb_anchor) if zh else
        "Each table groups papers by the pipeline stage they primarily modify, alongside that stage's Table 1 value. "
        f"Papers under {probs['psb']['name'].lower()} span multiple stages or provide benchmarks; see the [README]({readme}#{psb_anchor}).", "",
        (X["compare"] if zh else "Side-by-side comparison tables: ") + compare, "",
    ]
    for s in STAGES:
        s_head = f"{ZH_LABELS['stages_zh'][s]}（{s}）" if zh else s
        rows = [[link(r), r["venue"], band(probs[r["problem"]], zh),
                 f"`{r['tokenizer']} / {r['objective']}`" if s == "Training" else f"`{r[s.lower()]}`"]
                for r in ordered if r["stage"] == s]
        stages += [f"## {s_head}", "", *table([*head, s_head], rows), ""]

    coded = [r for r in ordered if code_links(r)]
    code = [
        f"# {X['code_title'] if zh else 'Papers with Code'}", "", switch("code.md"), "",
        X["code_intro"].format(n=len(coded)) if zh else
        f"{len(coded)} papers link to public code. `Code` marks an official author repository; `Code (third-party)` marks a community implementation.", "",
        *table([head[0], head[1], cell_h, X["code"] if zh else "Code"],
               [[link(r), r["venue"], cell_label(r, probs, zh), " · ".join(f"[{l}]({u})" for l, u in code_links(r, zh))]
                for r in coded]), "",
    ]

    poi = [r for r in ordered if r.get("poi")]
    poi_page = [
        f"# {X['poi_title'] if zh else 'POI and Local-Life Papers'}", "", switch("poi.md"), "",
        X["poi_intro"].format(n=len(poi)) if zh else
        f"{len(poi)} papers target POI, local-life, or spatial recommendation. Bold marks the stage each paper primarily modifies.", "",
        *table([head[0], head[1], cell_h, X["pipeline"] if zh else "Pipeline"],
               [[link(r), r["venue"], cell_label(r, probs, zh), pipeline(r)] for r in poi]), "",
    ]

    new_table = lambda head, rows: [f"| {' | '.join(head)} |", "|" + " :--- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]]
    grouped_mod = group_papers_by_modality(papers, vocab)
    mod_back_anchor = slugify_heading(R["modality_title"] if zh else "Papers by Modality")
    sid_col = X["sid_inputs_col"] if zh else "SID Inputs"
    dom_col = X["domain_col"] if zh else "Domain"
    mod_cols = [head[0], head[1], cell_h, sid_col, dom_col]
    mod_page = [
        f"# {X['modality_title'] if zh else 'Papers by Modality'}", "",
        f"[← README]({readme}#{mod_back_anchor}) · {switch('modality.md')}", "",
        X["modality_intro"] if zh else (
            "Papers grouped by the signals fed into the SID tokenizer (rules defined in `data/vocab.yaml`). "
            "Content groups are evaluated per branch, collaborative and context groups across all branches combined; "
            "a paper appears in every matching group with its full branch values and application domains."
        ), "",
        *build_modality_nav(papers, vocab, "", zh=zh), "",
    ]
    for g in vocab["modality_groups"]:
        sec_title = g["name_zh"] if zh else g["name"]
        sec_desc = g["description_zh"] if zh else g["description"]
        members = grouped_mod[g["value"]]
        cnt = len(members)
        cnt_txt = f"共 {cnt} 篇。" if zh else f"{cnt} paper{'s' if cnt != 1 else ''}. "
        mod_page += [f"## {sec_title}", "", f"> {cnt_txt}{sec_desc}", ""]
        if members:
            rows = [
                [link(r), r["venue"], cell_label(r, probs, zh), format_modality(r), format_domain(r, dom_zh, zh=zh)]
                for r in members
            ]
            mod_page += [*new_table(mod_cols, rows), ""]
        else:
            mod_page += [X["empty_group"] if zh else "No papers currently fall in this group.", ""]

    dom_buckets = ordered_domains(papers, vocab)
    dom_back_anchor = slugify_heading(R["domain_title"] if zh else "Papers by Domain")
    dom_cols = [head[0], head[1], cell_h, dom_col, sid_col]
    dom_svg = f"{up}assets/figures/domain-distribution.zh.svg" if zh else f"{up}assets/figures/domain-distribution.svg"
    dom_page = [
        f"# {X['domain_title'] if zh else 'Papers by Domain'}", "",
        f"[← README]({readme}#{dom_back_anchor}) · {switch('domain.md')}", "",
        X["domain_intro"] if zh else (
            "Papers grouped by the business domain of their evaluation datasets (multi-domain papers appear in each matching section). "
            "The dot plot below ranks all 19 domains by paper count:"
        ), "",
        *render_figure_block(figs["domain"], dom_svg, zh=zh), "",
        X["domain_nav_note"] if zh else "Click any domain below to jump to its paper table:", "",
        *build_domain_nav(papers, vocab, "", zh=zh), "",
    ]
    for entry, members in dom_buckets:
        sec_title = entry["name_zh"] if zh else entry["value"]
        sec_desc = entry["description_zh"] if zh else entry["description"]
        cnt = len(members)
        cnt_txt = f"共 {cnt} 篇。" if zh else f"{cnt} paper{'s' if cnt != 1 else ''}. "
        dom_page += [f"## {sec_title}", "", f"> {cnt_txt}{sec_desc}", ""]
        if members:
            rows = [
                [link(r), r["venue"], cell_label(r, probs, zh), format_domain(r, dom_zh, zh=zh), format_modality(r)]
                for r in members
            ]
            dom_page += [*new_table(dom_cols, rows), ""]
        else:
            dom_page += [X["empty_group"] if zh else "No papers currently fall in this group.", ""]

    return {
        "stages.md": "\n".join(stages),
        "code.md": "\n".join(code),
        "poi.md": "\n".join(poi_page),
        "modality.md": "\n".join(mod_page),
        "domain.md": "\n".join(dom_page),
    }


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
    lines = [
        f"# {G['title'] if zh else 'Glossary'}", "",
        "[English](glossary.md) | 中文" if zh else "English | [中文](glossary.zh.md)", "",
        G["intro"] if zh else "This page is generated from [`data/vocab.yaml`](../data/vocab.yaml). "
        "It defines the controlled vocabulary values used in Table 1, the paper pages, and the indexes.", "",
        f"## {G['symbols'] if zh else 'Symbols'}", "", *[f"- {m}{colon}{t}" for m, t in (ZH_LABELS["legend"] if zh else LEGEND)[:5]], "",
        f"## {G['problems'] if zh else 'Problems'}", "",
        *[entry(p["value"], f"**{pname(p)}** {pdesc(p)}") for p in vocab["problem"]], "",
    ]
    for c, s in zip(TECH_COLS, COL_STAGES):
        head = ZH_LABELS["cols_zh"][c] if zh else (c.capitalize() + ("" if s == c.capitalize() else f" ({s})"))
        lines += [f"## {head}", "", *[entry(e["value"], e.get(desc_key) or e.get("description")) for e in vocab[c]], ""]
    extra_sections = [
        ("modality", G["modality"] if zh else "SID Input Modalities"),
        ("domain", G["domain"] if zh else "Domains"),
        ("settings", G["settings"] if zh else "Evaluation Settings"),
    ]
    for sec_key, sec_head in extra_sections:
        lines += [
            f"## {sec_head}", "",
            *[
                entry(
                    f"{e['name_zh']} / {e['value']}" if zh and e.get("name_zh") else e["value"],
                    e.get(desc_key) or e.get("description"),
                )
                for e in vocab[sec_key]
            ],
            "",
        ]
    return "\n".join(lines)


def llm_fields(rec: dict, probs: dict, dom_zh: dict, set_zh: dict) -> list:
    f = [
        f"Problem: {band(probs[rec['problem']])}",
        f"Stage: {stage_label(rec)}",
        f"Changes: {format_changes_inline(rec, zh=False, sep='; ', empty='none')}",
        f"SID inputs: {format_modality(rec, code_wrap=False)}",
        f"Domain: {format_domain(rec, dom_zh, zh=False, code_wrap=False)}",
        f"Settings: {format_settings(rec, set_zh, zh=False, code_wrap=False, empty='none')}",
        "; ".join(f"{c.capitalize()}: {rec[c]}" for c in TECH_COLS),
    ]
    f += [f"TL;DR: {rec['tldr'].strip()}"] if rec.get("tldr") else []
    f += [f"[{l}]({u})" for l, u in code_links(rec)]
    return f + [f"Setup card: {'yes' if rec.get('setup') else 'no'}", f"Relations: {len(rec.get('related', []))}"]


WHERE_TOKEN_RE = re.compile(
    r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+"
    r"|(?:arXiv:)?\b\d{4}\.\d{4,5}(?:v\d+)?\b"
    r"|#[A-Za-z0-9][A-Za-z0-9._-]*"
)


def extract_en_where(s: str) -> str:
    """Extract only URLs, arXiv version IDs, and section anchors from where; fall back to 'see paper'."""
    seen = []
    for m in WHERE_TOKEN_RE.finditer(s or ""):
        tok = m.group(0).rstrip(".,;:)")
        if tok and tok not in seen:
            seen.append(tok)
    return ", ".join(seen) if seen else "see paper"


def build_llms(vocab: dict, papers: list, notes: dict) -> tuple:
    probs = {e["value"]: e for e in vocab["problem"]}
    dom_zh = domain_zh_map(vocab)
    set_zh = settings_zh_map(vocab)
    ordered = sorted(papers, key=lambda x: x["id"])
    head = [
        "# Awesome Semantic ID Generative Recommendation", "",
        f"> {len(papers)} papers on generative recommendation with Semantic IDs (SIDs), organized by research problem "
        "and primary modified pipeline stage.", "",
        "## Core Files", "",
        "- [README.md](README.md): Problem × Stage matrix, per-paper stage changes tables, modality and domain entry points, and the full list of papers.",
        "- [guides/glossary.md](guides/glossary.md): Definitions of every problem, Table 1 value, modality, domain, and evaluation setting.",
        "- [pages/index/stages.md](pages/index/stages.md): Papers grouped by the stage they mainly change.",
        "- [pages/index/modality.md](pages/index/modality.md): Papers grouped by SID tokenizer input modality.",
        "- [pages/index/domain.md](pages/index/domain.md): Papers grouped by application domain.",
        "- [pages/index/code.md](pages/index/code.md): Papers that link to code.",
        "- [pages/index/poi.md](pages/index/poi.md): Papers on POI and local-life recommendation.",
        "- [data/vocab.yaml](data/vocab.yaml): Controlled vocabulary and modality grouping rules.",
        "- [schema/paper.schema.json](schema/paper.schema.json): JSON Schema for `data/papers/<id>.yaml`.", "",
    ]
    short = head + [f"## Papers ({len(papers)} records)", ""] + [
        f"- [{r['name']}](pages/papers/{r['id']}.md) · {r['venue']} · " + " · ".join(llm_fields(r, probs, dom_zh, set_zh))
        for r in ordered
    ]
    full = list(head)
    for r in ordered:
        full += [
            f"## {r['name']}", "",
            f"- Page: pages/papers/{r['id']}.md",
            f"- Venue: {r['venue']}",
            *[f"- {x}" for x in llm_fields(r, probs, dom_zh, set_zh)],
            "",
        ]
        other_changes = [
            (COL_HEADERS_EN[c], r[c], r["changes"][c])
            for c in TECH_COLS
            if change_kind(r["changes"][c]) == "other"
        ]
        if other_changes:
            full += [
                "### Other stage changes", "",
                *[f"- {col_name} ({col_val}): \"{info['quote']}\" ({extract_en_where(info['where'])})"
                  for col_name, col_val, info in other_changes],
                "",
            ]
        if r.get("settings"):
            full += [
                "### Special settings", "",
                *[
                    f"- {s['value'] + (' (' + s['scope'] + ')' if 'scope' in s else '')}: \"{s['quote']}\" ({extract_en_where(s['where'])})"
                    for s in r["settings"]
                ],
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
    svg_files, fig_meta = build_figures(vocab, papers)
    fig_dir = root / "assets/figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    for existing in fig_dir.glob("*.svg"):
        existing.unlink()
    for name, text in svg_files.items():
        (fig_dir / name).write_text(text, encoding="utf-8")
    outputs = {
        "pages/papers": {f"{r['id']}.md": build_paper_page(r, vocab, by_id, notes.get(r["id"]), root) for r in papers},
        "pages/zh/papers": {f"{r['id']}.md": build_paper_page(r, vocab, by_id, notes_zh.get(r["id"]), root, zh=True) for r in papers},
        "pages/index": build_indexes(vocab, papers, fig_meta),
        "pages/zh/index": build_indexes(vocab, papers, fig_meta, zh=True),
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
        "README.md": build_readme(vocab, papers, by_id, levels, updates, fig_meta),
        "README.zh.md": build_readme(vocab, papers, by_id, levels, updates, fig_meta, zh=True),
        "guides/glossary.md": build_glossary(vocab),
        "guides/glossary.zh.md": build_glossary(vocab, zh=True),
    }
    singles["llms.txt"], singles["llms-full.txt"] = build_llms(vocab, papers, notes)
    for name, text in singles.items():
        (root / name).write_text(text, encoding="utf-8")
    print(f"Built README.md, README.zh.md, {len(svg_files)} SVG figures, {len(papers)} paper pages in English and Chinese, "
          "5 index pages in English and Chinese, 3 comparison tables, guides/glossary.md, guides/glossary.zh.md, llms.txt, and llms-full.txt.")


if __name__ == "__main__":
    main()
