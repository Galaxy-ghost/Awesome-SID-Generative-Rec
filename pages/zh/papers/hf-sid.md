# HF-SID

| **题目** | *High-Fidelity Semantic IDs for Generative Retrieval in Location-Based Services* |
| :-- | :-- |
| **作者** | Lin et al. |
| **会议** | arXiv’26 |
| **问题与阶段** | `I. 信息量` · `Representation` · `POI` |
| **链接** | [论文](https://arxiv.org/abs/2608.30479) · [矩阵](../../../README.zh.md#i--representation) · [English](../../papers/hf-sid.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+Attr+Geo"] --> T["Tokenization<br/>R-KM"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class R main
```

- `Text+Attr+Geo`: Text, structured attributes, and geographic information.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> HF-SID 在量化前通过笛卡尔坐标、带单位数值编码与残差对比学习恢复 POI 表示中的地理、数值与结构细节，无需加长 SID。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | HF-SID 在量化前通过笛卡尔坐标、带单位数值编码与残差对比学习恢复 POI 表示中的地理、数值与结构细节，无需加长 SID。 |
| 主要改动阶段 | Representation |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：AMap-L (one day), AMap-S; remove POIs without interaction sequences and sessions without authenticated users. Foursquare NYC/TKY use Geo-CPT only; public-data filtering: not reported.
  - 出处：Sections 4.1 and 4.5: [S4.SS1.p1](https://arxiv.org/html/2608.30479v1#S4.SS1.p1) and [S4.SS5.p1](https://arxiv.org/html/2608.30479v1#S4.SS5.p1)
- **切分**：not reported; methods share identical splits.
  - 出处：Section 4.1 mentions identical baseline splits without specifying allocation: [S4.SS1.p2](https://arxiv.org/html/2608.30479v1#S4.SS1.p2)
- **候选集**：not reported
  - 出处：Sections 3.4 and 4.1 describe valid-SID generation but no full-catalog/sampled evaluation declaration: [S3.SS4.p4](https://arxiv.org/html/2608.30479v1#S3.SS4.p4) and [S4.SS1.p3](https://arxiv.org/html/2608.30479v1#S4.SS1.p3)
- **可见性**：warm; no unseen-item protocol is defined. Tokenizer fits representations of the entire POI corpus.
  - 出处：Sections 3.4 and 4.1: [S3.SS4.p1](https://arxiv.org/html/2608.30479v1#S3.SS4.p1) and [S4.SS1](https://arxiv.org/html/2608.30479v1#S4.SS1)
- **SID 规格**：3-level RQ-KMeans with last-residual contrastive refinement: 4096 codes/level on AMap-L, 512 on AMap-S. Public-data codebook sizes and collision materialization: not reported.
  - 出处：Sections 3.4 and 4.1: [S3.SS4.p3](https://arxiv.org/html/2608.30479v1#S3.SS4.p3) and [S4.SS1.p2](https://arxiv.org/html/2608.30479v1#S4.SS1.p2)
- **推理预算**：Valid-SID trie-constrained beam 300; Hit@200/300 on AMap, @5 on NYC/TKY. General experiments: 64 A100 GPUs; inference allocation, batch size, latency: not reported.
  - 出处：Sections 3.4, 4.1 and Table 5: [S3.SS4.p4](https://arxiv.org/html/2608.30479v1#S3.SS4.p4) and [S4.SS1.p4](https://arxiv.org/html/2608.30479v1#S4.SS1.p4) and [S4.T5](https://arxiv.org/html/2608.30479v1#S4.T5)
- **结果来源**：Original Tables 2/3/4/5/6: AMap comparison, ablation, numerical fidelity, public datasets, one-week online A/B.
  - 出处：Tables 2-6: [S4.T2](https://arxiv.org/html/2608.30479v1#S4.T2) and [S4.T3](https://arxiv.org/html/2608.30479v1#S4.T3) and [S4.T4](https://arxiv.org/html/2608.30479v1#S4.T4) and [S4.T5](https://arxiv.org/html/2608.30479v1#S4.T5) and [S4.T6](https://arxiv.org/html/2608.30479v1#S4.T6)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["HF-SID"]
    P -->|competitor| A["ProGEO"]
    P -->|competitor| B["GeoGR"]
    P -->|competitor| C["GNPR-SID"]
```

- **同期对比** · [ProGEO](progeo.md): Pro-GEO injects geography during quantization; HF-SID improves representations before quantization.
  - 出处：HF-SID v1, Sections 2 and 4.1, Table 2: https://arxiv.org/html/2608.30479v1#S2.p2; https://arxiv.org/html/2608.30479v1#S4.SS1.p2; https://arxiv.org/html/2608.30479v1#S4.T2.
- **同期对比** · [GeoGR](geogr.md): GeoGR uses co-visit alignment; HF-SID directly encodes coordinates and numerical attributes.
  - 出处：HF-SID v1, Sections 2 and 4.2, Table 2: https://arxiv.org/html/2608.30479v1#S2.p2; https://arxiv.org/html/2608.30479v1#S4.SS2.p2; https://arxiv.org/html/2608.30479v1#S4.T2.
- **同期对比** · [GNPR-SID](gnpr-sid.md): GNPR-SID regularizes codeword diversity; HF-SID focuses on representation fidelity.
  - 出处：HF-SID v1, Section 4.2 and Table 2: https://arxiv.org/html/2608.30479v1#S4.SS2.p2; https://arxiv.org/html/2608.30479v1#S4.T2.

[查看同格全部论文](../../../README.zh.md#i--representation)
