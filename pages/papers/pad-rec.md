# PAD-Rec

*Position-Aware Drafting for Inference Acceleration in LLM-Based Generative List-Wise Recommendation* — Chen et al., arXiv’26

[arXiv](https://arxiv.org/abs/2604.27747) · [Record](../../data/papers/pad-rec.yaml) · [← Catalog](../../README.md#v--inference)

> Abstract: "decoding remains sequential and thus latency-prone".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed / Multi-task NTP†` | **`Spec. Dec.`** |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Spec. Dec.`: Speculative decoding.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "decoding remains sequential and thus latency-prone".
- **`tokenizer`** (p6): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p6): Target model follows LC-Rec; inferred from LC-Rec's multi-task training. Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

在投机解码的草稿模型中加入 SID 位置信息，加速列表式生成。

## Same cell: V × Inference (5 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Spec. Dec.`** |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Self-Draft+Hash`** |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` → `R-KM†` → `Lazy Dec-Only†` → `Fixed† / NTP → RL†` → **`FP8+RecoGEM`** |
| [PFA](pfa.md) | arXiv’26 | `–` → `–` → `Enc-Dec` → `– / –` → **`Beam`** |
| [STATIC](static.md) | KDD’26 ADS | `–` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Vec. C-Beam`** |
