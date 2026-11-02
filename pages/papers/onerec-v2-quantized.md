# OneRec-V2-Quantized

*Quantized Inference for OneRec-V2* — Su et al. · arXiv’26

`V. Efficiency` · `Inference`

[Paper](https://arxiv.org/abs/2603.11486) · [Matrix](../../README.md#v--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed† / NTP → RL†` | **`FP8+RecoGEM`** |

- `Lazy Dec-Only†`: A lazy decoder-only backbone inferred from the adopted model.
- `FP8+RecoGEM`: FP8 inference with the RecoGEM execution framework.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--inference)
