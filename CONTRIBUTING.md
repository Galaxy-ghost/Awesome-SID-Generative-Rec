# Contributing

To add or update a paper in two steps:

1. Create or edit `data/papers/<id>.yaml` following [`schema/paper.schema.json`](schema/paper.schema.json), [`schema/README.md`](schema/README.md), and [`data/vocab.yaml`](data/vocab.yaml). Write `tldr` and its Chinese version `tldr_zh`. Optionally add notes in `notes/<id>.md` and the Chinese notes in `notes/zh/<id>.md`.
2. Run `make build && make check` to regenerate the English and Chinese READMEs and pages, the comparison tables, and `llms.txt`, and to verify all checks.

Rules for notes and records:

- Notes use the standard headings `### 1. Why This Paper Matters` to `### 4. Limitations & Critical Analysis`. `make build` sets the reading level.
- Chinese notes use `### 1. 为什么重要`, `### 2. 方法`, `### 3. 实验发现`, and `### 4. 局限与分析`, with the same headings, quotations (kept in English), and numbers as the English notes. `make check` compares them.
- Every number carries its location in the paper, for example (Table 1).
- Quotations are copied word for word and carry their location.
- Describe the paper with reports and states; mark inferences with suggests.
