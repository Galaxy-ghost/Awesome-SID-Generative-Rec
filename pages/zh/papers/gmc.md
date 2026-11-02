# GMC

| **题目** | *Generative Multi-Target Cross-Domain Recommendation* |
| :-- | :-- |
| **作者** | Jin et al. |
| **会议** | arXiv’25 |
| **问题与阶段** | `VI. 泛化` · `Tokenization` |
| **链接** | [论文](https://arxiv.org/abs/2507.12871) · [矩阵](../../../README.zh.md#vi--tokenization) · [English](../../papers/gmc.md) |
| **阅读级别** | 阅读笔记（第 2 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Cross-Dom"] --> T["Tokenization<br/>Unified RQ"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> GMC 用域感知对比损失分配跨域共享 SID，并在多个域上训练单一序列到序列生成器，不依赖域间重叠的用户或物品。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | VI. 泛化：Does it still work for new items, new domains, and shifting interests? |
| 核心贡献 | GMC 用域感知对比损失分配跨域共享 SID，并在多个域上训练单一序列到序列生成器，不依赖域间重叠的用户或物品。 |
| 主要改动阶段 | Tokenization |
| 局限 | 语义 ID（Semantic ID，SID）只来自文本嵌入，协同信号只能通过生成器的训练序列进入模型（Sec. 3）。 |

---

### 1. 为什么重要

现有多目标跨域推荐（MTCDR）方法依赖领域之间共享的用户或物品，而无重叠的场景没有这些（Abstract）。基于可跨域共享的语义表示的方法，往往需要大量辅助数据做预训练（Abstract）。

> "The core idea of GMC is to leverage semantically quantized discrete item identifiers as a medium for integrating multi-domain knowledge within a unified generative model."（Abstract）（以语义量化的离散物品标识为媒介，在一个生成模型里整合多领域知识。）

---

### 2. 方法

![GMC architecture diagram](../../../architectures/gmc.png)

```mermaid
flowchart LR
    A("各领域物品文本") --> B["LLM 嵌入"]
    B --> C["残差量化"]
    L1{{"领域感知对比损失"}}:::key -.-> C
    C --> D("共享 SID")
    D --> E["统一生成器"]
    E --> F["领域 LoRA，其余冻结"]:::key
    F --> G("各领域的推荐")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 学习语义标识

GMC 用残差向量量化把 LLM 文本嵌入变成各领域共享的 SID（Sec. 3）。这一步还加了一个领域感知的对比损失（Sec. 3.3，Eq. 6）。

> "Specifically, since items within the same domain are generally more similar to each other than items from different domains, we introduce a novel domain-aware contrastive loss that brings quantized embeddings of intra-domain items closer together."（Sec. 1）（同领域物品通常更相似，所以用对比损失拉近同领域物品的量化嵌入。）

#### 领域专属微调

统一训练之后，每个领域得到自己的 LoRA 模块（Sec. 1，Sec. 3.5）。

> "Specifically, we incorporate domain-specific LoRA modules (Hu et al., 2022) into the unified recommender and update the corresponding LoRA parameters using domain-specific data, while freezing all other parameters of the unified model."（Sec. 1）（冻结统一模型，只用领域数据更新对应的 LoRA 参数。）

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Multi-target cross-domain task on five Amazon 2018 Reviews subsets: Scientific, Pantry, Instruments, Arts, Office. Items without titles are removed and 5-core filtering is applied to users and items; sequences capped at 20 items. Sizes (users / items): 8,317 / 4,344; 13,073 / 4,897; 24,772 / 9,922; 45,141 / 20,956; 86,554 / 25,847.
  - 出处：Five Amazon subsets, title filter, 5-core, length 20: [S5.SS1.SSS1.p1](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS1.p1); statistics: [S5.T2](https://arxiv.org/html/2507.12871v3#S5.T2).
- **切分**：Per-user leave-one-out: last item for test, second latest for validation, the rest for training; results reported per domain and as a user-weighted average.
  - 出处：Leave-one-out allocation: [S5.SS1.SSS3.p1](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS3.p1).
- **候选集**：full catalog (the target item is ranked over the entire item set).
  - 出处：Ranking over the entire item set: [S5.SS1.SSS3.p1](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS3.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Standard split with no unseen-item protocol: [S5.SS1.SSS3.p1](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS3.p1).
- **SID 规格**：4-level RQ-VAE x 256 codewords (dimension 32) over LLaMA-3.1-8B text embeddings (D=4,096), with a codebook shared across domains and a domain-aware contrastive loss; first-level codes separate domains and deeper levels are shared. Collision handling: not reported.
  - 出处：L=4 x N=256, d=32, LLaMA-3.1 4,096-dimensional embeddings, shared codebook across domains: [S5.SS1.SSS4.p1](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS4.p1) and [S5.SS4.SSS1.p2](https://arxiv.org/html/2507.12871v3#S5.SS4.SSS1.p2); no collision rule found.
- **推理预算**：Beam size 20 for item generation; T5-small backbone with domain-specific LoRA. Recall and NDCG at K=5 and 10. Hardware, inference batch size, and latency: not reported.
  - 出处：Beam size 20: [S5.SS1.SSS4.p2](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS4.p2); T5-small backbone: [S5.SS1.SSS4.p2](https://arxiv.org/html/2507.12871v3#S5.SS1.SSS4.p2).
- **结果来源**：Table 3 (five domains and user-weighted average versus ID, ID-text, pre-training, and generative baselines); Table 4 (ablations); Figures 3-5 (code sharing, code similarity, multi-domain settings).
  - 出处：Main: [S5.T3](https://arxiv.org/html/2507.12871v3#S5.T3); ablation: [S5.T4](https://arxiv.org/html/2507.12871v3#S5.T4); code analysis: [S5.F3](https://arxiv.org/html/2507.12871v3#S5.F3) and [S5.F4](https://arxiv.org/html/2507.12871v3#S5.F4); domain settings: [S5.F5](https://arxiv.org/html/2507.12871v3#S5.F5).

</details>

- 主实验：在五个公开数据集上，GMC 好于多种基线（Abstract）。

---

### 4. 局限与分析

**Our analysis.**

- 对比损失把同一领域的物品拉到一起。由此推断，它和跨领域共享码之间存在权衡。
- VQ-Rec 也做跨域迁移，在 `Encoder` 上用 `OPQ` 码做 `Scoring`；GMC 用 `Enc-Dec` 生成器生成 `Unified RQ` 码。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["GMC"]
    P -->|competitor| A["TIGER"]
    P -->|competitor| B["VQ-Rec"]
    P -->|competitor| C["CID"]
    P -->|competitor| D["IDGenRec"]
```

- **同期对比** · [TIGER](tiger.md): TIGER learns one-domain RQ-VAE identifiers; GMC learns a domain-shared codebook with a domain-aware contrastive loss and adds domain-specific LoRA tuning to a unified generator.
  - 出处：GMC v3, generative baselines: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i2.p1; Table 1 comparison: https://arxiv.org/html/2507.12871v3#S3.T1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.
- **同期对比** · [VQ-Rec](vq-rec.md): VQ-Rec transfers across domains through vector-quantized codes for a discriminative model, pre-trained here on the five target domains; GMC generates shared semantic identifiers.
  - 出处：GMC v3, pre-training baselines with the adapted setting: https://arxiv.org/html/2507.12871v3#S5.I1.i3.p1 and https://arxiv.org/html/2507.12871v3#S5.I1.i3.I1.i2.p1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.
- **同期对比** · [CID](cid.md): P5-CID builds collaborative identifiers by spectral clustering within a domain; GMC builds semantic identifiers shared across domains.
  - 出处：GMC v3, generative baselines: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i1.p1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.
- **同期对比** · [IDGenRec](idgenrec.md): IDGenRec learns textual IDs with an ID generator; GMC quantizes LLM embeddings into codebook IDs shared across domains.
  - 出处：GMC v3, generative baselines: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i3.p1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.

[查看同格全部论文](../../../README.zh.md#vi--tokenization)
