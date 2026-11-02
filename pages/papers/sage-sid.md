# SAGE-SID

*SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation* — Xie et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2601.21452) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img†` | `R-KM†` | `Dec-Only†` | **`Fixed† / NTP → RL`** | `–` |

- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2014 Sports/Beauty/Toys; RecIF-Bench: about 120M interactions, 200K users, Short Video/Ad/Product. Filtering not reported.
  - Source: Section 4.1.1: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p1 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p2
- **Split**: RecIF: 20% users held out, per-user histories separated temporally from future targets. Amazon split and validation allocation not reported.
  - Source: Section 4.1.1: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p3
- **Candidates**: not reported for the SID branch
  - Source: Section 4.1.4 identifies inherited SID evaluation settings but does not specify candidate enumeration: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3
- **Visibility**: warm; no unseen-item protocol is defined. Amazon cold items are bottom 5% by training interaction frequency; RecIF holds out users, not explicitly items.
  - Source: Sections 4.1.1/4.1.3: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p3 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p1
- **SID**: OneRec-SAGE uses Semantic IDs and OpenOneRec checkpoints/settings; SID length, codebook sizes and collision handling not reported here.
  - Source: Sections 4.1.2/4.1.4: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p4 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3
- **Inference budget**: Reported slate length 10; Amazon Recall/NDCG@5/10; RecIF Pass/Recall@1/32 and label AUC. SID beam width, inference hardware, batch size and latency not reported.
  - Source: Sections 4.1.3/4.1.4: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p1 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p2 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p1 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3
- **Results from**: OneRec-SAGE rows in Tables 1/2 (Amazon) and 3/4 (RecIF). RecIF task-specific sequential and TIGER baseline numbers are reused from the benchmark; OneRec variants use public checkpoints/settings.
  - Source: Tables 1-4 and Section 4.1.4: https://arxiv.org/html/2601.21452v3#S3.T1 and https://arxiv.org/html/2601.21452v3#S3.T2 and https://arxiv.org/html/2601.21452v3#S3.T3 and https://arxiv.org/html/2601.21452v3#S4.T4 and https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3

### 5. Connections to Related Work

- **Predecessor** · [OneRec-V2](onerec-v2.md): SAGE extends the GBPO optimizer evaluated as OneRec-GBPO.
  - Source: SAGE v3, Sections 3.4.1/4.1.2: https://arxiv.org/html/2601.21452v3#S3.SS4.SSS1.p1; https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p4.
- **Competitor** · [LC-Rec](lc-rec.md): Adapted to a Qwen3-8B backbone for the RecIF comparison.
  - Source: SAGE v3, Section 4.1.2: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p3.
- **Competitor** · [TIGER](tiger.md): RecIF comparison reuses TIGER's reported benchmark numbers.
  - Source: SAGE v3, Section 4.1.4: https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3.

[View all papers in this cell](../../README.md#iv--training)
