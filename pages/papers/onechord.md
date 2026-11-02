# OneChord

*Distill What You Rank, Recommend in One Pass* — Li et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.25805) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `Par. OPQ` | `Non-AR` | **`Fixed / Next-item CE + Cons. KD + Rank KD`** | `Scoring` |

- `–`: Not reported in the paper.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Next-item CE + Cons. KD + Rank KD`: Next-item cross-entropy jointly optimized with consistency and ranking distillation.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
