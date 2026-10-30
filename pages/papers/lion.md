# LION

*Self-Evolving Memory for Generative Recommendation* — Lin et al., CIKM’26

[arXiv](https://arxiv.org/abs/2609.15598) · [Record](../../data/papers/lion.yaml) · [← Catalog](../../README.md#vi--backbone)

> 实现继承 TIGER，按其文本 SID 管线推断；本文未明确重述输入。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE†` | **`Enc-Dec`** | `Fixed† / NTP + Aux.` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `NTP + Aux.`: NTP plus another auxiliary loss.

## Same cell: VI × Backbone (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [DualGR](dualgr.md) | WWW’26 Short | `–` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Rank` → `Dual Beam` |
| [FedCGR](fedcgr.md) | CIKM’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP + Aux.` → `C-Beam` |
