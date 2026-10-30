# CMRec

*Cross-Country Code-Mixing for Generative Recommendation* — Gao et al., CIKM’26 Short

[arXiv](https://arxiv.org/abs/2609.28972) · [Record](../../data/papers/cmrec.yaml) · [← Catalog](../../README.md#vi--training)

> 文本/图像用Qwen-VL-32B编码，再跨国i2i sampled softmax对齐注入行为；动态属性仅混合筛选不计SID输入。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | `Dec-Only†` | **`– / NTP`** | `–` |

- `–`: No SID is built.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

## Same cell: VI × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [RecBase](recbase.md) | EMNLP’25 | `Text` → `Curr. RQ` → `Dec-Only` → **`Fixed / NTP`** → `Beam` |
| [AWARE](aware.md) | arXiv’26 | `Text+Geo` → `Geo-Prefix+HClus` → `Dec-Only` → **`Fixed / NTP`** → `–` |
| [CausalDPO](causaldpo.md) | ICML’26 | `Text` → `LLM-Vocab` → `Dec-Only` → **`Fixed / NTP → DPO`** → `Scoring` |
