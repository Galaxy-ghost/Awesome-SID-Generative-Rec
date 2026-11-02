# Spacetime-GR

*A Spacetime-Aware Generative Model for Large Scale Online POI Recommendation* — Lin et al. · arXiv’25

`I. Informativeness` · `Backbone` · `POI`

[Paper](https://arxiv.org/abs/2508.16126) · [Matrix](../../README.md#i--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Geo` | `Geo-Idx` | **`Dec-Only`** | `Fixed / NTP → DPO` | `Beam` |

- `Geo`: Geographic coordinates or spatial features.
- `Geo-Idx`: Identifiers constructed from geographic indexing.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--backbone)
