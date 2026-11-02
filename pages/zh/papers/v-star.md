# V-STAR

*Spend Search Where It Pays: Value-Guided Structured Sampling and Optimization for Generative Recommendation* — Jiang et al. · KDD’26

`IV. 实用目标` · `Training` · [论文](https://arxiv.org/abs/2602.10699) · [矩阵](../../../README.zh.md#iv--training) · [English](../../papers/v-star.md)

阅读级别：阅读笔记（第 2 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text†"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → RL"] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> V-STAR 在强化学习采样期间用价值引导解码加深高价值前缀的搜索，并用 Sibling-GRPO 计算兄弟分支相对优势，替代似然驱动的束搜索。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | IV. 实用目标：Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| 核心贡献 | V-STAR 在强化学习采样期间用价值引导解码加深高价值前缀的搜索，并用 Sibling-GRPO 计算兄弟分支相对优势，替代似然驱动的束搜索。 |
| 主要改动阶段 | Training |

### 1. 为什么重要

对生成式推荐器做强化学习微调时，候选用束搜索这类按似然驱动的解码来采样（Abstract）。作者指出这样做的两个问题。低概率分支里的高奖励物品会被过早剪掉；共享高概率前缀的候选奖励相关，削弱了强化学习的比较信号。加大束宽也解决不了，多出的算力大多花在重复的高概率候选上（Sec. 1）。V-STAR 改的是强化学习候选的构造方式和优势的计算方式。

> "Our V-STAR primarily focuses on training-time improvement."（Sec. 4.4）（V-STAR 主要改进训练阶段。）

### 2. 方法

![V-STAR architecture diagram](../../../architectures/v-star.png)

```mermaid
flowchart LR
    A[用户上下文] --> B[策略]
    B --> C[SID 前缀树]
    C --> D[价值引导扩展]
    D --> E[候选集]
    E --> F[Sibling-GRPO]
    F --> B
```

#### 价值头

价值头读取策略模型在每个语义 ID（Semantic ID，SID）前缀上的隐藏状态，预测它的价值（Sec. 4.1）。训练它所用的稠密语义回报，来自冻结文本编码器算出的物品嵌入。

#### 价值引导的高效解码

VED 把 SID 解码看作在固定算力预算下、在前缀树上构建候选集（Sec. 4.2）。先用按概率引导的束初始化前缀树。每个节点的优先级结合它的预测价值和策略熵；优先级高于同层平均值的节点新增一个子节点（Eq. 11）。新子节点从尚未展开的合法子节点中按归一化的策略概率采样。

> "We develop Value-Guided Efficient Decoding (VED) for budgeted candidate construction by allocating decoding compute to high-value and high-ambiguity nodes."（Sec. 1）（VED 把解码算力分给价值高、不确定性高的节点，在预算内构建候选。）

#### Sibling-GRPO

Sibling-GRPO 把每个父前缀下的子节点分成一组（Sec. 4.3）。每个子节点的分数是其后代候选的平均奖励，优势在兄弟节点之间归一化（Eq. 17）。

