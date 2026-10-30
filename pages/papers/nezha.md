# NEZHA: NEZHA: A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2511.18793`)](https://arxiv.org/abs/2511.18793) · [Source Record (`data/papers/nezha.yaml`)](../../data/papers/nezha.yaml)

> **Summary**: Abstract: "severely hindered by high inference latency".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Wang et al. (2026) | Published / posted in `WWW’26 Industry` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Self-Draft+Hash` | Self-drafting head generation with hash-set validity filtering (NEZHA). |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "severely hindered by high inference latency".
- **`tokenizer`** (§3.4, p6; Algorithm 3): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§3.4, p6; Algorithm 3): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `V. Efficiency` × `Inference` (5 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Spec. Dec.` |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed†` | `NTP → RL†` | `FP8+RecoGEM` |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP†` | `Spec. Dec.` |
| [PFA](pfa.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `–` | `Beam` |
| [STATIC](static.md) | KDD’26 ADS | `–` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Vec. C-Beam` |
