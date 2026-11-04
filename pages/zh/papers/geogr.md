# GeoGR

[← 问题 × 阶段矩阵](../../../README.zh.md#i--representation) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/geogr.md) | 中文

| **题目** | *Enabling Spatio-Temporal Aware Industrial-Scale Generative POI Recommendations* |
| :-- | :-- |
| **作者** | Wang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `I. 信息量` · `物品表示（Representation）` · `POI` |
| **改动** | ● 物品表示 · ○ 编号器更新 |
| **构码输入** | `Text` + `Geo` + `CF` |
| **领域** | `本地生活与 POI` · `搜索` |
| **应用场景** | `POI 与本地生活` · `查询驱动检索`；`线上实验或部署` |
| **链接** | [论文](https://arxiv.org/abs/2602.10411) |
| **阅读级别** | 阅读笔记（第 2 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>● Text+Geo+CF"] --> T["构码 Tokenization<br/>R-KM+EM"] --> B["生成骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>编号器更新: ○ Altern.†<br/>训练目标: Multi-task NTP"] --> I["推理 Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class R main
```

- `Text+Geo+CF`：文本表征结合地理空间特征与协同信号。
- `R-KM+EM`：带期望最大化（EM）精化的残差 k-means。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Altern.†`：编号器与生成器交替迭代更新（由配置推断）。
- `Multi-task NTP`：在多个对齐或推荐子任务上联合优化下一 token 预测损失。
- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。

### TL;DR

> [!NOTE]
> GeoGR 从受地理约束的共访对出发，经对比学习与迭代修正构建地理感知 POI SID，再通过持续预训练与微调将 LLM 与之对齐。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 主要发现 | 在高德地图（AMAP）为期三个月的线上部署中，GeoGR 取得 WINRATE +2.91% 与 PV_CTR +5.55% 的在线收益（Abstract）。 |
| 局限 | 语义 ID（Semantic ID，SID）依赖 LLM 的预测分布迭代重分配，码本版本与精修所用的特定 LLM 检查点绑定（Sec. 4.1.3）。 |

---

### 1. 为什么重要

常规兴趣点（POI）SID 编号器难以捕捉跨品类的时空共访关系，生成的离散码也与预训练大语言模型（LLM）存在分布错位（Abstract）。GeoGR 面向高德等工业级导航场景，先用 Swing 加权的时空共访对比损失训练编码器，再通过类 EM 的两阶段循环交替优化 RQ-Kmeans 码与 Qwen 生成器。

> "Instead, we explicitly model the joint constraints of geographic proximity and behavioral co-occurrence by constructing spatiotemporal co-visit POI pairs."（Sec. 4.1.1）

---

### 2. 方法

![GeoGR architecture diagram](../../../architectures/geogr.png)

```mermaid
flowchart LR
    subgraph Tok["地理-协同初始化"]
        A("POI 文本、坐标与 geohash") --> B["Qwen 编码器"]
        C("轨迹共访 POI 对") --> L1{{"Swing 加权 NCE（Eq. 4）"}}
        L1 -.-> B
        B --> D["3 层 RQ-Kmeans"]
    end
    subgraph Loop["EM 交替精修"]
        D --> E("层级 SID")
        E --> P1["阶段 1：固定 SID，CPT + SFT 微调 LLM"]
        P1 --> P2["阶段 2：固定 LLM，20 候选动态束重分配 SID"]:::key
        P2 -.->|更新码表| E
    end
    P1 --> H["动态束搜索"] --> O("Top-k POI")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 位置描述

每个 POI 的输入描述拼接经纬度坐标、地址以及名称、品牌、品类、geohash 编码、消费水平、活跃时段等属性，由 Qwen 编码器映射为稠密向量（Sec. 4.1.1）。

#### 共访对比学习

在用户轨迹中高频共现的 POI 对按 Swing 相似度赋权，压低热门地标的权重后以 NCE 对比损失训练编码器（Sec. 4.1.1，Eq. 4）。

#### 量化与迭代精修

RQ-Kmeans 先将对齐后的嵌入离散化为初始 3 层层级 SID（Sec. 1），随后交替更新生成器与重分配 SID：

> "As shown in Algorithm 1, the framework alternates between two phases: (1) fixing the SIDs and fine-tuning the LLM to better predict them, and (2) fixing the LLM and updating the SIDs based on its predictions."（Sec. 4.1.3）

#### 多阶段 LLM 训练

新增 SID token 不在基座词表内，GeoGR 先通过多任务提示模板执行继续预训练（CPT），注入 POI 属性与行为序列知识（Sec. 4.2.1），再经监督微调（SFT）学习下一 POI 生成（Abstract）。

> "Since the newly introduced SID tokens are out-of-vocabulary for the base LLM, we first perform Continued Pre-Training (CPT) to warm up these tokens and inject scenario-specific recommendation knowledge."（Sec. 4.2）

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Foursquare NYC and TKY (11 months of check-ins; POIs with fewer than 10 interactions and users with fewer than 10 check-ins removed, following GNPR-SID; 2,083 users / 5,135 POIs and 2,293 / 7,873), and AMAP industrial data: AMAP (one day of platform-wide traffic with users' traced histories; 7,536K users / 34,119K POIs) and AMAP-SH (one month in Shanghai; 4,820K users / 910K POIs). Industrial filtering rules: not reported.
  - 出处：Datasets and filtering: [S5.SS1.SSS1.p1](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p1) and [S5.SS1.SSS1.p2](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p2); statistics: [S5.T1](https://arxiv.org/html/2602.10411v2#S5.T1).
- **切分**：NYC and TKY: records sorted by time and split 80% / 10% / 10% into training, validation, and test. AMAP: one day for training and 1 million records randomly sampled from the following day for testing. AMAP-SH: last day held out for testing. Online: three-month A/B test against the legacy multi-stage retrieval.
  - 出处：Splits: [S5.SS1.SSS1.p2](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p2); online test: [S5.SS9.p2](https://arxiv.org/html/2602.10411v2#S5.SS9.p2).
- **候选集**：not reported (full catalog versus sampled evaluation candidates); top-k SIDs come from beam search.
  - 出处：Metrics only: [S5.SS1.SSS2.p1](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS2.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Temporal splits with no unseen-POI protocol: [S5.SS1.SSS1.p2](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p2).
- **SID 规格**：3 RQ-Kmeans layers over Qwen-4B POI embeddings with geographic co-visitation alignment; codebook size stated as 32 and 64 for NYC and TKY, respectively, and 4,096 for AMAP and AMAP-SH. SIDs are refined by an EM-style loop with the LLM, using a 20-candidate dynamic beam to prevent SID collisions; a final collision-resolution rule is not reported.
  - 出处：Three RQ-Kmeans layers and codebook sizes: [S5.SS1.SSS4.p1](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS4.p1) and [S4.SS1.SSS2.p2](https://arxiv.org/html/2602.10411v2#S4.SS1.SSS2.p2); RQ-Kmeans following OneRec: [S4.SS1.p1](https://arxiv.org/html/2602.10411v2#S4.SS1.p1); EM refinement with 20-candidate beam to avoid collisions: [S4.SS1.SSS3.p1](https://arxiv.org/html/2602.10411v2#S4.SS1.SSS3.p1).
- **推理预算**：Offline: beam search for the top-k SIDs; numerical beam width not reported. Online: dynamic beam search generating 50 candidate SIDs per request; GeoGR-0.6B averages 50 ms per request on NVIDIA H20 GPUs versus 90 ms for GeoGR-4B; inference batch size not reported. Training on 16 H20 GPUs with per-GPU batch 16.
  - 出处：Beam search for top-k: [S4.SS2.SSS2.p4](https://arxiv.org/html/2602.10411v2#S4.SS2.SSS2.p4); deployment budget and latency: [S5.SS9.p1](https://arxiv.org/html/2602.10411v2#S5.SS9.p1); training hardware: [S5.SS1.SSS4.p1](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS4.p1).
- **结果来源**：Table 2 (NYC, TKY versus traditional, POI, and generative baselines); Table 3 (AMAP, AMAP-SH); Table 4 (ablation); Table 5 (SID quality); Table 6 (CPT effect); Section 5.6 (model scaling); Table 7 and Section 5.9 (three-month online A/B test).
  - 出处：Public: [S5.T2](https://arxiv.org/html/2602.10411v2#S5.T2); industrial: [S5.T3](https://arxiv.org/html/2602.10411v2#S5.T3); ablation: [S5.T4](https://arxiv.org/html/2602.10411v2#S5.T4); SID evaluation: [S5.T5](https://arxiv.org/html/2602.10411v2#S5.T5); CPT: [S5.T6](https://arxiv.org/html/2602.10411v2#S5.T6); scaling: [S5.SS6.p2](https://arxiv.org/html/2602.10411v2#S5.SS6.p2); online: [S5.SS9.p2](https://arxiv.org/html/2602.10411v2#S5.SS9.p2).

</details>

- 离线对比：GeoGR 在 Foursquare 与高德等多个真实数据集上优于传统序列推荐、POI 推荐与生成式基线（Abstract）。
- 在线部署：在高德平台覆盖数百万用户的三个月在线 A/B 测试中，GeoGR 相比线上多级召回基线取得 WINRATE +2.91%、PV_CTR +5.55% 的提升（Abstract）。

---

### 4. 局限与分析

**Our analysis.**

- OneLoc 在表征中引入视觉模态并用 DPO 对齐 `Enc-Dec` 生成器；GeoGR 在编号阶段融合时空共访信号，并用 `Multi-task NTP` 训练 `Dec-Only` LLM。
- GNPR-SID 在训练生成器前冻结 `RQ-VAE` 码本；GeoGR 则根据生成器的预测概率迭代精修 `R-KM+EM` 码分配。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["GeoGR"]
    P -->|"同期对比"| A["OneLoc"]
    P -->|"同期对比"| B["GNPR-SID"]
    P -->|"同期对比"| C["TIGER"]
    P -->|"前序工作"| D["OneRec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **同期对比** · [OneLoc](oneloc.md): OneLoc injects geography into the SID input embedding and adds geographic rewards; GeoGR builds geo-aware SIDs from geographically constrained co-visitation and refines them with an EM loop tied to the LLM.
  - 出处：GeoGR v2, Table 2 (POI baseline) and Table 3 (strongest industrial baseline): [S5.T2](https://arxiv.org/html/2602.10411v2#S5.T2) and [S5.T3](https://arxiv.org/html/2602.10411v2#S5.T3); discussion in Section 5.2.2: [S5.SS2.SSS2.p3](https://arxiv.org/html/2602.10411v2#S5.SS2.SSS2.p3).
- **同期对比** · [GNPR-SID](gnpr-sid.md): GNPR-SID builds POI semantic IDs for next-POI generation; GeoGR follows its preprocessing and adds co-visitation alignment, EM-style SID refinement, and CPT plus SFT.
  - 出处：GeoGR v2, follows the GNPR-SID preprocessing: [S5.SS1.SSS1.p2](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p2); Tables 2, 3, 5, and 6: [S5.T2](https://arxiv.org/html/2602.10411v2#S5.T2), [S5.T3](https://arxiv.org/html/2602.10411v2#S5.T3), [S5.T5](https://arxiv.org/html/2602.10411v2#S5.T5), [S5.T6](https://arxiv.org/html/2602.10411v2#S5.T6).
- **同期对比** · [TIGER](tiger.md): TIGER uses content RQ-VAE SIDs with a small Transformer; GeoGR uses geo-aware RQ-Kmeans SIDs with an LLM aligned through continued pre-training.
  - 出处：GeoGR v2, Tables 2 and 3: [S5.T2](https://arxiv.org/html/2602.10411v2#S5.T2) and [S5.T3](https://arxiv.org/html/2602.10411v2#S5.T3).
- **前序工作** · [OneRec](onerec.md): GeoGR adopts OneRec's RQ-Kmeans tokenization and adds geographic co-visitation signals and EM-style refinement.
  - 出处：GeoGR v2, Section 4.1 adopts the RQ-Kmeans strategy of Deng et al. (2025): [S4.SS1.p1](https://arxiv.org/html/2602.10411v2#S4.SS1.p1).

[查看同格全部论文](../../../README.zh.md#i--representation)
