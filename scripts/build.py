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

import taxonomy_figure

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
        "Scenario": "应用场景",
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
        "toc": "[分类总图](#分类总图) · [应用场景](#应用场景) · [阅读导航](#阅读导航) · [全部论文](#全部论文) · [参与贡献](#参与贡献)",
        "scope_title": "收录范围",
        "scope": "本仓库收录 {n} 篇语义 ID（Semantic ID，SID）生成式推荐论文。这类方法用编号器将每个物品映射为离散 token，再由生成器逐位解码下一物品的 SID。"
                 "全库按研究问题与主要改动的流程阶段组织 {m} 篇方法论文，另收 {k} 篇范式、系统与基准论文。",
        "taxonomy_title": "分类总图",
        "taxonomy_note": "图中按研究问题（行）与主要改动的流程阶段（列）分格，每格给出该格论文总数并列出最多 5 篇论文（已发表优先于 arXiv，按年份从早到晚），篇名后的五个圆点按五阶段顺序标出该文改动的阶段。",
        "count": "{n} 篇",
        "start_title": "阅读导航",
        "start_note": "按你的查找目的，从下表选择对应入口：",
        "start_head": ("我想……", "去哪里看"),
        "start": [
            ("刚接触 Semantic ID，了解基本流程并从代表作读起", "[入门指南](guides/start-here.zh.md)"),
            ("找解决某类问题的方法（如码字冲突、表征对齐、推理效率）", "[全部论文](#全部论文)"),
            ("在同一个流程阶段内横向对比不同方法", "[按阶段索引](pages/zh/index/stages.md)"),
            ("找用多模态内容或协同过滤（CF）信号构码的论文", "[按模态找论文](pages/zh/index/modality.md)"),
            ("找某个业务领域的论文（如电商、本地生活 POI、短视频）", "[按领域找论文](pages/zh/index/domain.md)"),
            ("按应用场景找论文（如查询检索、POI、排序、线上部署）", "[按场景找论文](pages/zh/index/scenario.md)"),
            ("找公开了开源代码的论文", "[有代码的论文](pages/zh/index/code.md)"),
            ("让大模型或检索工具直接读取这个仓库", "[llms.txt](llms.txt)（英文）"),
        ],
        "starter_title": "代表性必读论文",
        "starter_note": "初读建议先看下表三篇代表作，分别对应标准五阶段流程、工业界本地生活扩展与长 ID 并行生成：",
        "starter_head": ("论文", "核心机制", "发表"),
        "modality_title": "按模态找论文",
        "modality_head": ("方面", "分组"),
        "domain_title": "按领域找论文",
        "domain_head": ("类别", "领域"),
        "scenario_section": "应用场景",
        "scenario_note": "下表按任务形态和部署条件统计论文数（一篇可有多种任务形态），点击合计可跳到分组列表：",
        "scenario_total": "合计",
        "scenario_task_head": "任务形态",
        "settings_line": "特殊评测设置：",
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
        "domain_intro": "本页按实验数据集所属的业务领域分组列出论文；涉及多个领域的论文同时列入各对应小节。",
        "domain_nav_note": "点击下表中的领域名称可直接跳到对应小节：",
        "sid_inputs_col": "构码输入",
        "domain_col": "领域",
        "empty_group": "当前暂无论文归入本组。",
        "scenario_title": "按场景找论文",
        "scenario_intro": "本页按应用场景分组列出论文：任务形态可多选，部署条件取论文达到的最高一级，特殊评测设置另列。一篇论文可进入多个分组。",
        "task_col": "任务形态",
        "deploy_col": "部署条件",
        "settings_col": "特殊设置",
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


def with_detail(label: str, detail: str, zh: bool = False) -> str:
    """'Other' values carry what the paper actually states: `Other` (detail) / `其他`（detail）."""
    detail = detail.replace("|", "\\|")
    return f"{label}（{detail}）" if zh else f"{label} ({detail})"


