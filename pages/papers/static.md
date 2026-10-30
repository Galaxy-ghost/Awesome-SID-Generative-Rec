# STATIC

*Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators* — Su et al., KDD’26 ADS

[arXiv](https://arxiv.org/abs/2602.22647) · [Record](../../data/papers/static.yaml) · [← Catalog](../../README.md#v--inference)

> Abstract: "incur severe latency penalties on hardware accelerators (TPUs/GPUs)".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Dec-Only` | `Fixed / NTP` | **`Vec. C-Beam`** |

- `–`: Not reported in the paper, or not applicable.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Vec. C-Beam`: Vectorized constrained beam search (STATIC).

## Evidence

- **`problem`** (arXiv abstract): Abstract: "incur severe latency penalties on hardware accelerators (TPUs/GPUs)".
- **`tokenizer`** (p8–9): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (p8–9): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: V × Inference (5 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Spec. Dec.`** |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Self-Draft+Hash`** |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` → `R-KM†` → `Lazy Dec-Only†` → `Fixed† / NTP → RL†` → **`FP8+RecoGEM`** |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP†` → **`Spec. Dec.`** |
| [PFA](pfa.md) | arXiv’26 | `–` → `–` → `Enc-Dec` → `– / –` → **`Beam`** |
