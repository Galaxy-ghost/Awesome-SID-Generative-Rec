# ACERec

*Unleash the Potential of Long Semantic IDs for Generative Recommendation* — Xia et al. · arXiv’26

`V. Efficiency` · `Backbone`

[Paper](https://arxiv.org/abs/2602.13573) · [Matrix](../../README.md#v--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Par. OPQ` | **`Non-AR`** | `Fixed / MTP + Ctr. + Aux.` | `Scoring` |

- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Ctr. + Aux.`: Multi-token prediction jointly optimized with contrastive and auxiliary objectives.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--backbone)
