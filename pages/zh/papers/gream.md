# GREAM

| **题目** | *Generative Reasoning Recommendation via LLMs* |
| :-- | :-- |
| **作者** | Hong et al. |
| **会议** | arXiv’25 |
| **问题与阶段** | `III. SID 与模型对齐` · `Training` |
| **链接** | [论文](https://arxiv.org/abs/2510.20815) · [代码](https://github.com/Indolent-Kawhi/GRRM) · [矩阵](../../../README.zh.md#iii--training) · [English](../../papers/gream.md) |
| **阅读级别** | 阅读笔记（第 2 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>RQ-KM"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → RL"] --> I["Inference<br/>Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### TL;DR

> [!NOTE]
> GREAM 结合协同-语义物品索引、思维链课程学习与 SRPO 后训练将 LLM 改造为推理推荐模型，同时支持直接生成和先推理后生成两种模式。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | III. SID 与模型对齐：Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| 核心贡献 | GREAM 结合协同-语义物品索引、思维链课程学习与 SRPO 后训练将 LLM 改造为推理推荐模型，同时支持直接生成和先推理后生成两种模式。 |
| 主要改动阶段 | Training |
| 局限 | 物品索引依赖 GPT-5 改写的描述，推理数据来自外部 LLM，复现要能用到这些模型（Sec. 4.1，Sec. 4.2）。 |

---

### 1. 为什么重要

作者指出，LLM 做生成式推理推荐有两个障碍：文本语义和协同过滤信号之间有差距；用户反馈稀疏且带随机性（Abstract）。GREAM 同时处理这两点，并在推理模式之外保留一个快速的直接模式。

> "GREAM natively supports two complementary inference modes: Direct Sequence Recommendation for high-throughput, low-latency deployment, and Sequential Reasoning Recommendation that first emits an interpretable reasoning chain for causal transparency."（Abstract）（两种推理模式：高吞吐低延迟的直接推荐，和先输出推理链的推理推荐。）

---

### 2. 方法

![GREAM architecture diagram](../../../architectures/gream.png)

```mermaid
flowchart LR
    A("标题、描述、评论") --> B["GPT-5 改写"]
    B --> C["RQ-KMeans"]
    C --> D("物品索引")
    D --> E["对齐 SFT + 辅助任务"]
    E --> F["推理课程 SFT"]
    F --> G["SRPO"]:::key
    L1{{"残差敏感的可验证奖励"}} -.-> G
    L2{{"奖励校准的组优势"}} -.-> G
    G --> H("直接模式或推理模式")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 协同-语义对齐

对每个物品，GPT-5 把标题、官方描述和精选评论改写成一段描述（Sec. 4.1）。RQ-KMeans 把这段描述的嵌入量化成物品索引（Sec. 4.1，Eq. 4-5）。辅助任务让语言表示落到交互语义上（Abstract）。

#### 推理课程激活

外部 LLM 从推荐结果反向推理，生成结构化的推理路径（Sec. 4.2）。

> "This process guides the model through a structured, five-stage logical chain—behavioral evidence extraction, latent preference modeling, intent inference, recommendation formulation, and denoised sequence rewriting"（Sec. 1）（五步推理链：提取行为证据、建模潜在偏好、推断意图、形成推荐、去噪改写序列。）

```mermaid
flowchart LR
    S1["1 行为证据"] --> S2["2 潜在偏好"] --> S3["3 意图"] --> S4["4 推荐"] --> S5["5 去噪序列"]
```

#### SRPO

稀疏正则组策略优化（SRPO）用残差敏感的可验证奖励和带奖励校准的组优势估计，在成功样本稀少时也能优化（Abstract）。

> "In the early stages of generative recommendation, exactly correct generations are typically rare."（Sec. 5.2）（训练初期完全正确的生成很少。）

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty, Sports and Outdoors, Musical Instruments, with 5-core filtering of users and items. Sizes (users / items / interactions): 22,363 / 12,101 / 198,360; 35,598 / 18,357 / 296,175; 24,733 / 9,923 / 206,153. Alignment and reasoning text is synthesized by Qwen3, GPT-5, Llama-3.1, and Gemini.
  - 出处：Datasets and 5-core: [S6.SS1.SSS1.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS1.p1); statistics: [S6.T1](https://arxiv.org/html/2510.20815v1#S6.T1).
- **切分**：Leave-one-out; the exact validation/test position allocation is not reported beyond the leave-one-out label.
  - 出处：Leave-one-out named only: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1).
- **候选集**：not reported (full catalog versus sampled evaluation candidates); direct mode reports Recall and NDCG at 5 and 10, reasoning mode reports Pass@1, 5, 10.
  - 出处：Metrics only: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Standard split with no unseen-item protocol: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1).
- **SID 规格**：RQ-KMeans indices over LLM last-hidden-state embeddings of GPT-5-enriched item text; fixed length 5 with 256 values per layer, where the fifth position is a conflict-resolution slot.
  - 出处：Length 5 with a conflict-resolution slot, 256 values per layer: [S6.SS1.SSS3.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS3.p1); RQ-KMeans over LLM embeddings of GPT-5-enriched text: [S3.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S3.SS1.SSS2.p1) and [S4.SS1.p1](https://arxiv.org/html/2510.20815v1#S4.SS1.p1).
- **推理预算**：Direct mode: beam size 20 for all generative methods. Reasoning mode: sampling with temperature 0.7 and top-p 0.9. Backbone Qwen3-4B-Instruct; experiments on a cluster of 24 NVIDIA A100 GPUs; inference batch size and latency: not reported.
  - 出处：Beam 20 and sampling settings: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1); hardware: [S6.SS1.SSS3.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS3.p1).
- **结果来源**：Table 2 (direct and reasoning modes on Beauty, Sports, Instruments versus traditional, Transformer, generative, and LLM baselines); Table 3 (alignment and RL ablations); Table 4 (data composition); Figure 3 (RL regimes on Instruments).
  - 出处：Main: [S6.T2](https://arxiv.org/html/2510.20815v1#S6.T2); ablations: [S6.T3](https://arxiv.org/html/2510.20815v1#S6.T3) and [S6.T4](https://arxiv.org/html/2510.20815v1#S6.T4); RL regimes: [S6.SS5.p2](https://arxiv.org/html/2510.20815v1#S6.SS5.p2).

</details>

- 主实验：在三个公开基准上，GREAM 在直接模式和推理模式下都稳定好于生成式基线和 LLM 基线（Abstract）。
- 索引质量：在增强后的嵌入上做 RQ-KMeans，索引冲突率约降低 50%（Sec. 4.1）。
- 推理的扩展性：推理激活阶段的合成思维链数据越多，Pass@Avg 在 10^16–10^19 训练 FLOPs 范围内几乎线性上升（Sec. 6.4，Fig. 1）。

---

### 4. 局限与分析

**Our analysis.**

- 推理模式要先输出推理链，再输出物品索引。由此推断，它的延迟高于直接模式。
- LC-Rec 和 EAGER-LLM 用 `Multi-task NTP` 训练 LLM；GREAM 加了一个强化学习阶段（`NTP → RL`）。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["GREAM"]
    P -->|competitor| A["EAGER-LLM"]
    P -->|competitor| B["LC-Rec"]
    P -->|competitor| C["TIGER"]
    P -->|competitor| D["CID"]
```

- **同期对比** · [EAGER-LLM](eager-llm.md): EAGER-LLM injects behavioral and semantic signals into a decoder-only LLM recommender; GREAM adds collaborative-semantic alignment data, reasoning curricula, and RL with a prefix-based verifiable reward.
  - 出处：GREAM v1, LLM-based baselines: https://arxiv.org/html/2510.20815v1#A2.I4.i2.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.
- **同期对比** · [LC-Rec](lc-rec.md): LC-Rec aligns LLaMA to VQ indices with language tasks; GREAM adds explicit reasoning chains and RL fine-tuning on Qwen3.
  - 出处：GREAM v1, LLM-based baselines: https://arxiv.org/html/2510.20815v1#A2.I4.i1.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.
- **同期对比** · [TIGER](tiger.md): TIGER generates RQ-VAE identifiers with a small T5; GREAM generates RQ-KMeans indices with an LLM that can reason before recommending.
  - 出处：GREAM v1, generative baselines: https://arxiv.org/html/2510.20815v1#A2.I3.i2.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.
- **同期对比** · [CID](cid.md): P5-CID uses collaborative IDs for a T5 recommender; GREAM uses semantic RQ-KMeans indices with LLM reasoning.
  - 出处：GREAM v1, generative baselines: https://arxiv.org/html/2510.20815v1#A2.I3.i1.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.

[查看同格全部论文](../../../README.zh.md#iii--training)
