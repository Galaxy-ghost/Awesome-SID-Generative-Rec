# APAO

*Bridging the Training-Inference Gap in Generative Recommendation via Adaptive Prefix-Aware Optimization* — Yu et al. · KDD’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2603.02730) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM` | `Enc-Dec / Dec-Only` | **`Fixed / NTP + Rank`** | `Beam` |

- `R-KM`: Residual k-means.
- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
