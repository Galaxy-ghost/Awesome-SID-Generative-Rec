# GNPR-SID

*Generative Next POI Recommendation with Semantic ID* — Wang et al. · KDD’25

`I. Informativeness` · `Tokenization` · `POI`

[Paper](https://arxiv.org/abs/2506.01375) · [Code](https://github.com/wds1996/GNPR-SID) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Attr+Geo+CF` | **`RQ-VAE`** | `Dec-Only` | `Fixed / NTP` | `–` |

- `Attr+Geo+CF`: Category and other attributes, plus geography, plus CF (POI).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 2. How It Works

![GNPR-SID architecture diagram](../../architectures/gnpr-sid.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Foursquare NYC and TKY, Gowalla CA. POIs with fewer than 10 interactions and users with fewer than 10 check-ins are removed (following Yan et al. 2023). Sizes (users / POIs): NYC 1,083 / 5,135; TKY 2,293 / 7,873; CA 6,592 / 14,027.
  - Source: Datasets, filters, splits: https://arxiv.org/html/2506.01375v2#S5.SS1.p1; statistics: https://arxiv.org/html/2506.01375v2#S5.T1.
- **Split**: Records sorted by time and split 80% / 10% / 10% into training, validation, and test; within each user's test sequence the last visited POI is the target. Separate cross-city test: train on one city and test on the others (Table 5).
  - Source: Temporal 80/10/10 split and last-visit target: https://arxiv.org/html/2506.01375v2#S5.SS1.p1; out-of-domain transfer: https://arxiv.org/html/2506.01375v2#S6.T5.
- **Candidates**: not reported (full catalog versus sampled candidates); the metric is top-1 accuracy (Acc@1) of the generated POI.
  - Source: Top-1 accuracy only: https://arxiv.org/html/2506.01375v2#S5.SS3.p1.
- **Visibility**: warm; users and POIs that do not appear in the training set are removed from the test set. The cross-city test in Table 5 uses POIs from another city, but their tokenizer visibility is not reported.
  - Source: Test users and POIs absent from training are removed: https://arxiv.org/html/2506.01375v2#S5.SS1.p1.
- **SID**: 3-level RQ-VAE with 32 (NYC) or 64 (TKY, CA) codewords of dimension 64, k-means-initialized, plus diversity and compactness losses. Remaining collisions get an appended fourth token that makes each POI's SID unique (e.g. <d_0>, <d_1>). Table 4 reports unique SIDs and collisions before the suffix (e.g. NYC 590 collisions at lambda=0.25).
  - Source: 3 layers x 32 (NYC) or 64 (TKY, CA), dimension 64, k-means initialization: https://arxiv.org/html/2506.01375v2#S5.SS2.p1; collision suffix: https://arxiv.org/html/2506.01375v2#S4.SS1.SSS2.p6; diversity loss and collision counts: https://arxiv.org/html/2506.01375v2#S4.SS1.SSS3.Px3.p1 and https://arxiv.org/html/2506.01375v2#S6.T4.
- **Inference budget**: LLaMA3-8B with LoRA; decoding method not reported beyond top-1 prediction. Fine-tuning on 4 NVIDIA L40 GPUs (batch 2 per GPU); inference batch size not reported. Table 6 (NYC): total test time 110.62 s versus 230.36 s for LLM4POI.
  - Source: Hardware for fine-tuning: https://arxiv.org/html/2506.01375v2#S5.SS2.p1; efficiency table: https://arxiv.org/html/2506.01375v2#S6.T6; decoding not specified in Section 5.
- **Results from**: Table 2 (Acc@1 on NYC, TKY, CA versus traditional, Transformer, GCN, time-aware, and LLM-based baselines); Table 3 (ablations); Table 4 (diversity-loss weight and SID collisions); Table 5 (cross-city generalization); Table 6 (efficiency).
  - Source: Main: https://arxiv.org/html/2506.01375v2#S6.T2; ablation: https://arxiv.org/html/2506.01375v2#S6.T3; diversity loss: https://arxiv.org/html/2506.01375v2#S6.T4; cross-city: https://arxiv.org/html/2506.01375v2#S6.T5; efficiency: https://arxiv.org/html/2506.01375v2#S6.T6.

## 旧卡片说明

迁自 `d61aa6c:papers/gnprsid.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### GNPR-SID：基于语义标识的生成式下一兴趣点推荐

> GNPR-SID 将 POI 的语义、地理、时间和协同信息构造成层次化 SID，再由大语言模型直接生成下一 POI 的完整标识。

### 研究动机与问题定义

传统下一 POI 推荐常使用随机数值 ID，模型难以从相近地点的标识之间迁移语义和地理关系。GNPR-SID 研究如何把 POI 描述与用户协同信息编码为可生成的语义标识，并根据用户历史访问记录和目标时间预测下一访问地点。

### TL;DR（核心摘要）

`POI内容/地理/时间/协同信息 → RQ-VAE量化 → POI SID → LLM生成 → 下一POI`

模型先用 POI 类别、区域、营业时间和协同关系构成语义向量，再用带多样性约束的残差量化得到层次化 SID；随后将用户历史 SID 与时间组织为提示，微调 LLM 自回归生成目标 SID。生成的 SID 通过标识表直接解析为 POI，不需要独立排序模型。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | POI 类别、区域、营业时间、用户协同信号和历史访问时间 |
| 信息融入位置 | SID 构建阶段及 LLM 的序列生成输入 |
| 语义标识结构 | 定长、多级离散序列 |
| 适用场景 | 下一 POI 推荐、跨域泛化和冷启动分析 |

### 方法设计

#### 4.1 语义标识构建
作者将 POI 的类别、区域、时间信号以及用户协同关系拼接为统一语义表示。协同部分依据用户共同访问 POI 的关系构造，使表示同时包含内容相似性和行为关联。

#### 4.1.1 POI 语义表示
每个 POI 的基本属性被转换为 one-hot 特征，并与区域、营业时间和协同用户信息拼接。这样构造出的向量既描述 POI 本身，也保留其在交互网络中的位置。

#### 4.1.2 POI 量化
模型使用 RQ-VAE 的编码器、残差量化器和解码器，将连续 POI 表示映射到多级 codebook。每一级量化当前残差，多个 code 组成层次化 SID；相近 POI 可共享前缀，从而为生成模型提供可迁移的语义结构。

#### 4.1.3 模型优化
除重构和量化目标外，方法加入 diversity loss，使 code 在离散空间中更均匀分布，减少大量 POI 使用相同 code 或形成碰撞。附录还给出了裁剪、填空式训练等数据增强方式。

#### 4.2 生成式 POI 推荐
用户历史被序列化为带时间的 SID 序列，模型在指定时间条件下生成下一 POI SID。训练阶段采用语言模型微调目标；推理时直接生成完整 SID 并通过映射确定 POI。论文还比较了移除 SID、时间信息和多样性损失后的效果。

### 实验结论

- 在三个 POI 数据集上，GNPR-SID 相比比较方法取得更好的下一地点预测效果，论文报告最高约 16% 的准确率提升。
- SID 的语义相关性分析表明，相似 POI 更倾向共享前缀；多样性损失有助于缓解离散标识分布不均。
- 论文报告了跨域、效率和序列长度分析，说明语义标识输入能减少部分生成负担，但具体线上服务收益未报告。

### 局限性与研究定位

#### 局限性

- SID 仍依赖离线量化和固定 POI 标识表，动态新增 POI 的处理方式未充分展开。
- 多级自回归生成的在线延迟和无效 SID 的容错机制仍需更系统的工程评估。

#### 研究定位

GNPR-SID 是较早将 Semantic ID 直接用于下一 POI 生成的工作，适合放在“地理场景生成式推荐”章节，重点体现内容-协同融合量化与时间条件生成。

### 相关资源

- [论文原文](https://arxiv.org/abs/2506.01375)
- [开源代码](https://github.com/wds1996/GNPR-SID)

### 标签

`下一兴趣点推荐` · `残差量化` · `多样性损失` · `大语言模型`

### 架构图来源

*图源：原论文，图2（[论文原文](https://arxiv.org/abs/2506.01375)）。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：将语义、地理、时间和协同信息构造成可生成 SID。
- 使用场景：下一 POI 推荐。

### 5. Connections to Related Work

- **Predecessor** · [LC-Rec](lc-rec.md): GNPR-SID follows LC-Rec in aligning an LLM to SID tokens through language-task prompts, and adds POI-specific quantization with time-aware prompts.
  - Source: GNPR-SID v2, Section 4.2 builds its prompts inspired by Zheng et al. (2024): https://arxiv.org/html/2506.01375v2#S4.SS2.p2.
- **Alternative** · [TIGER](tiger.md): TIGER is cited as generative recommendation with semantic IDs for products; GNPR-SID adapts RQ-VAE SIDs to POIs with diversity and compactness losses and an LLM generator.
  - Source: GNPR-SID v2, Section 2 cites Rajput et al. (2023): https://arxiv.org/html/2506.01375v2#S2.p2; not a baseline in Table 2.
- **Alternative** · [GeoGR](geogr.md): GeoGR later builds geo-aware SIDs from geographic co-visitation and an EM refinement loop, and reports gains over GNPR-SID's SIDs.
  - Source: Evidence is from the later GeoGR paper: it follows GNPR-SID preprocessing and compares against it in Tables 2, 3, and 5: https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p2, https://arxiv.org/html/2602.10411v2#S5.T2, https://arxiv.org/html/2602.10411v2#S5.T3, https://arxiv.org/html/2602.10411v2#S5.T5.

[View all papers in this cell](../../README.md#i--tokenization)
