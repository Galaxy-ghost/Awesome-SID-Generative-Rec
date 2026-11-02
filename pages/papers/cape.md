# CAPE

*Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval and Ranking* — Huang et al. · arXiv’26

`I. Informativeness` · `Inference`

[Paper](https://arxiv.org/abs/2610.29298) · [Matrix](../../README.md#i--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE†` | `Dec-Only / Enc-Dec` | `Fixed / Multi-task NTP† / NTP†` | **`Hybrid`** |

- `Dec-Only / Enc-Dec`: Decoder-only and encoder–decoder backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP† / NTP†`: Inferred multi-task or single-task next-token-prediction initialization in different backbones.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--inference)
