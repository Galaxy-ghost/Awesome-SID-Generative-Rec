# 参与贡献

[English](CONTRIBUTING.md) | 中文

## 维护流程

新增或更新论文记录与精读笔记只需两步：

1. 参照 [`schema/paper.schema.json`](schema/paper.schema.json)、[`schema/README.md`](schema/README.md) 与 [`data/vocab.yaml`](data/vocab.yaml) 创建或编辑 `data/papers/<id>.yaml`，同时填写英文 `tldr` 与中文 `tldr_zh`。若新增或修改 `notes/<id>.md` 中的精读笔记，需同步更新同结构的中文笔记 `notes/zh/<id>.md`。
2. 更新双语章节配对哈希并重新生成全部页面与索引：

```sh
python3 scripts/check.py --write-i18n
make build && make check
```

## 写作与双语规范

- **章节结构**：英文笔记依次使用 `## At a Glance`（含 `Key Findings:` 与 `Limitation:`）、`### 1. Why This Paper Matters`、`### 2. How It Works`、`### 3. Experimental Findings` 和 `### 4. Limitations & Critical Analysis`。中文笔记依次使用 `## At a Glance`（键名仍为 `Key Findings:` 与 `Limitation:`）、`### 1. 为什么重要`、`### 2. 方法`、`### 3. 实验发现` 和 `### 4. 局限与分析`，并保持完全相同的 `###` 与 `####` 标题层级树。
- **双语配对校验（`data/i18n.yaml`）**：参照 `@deepseek-ai/dsh` 的双语维护方式，`data/i18n.yaml` 按标题路径记录 `CONTRIBUTING.md`、`guides/start-here.md` 与 `notes/*.md` 中英文正文块（代码块之外）的 SHA-256 哈希。修改任一语言后，需同步修改另一语言并运行 `python3 scripts/check.py --write-i18n`。`make check` 会自动核对双语章节哈希、标题层级树、代码块与 Mermaid 图数量、英文原句引文以及全部数值。
- **内部算法可视化**：第 2 节至少包含一张展示论文内部算法细节的 Mermaid 图（流程用 `flowchart LR`，树结构用 `flowchart TD`，多步交互用 `sequenceDiagram`）：圆角框 `A("…")` 表示输入或张量，矩形框 `B["…")` 表示算子或模块，六边形框 `L{{"…"}}` 表示损失或优化目标，菱形框 `C{"…"}` 表示分支或剪枝条件；实线表示前向数据流，虚线表示梯度、奖励或蒸馏监督信号；论文的核心创新模块标为 `:::key`（`classDef key fill:#eaf2fb,stroke:#6b8fc7`）。
- **行文与证据规范**：直接用平实短句描述方法做了什么、解决什么问题。首次出现写“语义 ID（Semantic ID，SID）”，之后写 SID；tokenizer 译为“编号器”，generator 译为“生成器”，codebook 译为“码本”。每个实验数值需写明数据集、指标、对比基线与原文位置（如 `（Table 1）`）。英文引文保留原句与位置标注，不在引文后再附冗余括号翻译。局限部分区分作者自述（`**Stated by the authors.**`）与独立分析（`**Our analysis.**`）。
