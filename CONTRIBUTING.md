# Contributing

English | [中文](CONTRIBUTING.zh.md)

## Workflow

To add or update a paper record or reading note:

1. Create or edit `data/papers/<id>.yaml` following [`schema/paper.schema.json`](schema/paper.schema.json), [`schema/README.md`](schema/README.md), and [`data/vocab.yaml`](data/vocab.yaml). Provide both `tldr` and its Chinese counterpart `tldr_zh`. When adding or editing reading notes in `notes/<id>.md`, update the paired Chinese notes in `notes/zh/<id>.md` with the same section hierarchy.
2. Record bilingual section hashes and regenerate all views:

```sh
python3 scripts/check.py --write-i18n
make build && make check
```

## Writing and Bilingual Rules

- **Section structure**: English notes use `## At a Glance` (`Key Findings:` and `Limitation:`) followed by `### 1. Why This Paper Matters`, `### 2. How It Works`, `### 3. Experimental Findings`, and `### 4. Limitations & Critical Analysis`. Chinese notes use `## At a Glance` (`Key Findings:` and `Limitation:`) followed by `### 1. 为什么重要`, `### 2. 方法`, `### 3. 实验发现`, and `### 4. 局限与分析`, keeping the same `###` and `####` heading tree.
- **Bilingual pairing (`data/i18n.yaml`)**: Modeled on `@deepseek-ai/dsh`, `data/i18n.yaml` records per-heading-section SHA-256 hashes of the English and Chinese prose blocks outside fenced code blocks across `CONTRIBUTING.md`, `guides/start-here.md`, and `notes/*.md`. Editing either language requires updating its counterpart and running `python3 scripts/check.py --write-i18n`. `make check` verifies section-hash pairing, heading hierarchy, code/Mermaid block counts, verbatim English quotations, and numbers.
- **Algorithm diagrams**: Section 2 includes at least one Mermaid diagram (`flowchart LR`, `flowchart TD` for trees, or `sequenceDiagram` for multi-step interactions) depicting the paper's internal algorithm: tensors and inputs in rounded nodes `A("…")`, operators and modules in boxes `B["…"]`, losses and objectives in hexagons `L{{"…"}}`, and routing/pruning conditions in diamonds `C{"…"}`. Solid edges represent forward data flow; dotted edges represent gradients, rewards, or distillation signals; the paper's core mechanism uses `:::key` (`classDef key fill:#eaf2fb,stroke:#6b8fc7`).
- **Evidence and tone**: State what the method does directly with active verbs (`encodes`, `quantizes`, `predicts`, `decodes`). Every quantitative result carries its dataset, metric, baseline, and paper location (e.g., `(Table 1)`). Quotations are copied verbatim with their section location. Separate author-reported limitations (`**Stated by the authors.**`) from critical analysis (`**Our analysis.**`).
