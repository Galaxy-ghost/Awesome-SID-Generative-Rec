# SPRINT

*Single-Step Generative Recommendation via Average Probability Velocity* — Cai et al. · arXiv’26

`V. Efficiency` · `Backbone`

[Paper](https://arxiv.org/abs/2609.34306) · [Matrix](../../README.md#v--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Par. OPQ` | **`Non-AR`** | `Fixed / Dual-level Flow Ctr.` | `Scoring` |

- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Dual-level Flow Ctr.`: Contrastive training at token and complete-identifier levels in a flow-based model.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--backbone)
