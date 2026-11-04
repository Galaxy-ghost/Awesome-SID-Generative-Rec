"""Taxonomy figure: research problem (rows) x primary pipeline stage (columns), with representative papers.

Each cell lists up to CONFIG["max_per_cell"] papers: published papers first, then arXiv preprints, each group earliest first.
Five dots after each name mark the stages the paper changes, in pipeline order.
All layout and colour settings live in CONFIG; text width uses Arial-compatible glyph metrics.
"""
import html
import re

CONFIG = {
    "max_per_cell": 5,
    "margin": 20,
    "font_name": 12,
    "font_head": 13,
    "font_small": 10.5,
    "line_h": 18,
    "pad_x": 10,
    "pad_y": 8,
    "col_gap": 12,
    "row_gap": 10,
    "band_h": 21,  # problem name line above each row
    "name_max_w": 126,  # longer names wrap after a hyphen or space; the year stays with the last piece
    "wrap_indent": 8,
    "min_col_w": 132,
    "dot_r": 3.3,
    "dot_step": 8.6,
    "width_slack": 1.06,  # viewer fonts (SF, Segoe UI) run slightly wider than Arial
    "bg": "#fcfcfb",
    "text": "#1f2328",
    "muted": "#6e7781",
    "empty": "#e4e3df",
    "hollow": "#cfcdc7",
    "psb_fill": "#f6f6f4",
    "psb_stroke": "#d9d8d3",
    # Light five-stage palette after arc.pdf (green, peach, lavender, pink, blue): cell fill, border, dot.
    "stages": {
        "Representation": ("#eef9f0", "#b9e2c2", "#7fcf95"),
        "Tokenization": ("#fff6ea", "#f3d3a8", "#f0b46e"),
        "Backbone": ("#f6f0fd", "#d8c8f3", "#b49be6"),
        "Training": ("#fdf0f7", "#f1c6de", "#e597c3"),
        "Inference": ("#eef5fc", "#bfd8f2", "#84b3e6"),
    },
}

STAGES = list(CONFIG["stages"])
# Stage -> change keys in data/papers/<id>.yaml; Training covers tokenizer schedule and objective.
STAGE_KEYS = {"Representation": ("representation",), "Tokenization": ("tokenization",), "Backbone": ("backbone",),
              "Training": ("tokenizer", "objective"), "Inference": ("inference",)}

TEXT = {
    "en": {
        "count": "{n} papers",
        "count_one": "1 paper",
        "legend_dots": "changed stage",
        "legend_hollow": "unchanged",
        "legend_order": "Dots follow the stage order: Representation · Tokenization · Backbone · Training · Inference.",
        "legend_rule": "Each cell lists up to {k} papers: published first, then arXiv, earliest first. Full lists are below.",
        "title": "Taxonomy of {n} Semantic ID generative recommendation papers",
        "alt": ("Taxonomy of {n} Semantic ID generative recommendation papers: rows are six research problems plus "
                "paradigms, systems and benchmarks; columns are the five pipeline stages a paper mainly changes. "
                "Each cell lists up to {k} representative papers with year, and five dots after each name mark the stages the paper changes."),
    },
    "zh": {
        "count": "{n} 篇",
        "count_one": "1 篇",
        "legend_dots": "改动的阶段",
        "legend_hollow": "未改动",
        "legend_order": "圆点按阶段顺序排列：物品表示 · 构码 · 生成骨干 · 训练 · 推理。",
        "legend_rule": "每格最多列 {k} 篇：先列已发表的，再列 arXiv，按时间从早到晚。完整清单见下文。",
        "title": "{n} 篇 Semantic ID 生成式推荐论文的分类",
        "alt": ("{n} 篇 Semantic ID 生成式推荐论文的分类：行是六个研究问题和范式、系统与基准，列是论文主要改动的五个流程阶段。"
                "每格最多列 {k} 篇代表论文和年份，名字后的五个圆点标出该论文改动了哪些阶段。"),
    },
}

