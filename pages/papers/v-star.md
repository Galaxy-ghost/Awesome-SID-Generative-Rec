# V-STAR: Spend Search Where It Pays: Value-Guided Structured Sampling and Optimization for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.10699`)](https://arxiv.org/abs/2602.10699) · [Source Record (`data/papers/v-star.yaml`)](../../data/papers/v-star.yaml)

> **Summary**: Abstract: "fine-tuning these models with Reinforcement Learning (RL) often suffers from a fundamental probability-reward mismatch".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Jiang et al. (2026) | Published / posted in `KDD’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text†` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Architecture

![V-STAR architecture diagram](../../architectures/v-star.png)

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "fine-tuning these models with Reinforcement Learning (RL) often suffers from a fundamental probability-reward mismatch".
- **`representation`** (§5.1, p6; §4.1, p4): Embedding used to build SIDs is not stated; inferred from MiniOneRec (Text in Table 1).
- **`objective`** (p6; §3.1, p3; §4.3, p5): Location from the pre-10-26 Training evidence in the appendix.

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

## Peer Methods in `IV. Utility` × `Training` (21 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [APAO](apao.md) | KDD’26 | `Text` | `R-KM` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Rank` | `Beam` |
| [DASO](daso.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
| [DPE-Rec](dpe-rec.md) | arXiv’26 | `– / Text+Img` | `RQ` | `Non-AR` | `Fixed` | `Masked → RL (→ Masked KD for Fast)` | `Diff.+Legalize` |
| [GEM-Rec](gem-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Bid-Aware Beam` |
| [GenRec-JD](genrec-jd.md) | SIGIR’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [GFlowGR](gflowgr.md) | SIGIR’26 | `Text / Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `Beam† / C-Beam†` |
| [Ghost](ghost.md) | NeurIPS’26 | `Text` | `Skeleton R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `–` |
| [HASTE](haste.md) | arXiv’26 | `Text / MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `–` |
| [HCGRec](hcgrec.md) | CIKM’26 | `–` | `RQ` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [IDM/CMM](idm-cmm.md) | arXiv’26 | `Text` | `Subspace RQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` | `R-KM` | `Enc-Dec` | `Fixed†` | `(NTP† / (NTP + Aux.)†) → KL-weighted OPD` | `C-Beam` |
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` | `RQ-VAE` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [NAU](nau.md) | arXiv’26 | `–` | `R-KM` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `–` |
| [OneChord](onechord.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Next-item CE + Cons. KD + Rank KD` | `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` | `R-KM†` | `Dec-Only†` | `Fixed†` | `NTP → RL` | `–` |
| [SAHL](sahl.md) | arXiv’26 | `Text` | `SRBQ` | `Non-AR` | `Fixed` | `(MTP + Masked Rec.) → MTP` | `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` | `–` | `Dec-Only` | `Fixed` | `NTP` | `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → (RL + Rank)` | `Beam` |
