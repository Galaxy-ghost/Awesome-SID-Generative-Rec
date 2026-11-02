# IDGenRec

*Llm-recsys alignment with textual id learning* — Tan et al. · SIGIR’24

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2403.19021) · [Code](https://github.com/agiresearch/IDGenRec) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`LLM-Vocab`** | `Enc-Dec` | `Altern. / NTP` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Altern.`: Tokenizer and generator are updated in turns.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

IDGenRec trains a textual ID generator alongside an LLM recommender, so each item receives a concise ID made of natural-language tokens, and tests zero-shot transfer to unseen platforms.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Key Contribution | IDGenRec trains a textual ID generator alongside an LLM recommender, so each item receives a concise ID made of natural-language tokens, and tests zero-shot transfer to unseen platforms. |
| Modified Stage | Tokenization |

### 2. How It Works

![IDGenRec architecture diagram](../../architectures/idgenrec.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Standard: Amazon Sports, Beauty, Toys and Yelp, filtering users and items with fewer than 5 interactions (following P5 and Hua et al. 2023). Zero-shot: a Fusion pre-training corpus from 19 other Amazon categories, each downsampled to at most 30,000 users (183,918 users / 233,323 items), tested on Sports, Beauty, Toys, Music, Instruments, and Yelp.
  - Source: Standard datasets and 5-interaction filter: https://arxiv.org/html/2403.19021v2#S3.SS1.p1; zero-shot data rules: https://arxiv.org/html/2403.19021v2#S3.SS1.p3 and https://arxiv.org/html/2403.19021v2#S3.SS1.p4; statistics: https://arxiv.org/html/2403.19021v2#S3.T3.
- **Split**: Leave-one-out for testing (validation allocation not restated). Zero-shot: train once on Fusion and test directly on held-out datasets.
  - Source: Leave-one-out: https://arxiv.org/html/2403.19021v2#S3.SS3.p1; zero-shot setting: https://arxiv.org/html/2403.19021v2#S3.SS5.p1.
- **Candidates**: full catalog (no negative sampling; ranking over all items).
  - Source: Ranking over all items without negative sampling: https://arxiv.org/html/2403.19021v2#S3.SS3.p1.
- **Visibility**: Standard: warm; no unseen-item protocol is defined. Zero-shot: users and items of the test datasets are not seen in training; the ID generator is also trained only on the Fusion corpus, so test items are unseen by tokenizer too and receive IDs generated from their text.
  - Source: Zero-shot: users and items unseen in training: https://arxiv.org/html/2403.19021v2#S3.SS5.p1; the ID generator is trained with the recommender on the training data: https://arxiv.org/html/2403.19021v2#S3.SS2.p3.
- **SID**: Textual IDs generated from item text by a T5-small ID generator with diverse beam search (k=10 groups, diversity penalty raised from 1 to 10), length initially in [1, 10) tokens and extended to [10, 20) when needed; uniqueness is enforced at generation time by rejecting duplicates. SentencePiece vocabulary of 32,128.
  - Source: Diverse beam search for unique textual IDs, length ranges: https://arxiv.org/html/2403.19021v2#S2.SS3.p2 and https://arxiv.org/html/2403.19021v2#S3.SS2.p2; T5-small ID generator: from Section 2.
- **Inference budget**: Constrained decoding over a prefix tree of all generated item IDs; beam width, hardware, inference batch size, and latency: not reported. HR and NDCG at 5 and 10.
  - Source: Constrained decoding with a prefix tree over generated IDs: Section 2 inference; no beam width or hardware found.
- **Results from**: Table 4 (standard evaluation versus traditional and P5-variant baselines); Table 5 (training strategies); Table 6 (user and item IDs); Table 7 (zero-shot intra- and inter-platform).
  - Source: Standard: https://arxiv.org/html/2403.19021v2#S3.T4; training strategies: https://arxiv.org/html/2403.19021v2#S3.T5; user/item IDs: https://arxiv.org/html/2403.19021v2#S3.T6; zero-shot: https://arxiv.org/html/2403.19021v2#S3.T7.

## 旧卡片说明

迁自 `d61aa6c:papers/idgenrec.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### IDGenRec：文本 ID 学习的 LLM-推荐系统对齐

> IDGenRec 同时学习物品文本 ID 和推荐生成器，使 LLM 能直接生成可识别的目标物品 ID。

### 研究动机与问题定义

随机 ID 难以利用 LLM 的语言知识，直接使用长文本又会造成冗余和幻觉。IDGenRec 将物品元信息压缩为文本 ID，并让这些 ID 与推荐器共同适配。

### TL;DR（核心摘要）

`物品元信息 → ID生成器 → 文本ID → 推荐提示 → 基础推荐器 → 目标ID`

ID 生成器从标题、类别、价格等元信息生成简短 token 序列，并用多样束搜索减少重复。基础推荐器接收用户历史中的文本 ID，通过前缀树约束直接生成目标 ID；两者交替训练，生成结果可映射到物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 物品元信息、用户交互和推荐目标 |
| 信息融入位置 | ID 生成、提示输入和交替训练目标 |
| 语义标识结构 | 变长文本 token 序列 |
| 适用场景 | 序列推荐和零样本扩展 |

### 方法设计

#### 2.1 生成过程
旧卡片的速览将 ID 生成器和基础推荐器都记为 T5 编码器-解码器。IDGenRec 把物品元信息转成简短文本 ID，再将用户历史中的物品替换为这些 ID，填入推荐提示。基础推荐器以提示和历史 ID 为条件，逐 token 生成目标物品 ID。

#### 2.2 ID 生成器
ID 生成器读取标题、类别、价格、描述等 plain text，输出短而具有区分性的 token 序列。它使用语言模型的文本知识进行压缩，不要求扩展为独立数值词表。

#### 2.3 多样 ID 生成
为减少不同物品获得相同 ID，论文使用多样束搜索，逐步提高多样性惩罚；必要时增加 ID 长度。生成过程维护已分配 ID 集合，直到获得可区分标识。

#### 2.4 基础推荐器与交替训练
基础推荐器使用前缀树进行约束解码，确保目标 ID 对应真实物品。ID 生成器和推荐器交替更新：前者学习可被推荐器使用的 ID，后者学习根据当前 ID 预测下一物品。

### 实验结论

- IDGenRec 在标准序列推荐和零样本设置中均展示了生成能力。
- 交替训练改善了文本 ID 与推荐器之间的可用性。

### 局限性与研究定位

#### 局限性
- ID 生成器和基础推荐器构成双模型流程，训练成本更高。
- 前缀树与多样束搜索需要维护候选 ID 库。
- 最终泛化受元信息质量影响。

#### 研究定位
IDGenRec 的贡献是以文本 ID 作为 LLM 与推荐系统之间的接口，适合放在“文本化物品标识与 LLM 对齐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2403.19021)

### 标签

`文本ID` · `交替训练` · `LLM对齐` · `生成式推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：以文本ID对齐LLM与推荐器。
- 使用场景：序列推荐。

### 5. Connections to Related Work

- **Competitor** · [CID](cid.md): P5-SID, P5-CID, and P5-SemID assign sequential, collaborative, or category IDs; IDGenRec learns a textual ID generator jointly with the recommender.
  - Source: IDGenRec v2, baselines: https://arxiv.org/html/2403.19021v2#S3.I1.i2.p1; Table 4: https://arxiv.org/html/2403.19021v2#S3.T4.
- **Alternative** · [GRAM](gram.md): GRAM later builds hierarchical textual IDs by clustering and reports that IDGenRec's user IDs concatenate validation and test items; it reruns IDGenRec without user IDs.
  - Source: Evidence is from the later GRAM paper: Table 9 and Appendix E: https://arxiv.org/html/2506.01673v1#A4.T9 and https://arxiv.org/html/2506.01673v1#A5.p3; Table 2: https://arxiv.org/html/2506.01673v1#S4.T2.
- **Alternative** · [GRLM](grlm.md): GRLM later replaces free textual IDs with a fixed number of standardized vocabulary terms to reduce synonym ambiguity.
  - Source: Evidence is from the later GRLM paper: baselines and Table 2: https://arxiv.org/html/2601.06798v1#S4.I1.i3.p1 and https://arxiv.org/html/2601.06798v1#S5.T2; case study: https://arxiv.org/html/2601.06798v1#A3.p1.
- **Alternative** · [GMC](gmc.md): GMC later compares against IDGenRec in a multi-domain setting with codebook IDs shared across domains.
  - Source: Evidence is from the later GMC paper: generative baselines and Table 3: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i3.p1 and https://arxiv.org/html/2507.12871v3#S5.T3.

[View all papers in this cell](../../README.md#iii--tokenization)
