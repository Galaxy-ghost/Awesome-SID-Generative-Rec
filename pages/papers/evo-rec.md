# Evo-Rec

*Learning Better Reasoning for Generative Recommendation with Semantic IDs* — Zhu et al., arXiv’26

[arXiv](https://arxiv.org/abs/2609.29973) · [Record](../../data/papers/evo-rec.yaml) · [← Catalog](../../README.md#iii--training)

> 提出推理效用筛选和基于 SID 排名的 GRPO，完整约束 SID 解码。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / NTP → RL`** | `CoT+C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT+C-Beam`: Reasoning followed by constrained beam-search decoding.

## Same cell: III × Training (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `Beam` |
| [ETEGRec](etegrec.md) | SIGIR’25 | `CF` → `Learn. RQ` → `Enc-Dec` → **`Altern. / NTP + Ctr.`** → `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` → `RQ-KM` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [OneRec-Think](onerec-think.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT` |
| [GTI](gti.md) | arXiv’26 | `Text+CF / Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `–` |
| [Intent-Driven-News](intent-driven-news.md) | ACL’26 Industry | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `CoT+Fuzzy Match` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+Beam` |
