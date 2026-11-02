# VQ-Rec

| **题目** | *Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders* |
| :-- | :-- |
| **作者** | Hou et al. |
| **会议** | WWW’23 |
| **问题与阶段** | `VI. 泛化` · `Tokenization` |
| **链接** | [论文](https://arxiv.org/abs/2210.12316) · [代码](https://github.com/RUCAIBox/VQ-Rec) · [矩阵](../../../README.zh.md#vi--tokenization) · [English](../../papers/vq-rec.md) |
| **阅读级别** | 阅读笔记（第 2 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Multi-Dom"] --> T["Tokenization<br/>OPQ"] --> B["Backbone<br/>Encoder"] --> TR["Training<br/>Fixed / Discrim."] --> I["Inference<br/>Scoring"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `OPQ`: Optimized product quantization.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### TL;DR

> [!NOTE]
> VQ-Rec 将物品文本映射为离散码并查表组合码嵌入作为物品表示，配合对比预训练与跨域微调，解除文本与物品表示之间的强绑定。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | VI. 泛化：Does it still work for new items, new domains, and shifting interests? |
| 核心贡献 | VQ-Rec 将物品文本映射为离散码并查表组合码嵌入作为物品表示，配合对比预训练与跨域微调，解除文本与物品表示之间的强绑定。 |
| 主要改动阶段 | Tokenization |

---

### 1. 为什么重要

可迁移推荐器用预训练语言模型（PLM）编码物品文本，把编码直接当作物品表示（Abstract）。作者认为，这种紧绑定过于强调文本特征，放大了领域差异的影响（Abstract，Sec. 4）。VQ-Rec 在文本和表示之间插入离散码：物品文本先映射成一个离散索引向量，即物品码，再用这个码到嵌入表里查出物品表示（Sec. 2.1）。VQ-Rec 是判别式序列推荐器，不是生成式的；后来的语义 ID（Semantic ID，SID）论文沿用了它的编码方案。

---

### 2. 方法

![VQ-Rec architecture diagram](../../../architectures/vq-rec.png)

```mermaid
flowchart LR
    A("物品文本") --> B["固定的 BERT"]
    B --> C["OPQ"]
    C --> D("物品码")
    D --> E["查码嵌入 + 取平均"]:::key
    E --> F["Transformer 编码器"]
    L1{{"对比：半合成负例 + 混合领域负例"}} -.-> F
    F --> G("物品分数")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 文本到码

固定的 BERT 编码器嵌入物品文本，优化乘积量化（OPQ）把嵌入切成若干子空间，在每个子空间里独立分配一个索引（Sec. 2.2.1，Eq. 2）。PQ 中心从所有训练领域的文本编码中学得。

#### 码到表示

码的每一位有自己的码嵌入表，物品表示是查出的各嵌入的平均（Sec. 2.2.2，Eq. 3）。码嵌入和 PQ 中心是两套独立的参数。

#### 对比预训练

Transformer 编码物品表示组成的序列（Sec. 2.3.1）。真实的下一物品是正例。半合成负例随机替换物品码的一部分，混合领域负例是同批的其他物品（Sec. 2.3）。预训练更新码嵌入和 Transformer；BERT 固定，PQ 事先算好（Sec. 2.4）。

#### 跨域微调

到新领域时，VQ-Rec 重新训练 PQ 中心，用可微的置换网络把它们和已有的码嵌入对齐，再微调置换后的嵌入表（Sec. 2.4.1）。

> "During fine-tuning, we fix the Transformer sequence encoder (transferred across different domains), and only optimize the parameters involved in item representations, enabling parameter-efficient fine-tuning."（Sec. 2.4）（微调时固定跨领域迁移的 Transformer，只优化物品表示相关的参数。）

已知领域里出现新物品时不需要重训。

> "When a new item emerges, one can encode its item text into discrete indices, and then obtain the corresponding item representations by embedding lookup."（Sec. 2.4.2）（新物品的文本编码成离散索引，查嵌入表即得表示。）

```mermaid
flowchart LR
    A("新领域文本") --> B["重训 PQ 中心"]
    B --> C["可微置换，对齐旧码嵌入"]:::key
    C --> D["微调置换后的嵌入表，Transformer 固定"]
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Pre-training on five Amazon domains (Food, Home, CDs, Kindle, Movies; 1,361,408 users / 446,975 items); downstream on Amazon Scientific, Pantry, Instruments, Arts, Office and the cross-platform Online Retail dataset. Users and items with fewer than 5 interactions are filtered (following UniSRec); item text truncated to 512 tokens.
  - 出处：Pre-training and downstream domains: [S3.SS1.SSS1.p1](https://arxiv.org/html/2210.12316v2#S3.SS1.SSS1.p1); filtering: [S3.SS1.SSS1.p2](https://arxiv.org/html/2210.12316v2#S3.SS1.SSS1.p2); statistics: [S2.T1](https://arxiv.org/html/2210.12316v2#S2.T1).
- **切分**：Leave-one-out: latest item for test, the one before for validation, the rest for training; pre-train on source domains, then fine-tune per downstream dataset.
  - 出处：Leave-one-out allocation: [S3.SS1.SSS3.p1](https://arxiv.org/html/2210.12316v2#S3.SS1.SSS3.p1).
- **候选集**：full catalog (the ground-truth item is ranked among all other items).
  - 出处：Ranked among all other items: [S3.SS1.SSS3.p1](https://arxiv.org/html/2210.12316v2#S3.SS1.SSS3.p1).
- **可见性**：warm; no unseen-item protocol is defined. Figure 4 groups test items by popularity (e.g. [0, 5) interactions on Office), which are low-frequency rather than strictly unseen; the inductive no-retraining claim is not separately tested.
  - 出处：Cold-start groups by popularity, inductive capability without a dedicated unseen-item test: [S3.SS4.SSS3.p1](https://arxiv.org/html/2210.12316v2#S3.SS4.SSS3.p1) and [S3.SS2.p3](https://arxiv.org/html/2210.12316v2#S3.SS2.p3).
- **SID 规格**：OPQ codes over item text embeddings, written as (M=32) x (D=256) PQ indices in the implementation; the method section uses D for the number of code sets and M for the centroids per set, so the two notations do not state the same split unambiguously. The paper argues that K-means-trained OPQ tends to give near-uniform code distributions, which keeps collisions low; a rule for items sharing a code: not reported. Downstream domains re-train PQ centroids with a permutation-based code-embedding alignment.
  - 出处：(M=32) x (D=256) PQ indices: [S3.SS1.SSS4.p1](https://arxiv.org/html/2210.12316v2#S3.SS1.SSS4.p1); D sets of M centroids in the method: [S2.SS2.SSS1.p3](https://arxiv.org/html/2210.12316v2#S2.SS2.SSS1.p3); uniform code distribution argument: [S2.SS2.SSS3.p1](https://arxiv.org/html/2210.12316v2#S2.SS2.SSS3.p1); domain re-training of centroids: [S2.SS4.SSS1.p2](https://arxiv.org/html/2210.12316v2#S2.SS4.SSS1.p2).
- **推理预算**：n/a for generation (a Transformer sequence encoder scores items through pooled code embeddings; implemented with Faiss and RecBole). Hardware, inference batch size, and latency: not reported.
  - 出处：Discriminative ranking with Faiss and RecBole: [S3.SS1.SSS4.p1](https://arxiv.org/html/2210.12316v2#S3.SS1.SSS4.p1).
- **结果来源**：Table 2 (cross-domain and cross-platform comparison with ID, text, and transferable baselines); Table 3 (ablations); Figure 4 (popularity groups).
  - 出处：Main: [S3.T2](https://arxiv.org/html/2210.12316v2#S3.T2); ablation: [S3.T3](https://arxiv.org/html/2210.12316v2#S3.T3); cold-start groups: [S3.F4](https://arxiv.org/html/2210.12316v2#S3.F4).

</details>

- 主实验：在跨领域和跨平台设置下，VQ-Rec 在六个下游数据集上都是最好或第二好（Table 2）。
- 消融：不微调预训练模型，效果大幅下降；去掉预训练，所有测试数据集上的结果也都下降（Sec. 3.3，Table 3）。
- 热度分组：在每个物品热度分组中，VQ-Rec 都好于 SASRec（Sec. 3.4.3，Fig. 4）。

  > "VQ-Rec has better performance than SASRec in all groups, especially in cold-start groups."（Sec. 3.4.3）（各组都好于 SASRec，冷启动组尤其明显。）

---

### 4. 局限与分析

**Our analysis.**

- ActionPiece 从同类的 `OPQ` 码出发，但把码合并成依赖上下文的 token，用 `Enc-Dec` 生成器生成；VQ-Rec 用 `Encoder` 给物品打分（`Scoring`）。
- UTGRec 也面向多领域迁移（`Multi-Dom`），但用 `Tree` 编号器替代乘积量化，用 `Beam` 解码。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["VQ-Rec"]
    P -->|successor| A["ActionPiece"]
    P -->|successor| B["LC-Rec"]
    P -->|alternative| C["UTGRec"]
```

- **后续工作** · [ActionPiece](actionpiece.md): ActionPiece later follows VQ-Rec in quantizing sentence embeddings with OPQ into unordered codes and merges them into context-dependent tokens for generation.
  - 出处：Evidence is from the later ActionPiece paper, Appendix F: https://arxiv.org/html/2502.13581v3#A6.I1.i3.p1; VQ-Rec is a Table 4 baseline: https://arxiv.org/html/2502.13581v3#S3.T4.
- **后续工作** · [LC-Rec](lc-rec.md): LC-Rec later borrows VQ-Rec's idea of learned discrete indices for items and builds RQ indices for LLM tuning.
  - 出处：Evidence is from the later LC-Rec paper, Section 3.2.1: https://arxiv.org/html/2311.09049v4#S3.SS2.SSS1.p1 and https://arxiv.org/html/2311.09049v4#S3.SS2.SSS1.p4.
- **替代方案** · [UTGRec](utgrec.md): UTGRec later compares against VQ-Rec for cross-domain transfer and replaces PQ codes with a universal tree tokenizer for generative recommendation.
  - 出处：Evidence is from the later UTGRec paper: content-based baselines and Table 2: https://arxiv.org/html/2504.04405v3#S3.SS1.SSS2.p11 and https://arxiv.org/html/2504.04405v3#S3.T2.

[查看同格全部论文](../../../README.zh.md#vi--tokenization)
