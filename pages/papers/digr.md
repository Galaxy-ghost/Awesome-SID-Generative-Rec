# DiGR

*From Token Generation to Item Ranking: Direct Generative Recommendation with Semantic IDs* — Zhao et al. · arXiv’26

`IV. Utility` · `Backbone`

[Paper](https://arxiv.org/abs/2602.07847) · [Matrix](../../README.md#iv--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | **`Dec-Only`** | `Fixed / Discrim.` | `Scoring` |

- `–`: Not reported in the paper.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--backbone)
