# Gryphon

*A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations* — Tikhonovich et al., CIKM’26 Short

[arXiv](https://arxiv.org/abs/2606.08604) · [Record](../../data/papers/gryphon.yaml) · [← Catalog](../../README.md#iv--backbone)

> 有完整 SID 生成和 item-level scoring 新架构；放弃唯一 SID 并不使其成为非 SID。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `R-KM` | **`Enc-Dec`** | `Fixed / NTP + Rank` | `Hybrid` |

- `–`: Not reported in the paper, or not applicable.
- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

## Same cell: IV × Backbone (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [DiGR](digr.md) | arXiv’26 | `–` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Discrim.` → `Scoring` |
| [RecoChain](recochain.md) | arXiv’26 | `Text+Img` → `RQ` → **`Dec-Only`** → `Fixed / NTP + Rank` → `Hybrid` |
