# ProGEO

*Birds of a Feather Cluster Nearby: A Proximity-Aware Geo-Codebook for Local Service Recommendation* — He et al. · arXiv’26

`I. 信息量` · `Tokenization` · `POI` · [论文](https://arxiv.org/abs/2604.23156) · [矩阵](../../../README.zh.md#i--tokenization) · [English](../../papers/progeo.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+Geo"] --> T["Tokenization<br/>R-KM+Geo-CB"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>Beam+Geo-Filter"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `R-KM+Geo-CB`: Residual k-means combined with a geographic codebook.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Beam+Geo-Filter`: Beam search with geographically restricted candidates.

### TL;DR

> [!NOTE]
> ProGEO 结合地理质心局部坐标系与地理旋转位置编码构建邻近感知地理码本，使 SID 同时刻画语义与地理邻近性。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | ProGEO 结合地理质心局部坐标系与地理旋转位置编码构建邻近感知地理码本，使 SID 同时刻画语义与地理邻近性。 |
| 主要改动阶段 | Tokenization |

### 2. 方法

![ProGEO architecture diagram](../../../architectures/progeo.png)

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Industrial: two months of transaction records from a Chinese local-life service platform (search query, user location, merchant exposure sequence, interactions); size and filtering not reported. Public: Foursquare NYC (1,083 users / 5,135 POIs) and TKY (2,293 / 7,873), filtered as in GNPR-SID (POIs with fewer than 10 interactions, users with fewer than 10 check-ins removed), and Yelp (150,346 POIs; clustering analysis only).
  - 出处：Industrial and public data: [A2.SS1.p1](https://arxiv.org/html/2604.23156v1#A2.SS1.p1); public statistics: [A2.SS2.SSS2.p1](https://arxiv.org/html/2604.23156v1#A2.SS2.SSS2.p1).
- **切分**：Industrial: two months of records for training and additional daily data reserved for validation; the test construction is not reported. Public: preprocessing follows GNPR-SID; the split is not restated.
  - 出处：Two-month training with extra daily validation data: [A2.SS1.p1](https://arxiv.org/html/2604.23156v1#A2.SS1.p1); public split follows GNPR-SID but is not restated.
- **候选集**：Industrial inference: for each generated semantic ID, the 10 POIs closest to the user's location form the candidate set, with beam width 20. Evaluation reports Hit@1, Hit@50, Hit@100 and NDCG@50, @100; full catalog versus sampled not otherwise stated.
  - 出处：Ten location-nearest POIs per semantic ID as candidates, then beam search: [A2.SS2.SSS1.p1](https://arxiv.org/html/2604.23156v1#A2.SS2.SSS1.p1); metrics: [A2.SS3.p3](https://arxiv.org/html/2604.23156v1#A2.SS3.p3).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：No unseen-item protocol: [A2.SS1.p1](https://arxiv.org/html/2604.23156v1#A2.SS1.p1).
- **SID 规格**：Residual quantization with geographic rotary encoding (Geo-RoPE) at the third layer over 128-dimensional Qwen3-Embedding-8B text embeddings. Codebooks: [512, 512, 512] industrial; [32, 32, 32] NYC/TKY; [64, 64, 64] Yelp. Conflicts: industrial uses closest-location matching among POIs sharing a SID (best in Table 3); public datasets use a TIGER-style fourth-layer code because user location is unavailable.
  - 出处：Codebooks [512,512,512] industrial, [32,32,32] NYC/TKY, [64,64,64] Yelp, Geo-RoPE at layer 3: [A2.SS2.SSS1.p1](https://arxiv.org/html/2604.23156v1#A2.SS2.SSS1.p1) and [A2.SS2.SSS2.p1](https://arxiv.org/html/2604.23156v1#A2.SS2.SSS2.p1); conflict strategies: [S4.T3](https://arxiv.org/html/2604.23156v1#S4.T3).
- **推理预算**：Beam search with width 20 on Qwen2.5-1.5B; all experiments on 8 GPUs with 80GB memory. Inference batch size and latency: not reported.
  - 出处：Beam width 20 and hardware: [A2.SS2.SSS1.p1](https://arxiv.org/html/2604.23156v1#A2.SS2.SSS1.p1) and [A2.SS2.SSS2.p1](https://arxiv.org/html/2604.23156v1#A2.SS2.SSS2.p1).
- **结果来源**：Table 1 (industrial quantization and recommendation metrics versus RQ-VAE, RQ-Kmeans, HyMiRec-style RQ-Kmeans, RQ-OPQ); Table 2 (geographic attributes); Table 3 (conflict-resolution strategies); Table 6 (public datasets versus RQ-Kmeans); Figures 7-10 (sensitivity and case studies).
  - 出处：Main: [S4.T1](https://arxiv.org/html/2604.23156v1#S4.T1); geographic attributes: [S4.T2](https://arxiv.org/html/2604.23156v1#S4.T2); conflicts: [S4.T3](https://arxiv.org/html/2604.23156v1#S4.T3); public: [A2.T6](https://arxiv.org/html/2604.23156v1#A2.T6); sensitivity: [S4.F7](https://arxiv.org/html/2604.23156v1#S4.F7).

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["ProGEO"]
    P -->|competitor| A["OneRec"]
    P -->|competitor| B["TIGER"]
    P -->|predecessor| C["GNPR-SID"]
    P -->|alternative| D["OneLoc"]
    P -->|alternative| E["LGSID"]
```

- **同期对比** · [OneRec](onerec.md): OneRec's RQ-Kmeans is the second-best tokenizer in Table 1; Pro-GEO injects geographic rotary encoding at the third quantization layer and resolves SID conflicts by user distance.
  - 出处：Pro-GEO v1, baseline RQ-Kmeans (Deng et al., 2025): https://arxiv.org/html/2604.23156v1#A2.SS4.p1; Table 1 and public Table 6: https://arxiv.org/html/2604.23156v1#S4.T1 and https://arxiv.org/html/2604.23156v1#A2.T6.
- **同期对比** · [TIGER](tiger.md): TIGER's RQ-VAE is a tokenizer baseline; Pro-GEO also borrows TIGER's fourth-layer code for conflicts on public data where user location is missing.
  - 出处：Pro-GEO v1, baseline RQ-VAE: https://arxiv.org/html/2604.23156v1#A2.SS4.p1; Table 1: https://arxiv.org/html/2604.23156v1#S4.T1; Layer-4 coding follows TIGER: https://arxiv.org/html/2604.23156v1#A2.SS2.SSS2.p1.
- **前序工作** · [GNPR-SID](gnpr-sid.md): Pro-GEO follows GNPR-SID's POI preprocessing for NYC and TKY; GNPR-SID's SIDs carry no explicit geographic encoding.
  - 出处：Pro-GEO v1, Appendix B.1 and B.2.2 follow Wang et al. (2025a): https://arxiv.org/html/2604.23156v1#A2.SS1.p1 and https://arxiv.org/html/2604.23156v1#A2.SS2.SSS2.p1.
- **替代方案** · [OneLoc](oneloc.md): OneLoc adds location context to the SID input embedding for local-life video; Pro-GEO rotates residuals by geography inside the quantizer.
  - 出处：Pro-GEO v1, Sections 1 and 2.1 cite Wei et al. (2025): https://arxiv.org/html/2604.23156v1#S1.p2 and https://arxiv.org/html/2604.23156v1#S2.SS1.p2.
- **替代方案** · [LGSID](lgsid.md): LGSID aligns LLM embeddings with geographic rewards before quantization; Pro-GEO encodes geography within the quantization layers.
  - 出处：Pro-GEO v1, Section 2.1 cites LGSID: https://arxiv.org/html/2604.23156v1#S2.SS1.p2.

[查看同格全部论文](../../../README.zh.md#i--tokenization)
