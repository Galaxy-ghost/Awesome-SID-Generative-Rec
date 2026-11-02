## At a Glance

Key Findings: 在公开数据集上，Align3GR 比最强基线的 Recall@10 高 +17.8%，NDCG@10 高 +20.2%（Abstract）。

### 1. 为什么重要

把大语言模型（LLM）改造成推荐器，会遇到语义和行为两方面的错位（Abstract）。LC-Rec 等早期 LLM 推荐器用监督任务对齐物品 token。Align3GR 把 token、行为建模和偏好三个层级的对齐放在一起处理。

> "To bridge this gap, we propose Align3GR, a novel framework that unifies token-level, behavior modeling-level, and preference-level alignment."（Abstract）（把 token、行为建模、偏好三级对齐统一起来。）

### 2. 方法

```mermaid
flowchart LR
    A[用户与物品] --> B[双路 SC 编码器]
    B --> C[SCID]
    C --> D[多任务 SFT]
    D --> E[SP-DPO]
    E --> F[RF-DPO]
```

#### token 级对齐

两路语义-协同（SC）编码器配 RQ-VAE，为用户和物品都生成 SCID（Fig. 2 caption）。这些 token 加进 LLM 的词表。

> "Following previous work (Zheng et al. 2024), we first expand the LLM vocabulary to include the SCID tokens of the user and the item, thus avoiding out-of-vocabulary issues and ensuring smooth integration with autoregressive generation tasks."（Behavior Modeling-level Alignment）（先把用户和物品的 SCID token 加进词表，避免词表外问题。）

#### 行为建模级对齐

监督微调（SFT）沿用 LC-Rec 的四个任务：序列物品预测、非对称物品预测、按用户意图预测物品、个性化偏好推断（Multi-task SFT）。每个任务的提示里都有用户的 SCID token，其中一个任务要从用户 SCID 还原用户画像文本（Multi-task SFT）。

#### 偏好级对齐

自博弈 DPO（SP-DPO）分 Easy、Medium、Hard 三个阶段，阶段按层级 SCID 的前缀 n-gram 匹配划分（Preference-level Alignment）。之后的真实反馈 DPO（RF-DPO）使用标为 disliked、neutral、liked 的反馈（Preference-level Alignment）。

> "Specifically, considering the hierarchical nature of SCID, we divide progressive SP-DPO learning into three stages: Easy, Medium, and Hard, using a prefix-ngram match metric (Zheng et al. 2025)"（Preference-level Alignment）（按前缀 n-gram 匹配把 SP-DPO 分成三个由易到难的阶段。）

### 3. 实验发现

- 工业部署：作者报告了在工业推荐平台上的在线 A/B 测试收益和全量部署（Abstract）。

### 4. 局限与分析

**Our analysis.**

- 流程依次训练 SCID 编号器、多任务 SFT 和两轮 DPO。由此推断，物品库一变就要重跑好几个阶段。
- EAGER-LLM 同样把语义和协同信号输入 `Dec-Only` LLM，但用 `Dual H-KM` 码；Align3GR 用 `Dual RQ` 码，并加了 DPO。
