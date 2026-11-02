# SPAR-Youku

*SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced Semantic IDs* — Zhang et al. · arXiv’26

`I. Informativeness` · `Backbone`

[Paper](https://arxiv.org/abs/2610.27898) · [Matrix](../../README.md#i--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-PIB` | **`Dec-Only`** | `Fixed / NTP → DPO` | `C-Beam` |

- `–`: Not reported in the paper.
- `RQ-PIB`: Residual Quantization with Prefix-aware Interaction Balancing
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--backbone)
