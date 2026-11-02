## At a Glance

Limitation: 扩展性实验只测了模型变大时的训练损失和评估损失，没有测排序指标（Sec. 5.2，Fig. 1）。

### 1. 为什么重要

用语义 ID（Semantic ID，SID）序列替代嵌入表的工业生成式推荐器大多不公开（Abstract）。作者想知道两件事：扩展定律在公开基准上是否成立；要达到有竞争力的效果，最少需要怎样的后训练流程。

> "Yet most industrial deployments remain proprietary, leaving two fundamental questions open: (1) Do the expected scaling laws hold on public benchmarks? (2) What is the minimal post-training recipe that enables competitive performance?"（Abstract）（工业部署大多不公开，留下两个问题：扩展定律在公开基准上是否成立；最小的后训练配方是什么。）

MiniOneRec 的回答是一个开源框架，覆盖 SID 构建、监督微调（SFT）和强化学习（RL），并公开代码、训练流程和检查点（Sec. 1）。

### 2. 方法

```mermaid
flowchart LR
    A[物品文本] --> B[RQ-VAE]
    B --> C[加入词表的 SID]
    C --> D[SFT]
    D --> E[GRPO]
    E --> F[约束束搜索]
    F --> G[下一物品]
```

#### 物品编号

冻结的文本编码器嵌入物品标题和描述，RQ-VAE 把嵌入量化成层级 SID（Sec. 3.2）。

> "The codebooks, the encoder and the decoder are trained jointly, while the text encoder remains frozen."（Sec. 3.2）（码本、编码器、解码器联合训练，文本编码器冻结。）

#### 全流程 SID 对齐

SID token 加进 LLM 的词表。下一物品预测和辅助对齐任务（如标题与 SID 互相映射）在 SFT 和 RL 两个阶段都一起优化（Sec. 3.3，Sec. 6）。

#### 强化偏好优化

RL 阶段用 GRPO，以约束束搜索作采样器，生成的物品都合法（Sec. 3.4.1）。默认奖励把二元的正确性规则和惩罚困难负例的排序项结合起来（Sec. 3.4.2）。

> "The mixed reward discussed combines binary correctness with a soft ranking term, helping the LLM tell hard negatives apart."（Sec. 3.4.2）（混合奖励结合二元正确性和软排序项，帮 LLM 区分困难负例。）

### 3. 实验发现

- 扩展性：Qwen 骨干从 0.5B 增到 7B 参数，训练损失和评估损失都下降（Abstract，Sec. 5.2）。
- 对齐：在各对齐变体中，全流程保持 SID 对齐的变体在每个指标上都最高（Sec. 5.5.1，Fig. 4a）。
- 跨域：只在 Industrial 上训练的模型，不再调优，直接用到没见过的 Office 领域（Sec. 5.4，Table 2）。
- 世界知识：论文比较了预训练骨干和随机初始化骨干（Sec. 5.6，Table 3）。

### 4. 局限与分析

**Our analysis.**

- LC-Rec 也用辅助任务把 `Dec-Only` LLM 对齐到 `RQ-VAE` SID（`Multi-task NTP`）；MiniOneRec 在后面的 RL 阶段继续保留这些任务（`NTP → RL`）。
- OneRec 用 `R-KM` 从多模态和协同信号（`MM+CF`）构建 SID；MiniOneRec 只用文本（`Text`）和 `RQ-VAE`。
