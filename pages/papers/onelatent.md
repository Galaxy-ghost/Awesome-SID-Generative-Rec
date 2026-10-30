# OneLatent

*Latent Reasoning for Efficient Foundation Recommendation Models* — Jiang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.30675) · [Record](../../data/papers/onelatent.yaml) · [← Catalog](../../README.md#v--training)

> 明确生成Res-Kmeans三位SID；首次2026-10-22在补搜窗口，提出新的latent对齐训练与高效推荐方法。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `MM` | `R-KM` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `Beam` |

- `MM`: 原文明确使用PinCLIP多模态物品嵌入，但未展开具体构码模态组成。
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