def format_modality(rec: dict, code_wrap: bool = True, zh: bool = False) -> str:
    w = (lambda s: f"`{s}`") if code_wrap else str
    m = rec["modality"]
    details = {item.get("branch"): item["zh" if zh else "en"] for item in rec.get("modality_other") or []}
    tok = lambda x, br: with_detail(w("其他" if zh else "Other"), details.get(br, ""), zh) if x == "Other" else w(x)
    if isinstance(m, dict):
        sep = " · " if code_wrap else "; "
        return sep.join(f"{br}: " + (" + ".join(tok(x, br) for x in vals) if vals else "–") for br, vals in m.items())
    return " + ".join(tok(x, None) for x in m)


def domain_zh_map(vocab: dict) -> dict:
    return {e["value"]: e["name_zh"] for e in vocab["domain"]}


def settings_zh_map(vocab: dict) -> dict:
    return {e["value"]: e["name_zh"] for e in vocab["settings"]}


def format_domain(rec: dict, dom_zh: dict, zh: bool = False, code_wrap: bool = True) -> str:
    w = (lambda s: f"`{s}`") if code_wrap else str
    sep = " · " if code_wrap else ", "
    other = (rec.get("domain_other") or {}).get("zh" if zh else "en", "")
    return sep.join(with_detail(w(dom_zh[d] if zh else d), other, zh) if d == "Other" else w(dom_zh[d] if zh else d)
                    for d in rec["domain"])


def vocab_name(vocab: dict, sec: str, value: str, zh: bool = False) -> str:
    e = next(x for x in vocab[sec] if x["value"] == value)
    return e["name_zh"] if zh else e.get("name", value)


def format_scenario(rec: dict, vocab: dict, zh: bool = False, code_wrap: bool = True) -> str:
    w = (lambda s: f"`{s}`") if code_wrap else str
    sc = rec["scenario"]
    tasks = (" · " if code_wrap else ", ").join(w(vocab_name(vocab, "scenario_task", t["value"], zh)) for t in sc["tasks"])
    return f"{tasks}；{w(vocab_name(vocab, 'deploy', sc['deploy'], zh))}" if zh else f"{tasks}; {w(vocab_name(vocab, 'deploy', sc['deploy']))}"


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
    """Return [(domain_entry, papers_in_domain), ...] ordered by descending paper count, keeping Other last."""
    ordered = by_year(papers)
    buckets = []
    for idx, entry in enumerate(vocab["domain"]):
        val = entry["value"]
        members = [r for r in ordered if val in r["domain"]]
        is_unk = val == "Other"
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


def build_figures(vocab: dict, papers: list) -> tuple[dict, dict]:
    """Return ({svg file name: text}, {lang: {figure key: alt text}}) for the taxonomy figure in English and Chinese."""
    names = {p["value"]: band(p) for p in vocab["problem"]}
    names_zh = {p["value"]: band(p, zh=True) for p in vocab["problem"]}
    svg_en, alt_en = taxonomy_figure.build(vocab, papers, {s: s for s in STAGES}, names)
    svg_zh, alt_zh = taxonomy_figure.build(vocab, papers, ZH_LABELS["stages_zh"], names_zh, zh=True)
    return {"taxonomy.svg": svg_en, "taxonomy.zh.svg": svg_zh}, {"en": {"taxonomy": alt_en}, "zh": {"taxonomy": alt_zh}}


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
        ("SID inputs", format_modality(rec, code_wrap=True, zh=zh)),
        ("Domain", format_domain(rec, dom_zh, zh=zh, code_wrap=True)),
        *([("Settings", settings_str)] if settings_str else []),
        ("Scenario", format_scenario(rec, vocab, zh=zh)),
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


