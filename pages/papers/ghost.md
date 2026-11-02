# Ghost

*Echoes in Filter Bubble: Diagnosing and Curing Popularity Bias in Generative Recommenders* — Yin et al. · NeurIPS’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2605.16825) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Skeleton R-KM` | `Dec-Only` | **`Fixed / NTP + Aux.`** | `–` |

- `Skeleton R-KM`: Residual k-means organized around a shared semantic skeleton.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
