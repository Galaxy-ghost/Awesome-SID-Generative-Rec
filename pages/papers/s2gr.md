# S2GR

*Stepwise Semantic-Guided Reasoning in Latent Space for Generative Recommendation* — Guo et al., KDD’26

[arXiv](https://arxiv.org/abs/2601.18664) · [Record](../../data/papers/s2gr.yaml) · [← Catalog](../../README.md#iii--backbone)

> Abstract: "degrading quality for SID codes". Candidates: III / none (rule: judged by the abstract's complaint first).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `CoBa RQ-VAE` | **`Enc-Dec`** | `Fixed / NTP + Ctr.` | `Beam` |

- `CoBa RQ-VAE`: Collaborative and Balanced RQ-VAE: item co-occurrence signal, codebook uniformity and load balancing (S2GR).
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.

## Architecture

![S2GR architecture diagram](../../architectures/s2gr.png)

## Evidence

- **`problem`** (arXiv abstract): Abstract: "degrading quality for SID codes". Candidates: III / none (rule: judged by the abstract's complaint first).
- **`representation`** (§5.1.3, p7; §4.2.1, p4, Eq. 3–5): Public-data (Beauty) setting; industrial data uses video frames.
- **`tokenizer`** (§5.1.3, p7; §5.3, p7): Location from the pre-10-26 Training evidence in the appendix.

## 旧卡片说明

迁自 `d61aa6c:papers/s2gr.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### S2GR：潜空间逐步语义引导推理

> S2GR 在生成 SID 的每一步注入语义引导信号，使模型在潜空间中逐步缩小推荐候选范围。

### 研究动机与问题定义

传统生成器通常只在最终 SID 上接受监督，缺乏对中间 token 决策的细粒度引导。S2GR 研究如何利用 SID 层次结构在生成过程中表达逐步推理。

### TL;DR（核心摘要）

`交互图与物品内容 → 协同平衡RQ-VAE → 逐步语义引导 → 生成SID → 推荐物品`

模型先构造物品共现图并学习兼顾协同关系和码本均衡的 RQ-VAE。生成时把逐步思考 token 插入 SID 序列，并用语义引导对齐监督中间状态；完整 SID 直接确定物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户交互、物品内容和物品共现图 |
| 信息融入位置 | RQ-VAE、生成中间状态和对齐目标 |
| 语义标识结构 | 层次化序列，交织推理 token |
| 适用场景 | 常规和工业生成式推荐 |

### 方法设计

#### 4.1 协同与均衡 RQ-VAE
S2GR 先根据物品共现构建协同图，并在 RQ-VAE 中加入码本均衡约束。量化器得到层次化 SID，同时减少 codeword 使用偏斜，为后续逐步推理提供稳定结构。

#### 4.2 逐步语义引导推理
模型把 thinking token 交织到 SID 生成过程中。每个 thinking token 对应一个层次或候选簇，生成器据此从粗粒度语义逐步缩小到细粒度 code；中间状态接受语义对齐监督。

#### 4.3 训练与部署
训练联合 next-item 生成、语义-行为对齐、码本均衡和逐步监督。推理时按层次顺序生成 thinking token 与 SID，最终完整标识直接映射到物品。论文还报告线上测试和不同规模分析。

### 实验结论

- 逐步语义引导提升了推荐效果。
- 协同平衡量化和中间状态监督均有贡献。
- 论文报告了工业线上测试结果。

### 局限性与研究定位

#### 局限性
- 交织推理 token 增加序列长度与服务成本。
- 工业线上收益的可复现细节有限。

#### 研究定位
S2GR 的贡献是把 SID 的层次结构转化为逐步推理信号，适合放在“潜空间推理与结构化生成”章节。

### 标签

`潜空间推理` · `语义引导` · `协同量化` · `生成式推荐`

### 架构图来源

*图源：原论文，图3。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：逐步语义引导潜空间推理。
- 使用场景：工业推荐。

## Same cell: III × Backbone (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` → `Par. VQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP` → `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` → `SimHash` → **`Non-AR`** → `Fixed / MTP + Aux.` → `Scoring` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` → `RQ-VAE / R-KM / LETTER` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` → `Par. OPQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Multi-task NTP` → `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed† / NTP†` → `C-Beam` |
