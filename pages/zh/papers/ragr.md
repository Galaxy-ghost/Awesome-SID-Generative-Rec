# RAGR

| **题目** | *Review-Augmented Generative Recommendation* |
| :-- | :-- |
| **作者** | Zhang et al. |
| **会议** | arXiv’26 |
| **问题与阶段** | `I. 信息量` · `Training` |
| **链接** | [论文](https://arxiv.org/abs/2605.17267) · [代码](https://github.com/Zhang-Yingyi/TKDE_RAGR) · [矩阵](../../../README.zh.md#i--training) · [English](../../papers/ragr.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP → DPO"] --> I["Inference<br/>Beam† / –"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.
- `Beam† / –`: Inherited beam search in one configuration; decoding not reported in the other.

### TL;DR

> [!NOTE]
> RAGR 在用户序列中按时间交错排列物品 SID 与评论 SID，并用 DPO 在预测位置偏好物品 token，替代仅建模物品序列的做法。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | RAGR 在用户序列中按时间交错排列物品 SID 与评论 SID，并用 DPO 在预测位置偏好物品 token，替代仅建模物品序列的做法。 |
| 主要改动阶段 | Training |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty, Sports and Outdoors, Toys and Games, with historical review text; remove users/items with fewer than five interactions; maximum history 20, truncating oldest interactions.
  - 出处：[S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS1.p1) ; #S4.SS1.SSS4.p3
- **切分**：Per-user chronological leave-one-out: last interaction test, second last validation, remaining interactions training.
  - 出处：[S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS1.p1)
- **候选集**：not reported
  - 出处：Experimental settings report top-K metrics but no candidate universe: [S4.SS1](https://arxiv.org/html/2605.17267v1#S4.SS1)
- **可见性**：warm; no unseen-item protocol is defined. Historical reviews are retained; tokenizer fitting exposure to test items not reported.
  - 出处：[S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS1.p1) ; #S4.SS4.p4
- **SID 规格**：RQ-VAE: 4 x 256, 32-dimensional codewords, shared item/review token space. Default tokenizer fits item text only; collision handling not reported.
  - 出处：[S4.SS1.SSS4.p2](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS4.p2) ; #S4.SS4.p4 ; #S4.SS5.p4
- **推理预算**：Autoregressive item-SID prediction; HIT/NDCG@5/10/20. Decoding algorithm/beam width, inference batch size and latency not reported. General experiment server: 8 RTX PRO 6000 96GB GPUs; inference-specific allocation not reported.
  - 出处：[S4.SS1.SSS3.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS3.p1) ; #S4.SS1.SSS4.p1 ; #S4.SS1.SSS4.p5
- **结果来源**：Original Table II: TIGER/LETTER with and without RAGR, means over seeds 42/43/44; all baselines trained/evaluated with the common split/protocol. Table III: ablations; Tables IV-V: tokenizer efficiency/collisions. No baseline-result reuse stated.
  - 出处：[S4.T2](https://arxiv.org/html/2605.17267v1#S4.T2) ; #S4.T3 ; #S4.T4 ; #S4.T5 ; #S4.SS1.SSS4.p1 ; #S4.SS1.SSS4.p5

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["RAGR"]
    P -->|predecessor| A["TIGER"]
    P -->|predecessor| B["LETTER"]
```

- **前序工作** · [TIGER](tiger.md): RAGR augments TIGER with interleaved review SIDs, review-generation supervision and DPO alignment toward item generation.
  - 出处：RAGR v1, Section IV-A and Table II: https://arxiv.org/html/2605.17267v1#S4.SS1.SSS4.p1; https://arxiv.org/html/2605.17267v1#S4.T2.
- **前序工作** · [LETTER](letter.md): LETTER is the second backbone receiving the same review augmentation and item-centric DPO alignment.
  - 出处：RAGR v1, Section IV-A and Table II: https://arxiv.org/html/2605.17267v1#S4.SS1.SSS4.p1; https://arxiv.org/html/2605.17267v1#S4.T2.

[查看同格全部论文](../../../README.zh.md#i--training)
