# STATIC: Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.22647`)](https://arxiv.org/abs/2602.22647) · [Source Record (`data/papers/static.yaml`)](../../data/papers/static.yaml)

> **Summary**: Abstract: "incur severe latency penalties on hardware accelerators (TPUs/GPUs)".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Su et al. (2026) | Published / posted in `KDD’26 ADS` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Vec. C-Beam` | Vectorized constrained beam search (STATIC). |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "incur severe latency penalties on hardware accelerators (TPUs/GPUs)".
- **`tokenizer`** (p8–9): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (p8–9): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `V. Efficiency` × `Inference` (5 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Spec. Dec.` |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Self-Draft+Hash` |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed†` | `NTP → RL†` | `FP8+RecoGEM` |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP†` | `Spec. Dec.` |
| [PFA](pfa.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `–` | `Beam` |
