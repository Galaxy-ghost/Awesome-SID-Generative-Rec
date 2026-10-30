# AtSpeed

*Efficient Inference for Large Language Model-based Generative Recommendation* — Lin et al., ICLR’25

[arXiv](https://arxiv.org/abs/2410.05165) · [Record](../../data/papers/atspeed.yaml) · [← Catalog](../../README.md#v--inference)

> Abstract: "excessive inference latency caused by autoregressive decoding".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | `Fixed / NTP` | **`Spec. Dec.`** |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Spec. Dec.`: Speculative decoding.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "excessive inference latency caused by autoregressive decoding".
- **`representation`** (§4.1 Implementation Details, p7; Appendix A.3.1, p21): Taken from the LC-Rec row of Table 1.
- **`tokenizer`** (p7): Location from the 10-26 'Training split' table in the appendix.

## Same cell: V × Inference (5 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Self-Draft+Hash`** |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` → `R-KM†` → `Lazy Dec-Only†` → `Fixed† / NTP → RL†` → **`FP8+RecoGEM`** |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP†` → **`Spec. Dec.`** |
| [PFA](pfa.md) | arXiv’26 | `–` → `–` → `Enc-Dec` → `– / –` → **`Beam`** |
| [STATIC](static.md) | KDD’26 ADS | `–` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Vec. C-Beam`** |
