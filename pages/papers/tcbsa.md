# TCBSA

*From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for Generative Recommendation* — Shan et al. · arXiv’26

`IV. Utility` · `Inference`

[Paper](https://arxiv.org/abs/2610.32098) · [Matrix](../../README.md#iv--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM` | `Enc-Dec† / Dec-Only†` | `Fixed / NTP† / NTP → RL` | **`CF-Guided C-Beam`** |

- `R-KM`: Residual k-means.
- `Enc-Dec† / Dec-Only†`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP† / NTP → RL`: Inferred next-token training in one configuration, or next-token training followed by reinforcement learning in another.
- `CF-Guided C-Beam`: Constrained beam search guided by collaborative signals.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--inference)
