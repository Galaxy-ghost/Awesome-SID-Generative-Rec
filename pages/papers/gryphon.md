# Gryphon

*A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations* — Tikhonovich et al. · CIKM’26 Short

`IV. Utility` · `Backbone`

[Paper](https://arxiv.org/abs/2606.08604) · [Matrix](../../README.md#iv--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `R-KM` | **`Enc-Dec`** | `Fixed / NTP + Rank` | `Hybrid` |

- `–`: Not reported in the paper.
- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--backbone)
