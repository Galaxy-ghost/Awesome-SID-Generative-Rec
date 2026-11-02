# DiGR

| **题目** | *From Token Generation to Item Ranking: Direct Generative Recommendation with Semantic IDs* |
| :-- | :-- |
| **作者** | Zhao et al. |
| **会议** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `Backbone` |
| **链接** | [论文](https://arxiv.org/abs/2602.07847) · [代码](https://anonymous.4open.science/r/SimGR-C408/) · [矩阵](../../../README.zh.md#iv--backbone) · [English](../../papers/digr.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>–"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / Discrim."] --> I["Inference<br/>Scoring"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class B main
```

- `–`: Not reported in the paper.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### TL;DR

> [!NOTE]
> DiGR 论证逐 token 解码不增加排序表达力后，将 SID token 作为物品表示并用单一物品级函数直接打分，不再逐位生成 token。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | IV. 实用目标：Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| 核心贡献 | DiGR 论证逐 token 解码不增加排序表达力后，将 SID token 作为物品表示并用单一物品级函数直接打分，不再逐位生成 token。 |
| 主要改动阶段 | Backbone |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2018: Musical Instruments, Arts/Crafts/Sewing, Video Games; user/item 5-core; chronological histories capped at 20.
  - 出处：[Sx5.SSx1.SSSx1.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx1.p1)
- **切分**：Per-user leave-one-out: last interaction test, penultimate validation, all earlier interactions training; learning rate and training epochs selected by validation grid search.
  - 出处：[Sx5.SSx1.SSSx3.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx3.p1) ; [Sx5.SSx1.SSSx4.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx4.p1)
- **候选集**：full catalog for DiGR and other scoring-based methods; autoregressive baselines use prefix-constrained beam 20; history exclusion not reported.
  - 出处：[Sx5.SSx1.SSSx3.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx3.p1)
- **可见性**：warm; no unseen-item protocol is defined. Tokenizer exposure to test items is not reported.
  - 出处：[Sx5.SSx1.SSSx3.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx3.p1) ; inductive capability is discussed, not evaluated as an item-holdout protocol.
- **SID 规格**：RQ-VAE SIDs composed by mean-pooling shared position-specific SID-token embeddings; SID length, codebook sizes, tokenizer input encoder and collision handling not reported. Appendix D additionally compares R-KMeans and OPQ on Instruments.
  - 出处：[Sx5.SSx1.SSSx4.p2](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx4.p2) ; [Sx4.SSx2.SSS0.Px2.p1](https://arxiv.org/html/2602.07847v2#Sx4.SSx2.SSS0.Px2.p1) ; [A4.p1](https://arxiv.org/html/2602.07847v2#A4.p1)
- **推理预算**：Precomputed item vectors and direct item-level scoring; no SID decoding. HR@1/5/10 and NDCG@5/10. Instruments timing: 0.074 s/user on one NVIDIA A100; inference batch size not reported. Beam 20 belongs to main autoregressive baselines, with 50/100 in the separate timing study.
  - 出处：[Sx4.SSx2.SSS0.Px3.p1](https://arxiv.org/html/2602.07847v2#Sx4.SSx2.SSS0.Px3.p1) ; [Sx5.T3](https://arxiv.org/html/2602.07847v2#Sx5.T3) ; [Sx5.SSx1.SSSx3.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx3.p1)
- **结果来源**：Own recommendation comparison and controlled ranking/efficiency studies; ID baselines use RecBole, generative baselines follow official designs, LC-Rec shares Qwen3-4B/LoRA settings. Ranking-overlap reference is exhaustive LC-Rec scoring, not observed ground-truth preference order. Appendix D uses GPT-2 controls; no imported baseline scores stated; run counts/variance not reported.
  - 出处：[Sx5.T2](https://arxiv.org/html/2602.07847v2#Sx5.T2) ; [Sx5.SSx1.SSSx4.p2](https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx4.p2) ; [Sx5.SSx3.p1](https://arxiv.org/html/2602.07847v2#Sx5.SSx3.p1) ; [A4.p1](https://arxiv.org/html/2602.07847v2#A4.p1)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["DiGR"]
    P -->|competitor| A["LC-Rec"]
    P -->|competitor| B["RPG"]
    P -->|competitor| C["TIGER"]
```

- **同期对比** · [LC-Rec](lc-rec.md): Matched-backbone baseline and exhaustive-ranking reference.
  - 出处：https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx4.p2 ; https://arxiv.org/html/2602.07847v2#Sx5.SSx3.p1
- **同期对比** · [RPG](rpg.md): Parallel SID-generation baseline in the main comparison.
  - 出处：https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx2.p1 ; https://arxiv.org/html/2602.07847v2#Sx5.T2
- **同期对比** · [TIGER](tiger.md): Autoregressive SID-generation baseline in the main comparison.
  - 出处：https://arxiv.org/html/2602.07847v2#Sx5.SSx1.SSSx2.p1 ; https://arxiv.org/html/2602.07847v2#Sx5.T2

[查看同格全部论文](../../../README.zh.md#iv--backbone)
