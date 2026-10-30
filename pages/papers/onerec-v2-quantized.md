# OneRec-V2-Quantized: Quantized Inference for OneRec-V2

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2603.11486`)](https://arxiv.org/abs/2603.11486) · [Source Record (`data/papers/onerec-v2-quantized.yaml`)](../../data/papers/onerec-v2-quantized.yaml)

> **Summary**: 新增可区分的 FP8 PTQ 与执行栈/算子设计，适合单独 V × Inference 条目，而非只重复 OneRec-V2。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Su et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text+Img+CF†` |  |
| **Tokenization** | `R-KM†` |  |
| **Backbone** | `Lazy Dec-Only†` | 主生成模块以lazy decoder-only处理长历史，后两码用轻量顺序条件模块。 |
| **Tokenizer Training** | `Fixed†` |  |
| **Training Objective** | `NTP → RL†` |  |
| **Inference Decoding** | `FP8+RecoGEM` | FP8 权重/激活 PTQ 加直接构建 TensorRT 图及专门 TopK、attention、MoE 算子。 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Inference` (5 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Spec. Dec.` |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Self-Draft+Hash` |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP†` | `Spec. Dec.` |
| [PFA](pfa.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `–` | `Beam` |
| [STATIC](static.md) | KDD’26 ADS | `–` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Vec. C-Beam` |
