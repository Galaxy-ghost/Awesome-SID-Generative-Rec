# DiGR

*From Token Generation to Item Ranking: Direct Generative Recommendation with Semantic IDs* — Zhao et al., arXiv’26

[arXiv](https://arxiv.org/abs/2602.07847) · [Record](../../data/papers/digr.yaml) · [← Catalog](../../README.md#iv--backbone)

> 保留真实离散 SID 并提出完整的新推荐模型，虽不逐码生成，可按已准许例外收录。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | **`Dec-Only`** | `Fixed / Discrim.` | `Scoring` |

- `–`: Not reported in the paper, or not applicable.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

## Same cell: IV × Backbone (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [Gryphon](gryphon.md) | CIKM’26 Short | `–` → `R-KM` → **`Enc-Dec`** → `Fixed / NTP + Rank` → `Hybrid` |
| [RecoChain](recochain.md) | arXiv’26 | `Text+Img` → `RQ` → **`Dec-Only`** → `Fixed / NTP + Rank` → `Hybrid` |
