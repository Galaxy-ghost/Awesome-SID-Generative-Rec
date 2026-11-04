# VarLenRec (TIGER)

[← Problem × Stage Matrix](../../README.md#i--tokenization) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/varlenrec-tiger.md)

| **Title** | *Learning Variable-Length Tokenization for Generative Recommendation* |
| :-- | :-- |
| **Authors** | Wang et al. |
| **Venue** | arXiv’26 |
| **Problem × Stage** | `I. Informativeness` · `Tokenization` |
| **Changes** | ● Tokenization · ○ Backbone · ○ Objective · ○ Inference |
| **SID inputs** | `Text` |
| **Domain** | `E-commerce` · `POI / Local` |
| **Links** | [Paper](https://arxiv.org/abs/2605.17779) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>● HARQ"] --> B["Backbone<br/>○ Enc-Dec"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: ○ NTP + Aux."] --> I["Inference<br/>○ C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class B,TR,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text`: Textual item metadata (titles, descriptions, categories, or prompts).
- `HARQ`: Hyperbolic Adaptive Residual Quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> VarLenRec (TIGER) gives popular items shorter Semantic IDs and tail items longer ones through hyperbolic residual quantization and a soft length controller, instead of fixed-length tokenization.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Beauty, Sports and Outdoors, Toys and Games, and Yelp; exclude users/items with fewer than five interactions. Maximum history length not reported.
  - Source: [S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS1.p1)
- **Split**: Per-user leave-one-out: most recent item test, second most recent validation, all remaining items training.
  - Source: [S4.SS1.SSS4.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS4.p1)
- **Candidates**: full catalog; full ranking without negative sampling.
  - Source: [S4.SS1.SSS3.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS3.p1)
- **Visibility**: warm; no unseen-item protocol is defined. Cold-start maximum-length assignment is discussed for deployment, not evaluated as a held-out-item protocol; tokenizer exposure to test items not reported.
  - Source: [S4.SS1.SSS4.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS4.p1) ; #S3.SS4.p6
- **SID**: HARQ on Sentence-T5 embeddings: variable semantic length up to 10 levels x 256 codes, in hyperbolic space with curvature 1. Colliding IDs receive unique appended tokens from a disjoint 256-entry auxiliary vocabulary.
  - Source: [S4.SS1.SSS4.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS4.p1) ; #S3.SS4.p2
- **Inference budget**: VarLenRec-TIGER uses T5, a user-side target-length predictor and trie-constrained beam 30, decoding exactly the predicted length; Recall/NDCG@5/10. Table III test seconds/epoch on Beauty/Sports/Toys/Yelp: 63.7/81.2/70.0/83.3. Experiments use A800 GPUs; count, inference batch size and per-request latency not reported.
  - Source: [S3.SS4.p4](https://arxiv.org/html/2605.17779v2#S3.SS4.p4) ; #S3.SS4.p5 ; #S4.SS1.SSS4.p1 ; #S4.T3
- **Results from**: Original v2 Table I: VarLenRec-TIGER and VarLenRec-LCRec comparisons; Table II: VarLenRec-TIGER ablations; Table III: timing. Baseline-result reuse not stated. This record covers the TIGER generative branch; SASRec is only a baseline in v2.
  - Source: [S4.SS2.p1](https://arxiv.org/html/2605.17779v2#S4.SS2.p1) ; #S4.T2 ; #S4.T3 ; #S4.SS1.SSS2.p1

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["VarLenRec (TIGER)"]
    P -->|"predecessor"| A["TIGER"]
    P -->|"competitor"| B["ETEGRec"]
    P -->|"competitor"| C["LETTER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Predecessor** · [TIGER](tiger.md): VarLenRec-TIGER replaces uniform-length RQ tokenization with hyperbolic variable-length IDs and adds user-conditioned length prediction before constrained generation.
  - Source: VarLenRec v2, Sections III-D/IV-B: [S3.SS4.p3](https://arxiv.org/html/2605.17779v2#S3.SS4.p3); [S4.SS2.p1](https://arxiv.org/html/2605.17779v2#S4.SS2.p1).
- **Competitor** · [ETEGRec](etegrec.md): ETEGRec is a fixed-length generative baseline with joint-training optimization; VarLenRec changes the per-item encoding budget and target decoding length.
  - Source: VarLenRec v2, Sections IV-A/IV-B: [S4.SS1.SSS2.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS2.p1); [S4.SS2.p2](https://arxiv.org/html/2605.17779v2#S4.SS2.p2).
- **Competitor** · [LETTER](letter.md): LETTER improves codebook learning on TIGER/LCRec backbones; VarLenRec instead allocates variable ID lengths and compares against LETTER-TIGER.
  - Source: VarLenRec v2, Sections IV-A/IV-B: [S4.SS1.SSS2.p1](https://arxiv.org/html/2605.17779v2#S4.SS1.SSS2.p1); [S4.SS2.p2](https://arxiv.org/html/2605.17779v2#S4.SS2.p2).

[View all papers in this cell](../../README.md#i--tokenization)
