# ColaRec

*Content-based collaborative generation for recommender systems* — Wang et al. · CIKM’24

`I. 信息量` · `Backbone` · [论文](https://arxiv.org/abs/2403.18480) · [代码](https://github.com/Junewang0614/ColaRec) · [矩阵](../../../README.zh.md#i--backbone) · [English](../../papers/colarec.md)

阅读级别：阅读笔记（第 2 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>H-KM"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP + Ctr."] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class B main
```

- `H-KM`: Hierarchical k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> ColaRec 从预训练协同过滤模型构造生成式标识，结合物品索引任务与对比损失对齐协同与内容空间，从交互物品内容生成目标 ID。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | ColaRec 从预训练协同过滤模型构造生成式标识，结合物品索引任务与对比损失对齐协同与内容空间，从交互物品内容生成目标 ID。 |
| 主要改动阶段 | Backbone |
| 局限 | 生成式标识（GID）来自离线的 LightGCN 嵌入和聚类，没有交互的物品就没有可聚类的协同表示（Sec. 4.2）。 |

### 1. 为什么重要

现有基于 LLM 的方法会融合内容和协同信号，但依赖文本生成；作者认为这和推荐任务并不完全对得上（Abstract）。ColaRec 改用为推荐定制的序列到序列模型，直接解码物品标识（Abstract）。

> "To model collaborative signals, the GIDs are constructed from a pretrained collaborative filtering model, and the user is represented as the content aggregation of interacted items."（Abstract）（GID 由预训练协同过滤模型构建，用户用交互过的物品内容聚合表示。）

### 2. 方法

![ColaRec architecture diagram](../../../architectures/colarec.png)

```mermaid
flowchart LR
    A[交互数据] --> B[LightGCN]
    B --> C[约束 K-means]
    C --> D[GID]
    E[物品内容] --> F[编码器-解码器]
    D --> F
    F --> G[下一物品 GID]
```

#### 构建生成式标识

ColaRec 对预训练 LightGCN 得到的物品表示逐层做约束 K-means（Sec. 4.2）。

> "Specifically, we first extract item representations from a pretrained LightGCN model. Then the constrained K-means algorithm is called hierarchically based on the item representations."（Sec. 4.2）（先取 LightGCN 物品表示，再逐层做约束 K-means。）

#### 物品索引任务

索引任务把物品的文本和与它交互过的用户映射到它的 GID（Sec. 4.4，Eq. 7）。它和推荐任务共用同一个编码器-解码器（Sec. 4.4）。

#### 训练目标

推荐损失、索引损失、带一个采样负例的 BPR 损失和加权对比损失一起训练（Sec. 4.5，Eq. 11）。

> "The idea is that items with similar GIDs should also be similar in the content-based semantic space."（Sec. 4.5）（GID 相近的物品，内容语义也应相近。）

#### 推理

约束束搜索只允许当前前缀下合法的 token（Sec. 4.5）。

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Product Reviews: Beauty, Sports and Outdoors, Cell Phones and Accessories (Phone); Food.com Recipe. Users and items with fewer than 5 interactions are filtered. Sizes (users / items / interactions): Beauty 22,363 / 12,101 / 198,502; Sports 35,598 / 18,357 / 296,337; Phone 27,879 / 10,429 / 194,439; Recipe 17,813 / 41,240 / 555,618.
  - 出处：Datasets and 5-interaction filter: [S5.SS1.p1](https://arxiv.org/html/2403.18480v2#S5.SS1.p1); statistics: [S4.T1](https://arxiv.org/html/2403.18480v2#S4.T1).
- **切分**：General recommendation, not sequential: each user's interactions are randomly split 8:1:1 into training, validation, and test. Three runs are averaged.
  - 出处：Random 8:1:1 per-user split for general (non-sequential) recommendation: [S5.SS2.p1](https://arxiv.org/html/2403.18480v2#S5.SS2.p1).
- **候选集**：full catalog
  - 出处：Candidate set is the whole item set: [S5.SS2.p1](https://arxiv.org/html/2403.18480v2#S5.SS2.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Random interaction split with no cold-start experiment: [S5.SS2.p1](https://arxiv.org/html/2403.18480v2#S5.SS2.p1); long-tail users are analyzed separately: [S5.T3](https://arxiv.org/html/2403.18480v2#S5.T3).
- **SID 规格**：GID length l=3 from hierarchical constrained K-means over pretrained LightGCN item embeddings, K=32 clusters per level (48 for Recipe). Collisions are avoided by construction: clusters hold at most K^(l-t) items and leaf positions are assigned randomly, so each item has a unique GID.
  - 出处：Constrained hierarchical K-means over LightGCN embeddings, random leaf assignment, one unique GID per item: [S4.SS2.p1](https://arxiv.org/html/2403.18480v2#S4.SS2.p1) and [S4.SS2.p2](https://arxiv.org/html/2403.18480v2#S4.SS2.p2); l=3, K=32 (Recipe 48): [S5.SS4.p1](https://arxiv.org/html/2403.18480v2#S5.SS4.p1).
- **推理预算**：Constrained beam search over valid GID prefixes; numerical beam width not reported. T5-small backbone. Recall and NDCG at n=5 and 10 (Table 2). Hardware, inference batch size, and latency: not reported.
  - 出处：Constrained beam search: [S4.SS5.p5](https://arxiv.org/html/2403.18480v2#S4.SS5.p5); no numerical width found in Section 5.
- **结果来源**：Table 2 (four datasets; mean of three runs); Table 3 (long-tail users); Table 4 (multi-task ablation and GID types); Figures 4-5 (GID length and cluster number).
  - 出处：Main: [S4.T2](https://arxiv.org/html/2403.18480v2#S4.T2); long-tail users: [S5.T3](https://arxiv.org/html/2403.18480v2#S5.T3); ablation and GID types: [S5.T4](https://arxiv.org/html/2403.18480v2#S5.T4); GID length and K: [S5.SS7.SSS2.p1](https://arxiv.org/html/2403.18480v2#S5.SS7.SSS2.p1) and [S5.SS7.SSS2.p2](https://arxiv.org/html/2403.18480v2#S5.SS7.SSS2.p2).

</details>

- 主实验：ColaRec 在四个基准数据集上好于各基线（Abstract，Table 2）。
- 消融：Table 4 分别去掉文本内容、索引任务、BPR 损失或对比损失，并把 GID 换成另外三种标识（Table 4）。

### 4. 局限与分析

**Our analysis.**

- 对比损失把内容表示拉向 GID 的结构。由此推断，内容相似度会被协同聚类重新塑形，聚类有噪声的物品可能受损。
- SEATER 也从 `CF` 输入构建树状标识（`Tree-Clus.`）；ColaRec 在输入里加了物品内容（`Text+CF`）。

### 5. 相关工作

```mermaid
flowchart LR
    P["ColaRec"]
    P -->|competitor| A["TIGER"]
    P -->|competitor| B["LC-Rec"]
    P -->|alternative| C["CID"]
    P -->|alternative| D["SEATER"]
