# LC-Rec

*Adapting large language models by integrating collaborative semantics for recommendation* — Zheng et al. · ICDE’24

`III. SID–Model Alignment` · `Training`

[Paper](https://arxiv.org/abs/2311.09049) · [Code](https://github.com/RUCAIBox/LC-Rec/) · [Matrix](../../README.md#iii--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

### TL;DR

LC-Rec assigns non-conflicting item indices by vector quantization with uniform semantic mapping and tunes an LLM with alignment tasks, so it generates items from the whole catalog without candidate lists.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Key Contribution | LC-Rec assigns non-conflicting item indices by vector quantization with uniform semantic mapping and tunes an LLM with alignment tasks, so it generates items from the whole catalog without candidate lists. |
| Modified Stage | Training |

### 2. How It Works

![LC-Rec architecture diagram](../../architectures/lc-rec.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews (May 1996-October 2018): Musical Instruments, Arts Crafts and Sewing, Video Games; users and items with fewer than 5 interactions are filtered; sequences capped at 20 items. Sizes (users / items / interactions): Instruments 24,773 / 9,923 / 206,153; Arts 45,142 / 20,957 / 390,832; Games 50,547 / 16,860 / 452,989.
  - Source: Amazon 2018 subsets, 5-interaction filter, length 20: https://arxiv.org/html/2311.09049v4#S4.SS1.SSS1.p1; statistics: https://arxiv.org/html/2311.09049v4#S4.T2.
- **Split**: Per-user leave-one-out: most recent item for test, second most recent for validation, the rest for training.
  - Source: Leave-one-out allocation: https://arxiv.org/html/2311.09049v4#S4.SS1.SSS3.p1.
- **Candidates**: full catalog (full ranking over the entire item set instead of sampled evaluation). Separate analysis (Table 5): choose between the target and one negative that is language-similar, collaborative-similar (by SASRec embeddings), or random; history exclusion for these negatives not reported.
  - Source: Full ranking over the entire item set: https://arxiv.org/html/2311.09049v4#S4.SS1.SSS3.p1; separate pairwise test with one negative: https://arxiv.org/html/2311.09049v4#S4.SS4.SSS0.Px3.p1.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2311.09049v4#S4.SS1.SSS3.p1.
- **SID**: 4-level RQ-VAE x 256 codewords (dimension 32) over mean-pooled LLaMA embeddings of title and description, added to the LLaMA tokenizer as new tokens. Conflicts are resolved without an extra suffix level: the last-level codewords of each conflicting group are redistributed under a uniform-distribution constraint.
  - Source: 4 levels x 256 x 32 over LLaMA text embeddings: https://arxiv.org/html/2311.09049v4#S4.SS1.SSS4.p1; uniform last-level redistribution for conflicts: https://arxiv.org/html/2311.09049v4#S3.SS2.SSS2.p2 and https://arxiv.org/html/2311.09049v4#S3.SS2.SSS2.p3.
- **Inference budget**: Beam search with beam size 20 for all generative methods; tokens leading to invalid item indices get zero probability. LLaMA backbone with DeepSpeed; hardware, inference batch size, and latency: not reported. HR and NDCG at 1, 5, 10.
  - Source: Beam size 20 and invalid-token masking: https://arxiv.org/html/2311.09049v4#S4.SS1.SSS3.p1 and https://arxiv.org/html/2311.09049v4#S3.SS4.SSS2.p1.
- **Results from**: Table 3 (Instruments, Arts, Games; LC-Rec averaged over instruction templates); Table 4 (alignment-task ablation); Table 5 (similar-negative ranking accuracy).
  - Source: Main: https://arxiv.org/html/2311.09049v4#S4.T3; ablation: https://arxiv.org/html/2311.09049v4#S4.T4; negative-item analysis: https://arxiv.org/html/2311.09049v4#S4.T5.

## 旧卡片说明

迁自 `d61aa6c:papers/lcrec.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### LC-Rec：协同语义融合的语言模型推荐

> LC-Rec 将语言语义与协同语义共同编码为物品索引，并通过多任务对齐使语言模型直接生成推荐物品标识。

### 研究动机与问题定义

纯文本 LLM 推荐难以表达用户-物品协同关系，纯 ID 建模又缺乏语义。LC-Rec 试图在有限增加词表的前提下，把两类信息纳入统一的生成式推荐模型。

### TL;DR（核心摘要）

`物品文本与交互 → 向量量化/统一映射 → LLM 对齐 → 生成物品索引 → 推荐物品`

模型利用文本编码器构造层次化物品索引，将索引 token 接入 LLM，再通过对齐任务引入协同信号。训练包含序列物品预测、显式索引-语言映射以及推荐对齐任务；在线生成的索引直接对应物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 物品标题/描述、用户交互和协同表示 |
| 信息融入位置 | 索引构建、词表扩展和对齐目标 |
| 语义标识结构 | 层次化序列索引 |
| 适用场景 | 序列推荐、意图预测和物品索引 |

### 方法设计

#### III-A 方法概览（Overview of the Approach）
LC-Rec 的目标是缩小语言语义与协同语义之间的差距。系统由物品索引学习和 LLM 对齐两部分组成：前者建立可生成的离散索引，后者让语言模型理解索引的推荐含义。

#### III-B 物品索引学习（Learning Item Indices）
论文使用物品文本编码器获得语义向量，再通过向量量化得到层次化 item index，并设计统一语义映射减少索引冲突。索引 token 被加入语言模型词表，作为文本语义和协同语义的共同接口。

#### III-C 语言-协同语义对齐
模型训练序列物品预测、显式索引生成、物品意图预测和协同/语言语义对齐等任务。不同任务分别从物品、用户历史和推荐目标施加约束，使 LLM 能在生成索引的同时利用协同结构。

#### III-D 训练与推理
论文采用分阶段对齐与推荐训练。推理时模型生成目标 item index，标识直接对应物品；索引构建和模型输入中的信息来源被明确区分。

### 实验结论

- 语言-协同联合对齐提升了物品预测和索引相关任务表现。
- 推荐对齐任务有助于缩小语言语义与协同语义之间的差距。

### 局限性与研究定位

#### 局限性
- 依赖离线物品索引构建，动态物品更新成本未充分讨论。
- 多任务对齐增加了训练和词表管理复杂度。

#### 研究定位
LC-Rec 的核心价值是把协同语义显式注入 LLM 的物品索引体系。它适合放在“LLM 推荐的协同语义对齐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2311.09049)

### 标签

`协同语义` · `多任务对齐` · `层次化量化` · `LLM推荐`

### 架构图来源

*图源：原论文，图1。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：把协同语义注入LLM物品索引。
- 使用场景：LLM推荐。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER resolves leaf conflicts with an extra index level and uses a small seq2seq model; LC-Rec redistributes conflicting last-level codes uniformly and tunes LLaMA with language-collaborative alignment tasks.
  - Source: LC-Rec v4, conflict discussion: https://arxiv.org/html/2311.09049v4#S3.SS2.SSS2.p1; baselines and Table 3: https://arxiv.org/html/2311.09049v4#S4.I1.i10.p1 and https://arxiv.org/html/2311.09049v4#S4.T3.
- **Competitor** · [CID](cid.md): P5-CID builds collaborative indices and also adds a supplementary index for conflicts; LC-Rec learns semantic RQ indices from LLM text embeddings.
  - Source: LC-Rec v4, conflict discussion: https://arxiv.org/html/2311.09049v4#S3.SS2.SSS2.p1; baselines and Table 3: https://arxiv.org/html/2311.09049v4#S4.I1.i9.p1 and https://arxiv.org/html/2311.09049v4#S4.T3.
- **Predecessor** · [VQ-Rec](vq-rec.md): LC-Rec borrows the idea of learned semantic indices from VQ-Rec and TIGER, then adapts it for LLM tuning.
  - Source: LC-Rec v4, Section 3.2.1: https://arxiv.org/html/2311.09049v4#S3.SS2.SSS1.p1 and https://arxiv.org/html/2311.09049v4#S3.SS2.SSS1.p4.
- **Alternative** · [TransRec](transrec.md): TransRec also builds LLM-based generative recommendation with multi-facet identifiers; LC-Rec uses learned VQ indices with alignment tuning.
  - Source: LC-Rec v4, Section 2.2 and Section 3.5 related work: https://arxiv.org/html/2311.09049v4#S2.SS2.p3 and https://arxiv.org/html/2311.09049v4#S3.SS5.p3.

[View all papers in this cell](../../README.md#iii--training)
