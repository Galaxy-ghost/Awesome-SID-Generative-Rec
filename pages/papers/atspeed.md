# AtSpeed: Efficient Inference for Large Language Model-based Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2410.05165`)](https://arxiv.org/abs/2410.05165) · [Source Record (`data/papers/atspeed.yaml`)](../../data/papers/atspeed.yaml)

> **Summary**: Abstract: "excessive inference latency caused by autoregressive decoding".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Lin et al. (2025) | Published / posted in `ICLR’25` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Spec. Dec.` | Speculative decoding. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "excessive inference latency caused by autoregressive decoding".
- **`representation`** (§4.1 Implementation Details, p7; Appendix A.3.1, p21): Taken from the LC-Rec row of Table 1.
- **`tokenizer`** (p7): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `V. Efficiency` × `Inference` (5 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Self-Draft+Hash` |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed†` | `NTP → RL†` | `FP8+RecoGEM` |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP†` | `Spec. Dec.` |
| [PFA](pfa.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `–` | `Beam` |
| [STATIC](static.md) | KDD’26 ADS | `–` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Vec. C-Beam` |
