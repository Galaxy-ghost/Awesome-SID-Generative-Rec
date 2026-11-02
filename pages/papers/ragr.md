# RAGR

*Review-Augmented Generative Recommendation* — Zhang et al. · arXiv’26

`I. Informativeness` · `Training`

[Paper](https://arxiv.org/abs/2605.17267) · [Code](https://github.com/Zhang-Yingyi/TKDE_RAGR) · [Matrix](../../README.md#i--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP → DPO"] --> I["Inference<br/>Beam† / –"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.
- `Beam† / –`: Inherited beam search in one configuration; decoding not reported in the other.

### TL;DR

RAGR interleaves item Semantic IDs and review Semantic IDs chronologically in the user sequence and uses DPO to favor item tokens at prediction positions, instead of modeling item-only sequences.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | RAGR interleaves item Semantic IDs and review Semantic IDs chronologically in the user sequence and uses DPO to favor item tokens at prediction positions, instead of modeling item-only sequences. |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty, Sports and Outdoors, Toys and Games, with historical review text; remove users/items with fewer than five interactions; maximum history 20, truncating oldest interactions.
- **Split**: Per-user chronological leave-one-out: last interaction test, second last validation, remaining interactions training.
- **Candidates**: not reported
- **Visibility**: warm; no unseen-item protocol is defined. Historical reviews are retained; tokenizer fitting exposure to test items not reported.
- **SID**: RQ-VAE: 4 x 256, 32-dimensional codewords, shared item/review token space. Default tokenizer fits item text only; collision handling not reported.
- **Inference budget**: Autoregressive item-SID prediction; HIT/NDCG@5/10/20. Decoding algorithm/beam width, inference batch size and latency not reported. General experiment server: 8 RTX PRO 6000 96GB GPUs; inference-specific allocation not reported.
- **Results from**: Original Table II: TIGER/LETTER with and without RAGR, means over seeds 42/43/44; all baselines trained/evaluated with the common split/protocol. Table III: ablations; Tables IV-V: tokenizer efficiency/collisions. No baseline-result reuse stated.

<details>
<summary>Sources</summary>

- **Datasets**: [S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS1.p1) ; #S4.SS1.SSS4.p3
- **Split**: [S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS1.p1)
- **Candidates**: Experimental settings report top-K metrics but no candidate universe: [S4.SS1](https://arxiv.org/html/2605.17267v1#S4.SS1)
- **Visibility**: [S4.SS1.SSS1.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS1.p1) ; #S4.SS4.p4
- **SID**: [S4.SS1.SSS4.p2](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS4.p2) ; #S4.SS4.p4 ; #S4.SS5.p4
- **Inference budget**: [S4.SS1.SSS3.p1](https://arxiv.org/html/2605.17267v1#S4.SS1.SSS3.p1) ; #S4.SS1.SSS4.p1 ; #S4.SS1.SSS4.p5
- **Results from**: [S4.T2](https://arxiv.org/html/2605.17267v1#S4.T2) ; #S4.T3 ; #S4.T4 ; #S4.T5 ; #S4.SS1.SSS4.p1 ; #S4.SS1.SSS4.p5

</details>

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["RAGR"]
    P -->|predecessor| A["TIGER"]
    P -->|predecessor| B["LETTER"]
```

- **Predecessor** · [TIGER](tiger.md): RAGR augments TIGER with interleaved review SIDs, review-generation supervision and DPO alignment toward item generation.
  - Source: RAGR v1, Section IV-A and Table II: https://arxiv.org/html/2605.17267v1#S4.SS1.SSS4.p1; https://arxiv.org/html/2605.17267v1#S4.T2.
- **Predecessor** · [LETTER](letter.md): LETTER is the second backbone receiving the same review augmentation and item-centric DPO alignment.
  - Source: RAGR v1, Section IV-A and Table II: https://arxiv.org/html/2605.17267v1#S4.SS1.SSS4.p1; https://arxiv.org/html/2605.17267v1#S4.T2.

[View all papers in this cell](../../README.md#i--training)