def readme_head(papers: list, updates: list, zh: bool = False) -> list:
    """Centered title, one-line description, light badges, language switch, and TOC line."""
    R = ZH_LABELS["readme"]
    labels = R["badges"] if zh else ("papers", "updated", "license")
    latest = max((u["date"] for u in updates), default="")
    badges = [(labels[0], len(papers), "papers", "#" + slugify_heading(R["all_title"] if zh else "All Papers")),
              (labels[1], latest, "updated", "#" + slugify_heading(R["updates_title"] if zh else "Recent Updates")),
              (labels[2], LICENSE_ID, "license", "LICENSE")]
    intro = R["intro"] if zh else ("Papers and annotated deep dives on Semantic ID generative recommendation, "
                                   "indexed by research problem and pipeline stage.")
    toc = R["toc"] if zh else (
        "[Taxonomy](#taxonomy) · [Scenarios](#scenarios) · [Where to Start](#where-to-start) · [All Papers](#all-papers) · [Contributing](#contributing)"
    )
    return ['<div align="center">', "",
            "# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)", "",
            intro, "",
            " ".join(f"[![{l}]({shield(l, v, BADGE_COLORS[k])})]({href})" for l, v, k, href in badges), "",
            "[English](README.md) | 中文" if zh else "English | [中文](README.zh.md)", "",
            toc, "",
            "</div>"]


def scenario_section(vocab: dict, papers: list, zh: bool = False) -> list:
    """README: task form x deployment counts; totals link to the scenario index page."""
    R = ZH_LABELS["readme"]
    page = "pages/zh/index/scenario.md" if zh else "pages/index/scenario.md"
    deps = [e["value"] for e in vocab["deploy"]]
    head = [R["scenario_task_head"] if zh else "Task form", *(vocab_name(vocab, "deploy", d, zh) for d in deps), R["scenario_total"] if zh else "Total"]
    rows = []
    for t in vocab["scenario_task"]:
        members = [r for r in papers if any(x["value"] == t["value"] for x in r["scenario"]["tasks"])]
        if not members:
            continue
        name = vocab_name(vocab, "scenario_task", t["value"], zh)
        counts = [str(sum(r["scenario"]["deploy"] == d for r in members)) for d in deps]
        rows.append([name, *counts, f"[{len(members)}]({page}#{slugify_heading(name)})"])
    set_zh = settings_zh_map(vocab)
    sets = []
    for e in vocab["settings"]:
        n = sum(any(s["value"] == e["value"] for s in r.get("settings") or []) for r in papers)
        label = set_zh[e["value"]] if zh else e["value"]
        sets.append(f"[{label}（{n}）]({page}#{slugify_heading(label)})" if zh else f"[{label} ({n})]({page}#{slugify_heading(label)})")
    note = R["scenario_note"] if zh else (
        "Papers by task form and deployment level (a paper can have several task forms); click a total to open its list:")
    return [f"## {R['scenario_section'] if zh else 'Scenarios'}", "", note, "",
            *align([f"| {' | '.join(head)} |", "| :-- |" + " :-: |" * (len(head) - 1), *[f"| {' | '.join(r)} |" for r in rows]]), "",
            (R["settings_line"] if zh else "Evaluation settings: ") + " · ".join(sets), ""]


