# LGSID

*LLM-Aligned Geographic Item Tokenization for Local-Life Recommendation* — Jiang et al. · AAAI’26

`I. Informativeness` · `Representation` · `POI`

[Paper](https://arxiv.org/abs/2511.14221) · [Code](https://github.com/JiangHaoPG11/LGSID) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Geo+CF`** | `Geo-Idx+RQ` | `Disc. / Enc-Dec` | `Fixed / Discrim. / NTP` | `Scoring / Beam†` |

- `Geo-Idx+RQ`: Geographic indexing combined with residual quantization.
- `Disc. / Enc-Dec`: Discriminative scoring and encoder–decoder generation variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim. / NTP`: Discriminative scoring or next-token prediction in different configurations.
- `Scoring / Beam†`: Discriminative candidate scoring vs. generative beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 2. How It Works

![LGSID architecture diagram](../../architectures/lgsid.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Kuaishou local-life feed data only: 50,000,000 samples, 19,080,888 users, 2,325,266 items, 19,408 brands, 818 categories, with item text and geographic location. For discriminative models, all positives are kept and negatives down-sampled 1:4. Further filtering: not reported.
  - Source: Industrial-only dataset and preprocessing: https://arxiv.org/html/2511.14221v1#A2.SS0.SSSx1.p1; statistics: https://arxiv.org/html/2511.14221v1#A2.T4.
- **Split**: Generative models: leave-one-out on the down-sampled data (last item for test, second-last for validation, the rest for training). Discriminative models: split rule not reported; settings selected on validation data.
  - Source: Leave-one-out for generative models on the down-sampled data: https://arxiv.org/html/2511.14221v1#A2.SS0.SSSx1.p1; split for discriminative AUC not stated.
- **Candidates**: Discriminative AUC: evaluation samples with negatives down-sampled at 1:4 to positives; how negatives are drawn and whether user history is excluded: not reported. Generative Hit and NDCG at 5 and 10: full catalog versus sampled not reported.
  - Source: Negative down-sampling and metrics: https://arxiv.org/html/2511.14221v1#A2.SS0.SSSx1.p1.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2511.14221v1#A2.SS0.SSSx1.p1.
- **SID**: Hierarchical residual quantizer over G-DPO-aligned BGE embeddings (1,024-dimensional) with a KL regularizer toward uniform cluster usage; number of levels and per-level codebook sizes K_l: not reported. Collision handling: not reported.
  - Source: Hierarchical quantizer with uniform-usage regularization: https://arxiv.org/html/2511.14221v1#Sx4.SSx3.p4 and https://arxiv.org/html/2511.14221v1#Sx4.SSx3.p5; BGE embeddings: https://arxiv.org/html/2511.14221v1#A2.SSx1.p1; no codebook sizes or collision rule found.
- **Inference budget**: SIDs are used as features in DIN, DIEN, SIM, TWIN, ETA and as targets in TIGER and OneRec generators; decoding method and beam width: not reported. All experiments on two 48GB GPUs; inference batch size and latency: not reported.
  - Source: Hardware: https://arxiv.org/html/2511.14221v1#A2.SSx2.p1; generative backbones: https://arxiv.org/html/2511.14221v1#A2.SSx3.p1.
- **Results from**: Table 1 (AUC of five discriminative rankers with different tokenizers); Table 2 (TIGER and OneRec generators with different tokenizers); Table 3 (semantic and geographic coverage after alignment); Table 5 (robustness over runs); Table 6 (similarity weight).
  - Source: Discriminative: https://arxiv.org/html/2511.14221v1#Sx5.T1; generative: https://arxiv.org/html/2511.14221v1#Sx5.T2; alignment: https://arxiv.org/html/2511.14221v1#Sx5.T3; robustness: https://arxiv.org/html/2511.14221v1#A4.T5; lambda: https://arxiv.org/html/2511.14221v1#A4.T6.

## 旧卡片说明

迁自 `d61aa6c:papers/lgsid.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### LGSID：大语言模型对齐的地理物品分词

> LGSID 先用地理偏好对齐大语言模型，再将地理属性和内容表示分别量化为层次化 SID，以增强本地生活推荐的空间一致性。

### 研究动机与问题定义

本地生活物品的语义相似并不等于地理可行。仅把地点写进提示词，可能无法让 LLM 学到细粒度的城市、区域和街道关系。LGSID 试图让 LLM 的表示具有真实空间知识，并把这种表示用于生成可解释的地理物品 SID。

### TL;DR（核心摘要）

`内容/地理信息 → 地理奖励模型与G-DPO → 地理/语义表示 → 层次化量化 → 判别式或生成式推荐`

方法首先利用正负地理提示训练 list-wise reward model，再通过 G-DPO 将空间关系和协同信号注入 LLM。随后从对齐后的 LLM 表示和离散地理属性中构造主 token，并用残差量化补充细节 token；SID 分别用于判别式与生成式推荐模型。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | POI 文本内容、行政区、地理位置和用户行为 |
| 信息融入位置 | LLM 对齐、主 token 构建、残差量化和生成输入 |
| 语义标识结构 | 层次化主 token 加残差 token |
| 适用场景 | 本地生活和地理约束推荐 |

### 方法设计

#### 3.1 地理奖励模型训练
作者构造内容相同或相近但地理位置不同的提示对，并用实际地理关系生成排序偏好。奖励模型输出内容-地理匹配分数，作为后续 LLM 对齐的监督信号。

#### 3.2 基于 G-DPO 的地理 LLM 对齐
G-DPO 使用正、负地理信息和奖励模型分数构造偏好优化目标。模型需要提高符合真实位置关系的响应概率，同时保留原有语义能力；双相似度对比损失进一步约束内容和地理表示。

#### 3.3 层次化地理物品分词
HGIT 从 POI 的行政区、品牌、类别等离散属性得到地理 code，再使用对齐 LLM 表示进行多级残差量化。最终 SID 的前缀具有较粗粒度地理含义，后续 token 表达更细的内容与位置差异。

#### 3.4 下游推荐
论文分别评估判别式模型（DIN、TWIN、ETA 等，Table 1）和生成式模型（TIGER、OneRec，Table 2）。前者使用 SID 特征对候选评分，后者生成 SID；当前记录以 A / B 写法保留两个分支。

### 实验结论

- 在 Kuaishou 本地生活数据上，LGSID 相比比较方法取得更好的离线 AUC 和推荐效果。
- 可视化和属性解码实验表明，层次化 SID 前缀能保留城市、区域等地理结构，并提高属性可解释性。
- 论文报告不同 token 化策略的分布差异，但动态物品和线上延迟结果未报告。

### 局限性与研究定位

#### 局限性

- G-DPO 需要构造地理偏好对和奖励模型，训练流程较复杂。
- 地理主 token 依赖行政与属性索引，对跨区域、属性缺失和新增 POI 的适应性仍需验证。

#### 研究定位

LGSID 位于“LLM 对齐驱动的地理 SID 构建”方向，突出先获得空间感知表示、再进行层次化量化的设计。

### 相关资源

- [论文原文](https://arxiv.org/abs/2511.14221)

### 标签

`地理物品分词` · `G-DPO` · `层次化SID` · `本地生活`

### 架构图来源

*图源：原论文，图2（[论文原文](https://arxiv.org/abs/2511.14221)）。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：用地理对齐和层次化分词增强空间一致性。
- 使用场景：本地生活推荐。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER's RQ-VAE is a tokenizer baseline and TIGER is one of two generative backbones; LGSID aligns the LLM embedding with geographic rewards before a hierarchical quantizer.
  - Source: LGSID v1, baselines: https://arxiv.org/html/2511.14221v1#A2.SSx3.p1; Tables 1 and 2: https://arxiv.org/html/2511.14221v1#Sx5.T1 and https://arxiv.org/html/2511.14221v1#Sx5.T2.
- **Predecessor** · [OneRec](onerec.md): OneRec serves as the second generative backbone into which LGSID's SIDs are plugged.
  - Source: LGSID v1, baselines: https://arxiv.org/html/2511.14221v1#A2.SSx3.p1; Table 2: https://arxiv.org/html/2511.14221v1#Sx5.T2.
- **Alternative** · [GNPR-SID](gnpr-sid.md): GNPR-SID builds POI SIDs for next-POI generation; LGSID targets local-life ranking features and aligns embeddings with geographic distance rewards.
  - Source: LGSID v1, related work: https://arxiv.org/html/2511.14221v1#Sx2.SSx2.p1 and https://arxiv.org/html/2511.14221v1#Sx4.SSx2.p1.
- **Successor** · [LGRID](lgrid.md): LGRID later follows LGSID's candidate protocol and replaces its single fused representation with disentangled geographic and semantic streams.
  - Source: Evidence is from the later LGRID paper: protocol https://arxiv.org/html/2607.27944v1#A1.SS3.p2; baseline and collision comparison https://arxiv.org/html/2607.27944v1#S4.SS1.p2 and https://arxiv.org/html/2607.27944v1#S4.T5.

[View all papers in this cell](../../README.md#i--representation)
