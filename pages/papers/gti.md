# GTI

*Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation* — Chen et al., arXiv’26

[arXiv](https://arxiv.org/abs/2604.02324) · [Record](../../data/papers/gti.yaml) · [← Catalog](../../README.md#iii--training)

> 提出明确可复用的词嵌入 grounding 训练阶段，并在真实离散 RQ-VAE SID 推荐中验证。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF / Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `–` |

- `Text+CF / Text`: Text with collaborative signals, or text-only representations, in different configurations.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `–`: Not reported in the paper.

## Same cell: III × Training (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `Beam` |
| [ETEGRec](etegrec.md) | SIGIR’25 | `CF` → `Learn. RQ` → `Enc-Dec` → **`Altern. / NTP + Ctr.`** → `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` → `RQ-KM` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [OneRec-Think](onerec-think.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT` |
| [Evo-Rec](evo-rec.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [Intent-Driven-News](intent-driven-news.md) | ACL’26 Industry | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `CoT+Fuzzy Match` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+Beam` |
