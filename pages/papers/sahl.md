# SAHL

*Structure-Aligned History Learning with Subspace-Structured Semantic IDs for Generative Recommendation* — Wei et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.25093) · [Code](https://github.com/CQU-MM-Intelligent-Lab/SAHL) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `SRBQ` | `Non-AR` | **`Fixed / (MTP + Masked Rec.) → MTP`** | `Graph` |

- `SRBQ`: Semantic Residual Balanced Quantization
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `(MTP + Masked Rec.) → MTP`: Joint multi-token prediction and masked reconstruction, followed by multi-token prediction alone.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2014 Beauty, Toys and Games, Sports and Outdoors, CDs and Vinyl, in this order; user/item 5-core.
  - Source: Section 5.1: https://arxiv.org/html/2610.25093v1#S5.SS1.p1
- **Split**: Per-user chronological leave-one-out: last interaction test, penultimate validation, earlier interactions train.
  - Source: Section 5.2: https://arxiv.org/html/2610.25093v1#S5.SS2.p1
- **Candidates**: not reported
  - Source: Sections 5.2/5.4 specify graph-constrained decoding but not full-catalog versus sampled-negative evaluation: https://arxiv.org/html/2610.25093v1#S5.SS2 and https://arxiv.org/html/2610.25093v1#S5.SS4.p2
- **Visibility**: warm; no unseen-item protocol is defined. Low-frequency analysis is explicitly near-cold, not zero-interaction.
  - Source: Section 6.11.4: https://arxiv.org/html/2610.25093v1#S6.SS11.SSS4.p1
- **SID**: SRBQ: 4/8/8/16 subspaces x 4 residual levels x 256 codes, producing 16/32/32/64 tokens in dataset order. Colliding items remain separate, equal-scored candidates; fixed catalog indices break ties.
  - Source: Sections 4.2.2/5.4: https://arxiv.org/html/2610.25093v1#S4.SS2.SSS2.p1 and https://arxiv.org/html/2610.25093v1#S5.SS4.p1 and https://arxiv.org/html/2610.25093v1#S5.SS4.p2
- **Inference budget**: Dataset order: beam 100/200/100/50, graph neighbors 100/100/200/500, propagation depths 3/5/2/4; temperature 0.03; Recall/NDCG@5/10. Inference hardware, batch size and latency not reported; A6000 timings concern training.
  - Source: Section 5.4 and Section 6.11.2: https://arxiv.org/html/2610.25093v1#S5.SS4.p1 and https://arxiv.org/html/2610.25093v1#S6.SS11.SSS2.p1 and https://arxiv.org/html/2610.25093v1#S6.SS11.SSS2.p3
- **Results from**: Table 2: overall comparison. RPG*, MHL and SAHL use matched controlled experiments; Tlow follows its published matched protocol. Other baseline score provenance not reported.
  - Source: Sections 5.3/6.1 and Table 2: https://arxiv.org/html/2610.25093v1#S5.SS3.p2 and https://arxiv.org/html/2610.25093v1#S6.SS1.p1 and https://arxiv.org/html/2610.25093v1#S5.T2

### 5. Connections to Related Work

- **Predecessor** · [RPG](rpg.md): Supplies the parallel backbone and graph-constrained decoder retained by SAHL.
  - Source: SAHL v1, Sections 5.3/6.11.2: https://arxiv.org/html/2610.25093v1#S5.SS3.p2; https://arxiv.org/html/2610.25093v1#S6.SS11.SSS2.p3.
- **Competitor** · [Tlow](tlow.md): Tokenizer-oriented comparator; its scores follow the published matched protocol.
  - Source: SAHL v1, Section 5.3 and Table 2: https://arxiv.org/html/2610.25093v1#S5.SS3.p2; https://arxiv.org/html/2610.25093v1#S5.T2.
- **Competitor** · [TIGER](tiger.md): Included semantic-ID baseline; SAHL adds quantizer-aligned history reconstruction.
  - Source: SAHL v1, Section 5.3 and Table 2: https://arxiv.org/html/2610.25093v1#S5.SS3.p1; https://arxiv.org/html/2610.25093v1#S5.T2.

[View all papers in this cell](../../README.md#iv--training)
