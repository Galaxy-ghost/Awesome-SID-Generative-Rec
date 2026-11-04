# SPAR

[← Problem × Stage Matrix](../../README.md#i--representation) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/spar.md)

| **Title** | *Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception* |
| :-- | :-- |
| **Authors** | Wang et al. |
| **Venue** | arXiv’26 |
| **Problem × Stage** | `I. Informativeness` · `Representation` · `POI` |
| **Changes** | ● Representation · ○ Objective |
| **SID inputs** | `Text` + `Geo` |
| **Domain** | `POI / Local` |
| **Links** | [Paper](https://arxiv.org/abs/2609.02062) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>● Text+Geo"] --> T["Tokenization<br/>R-KM"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: ○ Multi-task NTP"] --> I["Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class R main
```

- `Text+Geo`: Text representations combined with geographic or spatial features.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

### TL;DR

> [!NOTE]
> SPAR fuses sinusoidal coordinate embeddings into Semantic ID construction, continually pre-trains the LLM on geospatial data, and anchors that knowledge as a frozen task vector during behavioral fine-tuning.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Public NYC/TKY; one month of AMAP logs from Beijing, Shanghai, Tianjin and Zhejiang. MG-CPT adds 25 geospatial datasets per city. Cleaning details not reported.
  - Source: Section 5.1, Table 1 and Appendix B: [S5.SS1.p1](https://arxiv.org/html/2609.02062v2#S5.SS1.p1) and [S5.T1](https://arxiv.org/html/2609.02062v2#S5.T1) and [A2.p1](https://arxiv.org/html/2609.02062v2#A2.p1)
- **Split**: Public: chronological 80%/10%/10% train/validation/test. Industrial: last day test, earlier interactions train; industrial validation allocation not reported. Each interaction uses its preceding history.
  - Source: Section 5.1: [S5.SS1.p1](https://arxiv.org/html/2609.02062v2#S5.SS1.p1)
- **Candidates**: not reported
  - Source: Section 5.1 reports metrics and splits without candidate enumeration or negative sampling: [S5.SS1](https://arxiv.org/html/2609.02062v2#S5.SS1)
- **Visibility**: warm; no unseen-item protocol is defined. Cold/warm users have <8/>=16 historical interactions; queries and real-time location remain available. Quantizer fits training POIs; test-POI exclusion not detailed.
  - Source: Sections 4.1.2/5.5: [S4.SS1.SSS2.p2](https://arxiv.org/html/2609.02062v2#S4.SS1.SSS2.p2) and [S5.SS5.p1](https://arxiv.org/html/2609.02062v2#S5.SS5.p1)
- **SID**: SI-SID: 3 residual K-Means codebooks x 32 codes for NYC/TKY or x 512 for AMAP, plus a fourth disambiguation index guaranteeing unique POI IDs.
  - Source: Sections 4.1.2/5.1: [S4.SS1.SSS2.p2](https://arxiv.org/html/2609.02062v2#S4.SS1.SSS2.p2) and [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4)
- **Inference budget**: Default Qwen3-4B; Recall/NDCG/MRR@5/10/20. Experiment environment: 64 A100 GPUs; beam width, inference batch size and latency not reported. Reported batch 32 is training.
  - Source: Section 5.1: [S5.SS1.p2](https://arxiv.org/html/2609.02062v2#S5.SS1.p2) and [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4)
- **Results from**: Original Tables 2/3: public/industrial recommendation comparisons; Table 5: sparse-history users. Generative baselines are standardized to four-level SIDs with final disambiguation indices.
  - Source: Original Tables 2/3/5 and Section 5.1: [S5.T2](https://arxiv.org/html/2609.02062v2#S5.T2) and [S5.T3](https://arxiv.org/html/2609.02062v2#S5.T3) and [S5.T5](https://arxiv.org/html/2609.02062v2#S5.T5) and [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["SPAR"]
    P -->|"competitor"| A["GNPR-SID"]
    P -->|"competitor"| B["PLUM"]
    P -->|"competitor"| C["TIGER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Competitor** · [GNPR-SID](gnpr-sid.md): SID POI baseline; SPAR explicitly injects and preserves urban spatial knowledge.
  - Source: SPAR v2, Section 5.1 and Tables 2/3: [S5.SS1.p3](https://arxiv.org/html/2609.02062v2#S5.SS1.p3); [S5.T2](https://arxiv.org/html/2609.02062v2#S5.T2); [S5.T3](https://arxiv.org/html/2609.02062v2#S5.T3).
- **Competitor** · [PLUM](plum.md): Generic SID-CPT-SFT comparator against SPAR's spatially specialized stages.
  - Source: SPAR v2, Section 5.2.2: [S5.SS2.SSS2.p2](https://arxiv.org/html/2609.02062v2#S5.SS2.SSS2.p2).
- **Competitor** · [TIGER](tiger.md): Evaluated with four-level SIDs including a final disambiguation index.
  - Source: SPAR v2, Section 5.1 and Tables 2/3: [S5.SS1.p3](https://arxiv.org/html/2609.02062v2#S5.SS1.p3); [S5.SS1.p4](https://arxiv.org/html/2609.02062v2#S5.SS1.p4); [S5.T2](https://arxiv.org/html/2609.02062v2#S5.T2); [S5.T3](https://arxiv.org/html/2609.02062v2#S5.T3).

[View all papers in this cell](../../README.md#i--representation)
