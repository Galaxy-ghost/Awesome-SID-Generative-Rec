## At a Glance

Limitation: 物品索引依赖 GPT-5 改写的描述，推理数据来自外部 LLM，复现要能用到这些模型（Sec. 4.1，Sec. 4.2）。

### 1. 为什么重要

作者指出，LLM 做生成式推理推荐有两个障碍：文本语义和协同过滤信号之间有差距；用户反馈稀疏且带随机性（Abstract）。GREAM 同时处理这两点，并在推理模式之外保留一个快速的直接模式。

> "GREAM natively supports two complementary inference modes: Direct Sequence Recommendation for high-throughput, low-latency deployment, and Sequential Reasoning Recommendation that first emits an interpretable reasoning chain for causal transparency."（Abstract）（两种推理模式：高吞吐低延迟的直接推荐，和先输出推理链的推理推荐。）

### 2. 方法

```mermaid
flowchart LR
    A[物品文本与评论] --> B[改写后的描述]
    B --> C[RQ-KMeans 索引]
    C --> D[对齐 SFT]
    D --> E[推理课程]
    E --> F[SRPO]
```

#### 协同-语义对齐

对每个物品，GPT-5 把标题、官方描述和精选评论改写成一段描述（Sec. 4.1）。RQ-KMeans 把这段描述的嵌入量化成物品索引（Sec. 4.1，Eq. 4-5）。辅助任务让语言表示落到交互语义上（Abstract）。

#### 推理课程激活

外部 LLM 从推荐结果反向推理，生成结构化的推理路径（Sec. 4.2）。

> "This process guides the model through a structured, five-stage logical chain—behavioral evidence extraction, latent preference modeling, intent inference, recommendation formulation, and denoised sequence rewriting"（Sec. 1）（五步推理链：提取行为证据、建模潜在偏好、推断意图、形成推荐、去噪改写序列。）

#### SRPO

稀疏正则组策略优化（SRPO）用残差敏感的可验证奖励和带奖励校准的组优势估计，在成功样本稀少时也能优化（Abstract）。

> "In the early stages of generative recommendation, exactly correct generations are typically rare."（Sec. 5.2）（训练初期完全正确的生成很少。）

### 3. 实验发现

- 主实验：在三个公开基准上，GREAM 在直接模式和推理模式下都稳定好于生成式基线和 LLM 基线（Abstract）。
- 索引质量：在增强后的嵌入上做 RQ-KMeans，索引冲突率约降低 50%（Sec. 4.1）。
- 推理的扩展性：推理激活阶段的合成思维链数据越多，Pass@Avg 在 10^16–10^19 训练 FLOPs 范围内几乎线性上升（Sec. 6.4，Fig. 1）。

### 4. 局限与分析

**Our analysis.**

- 推理模式要先输出推理链，再输出物品索引。由此推断，它的延迟高于直接模式。
- LC-Rec 和 EAGER-LLM 用 `Multi-task NTP` 训练 LLM；GREAM 加了一个强化学习阶段（`NTP → RL`）。
