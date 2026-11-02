# OneLatent

*Latent Reasoning for Efficient Foundation Recommendation Models* — Jiang et al. · arXiv’26

`V. Efficiency` · `Training`

[Paper](https://arxiv.org/abs/2610.30675) · [Matrix](../../README.md#v--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `MM` | `R-KM` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `Beam` |

- `MM`: Multimodal item representations.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--training)