def build_scenario_page(vocab: dict, papers: list, probs: dict, zh: bool = False) -> str:
    X = ZH_LABELS["index"]
    up = "../../../" if zh else "../../"
    readme = f"{up}README.zh.md" if zh else f"{up}README.md"
    back = slugify_heading(ZH_LABELS["readme"]["scenario_section"] if zh else "Scenarios")
    switch = f"[English](../../index/scenario.md) | 中文" if zh else "English | [中文](../zh/index/scenario.md)"
    head = X["head"] if zh else ("Paper", "Venue", "Problem")
    cols = [head[0], head[1], X["cell"] if zh else "Problem × Stage", X["task_col"] if zh else "Task Form",
            X["deploy_col"] if zh else "Deployment"]
    link = lambda r: f"[{r['name']}](../papers/{r['id']}.md)"
    task_cell = lambda r: " · ".join(f"`{vocab_name(vocab, 'scenario_task', t['value'], zh)}`" for t in r["scenario"]["tasks"])
    dep_cell = lambda r: f"`{vocab_name(vocab, 'deploy', r['scenario']['deploy'], zh)}`"
    table = lambda rows: [f"| {' | '.join(cols)} |", "|" + " :--- |" * len(cols),
                          *[f"| {link(r)} | {r['venue']} | {cell_label(r, probs, zh)} | {task_cell(r)} | {dep_cell(r)} |" for r in rows]]
    ordered = by_year(papers)
    out = [f"# {X['scenario_title'] if zh else 'Papers by Scenario'}", "", f"[← README]({readme}#{back}) · {switch}", "",
           X["scenario_intro"] if zh else (
               "Papers grouped by application scenario: task forms can be several per paper, deployment is the highest level a paper "
               "reaches, and special evaluation settings are listed separately. A paper can appear in several groups."), ""]
    count = lambda n: f"共 {n} 篇。" if zh else f"{n} paper{'s' if n != 1 else ''}. "
    groups = [(vocab_name(vocab, "scenario_task", e["value"], zh), e, [r for r in ordered if any(t["value"] == e["value"] for t in r["scenario"]["tasks"])])
              for e in vocab["scenario_task"]]
    groups += [(vocab_name(vocab, "deploy", e["value"], zh), e, [r for r in ordered if r["scenario"]["deploy"] == e["value"]]) for e in vocab["deploy"]]
    set_zh = settings_zh_map(vocab)
    groups += [(set_zh[e["value"]] if zh else e["value"], e, [r for r in ordered if any(s["value"] == e["value"] for s in r.get("settings") or [])])
               for e in vocab["settings"]]
    for title, e, members in groups:
        out += [f"## {title}", "", f"> {count(len(members))}{e['description_zh'] if zh else e['description']}", ""]
        out += [*table(members), ""] if members else [X["empty_group"] if zh else "No papers currently fall in this group.", ""]
    return "\n".join(out)


