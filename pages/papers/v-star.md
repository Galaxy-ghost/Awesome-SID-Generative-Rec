# V-STAR

*Spend Search Where It Pays: Value-Guided Structured Sampling and Optimization for Generative Recommendation* — Jiang et al. · KDD’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2602.10699) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE` | `Dec-Only` | **`Fixed / NTP → RL`** | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 2. How It Works

![V-STAR architecture diagram](../../architectures/v-star.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2023 Industrial and Scientific and Office Products, preprocessed following MiniOneRec (Kong et al., 2025b); online: WeChat Channels advertising traffic. Filtering and sizes: not restated.
  - Source: Datasets and MiniOneRec preprocessing: https://arxiv.org/html/2602.10699v2#S5.SS1.p1.
- **Split**: Chronological next-item prediction following MiniOneRec's preprocessing (allocation not restated). Online: 5-day A/B test on 5% of live requests, against beam search plus GRPO.
  - Source: Chronological next-item protocol: https://arxiv.org/html/2602.10699v2#S5.SS1.p1; online A/B: https://arxiv.org/html/2602.10699v2#S5.SS3.p1.
- **Candidates**: not reported (full catalog versus sampled); generation is restricted to valid catalog SIDs, with HR and NDCG at 3, 5, 10.
  - Source: Valid-SID constraint and metrics: https://arxiv.org/html/2602.10699v2#S5.SS1.p1.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: No unseen-item protocol: https://arxiv.org/html/2602.10699v2#S5.SS1.p1.
- **SID**: 3-level RQ-VAE semantic IDs (citing TIGER); the paper states each item is represented by a unique fixed-length SID. Codebook size and the mechanism that ensures uniqueness: not reported.
  - Source: 3-level RQ-VAE SIDs: https://arxiv.org/html/2602.10699v2#S5.SS1.p1; each item has a unique fixed-length SID: https://arxiv.org/html/2602.10699v2#S3.SS1.p1.
- **Inference budget**: Training rollouts use value-guided decoding (VED) with 16 candidates per query and an 8-wide beam to initialize the prefix tree; at inference, standard beam search is the default decoder (width not reported). Qwen2.5-1.5B on 8 GPUs; inference batch size and latency: not reported.
  - Source: VED budget, beam settings, inference decoder: https://arxiv.org/html/2602.10699v2#S5.SS1.p2.
- **Results from**: Table 1 (Industrial and Office versus sequential, generative, and RL baselines including MiniOneRec); Tables 2-4 (decoding, expansion rules, training objective); Table 6 (candidate diversity and max reward); Section 5.3 (online GMV +1.23%).
  - Source: Main: https://arxiv.org/html/2602.10699v2#S4.T1; ablations: https://arxiv.org/html/2602.10699v2#S5.T2, https://arxiv.org/html/2602.10699v2#S5.T3, https://arxiv.org/html/2602.10699v2#S5.T4; diversity: https://arxiv.org/html/2602.10699v2#S5.T6; online: https://arxiv.org/html/2602.10699v2#S5.SS3.p1.

## 旧卡片说明

迁自 `d61aa6c:papers/vstar.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### V-STAR：价值引导结构化采样与优化

> V-STAR 让生成式推荐把搜索预算集中到高价值分支，并联合学习价值模型与结构化解码策略。

### 研究动机与问题定义

束搜索会在大量低价值分支上浪费计算，单纯扩大搜索预算也未必改善推荐。V-STAR 研究如何使用价值估计选择值得继续探索的 SID 前缀。

### TL;DR（核心摘要）

`用户历史 → SID前缀搜索 → 价值模型 → 结构化采样 → 完整SID → 推荐物品`

方法学习估计候选前缀价值的模型，提出 Value-Guided Efficient Decoding 选择搜索分支，并用 Sibling-GRPO 让策略从同层兄弟候选的相对价值中学习。生成完整 SID 后直接得到物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户历史、SID 前缀概率和候选价值 |
| 信息融入位置 | 价值模型、解码选择和策略训练 |
| 语义标识结构 | 层次化序列 |
| 适用场景 | 搜索预算受限的生成式推荐 |

### 方法设计

#### 4.1 语义感知价值模型
V-STAR 学习估计 SID 前缀在当前用户上下文下的推荐价值。价值模型同时参考生成概率、语义/协同表示和候选结果质量，为搜索过程提供比局部 token 概率更长程的判断。

#### 4.2 价值引导高效解码
VED 在树状 SID 空间中优先扩展高价值前缀，将有限搜索预算集中到更有希望的分支。它保留结构化约束，避免生成无法映射到物品的标识。

#### 4.3 Sibling-GRPO
Sibling-GRPO 将同一父节点下的兄弟候选组成相对比较组，用组内优势更新生成策略。这样模型能学习在局部结构中选择真正有价值的分支。

#### 4.4 训练与测试
V-STAR 形成解码-学习自演化闭环：解码器提供候选，价值模型评价候选，策略优化再改善解码。实验比较搜索预算、离线指标、线上效果和消融。

### 实验结论

- 价值引导解码在相同搜索预算下优于普通束搜索。
- 价值模型与策略优化具有互补作用。

### 局限性与研究定位

#### 局限性
- 额外价值模型和采样逻辑增加系统复杂度。
- 价值估计误差可能导致高价值分支被错误剪枝。

#### 研究定位
V-STAR 的主要贡献是按候选价值分配生成搜索预算，适合放在“高效解码与搜索优化”章节。

### 标签

`价值引导解码` · `结构化采样` · `GRPO` · `生成式推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：按价值分配搜索预算。
- 使用场景：高效解码。

### 5. Connections to Related Work

- **Competitor** · [MiniOneRec](minionerec.md): MiniOneRec samples RL candidates by beam search and applies GRPO; V-STAR replaces candidate construction with value-guided prefix expansion and uses sibling-group advantages, while keeping MiniOneRec's preprocessing.
  - Source: V-STAR v2, preprocessing follows Kong et al. (2025b): https://arxiv.org/html/2602.10699v2#S5.SS1.p1; strongest RL baseline: https://arxiv.org/html/2602.10699v2#S5.SS2.p1; Table 1: https://arxiv.org/html/2602.10699v2#S4.T1.
- **Competitor** · [TIGER](tiger.md): TIGER's SIDs and beam search are the base; V-STAR targets the pruning of high-reward low-probability prefixes during RL sampling.
  - Source: V-STAR v2, SID-based baselines: https://arxiv.org/html/2602.10699v2#S5.SS2.p1; Table 1: https://arxiv.org/html/2602.10699v2#S4.T1.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec is an SID-based LLM recommender without RL; V-STAR adds value-guided RL on top of SFT.
  - Source: V-STAR v2, baselines: https://arxiv.org/html/2602.10699v2#S5.SS2.p1; Table 1: https://arxiv.org/html/2602.10699v2#S4.T1.
- **Alternative** · [OneRec](onerec.md): OneRec applies preference alignment with beam-sampled responses; V-STAR argues that probability-based beam sampling under-explores high-reward items.
  - Source: V-STAR v2, Sections 1 and 2.3 cite OneRec: https://arxiv.org/html/2602.10699v2#S1.p1 and https://arxiv.org/html/2602.10699v2#S2.SS3.p1.

[View all papers in this cell](../../README.md#iv--training)
