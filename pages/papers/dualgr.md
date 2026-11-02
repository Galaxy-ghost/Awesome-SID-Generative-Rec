# DualGR

*Generative Retrieval with Long and Short-Term Interests Modeling* — Yi et al. · WWW’26 Short

`VI. Generalization` · `Backbone`

[Paper](https://arxiv.org/abs/2511.12518) · [Matrix](../../README.md#vi--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `R-KM` | **`Dec-Only`** | `Fixed / NTP + Rank` | `Dual Beam` |

- `–`: Not reported in the paper.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.
- `Dual Beam`: Beam-search decoding in two branches with merged candidates.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--backbone)
