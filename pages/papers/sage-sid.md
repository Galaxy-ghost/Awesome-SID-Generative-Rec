# SAGE-SID

*SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation* — Xie et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2601.21452) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+Img†"] --> T["Tokenization<br/>R-KM†"] --> B["Backbone<br/>Dec-Only†"] --> TR["Training<br/>Fixed† / NTP → RL"] --> I["Inference<br/>–"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `–`: Not reported in the paper.

### TL;DR

SAGE-SID optimizes list-wise generators with a geometric-mean sequence ratio, decoupled multi-objective advantages, asymmetric adaptive bounds, and an entropy-aware penalty, replacing the symmetric bounds of GBPO.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Key Contribution | SAGE-SID optimizes list-wise generators with a geometric-mean sequence ratio, decoupled multi-objective advantages, asymmetric adaptive bounds, and an entropy-aware penalty, replacing the symmetric bounds of GBPO. |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2014 Sports/Beauty/Toys; RecIF-Bench: about 120M interactions, 200K users, Short Video/Ad/Product. Filtering not reported.
- **Split**: RecIF: 20% users held out, per-user histories separated temporally from future targets. Amazon split and validation allocation not reported.
- **Candidates**: not reported for the SID branch
- **Visibility**: warm; no unseen-item protocol is defined. Amazon cold items are bottom 5% by training interaction frequency; RecIF holds out users, not explicitly items.
- **SID**: OneRec-SAGE uses Semantic IDs and OpenOneRec checkpoints/settings; SID length, codebook sizes and collision handling not reported here.
- **Inference budget**: Reported slate length 10; Amazon Recall/NDCG@5/10; RecIF Pass/Recall@1/32 and label AUC. SID beam width, inference hardware, batch size and latency not reported.
- **Results from**: OneRec-SAGE rows in Tables 1/2 (Amazon) and 3/4 (RecIF). RecIF task-specific sequential and TIGER baseline numbers are reused from the benchmark; OneRec variants use public checkpoints/settings.

<details>
<summary>Sources</summary>

- **Datasets**: Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p1) and [S4.SS1.SSS1.p2](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p2)
- **Split**: Section 4.1.1: [S4.SS1.SSS1.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p3)
- **Candidates**: Section 4.1.4 identifies inherited SID evaluation settings but does not specify candidate enumeration: [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)
- **Visibility**: Sections 4.1.1/4.1.3: [S4.SS1.SSS1.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p3) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p1)
- **SID**: Sections 4.1.2/4.1.4: [S4.SS1.SSS2.p4](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p4) and [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)
- **Inference budget**: Sections 4.1.3/4.1.4: [S4.SS1.SSS3.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p1) and [S4.SS1.SSS3.p2](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p2) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p1) and [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)
- **Results from**: Tables 1-4 and Section 4.1.4: [S3.T1](https://arxiv.org/html/2601.21452v3#S3.T1) and [S3.T2](https://arxiv.org/html/2601.21452v3#S3.T2) and [S3.T3](https://arxiv.org/html/2601.21452v3#S3.T3) and [S4.T4](https://arxiv.org/html/2601.21452v3#S4.T4) and [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)

</details>

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["SAGE-SID"]
    P -->|predecessor| A["OneRec-V2"]
    P -->|competitor| B["LC-Rec"]
    P -->|competitor| C["TIGER"]
```

- **Predecessor** · [OneRec-V2](onerec-v2.md): SAGE extends the GBPO optimizer evaluated as OneRec-GBPO.
  - Source: SAGE v3, Sections 3.4.1/4.1.2: https://arxiv.org/html/2601.21452v3#S3.SS4.SSS1.p1; https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p4.
- **Competitor** · [LC-Rec](lc-rec.md): Adapted to a Qwen3-8B backbone for the RecIF comparison.
  - Source: SAGE v3, Section 4.1.2: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p3.
- **Competitor** · [TIGER](tiger.md): RecIF comparison reuses TIGER's reported benchmark numbers.
  - Source: SAGE v3, Section 4.1.4: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3.

[View all papers in this cell](../../README.md#iv--training)