```

- **同期对比** · [TIGER](tiger.md): TIGER builds content-only RQ-VAE identifiers; ColaRec builds collaborative GIDs from LightGCN embeddings and aligns them with item content through item-item indexing.
  - 出处：ColaRec v2, Section 5.3 baselines: https://arxiv.org/html/2403.18480v2#S5.SS3.p1 and https://arxiv.org/html/2403.18480v2#S5.I2.i8.p1 (adapted without sequential order); Table 2: https://arxiv.org/html/2403.18480v2#S4.T2.
- **同期对比** · [LC-Rec](lc-rec.md): LC-Rec learns TIGER-style indices and aligns an LLM through language tasks; ColaRec uses a T5-small generator with collaborative GIDs and a contrastive ranking loss.
  - 出处：ColaRec v2, Section 5.3 baselines: https://arxiv.org/html/2403.18480v2#S5.I2.i9.p1; Table 2: https://arxiv.org/html/2403.18480v2#S4.T2.
- **替代方案** · [CID](cid.md): P5-CID builds collaborative IDs for prompt-based P5 models that rank a candidate list in the prompt; ColaRec generates GIDs over the whole item set.
  - 出处：ColaRec v2, Section 5.3 explains why P5-based methods including Hua et al. (2023) are excluded as baselines: https://arxiv.org/html/2403.18480v2#S5.SS3.p2; related work: https://arxiv.org/html/2403.18480v2#S2.SS2.p3.
- **替代方案** · [SEATER](seater.md): SEATER also builds tree-structured identifiers for generative recommendation; ColaRec derives its tree from collaborative LightGCN embeddings and adds content-based item-item indexing.
  - 出处：ColaRec v2, Section 1 and Section 2.2 cite SEATER among generative identifier methods: https://arxiv.org/html/2403.18480v2#S1.p3 and https://arxiv.org/html/2403.18480v2#S2.SS2.p3; not a baseline in Table 2.

[查看同格全部论文](../../../README.zh.md#i--backbone)
