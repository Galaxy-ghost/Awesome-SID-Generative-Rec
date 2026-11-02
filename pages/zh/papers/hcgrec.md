# HCGRec

| **题目** | *Learning from Unreachable Rewards: Hint-Conditioned Reinforcement Learning for Generative Recommendation* |
| :-- | :-- |
| **作者** | Zhang et al. |
| **会议** | CIKM’26 |
| **问题与阶段** | `IV. 实用目标` · `Training` |
| **链接** | [论文](https://arxiv.org/abs/2608.11980) · [代码](https://github.com/WncFht/GRec) · [矩阵](../../../README.zh.md#iv--training) · [English](../../papers/hcgrec.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>–"] --> T["Tokenization<br/>RQ"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → RL"] --> I["Inference<br/>Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `–`: Not reported in the paper.
- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### TL;DR

> [!NOTE]
> HCGRec 在 GRPO 采样全部偏离正确物品时提供最小目标前缀提示，对提示 token 用监督损失、对采样后缀用 GRPO，从零奖励组中恢复训练信号。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | IV. 实用目标：Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| 核心贡献 | HCGRec 在 GRPO 采样全部偏离正确物品时提供最小目标前缀提示，对提示 token 用监督损失、对采样后缀用 GRPO，从零奖励组中恢复训练信号。 |
| 主要改动阶段 | Training |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Musical Instruments, Arts/Crafts/Sewing, Video Games; maximum history 50. Filtering: not reported.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS1.p1)
- **切分**：Per-user chronological leave-one-out: last item test, penultimate validation, remaining interactions training.
  - 出处：Section 4.1.2: [S4.SS1.SSS2.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS2.p1)
- **候选集**：full catalog
  - 出处：Section 4.1.2: [S4.SS1.SSS2.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS2.p1)
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Section 4.1 defines no unseen-item evaluation: [S4.SS1](https://arxiv.org/html/2608.11980v2#S4.SS1)
- **SID 规格**：Four-token residual-quantization SIDs, shared across variants; codebook sizes and collision handling: not reported.
  - 出处：Sections 3.1 and 4.1.1: [S3.SS1.p1](https://arxiv.org/html/2608.11980v2#S3.SS1.p1) and [S4.SS1.SSS1.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS1.p1)
- **推理预算**：Beam 50; HR/NDCG@5/10/50; no target-prefix hints at inference. Inference hardware, batch size, latency: not reported.
  - 出处：Sections 3.5 and 4.1.2: [S3.SS5.p1](https://arxiv.org/html/2608.11980v2#S3.SS5.p1) and [S4.SS1.SSS2.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS2.p1)
- **结果来源**：Original Table 2: main comparison; Figures 2-6 and Sections 4.3-4.5: reachability, hint policy, task/loss ablations, credit weight.
  - 出处：Table 2 and Figures 2-6: [S4.T2](https://arxiv.org/html/2608.11980v2#S4.T2) and [S4.F2](https://arxiv.org/html/2608.11980v2#S4.F2) and [S4.F6](https://arxiv.org/html/2608.11980v2#S4.F6)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["HCGRec"]
    P -->|predecessor| A["LC-Rec"]
    P -->|competitor| B["MiniOneRec"]
    P -->|competitor| C["TIGER"]
```

- **前序工作** · [LC-Rec](lc-rec.md): LC-Rec provides the supervised semantic-alignment checkpoint in this pipeline.
  - 出处：HCGRec v2, Section 4.2: https://arxiv.org/html/2608.11980v2#S4.SS2.p2.
- **同期对比** · [MiniOneRec](minionerec.md): MiniOneRec shares the SFT checkpoint and controlled post-training budget.
  - 出处：HCGRec v2, Section 4.2 and Table 2: https://arxiv.org/html/2608.11980v2#S4.SS2.p1; https://arxiv.org/html/2608.11980v2#S4.T2.
- **同期对比** · [TIGER](tiger.md): TIGER is the semantic-ID generative baseline in the main comparison.
  - 出处：HCGRec v2, Section 4.2 and Table 2: https://arxiv.org/html/2608.11980v2#S4.SS2.p2; https://arxiv.org/html/2608.11980v2#S4.T2.

[查看同格全部论文](../../../README.zh.md#iv--training)
