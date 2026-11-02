# SAHL

*Structure-Aligned History Learning with Subspace-Structured Semantic IDs for Generative Recommendation* — Wei et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.25093) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `SRBQ` | `Non-AR` | **`Fixed / (MTP + Masked Rec.) → MTP`** | `Graph` |

- `SRBQ`: Semantic Residual Balanced Quantization
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `(MTP + Masked Rec.) → MTP`: Joint multi-token prediction and masked reconstruction, followed by multi-token prediction alone.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
