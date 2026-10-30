# Intent-Driven-News

*Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation* — Su et al., ACL’26 Industry

[arXiv](https://arxiv.org/abs/2605.07613) · [Record](../../data/papers/intent-driven-news.yaml) · [← Catalog](../../README.md#iii--training)

> 明确生成离散 SID 前缀并接目录解析，适合广义 SID 生成综述；不属于完整唯一 SID 直接生成子集。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `CoT+Fuzzy Match` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `CoT+Fuzzy Match`: 生成推理与3层 SID 前缀，通过动态池模糊匹配落到文章，省略第4层近唯一判别码。

## Same cell: III × Training (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `Beam` |
| [ETEGRec](etegrec.md) | SIGIR’25 | `CF` → `Learn. RQ` → `Enc-Dec` → **`Altern. / NTP + Ctr.`** → `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` → `RQ-KM` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [OneRec-Think](onerec-think.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT` |
| [Evo-Rec](evo-rec.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [GTI](gti.md) | arXiv’26 | `Text+CF / Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `–` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+Beam` |
