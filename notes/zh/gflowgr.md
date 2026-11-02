## At a Glance

Key Findings: 在淘宝生产数据上，GFlowGR 的 H@20 为 0.444、N@20 为 0.452，SFT 为 0.358 和 0.371；15 天在线 A/B 测试中总收入提升 +0.43%（Sec. 5，Table 7）。
Limitation: 奖励模型从日志里的用户信号学习物品效用，微调目标的好坏取决于这些日志（Sec. 3.2）。

### 1. 为什么重要

生成式推荐（GR）模型通常用监督微调（SFT）的下一 token 损失或 DPO 类目标来微调（Abstract）。作者指出，这些目标只预测一个真实物品，并把所有交互看得一样重要（Abstract）。

> "To address these challenges, we reformulate GR as a sequential set-generation problem and propose GFlowGR, a GFlowNet-based fine-tuning framework that explicitly aligns generation probabilities with item-level utilities."（Abstract）（把 GR 看作序列式集合生成，用 GFlowNet 让生成概率和物品效用对齐。）

### 2. 方法

```mermaid
flowchart LR
    A[用户历史] --> B[轨迹采样器]
    B --> C[轨迹]
    C --> D[奖励模型]
    D --> E[GFlowNet 损失]
    E --> F[生成器]
```

#### 轨迹采样器

轨迹集合由四种方法构造（Sec. 3.1）。作者指出，随机样本会让训练不稳，也偏离模型自身的学习动态（Sec. 3.1）。

> "There are four methods for constructing the trajectory set: interaction log, random sampling, CM-based sampling, and on-policy sampling."（Sec. 3.1）（四种方法：交互日志、随机采样、基于 CM 的采样、在策略采样。）

#### 奖励模型

一个感知行为的奖励模型从多种用户信号中量化物品效用（Sec. 1，Sec. 3.2）。

#### GFlowNet 目标

论文从流匹配原理推出细致平衡（DB）和轨迹平衡（TB）两种目标（Sec. 2）。

### 3. 实验发现

- 公开数据：论文在两种 GR 骨干上评估 GFlowGR（Abstract）。
- 生产数据：GRPO 的 H@20 = 0.427，N@20 = 0.408（Sec. 5，Table 7）。

  > "The results show that GFlowGR achieves H@20 of 0.444 and N@20 of 0.452, substantially outperforming SFT (0.358/0.371) and GRPO (0.427/0.408), mirroring the conclusions on public datasets."（Sec. 5）（GFlowGR 明显好于 SFT 和 GRPO，与公开数据集的结论一致。）

- 在线测试：A/B 测试用了 10% 的流量，按 50/50 分组（Sec. 5）。
- 部署：自 2025 年 5 月起，GFlowGR 用于训练淘宝搜索广告的 GR 模型，覆盖手机淘宝、闲鱼和淘宝网页版（Sec. 5）。

### 4. 局限与分析

**Our analysis.**

- GFlowGR 只改微调目标。由此推断，它的收益可以叠加在编号器的选择之上，而不是替代编号器。
- OneRec 用 `NTP → DPO` 对齐生成器；GFlowGR 在下一 token 损失上加 GFlowNet 损失（`NTP + Aux.`）。
