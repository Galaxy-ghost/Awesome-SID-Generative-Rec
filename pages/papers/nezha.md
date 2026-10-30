# NEZHA

*A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations* — Wang et al., WWW’26 Industry

[arXiv](https://arxiv.org/abs/2511.18793) · [Record](../../data/papers/nezha.yaml) · [← Catalog](../../README.md#v--inference)

> Abstract: "severely hindered by high inference latency".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | `Fixed / NTP` | **`Self-Draft+Hash`** |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Self-Draft+Hash`: Self-drafting head generation with hash-set validity filtering (NEZHA).

## Evidence

- **`problem`** (arXiv abstract): Abstract: "severely hindered by high inference latency".
- **`tokenizer`** (§3.4, p6; Algorithm 3): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§3.4, p6; Algorithm 3): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: V × Inference (5 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Spec. Dec.`** |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` → `R-KM†` → `Lazy Dec-Only†` → `Fixed† / NTP → RL†` → **`FP8+RecoGEM`** |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP†` → **`Spec. Dec.`** |
| [PFA](pfa.md) | arXiv’26 | `–` → `–` → `Enc-Dec` → `– / –` → **`Beam`** |
| [STATIC](static.md) | KDD’26 ADS | `–` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Vec. C-Beam`** |
