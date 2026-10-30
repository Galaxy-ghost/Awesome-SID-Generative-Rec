# FedCGR

*Federated Cross-Domain Generative Recommendation* — Liu et al., CIKM’26

[arXiv](https://arxiv.org/abs/2608.10929) · [Record](../../data/papers/fedcgr.yaml) · [← Catalog](../../README.md#vi--backbone)

> BGE-base-en-v1.5 编码公共 title/category/description；本地 SASRec CF 是后加输入，不进入冻结 tokenizer。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Enc-Dec`** | `Fixed / NTP + Aux.` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

## Same cell: VI × Backbone (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [DualGR](dualgr.md) | WWW’26 Short | `–` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Rank` → `Dual Beam` |
| [LION](lion.md) | CIKM’26 | `Text†` → `RQ-VAE†` → **`Enc-Dec`** → `Fixed† / NTP + Aux.` → `Beam` |
