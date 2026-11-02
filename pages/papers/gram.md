# GRAM

*Generative recommendation via semantic-aware multi-granular late fusion* — Lee et al. · ACL’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2506.01673) · [Code](https://github.com/skleee/GRAM) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`H-KM`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `H-KM`: Hierarchical k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 2. How It Works

![GRAM architecture diagram](../../architectures/gram.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty, Toys and Games, Sports and Outdoors, and Yelp, with 5-core filtering of users and items (following Hua et al. 2023). Sizes (users / items / interactions): Beauty 22,363 / 12,101 / 198,502; Toys 19,412 / 11,924 / 167,597; Sports 35,598 / 18,357 / 296,337; Yelp 30,431 / 20,033 / 316,354.
  - Source: Datasets and 5-core: https://arxiv.org/html/2506.01673v1#S4.p1; statistics: https://arxiv.org/html/2506.01673v1#A7.T10.
- **Split**: Per-user leave-one-out: last item for test, second last for validation, the rest for training; sequences capped at 20 items. Three seeds.
  - Source: Leave-one-out allocation and history cap: https://arxiv.org/html/2506.01673v1#S4.p2 and https://arxiv.org/html/2506.01673v1#S4.p4.
- **Candidates**: full catalog (full-ranking evaluation on all items rather than sampled items).
  - Source: Full ranking on all items: https://arxiv.org/html/2506.01673v1#S4.p2.
- **Visibility**: warm; no unseen-item protocol is defined. A head/tail analysis splits test users by target-item popularity (top 20% versus bottom 80%).
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2506.01673v1#S4.p2; head/tail by target popularity: https://arxiv.org/html/2506.01673v1#S5.SS3.p2.
- **SID**: Hierarchical textual IDs: recursive k-means over item text embeddings, stopping when a cluster has fewer than c items or depth reaches l; each cluster index is mapped to an existing LLM vocabulary token chosen by TF-IDF. Final (l, k, c): Beauty (7, 128, 128); Toys (5, 32, 32); Sports and Yelp (7 or 9, 32, 32). Duplicate IDs receive an appended digit for uniqueness.
  - Source: Hierarchical k-means textual IDs: https://arxiv.org/html/2506.01673v1#S3.SS2.SSS1.p2 and https://arxiv.org/html/2506.01673v1#S3.SS2.SSS1.p3; final settings: https://arxiv.org/html/2506.01673v1#A7.T12; duplicate-ID digit: https://arxiv.org/html/2506.01673v1#S3.SS2.SSS1.p3.
- **Inference budget**: Constrained beam search with beam size 50 and a Trie over valid IDs; T5-small on OpenP5. Table 7: average inference time per user sequence with all user sequences in a single batch on one NVIDIA A6000 GPU (Beauty 0.2008 s, Toys 0.1605 s; LC-Rec 1.8312 s and 1.8125 s).
  - Source: Constrained beam 50 with Trie: https://arxiv.org/html/2506.01673v1#S4.p4 and https://arxiv.org/html/2506.01673v1#S3.SS4.p2; timing: https://arxiv.org/html/2506.01673v1#A3.T7.
- **Results from**: Table 2 (four datasets versus six sequential and eight generative baselines; three seeds); Table 3 (ablations); Table 4 (ID types); Figures 6-8 (head/tail, ID length, similar items); Tables 6-7 (preprocessing and inference time); Tables 8-9 (baseline reproduction fixes for ELMRec and IDGenRec).
  - Source: Main: https://arxiv.org/html/2506.01673v1#S4.T2; ablation: https://arxiv.org/html/2506.01673v1#S5.T3; ID types: https://arxiv.org/html/2506.01673v1#S5.T4; reproducibility: https://arxiv.org/html/2506.01673v1#A3.T8 and https://arxiv.org/html/2506.01673v1#A4.T9.

## 旧卡片说明

迁自 `d61aa6c:papers/gram.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### GRAM：语义感知多粒度后融合生成推荐

> GRAM 在层次化语义与协同语义之间进行多粒度后融合，由生成模型直接输出物品标识。

### 研究动机与问题定义

早期融合容易让不同来源的信息相互干扰，单一粒度的语义标识又难以兼顾概括性和区分性。GRAM 延迟融合多层语义，以改善生成推荐的表达与决策。

### TL;DR（核心摘要）

`物品内容与交互 → 层次化语义/协同信息 → 多粒度编码 → 后融合解码 → 推荐物品`

模型构造层次化语义标识，并将协同语义 verbalize 为可被语言模型处理的 token。多粒度编码器分别建模局部和整体语义，解码端进行 late fusion，直接生成目标物品标识。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户行为、物品文本语义和协同语义 |
| 信息融入位置 | 多粒度编码与解码端后融合 |
| 语义标识结构 | 层次化多粒度序列 |
| 适用场景 | 语义增强序列推荐 |

### 方法设计

#### 3.1 语义到词汇的转换
GRAM 先建立层次化语义索引，将物品整体语义拆成多个粒度，再把协同表示转换为可被语言模型处理的协同语义 token。这样既保留语义结构，也让用户行为信号进入文本生成空间。

#### 3.2 多粒度编码器
多粒度编码器分别处理粗粒度类别、细粒度属性和协同语义。编码结果保留各层级的位置信息和语义差异，为后续生成提供互补条件。

#### 3.3 后融合解码器
与输入端早期融合不同，GRAM 在解码端延迟组合多源表示。解码器在生成不同 SID 位置时选择对应粒度的语义信息，从而减少模态间相互干扰。

#### 3.4 训练与推理
模型以用户历史到目标 SID 的生成损失训练，推理时自回归生成完整标识并映射到物品。实验重点比较多粒度、融合位置和语义来源。

### 实验结论

- 多粒度后融合优于单粒度或早期融合设置。
- 语义和协同信息的联合使用带来互补收益。

### 局限性与研究定位

#### 局限性
- 多路编码和融合增加模型与推理开销。
- 动态物品加入和大规模线上服务仍未充分评估。

#### 研究定位
GRAM 的关键贡献是将多粒度语义融合位置推迟到解码阶段，适合放在“多源语义融合”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2506.01673)
- 代码公开情况未报告。

### 标签

`多粒度融合` · `语义标识` · `后融合` · `生成式推荐`

### 架构图来源

*图源：原论文，图4。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：多粒度语义后融合。
- 使用场景：语义增强推荐。

### 5. Connections to Related Work

- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec maps RQ-VAE codes to new out-of-vocabulary tokens; GRAM builds hierarchical IDs from existing vocabulary tokens and verbalizes collaborative signals in item prompts.
  - Source: GRAM v1, Section 3.2.1 contrasts the token choice: https://arxiv.org/html/2506.01673v1#S3.SS2.SSS1.p3; baselines and Table 2: https://arxiv.org/html/2506.01673v1#S4.p3 and https://arxiv.org/html/2506.01673v1#S4.T2; inference time in Table 7: https://arxiv.org/html/2506.01673v1#A3.T7.
- **Competitor** · [IDGenRec](idgenrec.md): IDGenRec generates textual IDs with a learned ID generator; GRAM derives hierarchical textual IDs by clustering, and the authors rerun IDGenRec without user IDs that leak test items.
  - Source: GRAM v1, baselines and Table 2: https://arxiv.org/html/2506.01673v1#S4.p3 and https://arxiv.org/html/2506.01673v1#S4.T2; reproduction in Table 9 and Appendix E: https://arxiv.org/html/2506.01673v1#A4.T9 and https://arxiv.org/html/2506.01673v1#A5.p3.
- **Competitor** · [TIGER](tiger.md): TIGER uses RQ-VAE codes as new tokens; GRAM's ID-type study also tests RQ-VAE IDs inside GRAM against hierarchical textual IDs.
  - Source: GRAM v1, baselines and Table 2: https://arxiv.org/html/2506.01673v1#S4.p3 and https://arxiv.org/html/2506.01673v1#S4.T2; Table 4 ID types: https://arxiv.org/html/2506.01673v1#S5.T4 and https://arxiv.org/html/2506.01673v1#S5.SS3.p1.
- **Competitor** · [CID](cid.md): P5-CID, P5-SID, and P5-SemID are fixed indexing schemes for P5; GRAM adds hierarchical semantic text IDs and collaborative prompts.
  - Source: GRAM v1, baselines and Table 2: https://arxiv.org/html/2506.01673v1#S4.p3 and https://arxiv.org/html/2506.01673v1#S4.T2; 5-core setting follows Hua et al. (2023): https://arxiv.org/html/2506.01673v1#S4.p1.
- **Competitor** · [LETTER](letter.md): LETTER learns a regularized RQ-VAE tokenizer; GRAM avoids learned codebooks and uses text clustering mapped to vocabulary tokens.
  - Source: GRAM v1, baselines and Table 2: https://arxiv.org/html/2506.01673v1#S4.p3 and https://arxiv.org/html/2506.01673v1#S4.T2.

[View all papers in this cell](../../README.md#i--tokenization)