_REG = ("278 278 355 556 556 889 667 191 333 333 389 584 278 333 278 278 556 556 556 556 556 556 556 556 556 556 278 278 "
        "584 584 584 556 1015 667 667 722 722 667 611 778 722 278 500 667 556 833 722 778 667 778 722 667 611 722 667 944 "
        "667 667 611 278 278 278 469 556 333 556 556 500 556 556 278 556 556 222 222 500 222 833 556 556 556 556 333 500 "
        "278 556 500 722 500 500 500 334 260 334 584")
_BOLD = ("278 333 474 556 556 889 722 238 333 333 389 584 278 333 278 278 556 556 556 556 556 556 556 556 556 556 333 333 "
         "584 584 584 611 975 722 722 722 722 667 611 778 722 278 556 722 611 833 722 778 667 778 722 667 611 722 667 944 "
         "667 667 611 333 278 333 584 556 333 556 611 556 611 556 333 611 611 278 278 556 278 889 611 611 611 611 389 556 "
         "333 611 556 778 556 556 500 389 280 389 584")
_W = {False: [int(x) for x in _REG.split()], True: [int(x) for x in _BOLD.split()]}
ARXIV_YM = re.compile(r"(\d{2})(\d{2})\.\d+")


def text_w(s: str, size: float, bold: bool = False) -> float:
    """Approximate rendered width; non-ASCII glyphs (CJK, dashes) count as one em."""
    units = sum(_W[bold][ord(c) - 32] if 32 <= ord(c) < 127 else 1000 for c in str(s))
    return units * size / 1000 * CONFIG["width_slack"]


def wrap(s: str, size: float, width: float, bold: bool = False) -> list:
    words, lines = str(s).split(" "), [""]
    for w in words:
        cand = f"{lines[-1]} {w}".strip()
        if lines[-1] and text_w(cand, size, bold) > width:
            lines.append(w)
        else:
            lines[-1] = cand
    return lines


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def date_key(rec: dict) -> tuple:
    """Sort by the year shown in the figure; the arXiv posting date breaks ties within a year."""
    m = ARXIV_YM.search((rec.get("links") or {}).get("arxiv") or "")
    return int(rec["year"]), (int(m.group(1)), int(m.group(2))) if m else (99, 12)


def is_published(rec: dict) -> bool:
    return not str(rec.get("venue", "")).lower().startswith("arxiv")


def pick(recs: list, k: int) -> list:
    pub = sorted((r for r in recs if is_published(r)), key=date_key)
    rest = sorted((r for r in recs if not is_published(r)), key=date_key)
    return (pub + rest)[:k]


def _changed(val) -> bool:
    return val == "primary" or (isinstance(val, dict) and val.get("value") == "other")


def changed_stages(rec: dict) -> list:
    ch = rec.get("changes") or {}
    return [any(_changed(ch.get(k)) for k in STAGE_KEYS[s]) for s in STAGES]


def year_text(rec: dict) -> str:
    return f"'{int(rec['year']) % 100:02d}"


def entry_lines(rec: dict) -> list:
    """Split 'Name ’YY' into lines no wider than name_max_w, breaking after hyphens or spaces."""
    C = CONFIG
    full = f"{rec['name']} {year_text(rec)}"
    if text_w(full, C["font_name"]) <= C["name_max_w"]:
        return [full]
    pieces = re.split(r"(?<=[- ])", rec["name"])
    pieces[-1] = f"{pieces[-1]} {year_text(rec)}"
    lines = [""]
    for piece in pieces:
        if lines[-1] and text_w(lines[-1] + piece, C["font_name"]) > C["name_max_w"]:
            lines.append(piece)
        else:
            lines[-1] += piece
    return [ln.rstrip() for ln in lines]


