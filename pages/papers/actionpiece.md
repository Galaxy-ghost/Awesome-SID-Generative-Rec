# ActionPiece

*Contextually Tokenizing Action Sequences for Generative Recommendation* — Hou et al. · ICML’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2502.13581) · [Code](https://github.com/google-deepmind/action_piece) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`OPQ`** | `Enc-Dec` | `Fixed / NTP` | `Ensemble` |

- `OPQ`: Optimized product quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

ActionPiece represents each action as a set of item features and merges co-occurring feature patterns into new tokens, so identical actions get context-dependent tokens instead of fixed independent ones.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | ActionPiece represents each action as a set of item features and merges co-occurring feature patterns into new tokens, so identical actions get context-dependent tokens instead of fixed independent ones. |
| Modified Stage | Tokenization |

### 2. How It Works

![ActionPiece architecture diagram](../../architectures/actionpiece.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews: Sports and Outdoors, Beauty, and CDs and Vinyl. Users with fewer than 5 reviews are filtered; an item-frequency filter is not reported. Processed sizes (users / items / actions): Sports 35,598 / 18,357 / 260,739; Beauty 22,363 / 12,101 / 176,139; CDs 75,258 / 64,443 / 1,022,334.
  - Source: Dataset categories: https://arxiv.org/html/2502.13581v3#S4.SS1.p1; user filter and truncation: https://arxiv.org/html/2502.13581v3#A6.p2; processed sizes: https://arxiv.org/html/2502.13581v3#S3.T3.
- **Split**: Per-user chronological leave-last-out: last item for test, second-to-last for validation, earlier items for training. Histories are truncated to 20 items for generative methods and 50 items for ID-based and feature-enhanced baselines.
  - Source: Leave-last-out allocation: https://arxiv.org/html/2502.13581v3#S4.SS1.p1; history truncation: https://arxiv.org/html/2502.13581v3#A6.p2.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); top-K lists are produced by beam search.
  - Source: Evaluation settings name metrics only: https://arxiv.org/html/2502.13581v3#S4.SS1.p3; top-K lists come from beam search: https://arxiv.org/html/2502.13581v3#A8.p4.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard leave-last-out protocol with no cold-start experiment: https://arxiv.org/html/2502.13581v3#S4.SS1.p1.
- **SID**: Each item is an unordered set of 4 OPQ codes x 256 codewords (sentence-t5-base text embeddings) plus 1 extra identification code to prevent conflicts. ActionPiece then merges co-occurring feature sets into a context-dependent vocabulary of 40,000 tokens (tuned over 5k-40k), so the same item can map to different tokens in different sequences.
  - Source: OPQ features, 256 codewords per digit, extra identification code: https://arxiv.org/html/2502.13581v3#A6.I1.i3.p1; vocabulary size 40,000 and tuning range: https://arxiv.org/html/2502.13581v3#A7.T7 and https://arxiv.org/html/2502.13581v3#A8.p2.
- **Inference budget**: Beam search with beam size 50; inference-time ensemble over q=5 set-permutation segmentations, with item scores averaged across the 5 ranking lists. Recall and NDCG at K=5 and 10. Inference hardware, inference batch size, and measured latency: not reported (each model is trained on one 40GB NVIDIA A100; the paper states only that latency stays comparable when segments run in parallel).
  - Source: Beam size 50 and q=5 segmentations: https://arxiv.org/html/2502.13581v3#A8.p2 and https://arxiv.org/html/2502.13581v3#A7.T7; score averaging: https://arxiv.org/html/2502.13581v3#S3.SS3.SSS2.p1; GPU statement is for training: https://arxiv.org/html/2502.13581v3#A8.p3; qualitative latency statement: https://arxiv.org/html/2502.13581v3#S3.SS4.p3.
- **Results from**: Table 4 (main comparison on Sports, Beauty, and CDs; averages over five seeds); Table 5 (ablations, including TIGER with varied vocabulary sizes); Figures 4-6 (vocabulary size, token utilization, and ensemble size). BERT4Rec, SASRec, FDSA, S3-Rec, TIGER, and LMIndexer numbers on Sports and Beauty are copied from earlier papers; other results are the authors' reimplementations.
  - Source: Main table: https://arxiv.org/html/2502.13581v3#S3.T4 and https://arxiv.org/html/2502.13581v3#S4.SS2.p1; ablation: https://arxiv.org/html/2502.13581v3#S4.T5; five seeds: https://arxiv.org/html/2502.13581v3#S4.SS1.p3; copied baseline numbers: https://arxiv.org/html/2502.13581v3#A8.p1.

## 旧卡片说明

迁自 `d61aa6c:papers/actionpiece.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### ActionPiece：上下文动作序列分词

> ActionPiece 根据同一动作内及相邻动作间的特征共现关系压缩行为序列，减少生成式推荐中的序列长度。

### 研究动机与问题定义

将每个动作展开为多个特征 token 会造成序列过长，并损失动作上下文。ActionPiece 关注的是行为序列的上下文分词效率，重点在已有物品特征的上下文组合。

### TL;DR（核心摘要）

`动作序列 → 共现统计 → ActionPiece 词表 → 序列压缩 → 生成式推荐输入`

方法按加权共现关系迭代合并 token，并用集合排列正则减轻特征顺序影响。生成模型接收压缩后的动作序列。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 动作中的物品特征及动作顺序 |
| 信息融入位置 | 行为序列分词与模型输入 |
| 语义标识结构 | 不适用 |
| 适用场景 | 长行为序列推荐 |

### 方法设计

#### 3.1 问题定义（Problem Formulation）
ActionPiece 将一次用户动作表示为无序物品特征集合，把一段行为历史表示为特征集合序列。目标是为动作序列学习更短且包含上下文的 token 序列。

#### 3.2 上下文动作序列分词器
词表从每个特征 token 初始化，通过统计同一集合内部和相邻集合之间的共现关系，反复合并高权重 token 对。由于集合内部无序，论文引入集合排列分段策略，为同一动作产生多个等价分词结果。

#### 3.3 生成式推荐模型
压缩后的 ActionPiece 序列被送入生成式推荐模型训练。推理时模型生成动作 token，再解析回推荐动作/物品。论文还使用多种分段结果进行推理时集成，以降低某一种分段方式的偶然影响。

#### 3.4 讨论与实验
实验分别考察序列长度、词表规模、token 利用率、分段策略和案例。该方法的核心对象是动作 token。

### 实验结论

- ActionPiece 能缩短动作序列，并改善 token 利用率。
- 上下文加权和集合排列正则对分词质量有贡献。

### 局限性与研究定位

#### 局限性
- 对最终推荐物品的直接可解释映射不是论文重点。

#### 研究定位
ActionPiece 更适合放在“生成式推荐的行为序列建模与分词”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2502.13581)
- [开源代码](https://github.com/google-deepmind/action_piece)

### 标签

`动作序列分词` · `子词合并` · `序列推荐`

### 架构图来源

*图源：原论文，图1（[论文原文](https://arxiv.org/abs/2502.13581)）。图片使用许可待核实。*

---

### 检索方式补充

迁自 `d61aa6c:tables/boundary-and-excluded-methods.md` 的机制说明。

重点是动作序列上下文分词；沿用的物品特征构码和生成配置见当前记录。

旧表的“核心／边界／排除”分组已由当前问题与阶段分类取代。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER tokenizes each item independently into ordered RQ-VAE codes, whereas ActionPiece merges unordered feature sets into context-dependent tokens; both use the same encoder-decoder and beam search.
  - Source: ActionPiece v3, Section 4.1 baselines: https://arxiv.org/html/2502.13581v3#S4.SS1.p2; Table 4: https://arxiv.org/html/2502.13581v3#S3.T4; same architecture statement: https://arxiv.org/html/2502.13581v3#A8.p2.
- **Predecessor** · [VQ-Rec](vq-rec.md): ActionPiece follows VQ-Rec in quantizing sentence embeddings with OPQ into unordered codes, then builds a merged contextual vocabulary over those codes for generation.
  - Source: ActionPiece v3, Appendix F follows Hou et al. (2023) for OPQ features: https://arxiv.org/html/2502.13581v3#A6.I1.i3.p1; VQ-Rec is a Table 4 baseline: https://arxiv.org/html/2502.13581v3#S3.T4.
- **Competitor** · [LMIndexer](lmindexer.md): LMIndexer learns text-based semantic indexes item by item, while ActionPiece tokenizes whole action sequences with context-aware merges.
  - Source: ActionPiece v3, Table 1 and Section 4.1 baselines: https://arxiv.org/html/2502.13581v3#S1.T1 and https://arxiv.org/html/2502.13581v3#S4.SS1.p2; Table 4: https://arxiv.org/html/2502.13581v3#S3.T4.
- **Competitor** · [CID](cid.md): P5-CID builds item IDs by hierarchical clustering, independent of sequence context; ActionPiece's tokens depend on neighboring actions.
  - Source: ActionPiece v3, Table 1 and Section 4.1 baselines: https://arxiv.org/html/2502.13581v3#S1.T1 and https://arxiv.org/html/2502.13581v3#S4.SS1.p2; Table 4: https://arxiv.org/html/2502.13581v3#S3.T4.

[View all papers in this cell](../../README.md#i--tokenization)
