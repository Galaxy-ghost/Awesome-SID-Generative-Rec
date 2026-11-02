# ColaRec

*Content-based collaborative generation for recommender systems* — Wang et al. · CIKM’24

`I. Informativeness` · `Backbone`

[Paper](https://arxiv.org/abs/2403.18480) · [Code](https://github.com/Junewang0614/ColaRec) · [Matrix](../../README.md#i--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `H-KM` | **`Enc-Dec`** | `Fixed / NTP + Ctr.` | `C-Beam` |

- `H-KM`: Hierarchical k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Backbone |

### 2. How It Works

![ColaRec architecture diagram](../../architectures/colarec.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Product Reviews: Beauty, Sports and Outdoors, Cell Phones and Accessories (Phone); Food.com Recipe. Users and items with fewer than 5 interactions are filtered. Sizes (users / items / interactions): Beauty 22,363 / 12,101 / 198,502; Sports 35,598 / 18,357 / 296,337; Phone 27,879 / 10,429 / 194,439; Recipe 17,813 / 41,240 / 555,618.
  - Source: Datasets and 5-interaction filter: https://arxiv.org/html/2403.18480v2#S5.SS1.p1; statistics: https://arxiv.org/html/2403.18480v2#S4.T1.
- **Split**: General recommendation, not sequential: each user's interactions are randomly split 8:1:1 into training, validation, and test. Three runs are averaged.
  - Source: Random 8:1:1 per-user split for general (non-sequential) recommendation: https://arxiv.org/html/2403.18480v2#S5.SS2.p1.
- **Candidates**: full catalog
  - Source: Candidate set is the whole item set: https://arxiv.org/html/2403.18480v2#S5.SS2.p1.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Random interaction split with no cold-start experiment: https://arxiv.org/html/2403.18480v2#S5.SS2.p1; long-tail users are analyzed separately: https://arxiv.org/html/2403.18480v2#S5.T3.
- **SID**: GID length l=3 from hierarchical constrained K-means over pretrained LightGCN item embeddings, K=32 clusters per level (48 for Recipe). Collisions are avoided by construction: clusters hold at most K^(l-t) items and leaf positions are assigned randomly, so each item has a unique GID.
  - Source: Constrained hierarchical K-means over LightGCN embeddings, random leaf assignment, one unique GID per item: https://arxiv.org/html/2403.18480v2#S4.SS2.p1 and https://arxiv.org/html/2403.18480v2#S4.SS2.p2; l=3, K=32 (Recipe 48): https://arxiv.org/html/2403.18480v2#S5.SS4.p1.
- **Inference budget**: Constrained beam search over valid GID prefixes; numerical beam width not reported. T5-small backbone. Recall and NDCG at n=5 and 10 (Table 2). Hardware, inference batch size, and latency: not reported.
  - Source: Constrained beam search: https://arxiv.org/html/2403.18480v2#S4.SS5.p5; no numerical width found in Section 5.
- **Results from**: Table 2 (four datasets; mean of three runs); Table 3 (long-tail users); Table 4 (multi-task ablation and GID types); Figures 4-5 (GID length and cluster number).
  - Source: Main: https://arxiv.org/html/2403.18480v2#S4.T2; long-tail users: https://arxiv.org/html/2403.18480v2#S5.T3; ablation and GID types: https://arxiv.org/html/2403.18480v2#S5.T4; GID length and K: https://arxiv.org/html/2403.18480v2#S5.SS7.SSS2.p1 and https://arxiv.org/html/2403.18480v2#S5.SS7.SSS2.p2.

## 旧卡片说明

迁自 `d61aa6c:papers/colarec.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### ColaRec：基于内容的协同生成推荐

> ColaRec 用 GNN 协同表示构造生成标识，并联合内容信息与推荐目标，直接生成物品 GID。

### 研究动机与问题定义

随机或纯内容型物品 ID 难以表达协同关系。ColaRec 将 GNN 学到的协同结构转化为层次化 GID，同时保留标题、描述等内容信息，解决生成推荐与物品索引之间的脱节。

### TL;DR（核心摘要）

`交互与内容 → GNN协同表示 → 层次化GID → 生成模型 → 推荐物品`

模型用 LightGCN 提取协同表示，以受约束的 K-means 构造树状 GID；用户-物品推荐和物品-GID 索引共享编码器-解码器。训练联合推荐、索引、排序和对比目标，生成的 GID 直接映射到物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户交互、物品文本内容和 GNN 协同表示 |
| 信息融入位置 | GID 构建、模型输入和联合目标 |
| 语义标识结构 | 定长树状序列 |
| 适用场景 | 内容增强的生成式推荐 |

### 方法设计

#### 4.1 ColaRec 总体结构
ColaRec 共享一个编码器-解码器，同时服务用户-物品推荐和物品-GID 索引两个任务。前者学习用户历史到下一物品的映射，后者学习物品内容到协同生成标识的映射。

#### 4.2 生成标识构建（Generative Identifier Construction）
论文先用 GNN/LightGCN 学习物品协同表示，再以受约束的层次化聚类构造 GID。树的路径就是物品标识，前缀表达较粗粒度的相似性，叶节点区分具体物品；内容信息通过文本和描述进入索引任务。

#### 4.3 用户-物品推荐与物品-物品索引
推荐任务根据用户历史自回归生成目标 GID。索引任务要求模型根据物品文本生成其 GID，使内容表示和协同标识保持一致。两个任务共享生成器，但目标分别对应推荐和索引。

#### 4.4 多任务训练
总目标联合推荐损失、索引损失、排序损失和对比损失。消融实验分别验证内容、协同 GID 以及各辅助目标的作用。

### 实验结论

- 内容-协同联合建模优于单独使用任一来源信息。
- 推荐和索引任务的联合训练均有贡献。

### 局限性与研究定位

#### 局限性
- GID 依赖离线 GNN 与聚类，目录变化时需要更新。
- 生成标识长度、聚类规模和在线效率之间的权衡仍需进一步研究。

#### 研究定位
ColaRec 展示了用协同图结构学习生成标识的一条路径，适合放在“协同语义标识构建”章节。

### 标签

`内容-协同融合` · `GID` · `GNN` · `联合学习`

### 架构图来源

*图源：原论文，图3。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：用协同图结构学习GID。
- 使用场景：内容增强推荐。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER builds content-only RQ-VAE identifiers; ColaRec builds collaborative GIDs from LightGCN embeddings and aligns them with item content through item-item indexing.
  - Source: ColaRec v2, Section 5.3 baselines: https://arxiv.org/html/2403.18480v2#S5.SS3.p1 and https://arxiv.org/html/2403.18480v2#S5.I2.i8.p1 (adapted without sequential order); Table 2: https://arxiv.org/html/2403.18480v2#S4.T2.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec learns TIGER-style indices and aligns an LLM through language tasks; ColaRec uses a T5-small generator with collaborative GIDs and a contrastive ranking loss.
  - Source: ColaRec v2, Section 5.3 baselines: https://arxiv.org/html/2403.18480v2#S5.I2.i9.p1; Table 2: https://arxiv.org/html/2403.18480v2#S4.T2.
- **Alternative** · [CID](cid.md): P5-CID builds collaborative IDs for prompt-based P5 models that rank a candidate list in the prompt; ColaRec generates GIDs over the whole item set.
  - Source: ColaRec v2, Section 5.3 explains why P5-based methods including Hua et al. (2023) are excluded as baselines: https://arxiv.org/html/2403.18480v2#S5.SS3.p2; related work: https://arxiv.org/html/2403.18480v2#S2.SS2.p3.
- **Alternative** · [SEATER](seater.md): SEATER also builds tree-structured identifiers for generative recommendation; ColaRec derives its tree from collaborative LightGCN embeddings and adds content-based item-item indexing.
  - Source: ColaRec v2, Section 1 and Section 2.2 cite SEATER among generative identifier methods: https://arxiv.org/html/2403.18480v2#S1.p3 and https://arxiv.org/html/2403.18480v2#S2.SS2.p3; not a baseline in Table 2.

[View all papers in this cell](../../README.md#i--backbone)