def build(vocab: dict, papers: list, stage_names: dict, problem_names: dict, zh: bool = False) -> tuple:
    """Return (svg_text, alt_text). stage_names maps stage -> display name; problem_names maps problem value -> display name."""
    C, T = CONFIG, TEXT["zh" if zh else "en"]
    k, fs, fh, fsm, lh = C["max_per_cell"], C["font_name"], C["font_head"], C["font_small"], C["line_h"]
    dots_w = 4 * C["dot_step"] + 2 * C["dot_r"]
    probs = [p["value"] for p in vocab["problem"] if p["value"] != "psb"]
    cells = {(p, s): [r for r in papers if (r["problem"], r["stage"]) == (p, s)] for p in probs for s in STAGES}
    psb_all = [r for r in papers if r["problem"] == "psb"]
    shown = {key: pick(v, k) for key, v in cells.items()}
    psb_shown = pick(psb_all, k)

    def entry_w(r):
        return max(text_w(ln, fs) + (C["wrap_indent"] if j else 0) for j, ln in enumerate(entry_lines(r))) + 10 + dots_w

    col_w = []
    for i, s in enumerate(STAGES):
        need = [entry_w(r) for p in probs for r in shown[(p, s)]]
        need += [entry_w(psb_shown[i])] if i < len(psb_shown) else []
        need += [text_w(stage_names[s], fh, True) + 8]
        col_w.append(max(C["min_col_w"], max(need) + 2 * C["pad_x"]))
    col_x, x0 = [], C["margin"]
    for w in col_w:
        col_x.append(x0)
        x0 += w + C["col_gap"]
    width = round(x0 - C["col_gap"] + C["margin"])

    body, y = [], C["margin"]
    pill_h = 30
    for i, s in enumerate(STAGES):
        fill, stroke, _ = C["stages"][s]
        body.append(f'  <rect x="{col_x[i]:.1f}" y="{y}" width="{col_w[i]:.1f}" height="{pill_h}" rx="15" fill="{fill}" stroke="{stroke}"/>')
        body.append(f'  <text x="{col_x[i] + col_w[i] / 2:.1f}" y="{y + pill_h / 2 + fh * 0.36:.1f}" font-size="{fh}" font-weight="700" '
                    f'text-anchor="middle" fill="{C["text"]}">{esc(stage_names[s])}</text>')
        if i:
            cx, cy = col_x[i] - C["col_gap"] / 2, y + pill_h / 2
            body.append(f'  <path d="M{cx - 2.5:.1f} {cy - 4.5:.1f} L{cx + 2.5:.1f} {cy:.1f} L{cx - 2.5:.1f} {cy + 4.5:.1f}" fill="none" '
                        f'stroke="{C["muted"]}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')
    y += pill_h + 6

    def dot(cx, cy, stage, on):
        color = C["stages"][stage][2]
        return (f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{C["dot_r"]}" fill="{color if on else "#ffffff"}" '
                f'stroke="{color if on else C["hollow"]}" stroke-width="1.1"/>')

    def entry(x, x_right, top_base, r):
        out = []
        lines = entry_lines(r)
        for j, ln in enumerate(lines):
            bx, by = x + (C["wrap_indent"] if j else 0), top_base + j * lh
            if j == len(lines) - 1:
                name, _, year = ln.rpartition(" ")
                out.append(f'  <text x="{bx:.1f}" y="{by:.1f}" font-size="{fs}" fill="{C["text"]}">{esc(name)}'
                           f'<tspan dx="4" fill="{C["muted"]}">{esc(year)}</tspan></text>')
            else:
                out.append(f'  <text x="{bx:.1f}" y="{by:.1f}" font-size="{fs}" fill="{C["text"]}">{esc(ln)}</text>')
        for j, (s, on) in enumerate(zip(STAGES, changed_stages(r))):
            out.append(dot(x_right - dots_w + C["dot_r"] + j * C["dot_step"], top_base - fs * 0.33, s, on))
        return out, len(lines)

    def count_text(n):
        return T["count_one"] if n == 1 else T["count"].format(n=n)

    def band(label, top):
        return f'  <text x="{C["margin"] + 2}" y="{top + fh + 3:.1f}" font-size="{fh}" font-weight="700" fill="{C["text"]}">{esc(label)}</text>'

    def cell_box(x, top, w, h, fill, stroke, n):
        return [f'  <rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}"/>',
                f'  <text x="{x + C["pad_x"]:.1f}" y="{top + C["pad_y"] + fsm:.1f}" font-size="{fsm}" '
                f'fill="{C["muted"]}">{esc(count_text(n))}</text>']

    first_base = C["pad_y"] + 15 + lh - 4
    for p in probs:
        y += C["row_gap"]
        body.append(band(problem_names[p], y))
        y += C["band_h"]
        n_lines = max([sum(len(entry_lines(r)) for r in shown[(p, s)]) for s in STAGES] + [1])
        h = C["pad_y"] * 2 + 15 + n_lines * lh
        for i, s in enumerate(STAGES):
            fill, stroke, _ = C["stages"][s]
            x, w, recs = col_x[i], col_w[i], cells[(p, s)]
            if not recs:
                body.append(f'  <rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="8" fill="none" '
                            f'stroke="{C["empty"]}" stroke-dasharray="4 3"/>')
                continue
            body += cell_box(x, y, w, h, fill, stroke, len(recs))
            used = 0
            for r in shown[(p, s)]:
                out, nl = entry(x + C["pad_x"], x + w - C["pad_x"], y + first_base + used * lh, r)
                body += out
                used += nl
        y += h

    if psb_all:
        y += C["row_gap"]
        body.append(band(problem_names["psb"], y))
        y += C["band_h"]
        n_lines = max(len(entry_lines(r)) for r in psb_shown)
        h = C["pad_y"] * 2 + 15 + n_lines * lh
        body += cell_box(col_x[0], y, col_x[-1] + col_w[-1] - col_x[0], h, C["psb_fill"], C["psb_stroke"], len(psb_all))
        for i, r in enumerate(psb_shown):
            body += entry(col_x[i] + C["pad_x"], col_x[i] + col_w[i] - C["pad_x"], y + first_base, r)[0]
        y += h

    y += 22
    lx = C["margin"] + 2
    body.append(dot(lx + C["dot_r"], y - fsm * 0.33, "Tokenization", True))
    lx += 2 * C["dot_r"] + 5
    body.append(f'  <text x="{lx:.1f}" y="{y:.1f}" font-size="{fsm}" fill="{C["muted"]}">{esc(T["legend_dots"])}</text>')
    lx += text_w(T["legend_dots"], fsm) + 14
    body.append(dot(lx + C["dot_r"], y - fsm * 0.33, "Tokenization", False))
    lx += 2 * C["dot_r"] + 5
    body.append(f'  <text x="{lx:.1f}" y="{y:.1f}" font-size="{fsm}" fill="{C["muted"]}">{esc(T["legend_hollow"])}</text>')
    lx += text_w(T["legend_hollow"], fsm) + 14
    body.append(f'  <text x="{lx:.1f}" y="{y:.1f}" font-size="{fsm}" fill="{C["muted"]}">{esc(T["legend_order"])}</text>')
    y += fsm + 8
    body.append(f'  <text x="{C["margin"] + 2}" y="{y:.1f}" font-size="{fsm}" fill="{C["muted"]}">{esc(T["legend_rule"].format(k=k))}</text>')
    height = round(y + C["margin"])

    n = len(papers)
    title = T["title"].format(n=n)
    font = ('-apple-system, "Segoe UI", "PingFang SC", "Noto Sans CJK SC", Helvetica, Arial, sans-serif' if zh
            else '-apple-system, "Segoe UI", Helvetica, Arial, sans-serif')
    svg = "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" '
        f'role="img" aria-label="{esc(title)}" font-family=\'{font}\'>',
        f"  <title>{esc(title)}</title>",
        f'  <rect x="0" y="0" width="{width}" height="{height}" rx="8" fill="{C["bg"]}"/>',
        *body, "</svg>", ""])
    return svg, T["alt"].format(n=n, k=k)
