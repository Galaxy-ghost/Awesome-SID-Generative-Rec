# SPAR

*Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception* — Wang et al. · arXiv’26

`I. Informativeness` · `Representation` · `POI`

[Paper](https://arxiv.org/abs/2609.02062) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Geo`** | `R-KM` | `Dec-Only` | `Fixed / Multi-task NTP` | `–` |

- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
