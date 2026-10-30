# ISD

*Understanding Semantic IDs: From Item Representation to Item Selection in Generative Recommendation* — Wang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2607.24995) · [Record](../../data/papers/isd.yaml) · [← Catalog](../../README.md#iv--inference)

> 有明确推理解码新设计 ISD，不能只按标题认定纯分析。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE†` | `Enc-Dec†` | `Fixed / NTP†` | **`ISD Beam`** |

- `Fixed`: SIDs are built first and not changed while the generator trains.
- `ISD Beam`: item rank在beam reduction前支持prefix，生成后同rank融合排序

## Same cell: IV × Inference (1 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [TCBSA](tcbsa.md) | arXiv’26 | `Text` → `R-KM` → `Enc-Dec† / Dec-Only†` → `Fixed / NTP† / NTP → RL` → **`CF-Guided C-Beam`** |
