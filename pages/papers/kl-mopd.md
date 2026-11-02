# KL-MOPD

*Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation* — Yang et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.36973) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | `R-KM` | `Enc-Dec` | **`Fixed† / (NTP† / (NTP + Aux.)†) → KL-weighted OPD`** | `C-Beam` |

- `CF`: Collaborative filtering signal.
- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `(NTP† / (NTP + Aux.)†) → KL-weighted OPD`: Inferred next-token-based initialization variants followed by KL-weighted on-policy distillation.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