def build_readme(vocab: dict, papers: list, by_id: dict, levels: dict, updates: list, fig_meta: dict, zh: bool = False) -> str:
    R = ZH_LABELS["readme"]
    lang = "zh" if zh else "en"
    problems = [p for p in vocab["problem"] if p["value"] != "psb"]
    psb = next(p for p in vocab["problem"] if p["value"] == "psb")
    ordered = by_year(papers)
    cell = {(p["value"], s): [r for r in ordered if (r["problem"], r["stage"]) == (p["value"], s)] for p in problems for s in STAGES}
    psb_list = [r for r in ordered if r["problem"] == "psb"]
    pdesc = lambda p: p.get("description_zh") if zh else p["description"]
    starters = [r for r in ordered if levels[r["id"]] == 3]
    tl = lambda r: ((r.get("tldr_zh") if zh else r.get("tldr")) or "").strip()
    two = lambda head, rows: align([f"| {' | '.join(head)} |", "|" + " :-- |" * len(head), *[f"| {' | '.join(r)} |" for r in rows]])
    n, k = len(papers), len(psb_list)
    m = n - k
    tax_svg = "assets/figures/taxonomy.zh.svg" if zh else "assets/figures/taxonomy.svg"
    tax_fig = [f"![{fig_meta[lang]['taxonomy']}]({tax_svg})"]
    count = lambda c: R["count"].format(n=c) if zh else (f"{c} papers" if c != 1 else "1 paper")
    if zh:
        top = [
            f"## {R['scope_title']}", "", R["scope"].format(n=n, m=m, k=k), "",
            f"## {R['taxonomy_title']}", "", R["taxonomy_note"], "", *tax_fig, "",
            *scenario_section(vocab, papers, zh=True),
            f"## {R['start_title']}", "", R["start_note"], "", *two(R["start_head"], R["start"]), "",
            f"## {R['starter_title']}", "", R["starter_note"], "",
        ]
    else:
        top = [
            "## Scope", "",
            f"This repository indexes {n} papers on Semantic ID (SID) generative recommendation. In these methods, a tokenizer maps each item "
            f"to discrete tokens and a generator decodes the next item's SID. The collection groups {m} method papers by research problem "
            f"and primary modified stage, plus {k} papers on {psb['name'].lower()}.", "",
            "## Taxonomy", "",
            "Each cell pairs a research problem (row) with a primary pipeline stage (column), showing the cell total and up to five papers "
            "(published before arXiv, earliest first); the five stage-ordered dots after each name mark the stages that paper modifies.", "",
            *tax_fig, "",
            *scenario_section(vocab, papers, zh=False),
            "## Where to Start", "",
            "Pick an entry point below based on what you want to look up:", "",
            *two(("I want to...", "Where to go"), [
                ("Understand how Semantic IDs work and which papers to read first", "[Start Here](guides/start-here.md)"),
                ("Find methods for a specific research problem (e.g., collisions, alignment, efficiency)", "[All Papers](#all-papers)"),
                ("Compare methods side by side within one pipeline stage", "[Papers by Stage](pages/index/stages.md)"),
                ("Find papers that tokenize multimodal content or collaborative filtering (CF) signals", "[Papers by Modality](pages/index/modality.md)"),
                ("Find papers in a specific domain (e.g., e-commerce, POI, short video)", "[Papers by Domain](pages/index/domain.md)"),
                ("Find papers by application scenario (e.g., query retrieval, POI, ranking, online deployment)", "[Papers by Scenario](pages/index/scenario.md)"),
                ("Find papers with open-source code", "[Papers with Code](pages/index/code.md)"),
                ("Feed this repository to an LLM or search tool", "[llms.txt](llms.txt)"),
            ]), "",
            "## Starter Papers", "",
            "Read these three papers first for the standard five-stage pipeline, industrial local-life extension, and parallel long-ID generation:", "",
        ]
    uchange = lambda u: (u.get("change_zh") or u["change"]).strip() if zh else u["change"].strip()
    updates_note = R["updates_note"] if zh else "Recent additions and Table 1 synchronization logs in reverse chronological order:"
    all_note = R["all_note"] if zh else (
        "Full paper list organized by research problem and primary modified stage (each entry includes a one-sentence summary and paper/code links):"
    )
    back_top = R["back_to_top"] if zh else "[↑ Back to top](#awesome-semantic-id-generative-recommendation)"
    folded = lambda c, body: ["<details>", f"<summary>{count(c)}</summary>", "", *body, "</details>", ""]
    lines = [
        "<!--lint disable awesome-github table-pipe-alignment double-link-->",
        *readme_head(papers, updates, zh), "",
        *top,
        *two(R["starter_head"] if zh else ("Paper", "Core mechanism", "Venue"),
             [(ref(r), tl(r).replace("|", "\\|"), r["venue"]) for r in starters]), "",
        f"## {R['updates_title'] if zh else 'Recent Updates'}", "",
        updates_note, "",
        *[f"- {u['date']}: {uchange(u)}" + ((f"{R['papers']}{'、'.join(ref(by_id[x]) for x in u['papers'])}。" if zh else
                                             f" Papers: {', '.join(ref(by_id[x]) for x in u['papers'])}.") if u["papers"] else "")
          for u in sorted(updates, key=lambda u: u["date"], reverse=True)], "",
        f"## {R['all_title'] if zh else 'All Papers'}", "",
        all_note, "",
        *[f"- [{band(p, zh)}][]" for p in [psb, *problems]], "",
        f"## {band(psb, zh)}", "", f"> {pdesc(psb)}", "",
        *folded(len(psb_list), [x for r in psb_list for x in (format_item(r, zh), "")]),
        back_top, "",
    ]
    for p in problems:
        body = []
        for s in STAGES:
            prim = cell[(p["value"], s)]
            if prim:
                body += [f"### {p['value']} × {s}", "", *(x for r in prim for x in (format_item(r, zh), ""))]
        lines += [f"## {band(p, zh)}", "", f"> {pdesc(p)}", "", *folded(sum(len(cell[(p["value"], s)]) for s in STAGES), body), back_top, ""]
    page_dir = "pages/zh/papers" if zh else "pages/papers"
    lines += [
        f"## {R['contrib_title'] if zh else 'Contributing'}", "",
        R["contrib"] if zh else "Add or update `data/papers/<id>.yaml` and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).", "",
        *[f"[{band(p, zh).lower()}]: #{slugify_heading(band(p, zh))}" for p in [psb, *problems]],
        *[f"[{r['id']}]: {page_dir}/{r['id']}.md" for r in sorted(papers, key=lambda x: x["id"])], "",
    ]
    return "\n".join(lines)


