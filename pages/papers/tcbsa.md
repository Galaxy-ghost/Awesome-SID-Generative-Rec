# TCBSA

*From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for Generative Recommendation* — Shan et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.32098) · [Record](../../data/papers/tcbsa.yaml) · [← Catalog](../../README.md#iv--inference)

> 提出不重训生成器的 SID 推理新算法，属于方法设计。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM` | `Enc-Dec† / Dec-Only†` | `Fixed / NTP† / NTP → RL` | **`CF-Guided C-Beam`** |

- `R-KM`: Residual k-means.
- `Enc-Dec† / Dec-Only†`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP† / NTP → RL`: TIGER继承NTP目标，本文未重述故†
- `CF-Guided C-Beam`: 协同评分在剪枝前逐边引导合法SID束搜索。

## Same cell: IV × Inference (1 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [ISD](isd.md) | arXiv’26 | `Text†` → `RQ-VAE†` → `Enc-Dec†` → `Fixed / NTP†` → **`ISD Beam`** |
