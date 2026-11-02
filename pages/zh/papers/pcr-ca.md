# PCR-CA

| **题目** | *Parallel Codebook Representations with Contrastive Alignment for Multiple-Category App Recommendation* |
| :-- | :-- |
| **作者** | Tan et al. |
| **会议** | KDD’26 |
| **问题与阶段** | `I. 信息量` · `Tokenization` |
| **链接** | [论文](https://arxiv.org/abs/2508.18166) · [矩阵](../../../README.zh.md#i--tokenization) · [English](../../papers/pcr-ca.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>PC-AE"] --> B["Backbone<br/>Disc."] --> TR["Training<br/>Joint / Discrim."] --> I["Inference<br/>Scoring"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `PC-AE`: Parallel Codebook Auto-Encoder
- `Disc.`: A discriminative recommendation model that scores candidates.
- `Joint`: The generator loss updates the tokenizer directly.
- `Discrim.`: Scores items; does not generate SIDs.

### TL;DR

> [!NOTE]
> PCR-CA 不同于层级 RQ-VAE，学习应用文本的并行码本表示，并通过对比学习将它与协同信号对齐，用于多类目应用的点击率预测。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | PCR-CA 不同于层级 RQ-VAE，学习应用文本的并行码本表示，并通过对比学习将它与协同信号对齐，用于多类目应用的点击率预测。 |
| 主要改动阶段 | Tokenization |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Microsoft Store impression logs with click/install labels over several months; approximately 80K apps, click rate 6.148%; histories up to 50 interactions. Filtering rules not reported.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1)
- **切分**：Chronological: 340M training interactions and latest 10M validation samples. Table 2 calls evaluation the test set, but a separate test allocation is not reported. Online A/B lasts two weeks.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1) ; #S4.T2 ; #S4.T5
- **候选集**：n/a for logged-impression CTR/AUC evaluation; candidate pool for top-10 diversity analysis not reported.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1) ; #S4.SS1.p6 ; #S4.SS4.p2
- **可见性**：Cold-start validation naturally includes apps/users unseen in CTR training. Unseen by CTR predictor only: PC-AE pretraining iterates over all 80K apps; no generative decoder is used.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1) ; #S4.SS1.p4
- **SID 规格**：PC-AE: 4 parallel codebooks x 32 entries, 16-dimensional vectors, selecting/summing two nearest codes per book. Codebooks train jointly with CTR prediction after pretraining. Unique-ID collision resolution: n/a; codes supply predictive features.
  - 出处：[S3.SS2.p3](https://arxiv.org/html/2508.18166v1#S3.SS2.p3) ; #S3.SS2.p7 ; #S4.SS1.p2
- **推理预算**：Discriminative scoring; beam n/a; top-10 lists for diversity. Simulated throughput: 120K candidate items/s versus base 150K/s on the same unspecified server. Inference hardware, batch size and request latency not reported; offline text embedding costs 22 ms/new app.
  - 出处：[S4.SS4.p2](https://arxiv.org/html/2508.18166v1#S4.SS4.p2) ; #S4.SS4.p3 ; #S4.SS4.p4
- **结果来源**：Original Table 2: AUC by app-popularity bucket; Tables 3-4: ablations; Table 5: online A/B. SaviorRec is explicitly reimplemented; no baseline-result reuse stated.
  - 出处：[S4.T2](https://arxiv.org/html/2508.18166v1#S4.T2) ; #S4.T3 ; #S4.T4 ; #S4.T5 ; #S4.SS1.p2

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["PCR-CA"]
    P -->|alternative| A["CoST"]
```

- **替代方案** · [CoST](cost.md): CoST uses residual vector quantization; PCR-CA replaces its hierarchy with parallel codebooks for multiple-category app features and CTR prediction.
  - 出处：PCR-CA v1, Introduction and Section 2.2, citing Yongchao Zhu et al. (2024): https://arxiv.org/html/2508.18166v1#S1.p4; https://arxiv.org/html/2508.18166v1#S2.SS2.p3.

[查看同格全部论文](../../../README.zh.md#i--tokenization)
