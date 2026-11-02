# SPAR

| **题目** | *Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception* |
| :-- | :-- |
| **作者** | Wang et al. |
| **会议** | arXiv’26 |
| **问题与阶段** | `I. 信息量` · `Representation` · `POI` |
| **链接** | [论文](https://arxiv.org/abs/2609.02062) · [矩阵](../../../README.zh.md#i--representation) · [English](../../papers/spar.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+Geo"] --> T["Tokenization<br/>R-KM"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / Multi-task NTP"] --> I["Inference<br/>–"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class R main
```

- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `–`: Not reported in the paper.

### TL;DR

> [!NOTE]
> SPAR 将正弦坐标嵌入融入 SID 构建，在地理空间数据上持续预训练 LLM，并在行为微调期间将该知识固定为冻结任务向量。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | SPAR 将正弦坐标嵌入融入 SID 构建，在地理空间数据上持续预训练 LLM，并在行为微调期间将该知识固定为冻结任务向量。 |
| 主要改动阶段 | Representation |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Public NYC/TKY; one month of AMAP logs from Beijing, Shanghai, Tianjin and Zhejiang. MG-CPT adds 25 geospatial datasets per city. Cleaning details not reported.
  - 出处：Section 5.1, Table 1 and Appendix B: [S5.SS1.p1](https://arxiv.org/html/2609.02062v2#S5.SS1.p1) and [S5.T1](https://arxiv.org/html/2609.02062v2#S5.T1) and [A2.p1](https://arxiv.org/html/2609.02062v2#A2.p1)
- **切分**：Public: chronological 80%/10%/10% train/validation/test. Industrial: last day test, earlier interactions train; industrial validation allocation not reported. Each interaction uses its preceding history.
  - 出处：Section 5.1: [S5.SS1.p1](https://arxiv.org/html/2609.02062v2#S5.SS1.p1)
- **候选集**：not reported
  - 出处：Section 5.1 reports metrics and splits without candidate enumeration or negative sampling: [S5.SS1](https://arxiv.org/html/2609.02062v2#S5.SS1)
- **可见性**：warm; no unseen-item protocol is defined. Cold/warm users have <8/>=16 historical interactions; queries and real-time location remain available. Quantizer fits training POIs; test-POI exclusion not detailed.
  - 出处：Sections 4.1.2/5.5: [S4.SS1.SSS2.p2](https://arxiv.org/html/2609.02062v2#S4.SS1.SSS2.p2) and [S5.SS5.p1](https://arxiv.org/html/2609.02062v2#S5.SS5.p1)
- **SID 规格**：SI-SID: 3 residual K-Means codebooks x 32 codes for NYC/TKY or x 512 for AMAP, plus a fourth disambiguation index guaranteeing unique POI IDs.
  - 出处：Sections 4.1.2/5.1: [S4.SS1.SSS2.p2](https://arxiv.org/html/2609.02062v2#S4.SS1.SSS2.p2) and [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4)
- **推理预算**：Default Qwen3-4B; Recall/NDCG/MRR@5/10/20. Experiment environment: 64 A100 GPUs; beam width, inference batch size and latency not reported. Reported batch 32 is training.
  - 出处：Section 5.1: [S5.SS1.p2](https://arxiv.org/html/2609.02062v2#S5.SS1.p2) and [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4)
- **结果来源**：Original Tables 2/3: public/industrial recommendation comparisons; Table 5: sparse-history users. Generative baselines are standardized to four-level SIDs with final disambiguation indices.
  - 出处：Original Tables 2/3/5 and Section 5.1: [S5.T2](https://arxiv.org/html/2609.02062v2#S5.T2) and [S5.T3](https://arxiv.org/html/2609.02062v2#S5.T3) and [S5.T5](https://arxiv.org/html/2609.02062v2#S5.T5) and [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["SPAR"]
    P -->|competitor| A["GNPR-SID"]
    P -->|competitor| B["PLUM"]
    P -->|competitor| C["TIGER"]
```

- **同期对比** · [GNPR-SID](gnpr-sid.md): SID POI baseline; SPAR explicitly injects and preserves urban spatial knowledge.
  - 出处：SPAR v2, Section 5.1 and Tables 2/3: https://arxiv.org/html/2609.02062v2#S5.SS1.p3; https://arxiv.org/html/2609.02062v2#S5.T2; https://arxiv.org/html/2609.02062v2#S5.T3.
- **同期对比** · [PLUM](plum.md): Generic SID-CPT-SFT comparator against SPAR's spatially specialized stages.
  - 出处：SPAR v2, Section 5.2.2: https://arxiv.org/html/2609.02062v2#S5.SS2.SSS2.p2.
- **同期对比** · [TIGER](tiger.md): Evaluated with four-level SIDs including a final disambiguation index.
  - 出处：SPAR v2, Section 5.1 and Tables 2/3: https://arxiv.org/html/2609.02062v2#S5.SS1.p3; https://arxiv.org/html/2609.02062v2#S5.SS1.p4; https://arxiv.org/html/2609.02062v2#S5.T2; https://arxiv.org/html/2609.02062v2#S5.T3.

[查看同格全部论文](../../../README.zh.md#i--representation)
