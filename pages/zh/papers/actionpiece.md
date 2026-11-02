# ActionPiece

| **题目** | *Contextually Tokenizing Action Sequences for Generative Recommendation* |
| :-- | :-- |
| **作者** | Hou et al. |
| **会议** | ICML’25 |
| **问题与阶段** | `I. 信息量` · `Tokenization` |
| **链接** | [论文](https://arxiv.org/abs/2502.13581) · [代码](https://github.com/google-deepmind/action_piece) · [矩阵](../../../README.zh.md#i--tokenization) · [English](../../papers/actionpiece.md) |
| **阅读级别** | 阅读笔记（第 2 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>OPQ"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>Ensemble"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `OPQ`: Optimized product quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

> [!NOTE]
> ActionPiece 将每次交互表示为物品特征集合，把共现特征模式合并为新 token，使相同动作获得随上下文变化的 token，而非固定独立的 token。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | ActionPiece 将每次交互表示为物品特征集合，把共现特征模式合并为新 token，使相同动作获得随上下文变化的 token，而非固定独立的 token。 |
| 主要改动阶段 | Tokenization |

---

### 1. 为什么重要

现有的生成式推荐（GR）模型对每个行为单独编号，同一个行为在任何序列里都得到相同的 token（Abstract）。作者认为，同一个行为放在不同的上下文里，意思可以不同（Abstract）。ActionPiece 让前后的行为决定一个行为怎样被编号。

> "However, existing GR models tokenize each action independently, assigning the same fixed tokens to identical actions across all sequences without considering contextual relationships."（Abstract）（现有 GR 模型孤立地给每个行为编号，不看上下文。）

---

### 2. 方法

![ActionPiece architecture diagram](../../../architectures/actionpiece.png)

```mermaid
flowchart LR
    A("特征集合组成的行为序列") --> B["统计集合内和相邻集合间的 token 对"]
    B --> C["加权合并"]:::key
    C --> D("依赖上下文的词表")
    D --> E["集合置换正则"]
    E --> F("多种切分")
    F --> G["Enc-Dec 生成器"]
    G --> H("集成后的排序")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 行为即特征集合

每个行为是一组无序的物品特征，用户历史就是一串特征集合（Abstract）。

#### 构建词表

合并计数既在单个集合内部做，也在相邻集合之间做（Abstract）。两类 token 对的权重不同（Sec. 1）。

> "Considering the structural differences between token pairs, e.g., whether they occur within a single set or between two adjacent sets, we assign different weights to different pairs."（Sec. 1）（集合内和跨集合的 token 对权重不同。）

#### 集合置换正则

特征集合没有顺序，所以集合置换正则可以把同一条行为序列切成多种语义相同的切分（Abstract）。这些切分在训练时用作数据增强，在推理时做集成（Sec. 3.2.2）。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews: Sports and Outdoors, Beauty, and CDs and Vinyl. Users with fewer than 5 reviews are filtered; an item-frequency filter is not reported. Processed sizes (users / items / actions): Sports 35,598 / 18,357 / 260,739; Beauty 22,363 / 12,101 / 176,139; CDs 75,258 / 64,443 / 1,022,334.
  - 出处：Dataset categories: [S4.SS1.p1](https://arxiv.org/html/2502.13581v3#S4.SS1.p1); user filter and truncation: [A6.p2](https://arxiv.org/html/2502.13581v3#A6.p2); processed sizes: [S3.T3](https://arxiv.org/html/2502.13581v3#S3.T3).
- **切分**：Per-user chronological leave-last-out: last item for test, second-to-last for validation, earlier items for training. Histories are truncated to 20 items for generative methods and 50 items for ID-based and feature-enhanced baselines.
  - 出处：Leave-last-out allocation: [S4.SS1.p1](https://arxiv.org/html/2502.13581v3#S4.SS1.p1); history truncation: [A6.p2](https://arxiv.org/html/2502.13581v3#A6.p2).
- **候选集**：not reported (full catalog versus sampled evaluation candidates); top-K lists are produced by beam search.
  - 出处：Evaluation settings name metrics only: [S4.SS1.p3](https://arxiv.org/html/2502.13581v3#S4.SS1.p3); top-K lists come from beam search: [A8.p4](https://arxiv.org/html/2502.13581v3#A8.p4).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Standard leave-last-out protocol with no cold-start experiment: [S4.SS1.p1](https://arxiv.org/html/2502.13581v3#S4.SS1.p1).
- **SID 规格**：Each item is an unordered set of 4 OPQ codes x 256 codewords (sentence-t5-base text embeddings) plus 1 extra identification code to prevent conflicts. ActionPiece then merges co-occurring feature sets into a context-dependent vocabulary of 40,000 tokens (tuned over 5k-40k), so the same item can map to different tokens in different sequences.
  - 出处：OPQ features, 256 codewords per digit, extra identification code: [A6.I1.i3.p1](https://arxiv.org/html/2502.13581v3#A6.I1.i3.p1); vocabulary size 40,000 and tuning range: [A7.T7](https://arxiv.org/html/2502.13581v3#A7.T7) and [A8.p2](https://arxiv.org/html/2502.13581v3#A8.p2).
- **推理预算**：Beam search with beam size 50; inference-time ensemble over q=5 set-permutation segmentations, with item scores averaged across the 5 ranking lists. Recall and NDCG at K=5 and 10. Inference hardware, inference batch size, and measured latency: not reported (each model is trained on one 40GB NVIDIA A100; the paper states only that latency stays comparable when segments run in parallel).
  - 出处：Beam size 50 and q=5 segmentations: [A8.p2](https://arxiv.org/html/2502.13581v3#A8.p2) and [A7.T7](https://arxiv.org/html/2502.13581v3#A7.T7); score averaging: [S3.SS3.SSS2.p1](https://arxiv.org/html/2502.13581v3#S3.SS3.SSS2.p1); GPU statement is for training: [A8.p3](https://arxiv.org/html/2502.13581v3#A8.p3); qualitative latency statement: [S3.SS4.p3](https://arxiv.org/html/2502.13581v3#S3.SS4.p3).
- **结果来源**：Table 4 (main comparison on Sports, Beauty, and CDs; averages over five seeds); Table 5 (ablations, including TIGER with varied vocabulary sizes); Figures 4-6 (vocabulary size, token utilization, and ensemble size). BERT4Rec, SASRec, FDSA, S3-Rec, TIGER, and LMIndexer numbers on Sports and Beauty are copied from earlier papers; other results are the authors' reimplementations.
  - 出处：Main table: [S3.T4](https://arxiv.org/html/2502.13581v3#S3.T4) and [S4.SS2.p1](https://arxiv.org/html/2502.13581v3#S4.SS2.p1); ablation: [S4.T5](https://arxiv.org/html/2502.13581v3#S4.T5); five seeds: [S4.SS1.p3](https://arxiv.org/html/2502.13581v3#S4.SS1.p3); copied baseline numbers: [A8.p1](https://arxiv.org/html/2502.13581v3#A8.p1).

</details>

- 词表大小：词表越大，推荐效果越好，归一化序列长度（NSL）越短（Sec. 4.4.1，Fig. 4）。作者把词表大小看作效果、序列长度和内存之间的权衡（Sec. 4.4.1）。
- 消融：提升不只来自词表变大（Sec. 4.3，Table 5）。

  > "These results suggest that the performance improvement of ActionPiece is not simply due to scaling the vocabulary size up or down."（Sec. 4.3）（提升不是单纯调大或调小词表带来的。）

- token 使用：同一物品按邻居得到不同的 token，提高了 token 的使用率，也起到数据增强的作用（Sec. 4.3）。
- 其他分析：论文还研究了 token 使用（Sec. 4.4.2）、集成数（Fig. 6）和案例（Sec. 4.5）。

---

### 4. 局限与分析

**Our analysis.**

- 推理时要对多种切分分别排序再平均分数。由此推断，除非并行处理，解码开销会随集成数增长。
- VQ-Rec 在 `Encoder` 上用 `OPQ` 码做 `Scoring`；ActionPiece 从同类的码出发，但用 `Enc-Dec` 生成器生成合并后的 token。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["ActionPiece"]
    P -->|competitor| A["TIGER"]
    P -->|predecessor| B["VQ-Rec"]
    P -->|competitor| C["LMIndexer"]
    P -->|competitor| D["CID"]
```

- **同期对比** · [TIGER](tiger.md): TIGER tokenizes each item independently into ordered RQ-VAE codes, whereas ActionPiece merges unordered feature sets into context-dependent tokens; both use the same encoder-decoder and beam search.
  - 出处：ActionPiece v3, Section 4.1 baselines: https://arxiv.org/html/2502.13581v3#S4.SS1.p2; Table 4: https://arxiv.org/html/2502.13581v3#S3.T4; same architecture statement: https://arxiv.org/html/2502.13581v3#A8.p2.
- **前序工作** · [VQ-Rec](vq-rec.md): ActionPiece follows VQ-Rec in quantizing sentence embeddings with OPQ into unordered codes, then builds a merged contextual vocabulary over those codes for generation.
  - 出处：ActionPiece v3, Appendix F follows Hou et al. (2023) for OPQ features: https://arxiv.org/html/2502.13581v3#A6.I1.i3.p1; VQ-Rec is a Table 4 baseline: https://arxiv.org/html/2502.13581v3#S3.T4.
- **同期对比** · [LMIndexer](lmindexer.md): LMIndexer learns text-based semantic indexes item by item, while ActionPiece tokenizes whole action sequences with context-aware merges.
  - 出处：ActionPiece v3, Table 1 and Section 4.1 baselines: https://arxiv.org/html/2502.13581v3#S1.T1 and https://arxiv.org/html/2502.13581v3#S4.SS1.p2; Table 4: https://arxiv.org/html/2502.13581v3#S3.T4.
- **同期对比** · [CID](cid.md): P5-CID builds item IDs by hierarchical clustering, independent of sequence context; ActionPiece's tokens depend on neighboring actions.
  - 出处：ActionPiece v3, Table 1 and Section 4.1 baselines: https://arxiv.org/html/2502.13581v3#S1.T1 and https://arxiv.org/html/2502.13581v3#S4.SS1.p2; Table 4: https://arxiv.org/html/2502.13581v3#S3.T4.

[查看同格全部论文](../../../README.zh.md#i--tokenization)