def build_indexes(vocab: dict, papers: list, zh: bool = False) -> dict:
    X = ZH_LABELS["index"]
    R = ZH_LABELS["readme"]
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
    back_anchor = slugify_heading(R["start_title"] if zh else "Where to Start")
    sid_col = X["sid_inputs_col"] if zh else "SID Inputs"
    dom_col = X["domain_col"] if zh else "Domain"
    mod_cols = [head[0], head[1], cell_h, sid_col, dom_col]
    mod_page = [
        f"# {X['modality_title'] if zh else 'Papers by Modality'}", "",
        f"[← README]({readme}#{back_anchor}) · {switch('modality.md')}", "",
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
                [link(r), r["venue"], cell_label(r, probs, zh), format_modality(r, zh=zh), format_domain(r, dom_zh, zh=zh)]
                for r in members
            ]
            mod_page += [*new_table(mod_cols, rows), ""]
        else:
            mod_page += [X["empty_group"] if zh else "No papers currently fall in this group.", ""]

    dom_buckets = ordered_domains(papers, vocab)
    dom_cols = [head[0], head[1], cell_h, dom_col, sid_col]
    dom_page = [
        f"# {X['domain_title'] if zh else 'Papers by Domain'}", "",
        f"[← README]({readme}#{back_anchor}) · {switch('domain.md')}", "",
        X["domain_intro"] if zh else (
            "Papers grouped by the business domain of their evaluation datasets (multi-domain papers appear in each matching section)."
        ), "",
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
                [link(r), r["venue"], cell_label(r, probs, zh), format_domain(r, dom_zh, zh=zh), format_modality(r, zh=zh)]
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
        "scenario.md": build_scenario_page(vocab, papers, probs, zh=zh),
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


def llm_fields(rec: dict, probs: dict, dom_zh: dict, set_zh: dict, vocab: dict) -> list:
    f = [
        f"Problem: {band(probs[rec['problem']])}",
        f"Stage: {stage_label(rec)}",
        f"Changes: {format_changes_inline(rec, zh=False, sep='; ', empty='none')}",
        f"SID inputs: {format_modality(rec, code_wrap=False)}",
        f"Domain: {format_domain(rec, dom_zh, zh=False, code_wrap=False)}",
        f"Settings: {format_settings(rec, set_zh, zh=False, code_wrap=False, empty='none')}",
        f"Scenario: {format_scenario(rec, vocab, zh=False, code_wrap=False)}",
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
        f"- [{r['name']}](pages/papers/{r['id']}.md) · {r['venue']} · " + " · ".join(llm_fields(r, probs, dom_zh, set_zh, vocab))
        for r in ordered
    ]
    full = list(head)
    for r in ordered:
        full += [
            f"## {r['name']}", "",
            f"- Page: pages/papers/{r['id']}.md",
            f"- Venue: {r['venue']}",
            *[f"- {x}" for x in llm_fields(r, probs, dom_zh, set_zh, vocab)],
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
        "README.md": build_readme(vocab, papers, by_id, levels, updates, fig_meta),
        "README.zh.md": build_readme(vocab, papers, by_id, levels, updates, fig_meta, zh=True),
        "guides/glossary.md": build_glossary(vocab),
        "guides/glossary.zh.md": build_glossary(vocab, zh=True),
    }
    singles["llms.txt"], singles["llms-full.txt"] = build_llms(vocab, papers, notes)
    for name, text in singles.items():
        (root / name).write_text(text, encoding="utf-8")
    print(f"Built README.md, README.zh.md, {len(svg_files)} SVG figures, {len(papers)} paper pages in English and Chinese, "
          "6 index pages in English and Chinese, 3 comparison tables, guides/glossary.md, guides/glossary.zh.md, llms.txt, and llms-full.txt.")


if __name__ == "__main__":
    main()
