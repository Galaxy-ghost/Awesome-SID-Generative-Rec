# PinGER

*Token-Efficient Generative Retrieval with Semantic IDs* — Li et al. · arXiv’26

`V. Efficiency` · `Backbone`

[Paper](https://arxiv.org/abs/2610.33435) · [Matrix](../../README.md#v--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | **`Dec-Only`** | `– / NTP → DPO` | `Div. C-Beam` |

- `Dec-Only`: Decoder-only.
- `–`: Not reported in the paper.
- `NTP → DPO`: NTP, then preference optimization.
- `Div. C-Beam`: Constrained beam search with an explicit diversity mechanism.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--backbone)