> "We introduce Sibling-GRPO, a tree-structured objective that uses sibling groups to mitigate advantage compression under correlated candidates."（Sec. 1）（用兄弟组缓解候选相关时的优势压缩。）

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2023 Industrial and Scientific and Office Products, preprocessed following MiniOneRec (Kong et al., 2025b); online: WeChat Channels advertising traffic. Filtering and sizes: not restated.
  - 出处：Datasets and MiniOneRec preprocessing: [S5.SS1.p1](https://arxiv.org/html/2602.10699v2#S5.SS1.p1).
- **切分**：Chronological next-item prediction following MiniOneRec's preprocessing (allocation not restated). Online: 5-day A/B test on 5% of live requests, against beam search plus GRPO.
  - 出处：Chronological next-item protocol: [S5.SS1.p1](https://arxiv.org/html/2602.10699v2#S5.SS1.p1); online A/B: [S5.SS3.p1](https://arxiv.org/html/2602.10699v2#S5.SS3.p1).
- **候选集**：not reported (full catalog versus sampled); generation is restricted to valid catalog SIDs, with HR and NDCG at 3, 5, 10.
  - 出处：Valid-SID constraint and metrics: [S5.SS1.p1](https://arxiv.org/html/2602.10699v2#S5.SS1.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：No unseen-item protocol: [S5.SS1.p1](https://arxiv.org/html/2602.10699v2#S5.SS1.p1).
- **SID 规格**：3-level RQ-VAE semantic IDs (citing TIGER); the paper states each item is represented by a unique fixed-length SID. Codebook size and the mechanism that ensures uniqueness: not reported.
  - 出处：3-level RQ-VAE SIDs: [S5.SS1.p1](https://arxiv.org/html/2602.10699v2#S5.SS1.p1); each item has a unique fixed-length SID: [S3.SS1.p1](https://arxiv.org/html/2602.10699v2#S3.SS1.p1).
- **推理预算**：Training rollouts use value-guided decoding (VED) with 16 candidates per query and an 8-wide beam to initialize the prefix tree; at inference, standard beam search is the default decoder (width not reported). Qwen2.5-1.5B on 8 GPUs; inference batch size and latency: not reported.
  - 出处：VED budget, beam settings, inference decoder: [S5.SS1.p2](https://arxiv.org/html/2602.10699v2#S5.SS1.p2).
- **结果来源**：Table 1 (Industrial and Office versus sequential, generative, and RL baselines including MiniOneRec); Tables 2-4 (decoding, expansion rules, training objective); Table 6 (candidate diversity and max reward); Section 5.3 (online GMV +1.23%).
  - 出处：Main: [S4.T1](https://arxiv.org/html/2602.10699v2#S4.T1); ablations: [S5.T2](https://arxiv.org/html/2602.10699v2#S5.T2), [S5.T3](https://arxiv.org/html/2602.10699v2#S5.T3), [S5.T4](https://arxiv.org/html/2602.10699v2#S5.T4); diversity: [S5.T6](https://arxiv.org/html/2602.10699v2#S5.T6); online: [S5.SS3.p1](https://arxiv.org/html/2602.10699v2#S5.SS3.p1).

</details>

- 解码预算：在相同的训练期解码预算下，VED 在所测指标上好于束搜索（Sec. 5.5，Fig. 4）。预算按候选构建中模型计算的 token 数计，不是端到端延迟。
- 训练目标：GRPO 加 Sibling-GRPO 在所试目标中 NDCG 和 HR 最高（Sec. 5.4，Table 4）。

### 4. 局限与分析

**Our analysis.**

- MiniOneRec 用同样的 `RQ-VAE` SID、`Dec-Only` 生成器和 `NTP → RL` 训练；V-STAR 只改强化学习候选的采样方式和优势的计算方式。

### 5. 相关工作

```mermaid
flowchart LR
    P["V-STAR"]
    P -->|competitor| A["MiniOneRec"]
    P -->|competitor| B["TIGER"]
    P -->|competitor| C["LC-Rec"]
    P -->|alternative| D["OneRec"]
```

- **同期对比** · [MiniOneRec](minionerec.md): MiniOneRec samples RL candidates by beam search and applies GRPO; V-STAR replaces candidate construction with value-guided prefix expansion and uses sibling-group advantages, while keeping MiniOneRec's preprocessing.
  - 出处：V-STAR v2, preprocessing follows Kong et al. (2025b): https://arxiv.org/html/2602.10699v2#S5.SS1.p1; strongest RL baseline: https://arxiv.org/html/2602.10699v2#S5.SS2.p1; Table 1: https://arxiv.org/html/2602.10699v2#S4.T1.
- **同期对比** · [TIGER](tiger.md): TIGER's SIDs and beam search are the base; V-STAR targets the pruning of high-reward low-probability prefixes during RL sampling.
  - 出处：V-STAR v2, SID-based baselines: https://arxiv.org/html/2602.10699v2#S5.SS2.p1; Table 1: https://arxiv.org/html/2602.10699v2#S4.T1.
- **同期对比** · [LC-Rec](lc-rec.md): LC-Rec is an SID-based LLM recommender without RL; V-STAR adds value-guided RL on top of SFT.
  - 出处：V-STAR v2, baselines: https://arxiv.org/html/2602.10699v2#S5.SS2.p1; Table 1: https://arxiv.org/html/2602.10699v2#S4.T1.
- **替代方案** · [OneRec](onerec.md): OneRec applies preference alignment with beam-sampled responses; V-STAR argues that probability-based beam sampling under-explores high-reward items.
  - 出处：V-STAR v2, Sections 1 and 2.3 cite OneRec: https://arxiv.org/html/2602.10699v2#S1.p1 and https://arxiv.org/html/2602.10699v2#S2.SS3.p1.

[查看同格全部论文](../../../README.zh.md#iv--training)
