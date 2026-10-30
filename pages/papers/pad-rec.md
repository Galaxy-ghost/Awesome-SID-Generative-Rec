# PAD-Rec: Position-Aware Drafting for Inference Acceleration in LLM-Based Generative List-Wise Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2604.27747`)](https://arxiv.org/abs/2604.27747) · [Source Record (`data/papers/pad-rec.yaml`)](../../data/papers/pad-rec.yaml)

> **Summary**: Abstract: "decoding remains sequential and thus latency-prone".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Chen et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text+SID` | Text representation plus semantic IDs (hybrid dense and generative retrieval). |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP†` |  |
| **Inference Decoding** | `Spec. Dec.` | Speculative decoding. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "decoding remains sequential and thus latency-prone".
- **`tokenizer`** (p6): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p6): Target model follows LC-Rec; inferred from LC-Rec's multi-task training. Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

在投机解码的草稿模型中加入 SID 位置信息，加速列表式生成。

## Peer Methods in `V. Efficiency` × `Inference` (5 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Spec. Dec.` |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Self-Draft+Hash` |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed†` | `NTP → RL†` | `FP8+RecoGEM` |
| [PFA](pfa.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `–` | `Beam` |
| [STATIC](static.md) | KDD’26 ADS | `–` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Vec. C-Beam` |
