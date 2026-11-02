# DualGR

*Generative Retrieval with Long and Short-Term Interests Modeling* — Yi et al. · WWW’26 Short

`VI. 泛化` · `Backbone` · [论文](https://arxiv.org/abs/2511.12518) · [矩阵](../../../README.zh.md#vi--backbone) · [English](../../papers/dualgr.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>–"] --> T["Tokenization<br/>R-KM"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP + Rank"] --> I["Inference<br/>Dual Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class B main
```

- `–`: Not reported in the paper.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.
- `Dual Beam`: Beam-search decoding in two branches with merged candidates.

### TL;DR

> [!NOTE]
> DualGR 加入长短期兴趣路由器，在当前粗粒度桶内解码细粒度 SID 层级，并在训练中把未点击曝光作为粗粒度难负例。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | VI. 泛化：Does it still work for new items, new domains, and shifting interests? |
| 核心贡献 | DualGR 加入长短期兴趣路由器，在当前粗粒度桶内解码细粒度 SID 层级，并在训练中把未点击曝光作为粗粒度难负例。 |
| 主要改动阶段 | Backbone |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Kuaishou double-column Explore-feed logs; filtering rules and dataset dates not reported.
  - 出处：Section 3: [S3.p1](https://arxiv.org/html/2511.12518v1#S3.p1)
- **切分**：Offline split not reported; online A/B test lasts one week with 6% traffic.
  - 出处：Sections 3 and 3.1: [S3.p1](https://arxiv.org/html/2511.12518v1#S3.p1) and [S3.SS1.p1](https://arxiv.org/html/2511.12518v1#S3.SS1.p1)
- **候选集**：not reported
  - 出处：Section 3 describes online HR without specifying a full-catalog or sampled-negative protocol: [S3.p1](https://arxiv.org/html/2511.12518v1#S3.p1)
- **可见性**：warm; no unseen-item protocol is defined. Item-level generator/tokenizer exposure: not reported.
  - 出处：Sections 2.1 and 3 do not specify generator/tokenizer item holdouts: [S2.SS1](https://arxiv.org/html/2511.12518v1#S2.SS1) and [S3](https://arxiv.org/html/2511.12518v1#S3)
- **SID 规格**：Residual k-means: 3 levels x 8192 codes; collision handling not reported.
  - 出处：Sections 2.2 and 3: [S2.SS2.p1](https://arxiv.org/html/2511.12518v1#S2.SS2.p1) and [S3.p1](https://arxiv.org/html/2511.12518v1#S3.p1)
- **推理预算**：Two branch-wise beam searches, followed by merging; HR@100/500/1000. Beam width, hardware, inference batch size, and numerical latency not reported; A/B test reports no measurable response-time increase.
  - 出处：Section 2.3, Table 1, and Section 3.1: [S2.SS3.p2](https://arxiv.org/html/2511.12518v1#S2.SS3.p2) and [S3.T1](https://arxiv.org/html/2511.12518v1#S3.T1) and [S3.SS1.p1](https://arxiv.org/html/2511.12518v1#S3.SS1.p1)
- **结果来源**：Original Table 1: online HR; Table 2: ablations; Section 3.1: A/B results.
  - 出处：Tables 1-2 and Section 3.1: [S3.T1](https://arxiv.org/html/2511.12518v1#S3.T1) and [S3.T2](https://arxiv.org/html/2511.12518v1#S3.T2) and [S3.SS1.p1](https://arxiv.org/html/2511.12518v1#S3.SS1.p1)

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["DualGR"]
    P -->|competitor| A["TIGER"]
```

- **同期对比** · [TIGER](tiger.md): TIGER is reimplemented as the generative baseline; DualGR adds explicit long/short routing and exposure-aware training.
  - 出处：DualGR v1, Section 3 and Table 1: https://arxiv.org/html/2511.12518v1#S3.p1; https://arxiv.org/html/2511.12518v1#S3.T1.

[查看同格全部论文](../../../README.zh.md#vi--backbone)
