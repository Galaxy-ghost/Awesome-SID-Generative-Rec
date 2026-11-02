# IDM/CMM

*Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation* — Xu et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.32943) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Subspace RQ` | `Non-AR` | **`Fixed / MTP + Aux.`** | `Scoring` |

- `Subspace RQ`: Residual quantization applied separately within embedding subspaces.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Aux.`: Multi-token prediction jointly optimized with auxiliary objectives.

### TL;DR

IDM/CMM distills a sequential recommender into a parallel Semantic ID generator by matching a reconstructed item distribution or per-position code marginals, instead of training on hard next-item labels alone.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Key Contribution | IDM/CMM distills a sequential recommender into a parallel Semantic ID generator by matching a reconstructed item distribution or per-position code marginals, instead of training on hard next-item labels alone. |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2014 Beauty, Toys and Games, Sports and Outdoors; existing 5-core data verified without further filtering or deduplication.
  - Source: Section 4.1 and Appendix A.1: https://arxiv.org/html/2610.32943v1#S4.SS1.SSS0.Px1.p1 and https://arxiv.org/html/2610.32943v1#A1.SS1.p1
- **Split**: Per-user chronological last/penultimate interactions are test/validation; earlier events train. Histories capped at 50; test histories include validation interaction.
  - Source: Appendix A.1: https://arxiv.org/html/2610.32943v1#A1.SS1.p1 and https://arxiv.org/html/2610.32943v1#A1.SS1.p2
- **Candidates**: full catalog; no historical-item masking
  - Source: Section 4.1: https://arxiv.org/html/2610.32943v1#S4.SS1.SSS0.Px3.p1
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Section 4.1 and Appendix A.1 define standard chronological holdouts, without an unseen-item experiment: https://arxiv.org/html/2610.32943v1#S4.SS1.SSS0.Px1.p1 and https://arxiv.org/html/2610.32943v1#A1.SS1
- **SID**: 16 subspaces x 3 residual levels x 256 codes; 48 fixed heads. Collisions retained with identical scores; each item remains a distinct catalog entry.
  - Source: Section 4.1 and Appendix A.1: https://arxiv.org/html/2610.32943v1#S4.SS1.SSS0.Px2.p2 and https://arxiv.org/html/2610.32943v1#A1.SS1.p3
- **Inference budget**: Single parallel student, no teacher; Recall/NDCG@5/10; evaluation batch 32, FP32. Beam n/a; evaluation hardware and latency not reported. RTX 5880 Ada is specified for training.
  - Source: Figure 1 and Appendix A.2: https://arxiv.org/html/2610.32943v1#S3.F1 and https://arxiv.org/html/2610.32943v1#A1.SS2.SSS0.Px1.p2
- **Results from**: Table 2: IDM/CMM, AsymRec and RPG reproduced, averaged over three runs; other baseline scores copied from RPG Table 2.
  - Source: Table 2: https://arxiv.org/html/2610.32943v1#S4.T2

### 5. Connections to Related Work

- **Competitor** · [RPG](rpg.md): Reproduced parallel baseline with graph-guided decoding; IDM/CMM add soft teacher supervision.
  - Source: IDM/CMM v1, Section 4.1 and Table 2: https://arxiv.org/html/2610.32943v1#S4.SS1.SSS0.Px2.p2; https://arxiv.org/html/2610.32943v1#S4.T2.
- **Competitor** · [TIGER](tiger.md): Autoregressive baseline; its comparison scores are taken from RPG.
  - Source: IDM/CMM v1, Sections 2.2/4.1 and Table 2: https://arxiv.org/html/2610.32943v1#S2.SS2.p2; https://arxiv.org/html/2610.32943v1#S4.SS1.SSS0.Px2.p1; https://arxiv.org/html/2610.32943v1#S4.T2.
- **Alternative** · [LLaDA-Rec](llada-rec.md): Iterative diffusion contrasts with the single-pass parallel predictor.
  - Source: IDM/CMM v1, Section 2.3: https://arxiv.org/html/2610.32943v1#S2.SS3.p1.

[View all papers in this cell](../../README.md#iv--training)
