# MQL4GRec

*MULTIMODAL QUANTITATIVE LANGUAGE FOR GEN-ERATIVE RECOMMENDATION* — Zhai et al. · ICLR’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2504.05314) · [Code](https://github.com/zhaijianyang/MQL4GRec) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`Dual RQ`** | `Enc-Dec` | `Fixed / Multi-task NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 2. How It Works

![MQL4GRec architecture diagram](../../architectures/mql4grec.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2018 (May 1996-October 2018). Pre-training on six categories (Pet, Cell, Automotive, Tools, Toys, Sports); target tasks on Instruments (17,112 users / 6,250 items), Arts (22,171 / 9,416), Games (42,259 / 13,839). Users and items with fewer than 5 interactions are filtered; sequences capped at 20 items.
  - Source: Pre-training and target categories: https://arxiv.org/html/2504.05314v1#S4.SS1.SSS0.Px1.p1 and https://arxiv.org/html/2504.05314v1#A1.p1; filtering and length: https://arxiv.org/html/2504.05314v1#A1.p2; statistics: https://arxiv.org/html/2504.05314v1#A1.T6.
- **Split**: Leave-one-out (allocation not restated beyond the label). Separate zero-shot study: models pre-trained on source categories are tested on the targets without fine-tuning.
  - Source: Leave-one-out named only: https://arxiv.org/html/2504.05314v1#S4.SS1.SSS0.Px2.p1; zero-shot study: https://arxiv.org/html/2504.05314v1#S4.SS5.p1.
- **Candidates**: full catalog (full ranking over the entire item set instead of sample-based evaluation).
  - Source: Full ranking over the entire item set: https://arxiv.org/html/2504.05314v1#S4.SS1.SSS0.Px2.p1.
- **Visibility**: Main: warm; no unseen-item protocol is defined. Zero-shot: target-domain items are unseen by the pre-trained generator; whether the RQ-VAE translators saw them: not reported.
  - Source: Standard split; zero-shot uses target-domain items absent from pre-training: https://arxiv.org/html/2504.05314v1#S4.SS5.p1.
- **SID**: Separate text (LLaMA) and image (ViT-L/14) quantitative languages from RQ-VAEs with 4 levels x 256 codewords (dimension 32). Colliding items have tokens reassigned by the distances between their residuals and code vectors, instead of an appended identifier.
  - Source: 4 levels x 256 x 32 per modality: https://arxiv.org/html/2504.05314v1#A3.p1; distance-based reassignment for collisions: https://arxiv.org/html/2504.05314v1#S3.SS1.SSS0.Px2.p2.
- **Inference budget**: Beam search with beam size 20 in each modality; the two recommendation lists are re-ranked so items in both rank higher. T5 encoder-decoder with 4 layers each. Hardware, inference batch size, and latency: not reported.
  - Source: Beam size 20 and dual-list re-ranking: https://arxiv.org/html/2504.05314v1#S4.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2504.05314v1#S3.SS3.SSS0.Px2.p1; T5 backbone: https://arxiv.org/html/2504.05314v1#A3.p2.
- **Results from**: Table 1 (Instruments, Arts, Games versus sequential, multimodal, and generative baselines); Table 2 (collision handling versus TIGER's appended index); Tables 3-4 (generation tasks and pre-training); Figures 3-4 (pre-training data and epochs); Table 5 (zero-shot).
  - Source: Main: https://arxiv.org/html/2504.05314v1#S4.T1; collisions: https://arxiv.org/html/2504.05314v1#S4.T2; tasks and pre-training: https://arxiv.org/html/2504.05314v1#S4.T3, https://arxiv.org/html/2504.05314v1#S4.T4; zero-shot: https://arxiv.org/html/2504.05314v1#S4.T5.

## 旧卡片说明

迁自 `d61aa6c:papers/mql4grec.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### MQL4GRec：生成式推荐的多模态量化语言

> MQL4GRec 将不同领域和模态的物品内容翻译为统一的离散量化语言，并以生成任务迁移推荐知识。

### 研究动机与问题定义

文本和图像内容形式复杂，跨域推荐中的表示难以共享。MQL4GRec 把量化器视为翻译器，将多模态内容映射到共享 codebook 语言，降低跨域迁移的表示差异。

### TL;DR（核心摘要）

`文本/图像 → RQ-VAE量化语言 → 预训练生成任务 → 目标域微调 → 推荐物品`

冻结模态编码器提取文本或图像表示，RQ-VAE 将其转为带模态前缀的离散 token；通过下一物品生成、非对称生成和量化语言对齐任务进行预训练，再在目标推荐数据上微调。论文在生成候选后进行模态结果重排，重排仍属于模型内部流程。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 文本、图像、用户交互和多域数据 |
| 信息融入位置 | 量化语言、预训练任务和目标域生成 |
| 语义标识结构 | 带模态前缀的多级序列 |
| 适用场景 | 多模态、跨域推荐 |

### 方法设计

#### 3.1 量化语言
MQL4GRec 将量化器视为翻译器。冻结的 LLaMA/ViT 编码器提取文本或图像表示，RQ-VAE 为每种模态学习多级 codebook，并通过模态前缀组成统一量化语言。碰撞物品再依据残差距离重新分配 code。

#### 3.2 量化语言生成任务
除同模态下一物品生成外，论文加入非对称生成：用文本历史预测图像量化语言，或反向预测；同时加入 text-to-image 和 image-to-text 的显式量化语言对齐任务。

#### 3.3 训练与推荐
模型先在多域、多模态数据上预训练，再在目标推荐任务上微调。生成器预测目标模态的量化 token，推理阶段综合不同模态生成列表，并依据模型分数进行内部重排。

#### 3.4 零样本与分析
实验考察跨域迁移、模态组合、消融和零样本能力，重点验证量化语言是否能把模态知识和推荐知识传递到新领域。

### 实验结论

- MQL4GRec 在 ICLR 2025 论文报告的跨域设置中优于比较方法。
- 量化语言预训练和跨模态对齐带来迁移收益。

### 局限性与研究定位

#### 局限性
- 模态候选重排增加了推理链路。
- 量化语言依赖模态编码器和离线 codebook。
- 开放物品和动态领域更新仍需验证。

#### 研究定位
MQL4GRec 的主要贡献是将多模态跨域知识迁移表述为量化语言生成，适合放在“跨域与多模态生成推荐”章节。

### 标签

`量化语言` · `多模态` · `跨域迁移` · `生成式推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：以量化语言促进跨域迁移。
- 使用场景：多模态跨域。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER uses one text modality and an appended index for collisions; MQL4GRec translates text and images into separate quantitative languages and reassigns colliding tokens by distance.
  - Source: MQL4GRec v1, Table 1 baseline TIGER: https://arxiv.org/html/2504.05314v1#S4.T1; collision comparison in Table 2: https://arxiv.org/html/2504.05314v1#S4.SS3.SSS0.Px1.p1 and https://arxiv.org/html/2504.05314v1#S4.T2.
- **Alternative** · [LC-Rec](lc-rec.md): LC-Rec spreads items across the last level with a uniform constraint, which MQL4GRec says does not fully remove collisions.
  - Source: MQL4GRec v1, Section 3.1 Handling Collisions cites Zheng et al. (2023): https://arxiv.org/html/2504.05314v1#S3.SS1.SSS0.Px2.p1.
- **Competitor** · [CID](cid.md): P5-CID uses collaborative indexing for a T5 model; MQL4GRec uses multimodal content codes with cross-modal generation tasks.
  - Source: MQL4GRec v1, baseline P5-CID: https://arxiv.org/html/2504.05314v1#A2.I1.i8.p1; Table 1: https://arxiv.org/html/2504.05314v1#S4.T1.
- **Competitor** · [VQ-Rec](vq-rec.md): VQ-Rec uses product-quantized text codes in a discriminative transferable model; MQL4GRec generates multimodal codes with pre-training across categories.
  - Source: MQL4GRec v1, Table 1 baseline VQ-Rec: https://arxiv.org/html/2504.05314v1#S4.T1.
- **Successor** · [MACRec](macrec.md): MACRec later reuses MQL4GRec's collision reassignment and dual-modality ensemble and adds cross-modal contrastive alignment during quantization.
  - Source: Evidence is from the later MACRec paper: https://arxiv.org/html/2511.15122v2#Sx3.SSx1.SSSx3.p5 and https://arxiv.org/html/2511.15122v2#Sx3.SSx2.SSSx3.p3; MQL4GRec is its main baseline in Table 2: https://arxiv.org/html/2511.15122v2#Sx4.T2.

[View all papers in this cell](../../README.md#i--tokenization)
