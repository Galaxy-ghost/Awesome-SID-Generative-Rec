# DOS

[← Problem × Stage Matrix](../../README.md#iii--tokenization) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/dos.md)

| **Title** | *Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan* |
| :-- | :-- |
| **Authors** | Yin et al. |
| **Venue** | WWW’26 Short |
| **Problem × Stage** | `III. SID–Model Alignment` · `Tokenization` · `POI` |
| **Changes** | ● Tokenization |
| **SID inputs** | `Text` + `CF` |
| **Domain** | `POI / Local` |
| **Scenario** | `General Item Recommendation` · `Ranking and Reranking`; `Online Experiment or Deployment` |
| **Links** | [Paper](https://arxiv.org/abs/2602.04460) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>● Orth. RQ"] --> B["Backbone<br/>Dec-Only†"] --> TR["Training<br/>Tokenizer: Fixed†<br/>Objective: NTP"] --> I["Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+CF`: Text representations combined with collaborative signals.
- `Orth. RQ`: Orthogonal residual quantization.
- `Dec-Only†`: Decoder-only autoregressive backbone (inferred).
- `Fixed†`: Tokenizer frozen before generator training (inferred).
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

> [!NOTE]
> DOS aligns the Semantic ID codebook with the generation space through a user-item dual flow over collaborative signals and rotates the semantic space with orthogonal residual quantization.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Private Meituan production data only: past-year quantization data covering 24M unique items, and 60-day downstream data with 180M interactions. User/item filtering not reported.
  - Source: [S3.SS1.SSS1.p1](https://arxiv.org/html/2602.04460v1#S3.SS1.SSS1.p1) ; #S3.SS1.SSS1.p2
- **Split**: Quantization data: train/validation/test 8:1:1, partition method not reported; 50-click histories predict the 51st item. Downstream data: first 57 days training, last 3 days validation; a generation test split is not separately reported.
  - Source: [S3.SS1.SSS1.p2](https://arxiv.org/html/2602.04460v1#S3.SS1.SSS1.p2) ; #S3.SS1.SSS2.p1
- **Candidates**: not reported for Hit@10 generation. Quantization classification uses randomly sampled negatives; negative count, sampling distribution and user-history exclusion not reported.
  - Source: [S3.SS1.SSS1.p2](https://arxiv.org/html/2602.04460v1#S3.SS1.SSS1.p2) ; #S3.SS1.SSS2.p1 ; #S3.SS2.SSS2.p1
- **Visibility**: warm; no unseen-item protocol is defined. The quantization dataset covers past-year business items; validation/test-item exposure during SID learning is not separately reported.
  - Source: [S3.SS1.SSS1.p2](https://arxiv.org/html/2602.04460v1#S3.SS1.SSS1.p2) ; #S3.SS1.SSS2.p1
- **SID**: Qwen3-0.6B-embedding encodes restaurant name/categories, reservation status, prices and dishes into 1,024 dimensions. Dual user/item Transformer flows share an orthogonal residual quantizer: 3 layers x 1,024 codes, with salient-feature selection and residual propagation. Collision handling not reported.
  - Source: [S2.SS1.p2](https://arxiv.org/html/2602.04460v1#S2.SS1.p2) ; #S2.SS1.p3 ; #S2.SS1.p6 ; #S2.SS1.p8 ; #S2.SS2.p5 ; #S3.SS1.SSS2.p1
- **Inference budget**: Downstream generation evaluated within HSTU. Model size, beam/decoding constraints, token budget, inference hardware/batch size and latency not reported; batch 1,024 is a training setting.
  - Source: [S3.SS2.SSS2.p1](https://arxiv.org/html/2602.04460v1#S3.SS2.SSS2.p1) ; #S3.SS1.SSS2.p1
- **Results from**: Own offline quantization AUC/F1 and HSTU Hit@10 experiments; RQ-KMeans/RQ-VAE baselines are fine-tuned for application metrics. Own one-week A/B test on 30% of production traffic reports +1.15% revenue from adding DOS SIDs to the original baseline.
  - Source: [S3.SS2.p1](https://arxiv.org/html/2602.04460v1#S3.SS2.p1) ; #S3.SS2.SSS2.p1 ; #S3.SS4.p1 ; #S3.SS4.p2

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["DOS"]
    P -->|"competitor"| A["DAS"]
    P -->|"alternative"| B["TIGER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B peer
```

- **Competitor** · [DAS](das.md): Industrial SID baseline compared offline and within HSTU; DOS contrasts direct sequence-target modeling with DAS's indirect collaborative alignment.
  - Source: [S3.SS2.SSS1.p1](https://arxiv.org/html/2602.04460v1#S3.SS2.SSS1.p1) ; #S3.SS2.SSS2.p1
- **Alternative** · [TIGER](tiger.md): Cited as task-agnostic SID learning whose codebook-generation gap motivates context-aware DOS quantization.
  - Source: [S1.p2](https://arxiv.org/html/2602.04460v1#S1.p2) (Rajput et al., 2023)

[View all papers in this cell](../../README.md#iii--tokenization)
