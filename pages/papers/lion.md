# LION

[← Problem × Stage Matrix](../../README.md#vi--backbone) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/lion.md)

| **Title** | *Self-Evolving Memory for Generative Recommendation* |
| :-- | :-- |
| **Authors** | Lin et al. |
| **Venue** | CIKM’26 |
| **Problem × Stage** | `VI. Generalization` · `Backbone` |
| **Changes** | ● Backbone · ○ Objective |
| **SID inputs** | `Text` |
| **Domain** | `E-commerce` |
| **Links** | [Paper](https://arxiv.org/abs/2609.15598) · [Code](https://github.com/JazyJiang/Self-Evolving-Memory-for-Generative-Recommendation) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text†"] --> T["Tokenization<br/>RQ-VAE†"] --> B["Backbone<br/>● Enc-Dec"] --> TR["Training<br/>Tokenizer: Fixed†<br/>Objective: ○ NTP + Aux."] --> I["Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text†`: Textual item representations (inferred).
- `RQ-VAE†`: Residual-Quantized Variational AutoEncoder (inferred).
- `Enc-Dec`: Encoder-decoder.
- `Fixed†`: Tokenizer frozen before generator training (inferred).
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `Beam`: Autoregressive beam search over Semantic ID tokens.

### TL;DR

> [!NOTE]
> LION adds a sparse key-value memory layer that isolates the evolution of different behavior patterns, with a consolidation loss, instead of updating all shared parameters on streaming interactions.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Games, CDs, and Toys; next-item samples with at most 10 previous interactions. Filtering rules not reported.
  - Source: Section 5.1.1: [S5.SS1.SSS1.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS1.p1)
- **Split**: Target timestamps define five equal-count chronological periods P0-P4; adapt through each period and evaluate the next (P1-P4). Current-period validation file used; validation fraction not reported.
  - Source: Sections 2/5.1.1/5.1.4: [S2.p3](https://arxiv.org/html/2609.15598v1#S2.p3) and [S5.SS1.SSS1.p2](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS1.p2) and [S5.SS1.SSS4.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS4.p1)
- **Candidates**: not reported
  - Source: Section 5.1.2 defines generated-list metrics but no evaluation candidate pool: [S5.SS1.SSS2.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS2.p1)
- **Visibility**: warm; no unseen-item protocol is defined. Item/tokenizer exposure across periods not reported.
  - Source: Section 5.1 defines streaming periods without an unseen-item holdout: [S5.SS1](https://arxiv.org/html/2609.15598v1#S5.SS1)
- **SID**: TIGER instantiation; tokenizer construction, SID length, codebook sizes, and collision handling not reported.
  - Source: Sections 2/5.1.4 give generic token identifiers and the TIGER implementation: [S2.p1](https://arxiv.org/html/2609.15598v1#S2.p1) and [S5.SS1.SSS4.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS4.p1)
- **Inference budget**: Beam 20; K=10/20. Sparse memory defaults: 64 keys per dimension, top-32 activation, decoder layer 5, routing history length 2. Hardware, inference batch size, and latency not reported.
  - Source: Section 5.1.2 and Appendix A.1: [S5.SS1.SSS2.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS2.p1) and [A1.SS1.p1](https://arxiv.org/html/2609.15598v1#A1.SS1.p1)
- **Results from**: Original Table 1: sample-weighted micro-average over four periods x five user groups; Table 2: period/group results; Table 3: ablations. Baselines adapted to TIGER in this paper.
  - Source: Section 5.1.3 and Tables 1-3: [S5.SS1.SSS3.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS3.p1) and [S5.T1](https://arxiv.org/html/2609.15598v1#S5.T1) and [S5.T2](https://arxiv.org/html/2609.15598v1#S5.T2) and [S5.T3](https://arxiv.org/html/2609.15598v1#S5.T3)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["LION"]
    P -->|"predecessor"| A["TIGER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A peer
```

- **Predecessor** · [TIGER](tiger.md): LION adds sparse evolving memory to TIGER's continual fine-tuning baseline.
  - Source: LION v1, Sections 5.1.3/5.1.4 and Table 1: [S5.SS1.SSS3.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS3.p1); [S5.SS1.SSS4.p1](https://arxiv.org/html/2609.15598v1#S5.SS1.SSS4.p1); [S5.T1](https://arxiv.org/html/2609.15598v1#S5.T1).

[View all papers in this cell](../../README.md#vi--backbone)
