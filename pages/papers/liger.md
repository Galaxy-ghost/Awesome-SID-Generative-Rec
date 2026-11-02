# LIGER

*Unifying generative and dense retrieval for sequential recommendation* — Yang et al. · arXiv’24

`VI. Generalization` · `Inference`

[Paper](https://arxiv.org/abs/2411.18814) · [Matrix](../../README.md#vi--inference)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed / NTP + Dense` | **`Hybrid`** |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Dense`: NTP plus dense-vector prediction.

### TL;DR

LIGER integrates sequential dense retrieval into a Semantic ID generative retriever, after a controlled comparison of both approaches, to narrow their performance gap and improve cold-start recommendation.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Key Contribution | LIGER integrates sequential dense retrieval into a Semantic ID generative retriever, after a controlled comparison of both approaches, to narrow their performance gap and improve cold-start recommendation. |
| Modified Stage | Inference |

### 2. How It Works

![LIGER architecture diagram](../../architectures/liger.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty, Sports and Outdoors, Toys and Games, and Steam with 5-core filtering of users and items; sequences truncated to the 20 most recent items. Sizes (users / items / cold-start items): Beauty 22,363 / 12,101 / 43; Toys 19,412 / 11,924 / 56; Sports 35,598 / 18,357 / 81; Steam 47,761 / 12,012 / 400.
  - Source: Datasets, 5-core, truncation: https://arxiv.org/html/2411.18814v2#S4.SS1.p1; statistics and cold-start counts: https://arxiv.org/html/2411.18814v2#A2.T3.
- **Split**: Per-user leave-one-out: last item for test, preceding item for validation, the rest for training; early stopping on in-set NDCG@10; mean and standard deviation over three seeds. Test targets are reported separately for in-set and cold-start items.
  - Source: Leave-one-out allocation: https://arxiv.org/html/2411.18814v2#S4.SS1.p4; three seeds: https://arxiv.org/html/2411.18814v2#S4.SS2.p1.
- **Candidates**: Hybrid: generative retrieval returns K=20 candidates by beam search, which are ranked together with the cold-start items by dense retrieval (K swept from 20 to 100 and K=N in Table 4). Dense baselines score the full catalog.
  - Source: Hybrid candidates (K from beam, ranked with cold-start items by dense scores): https://arxiv.org/html/2411.18814v2#S4.SS2.p2; K sweep: https://arxiv.org/html/2411.18814v2#A3.T4.
- **Visibility**: In-set targets: warm. Cold-start targets: unseen by tokenizer too; cold-start items are excluded from RQ-VAE training (the paper says to avoid contamination), and the generators fail to produce them. Exact criterion for selecting cold-start items beyond the counts in Table 3: not reported.
  - Source: Cold-start items excluded from RQ-VAE training: https://arxiv.org/html/2411.18814v2#S4.SS1.p4; cold-start definition beyond counts not stated.
- **SID**: 3-level RQ-VAE x 256 codewords (dimension 128) over sentence-T5-XXL text embeddings; following TIGER, an extra token is appended to make IDs unique.
  - Source: 3 levels x 256 with dimension 128 and an extra uniqueness token: https://arxiv.org/html/2411.18814v2#S4.SS1.p2.
- **Inference budget**: Beam search retrieves K candidates (K=20 for the main result) from a T5 encoder-decoder (6 layers each), then a dense head ranks them with cold-start items. Complexity is stated as O(tK) versus O(N) for dense retrieval (Table 1); hardware, inference batch size, and latency: not reported.
  - Source: Beam retrieval of K candidates and complexity: https://arxiv.org/html/2411.18814v2#S2.SS1.p3 and https://arxiv.org/html/2411.18814v2#S3.T1; model: https://arxiv.org/html/2411.18814v2#S4.SS1.p3.
- **Results from**: Table 2 (Beauty, Sports, Toys, Steam; in-set and cold-start Recall@10 and NDCG@10; three seeds); Table 4 (number of retrieved candidates K); Figures 1, 3, 4 (dense versus generative retrieval and cold-start generation probabilities); Appendix D (ablations).
  - Source: Main: https://arxiv.org/html/2411.18814v2#S4.T2; K sweep: https://arxiv.org/html/2411.18814v2#A3.T4; motivation figures: https://arxiv.org/html/2411.18814v2#S1.F1, https://arxiv.org/html/2411.18814v2#S2.F3, https://arxiv.org/html/2411.18814v2#S2.F4.

## 旧卡片说明

迁自 `d61aa6c:papers/liger.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### LIGER：生成检索与稠密检索统一

> LIGER 将生成式检索与稠密检索结合，以缓解生成模型对冷启动物品和开放物品集合的覆盖不足。

### 研究动机与问题定义

生成式检索能直接生成 SID，但对训练集中未出现或难以生成的物品不够稳健；稠密检索具有更好的开放集合覆盖。LIGER 研究两者的混合推荐流程。

### TL;DR（核心摘要）

`用户历史 → 生成式检索候选 + 稠密检索候选 → 外部融合/排序 → 推荐物品`

模型先用生成式检索产生 SID 候选，再将其与稠密检索结果及冷启动候选合并，并通过编码器相似度进行最终排序。因此，完整 SID 并不能单独决定最终推荐物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户序列、SID 表示和稠密用户/物品向量 |
| 信息融入位置 | 生成召回、稠密召回和融合排序 |
| 语义标识结构 | 多 token 序列 |
| 适用场景 | 开放物品、冷启动和混合检索 |

### 方法设计

#### 2.1 生成式检索与稠密检索
LIGER 对比两条序列推荐链路：生成式模型根据历史 SID 束搜索目标标识，稠密模型将历史和物品文本编码为向量并进行相似度检索。两者在物品表示、输入信息和预测机制上不同。

#### 2.2 混合检索模型
LIGER 将语义 ID、物品位置和文本表示共同输入编码器，同时产生用户/目标物品的稠密表示。生成式候选、稠密候选和冷启动物品被合并，再依据表示相似度完成最终排序。

#### 2.3 冷启动分析
论文重点研究生成式检索对未见物品的覆盖不足，并用稠密检索补充开放物品集合。该设计提升覆盖，但也意味着完整 SID 不是最终推荐的唯一决定因素。

#### 2.4 实验与讨论
实验比较生成、稠密和混合方法在集合内/集合外数据上的效果，并分析 SID 输入、文本表示和候选融合的作用。

### 实验结论

- 混合检索改善了生成模型对未见物品的覆盖。
- 稠密检索与生成检索具有互补性。

### 局限性与研究定位

#### 局限性
- 需要外部稠密检索和最终排序，未实现纯生成式端到端推荐。
- 多路召回与融合增加线上服务链路和延迟。

#### 研究定位
LIGER 适合放在“生成式推荐与稠密检索融合”章节。

### 标签

`生成检索` · `稠密检索` · `混合检索` · `冷启动`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 检索方式补充

迁自 `d61aa6c:tables/boundary-and-excluded-methods.md` 的机制说明。

生成 SID 后仍依赖稠密检索、候选融合和最终排序。

旧表的“核心／边界／排除”分组已由当前问题与阶段分类取代。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER retrieves only by beam search over semantic IDs and almost never generates cold-start items; LIGER reranks TIGER-style beam candidates plus cold-start items with a dense head trained jointly.
  - Source: LIGER v2, faithful TIGER implementation: https://arxiv.org/html/2411.18814v2#S1.p5; Table 2: https://arxiv.org/html/2411.18814v2#S4.T2; cold-start analysis of TIGER's epsilon quota: https://arxiv.org/html/2411.18814v2#S2.SS4.p3; LIGER builds on TIGER: https://arxiv.org/html/2411.18814v2#S4.SS2.p2.
- **Alternative** · [VQ-Rec](vq-rec.md): VQ-Rec uses vector-quantized codes inside a dense retriever; LIGER keeps generative beam search and adds dense ranking only over a small candidate set.
  - Source: LIGER v2, Appendix A related work: https://arxiv.org/html/2411.18814v2#A1.p2.
- **Alternative** · [COBRA](cobra.md): COBRA later cascades sparse-ID generation with a generated dense vector inside one decoder and cites LIGER for the fine-grained similarity gap of generative methods.
  - Source: Evidence is from the later COBRA paper, Section 1: https://arxiv.org/html/2503.02453v1#S1.p3.
- **Successor** · [GEM-Rec](gem-rec.md): GEM-Rec later builds on LIGER's reproduction of the TIGER architecture and its 5-core preprocessing.
  - Source: Evidence is from the later GEM-Rec paper, Section 5.4 and Appendix B.1: https://arxiv.org/html/2603.22231v1#S5.SS4.p1 and https://arxiv.org/html/2603.22231v1#A2.SS1.p1.

[View all papers in this cell](../../README.md#vi--inference)
