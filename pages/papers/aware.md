# AWARE

*Why Users Go There: World Knowledge-Augmented Generative Next POI Recommendation* — Ding et al., arXiv’26 · `POI`

[arXiv](https://arxiv.org/abs/2605.11807) · [Record](../../data/papers/aware.yaml) · [← Catalog](../../README.md#vi--training)

> 沿用ROS的SID生成骨干，增量是有原文机制和实验支撑的世界知识获取及历史选择。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Geo` | `Geo-Prefix+HClus` | `Dec-Only` | **`Fixed / NTP`** | `–` |

- `Geo-Prefix+HClus`: S2地理前缀加层次聚类
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

## Same cell: VI × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [RecBase](recbase.md) | EMNLP’25 | `Text` → `Curr. RQ` → `Dec-Only` → **`Fixed / NTP`** → `Beam` |
| [CausalDPO](causaldpo.md) | ICML’26 | `Text` → `LLM-Vocab` → `Dec-Only` → **`Fixed / NTP → DPO`** → `Scoring` |
| [CMRec](cmrec.md) | CIKM’26 Short | `Text+Img+CF` → `RQ-VAE` → `Dec-Only†` → **`– / NTP`** → `–` |
