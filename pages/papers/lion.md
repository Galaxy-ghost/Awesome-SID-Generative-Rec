# LION: Self-Evolving Memory for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2609.15598`)](https://arxiv.org/abs/2609.15598) · [Source Record (`data/papers/lion.yaml`)](../../data/papers/lion.yaml)

> **Summary**: 实现继承 TIGER，按其文本 SID 管线推断；本文未明确重述输入。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Lin et al. (2026) | Published / posted in `CIKM’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text†` |  |
| **Tokenization** | `RQ-VAE†` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed†` |  |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `VI. Generalization` × `Backbone` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [DualGR](dualgr.md) | WWW’26 Short | `–` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Rank` | `Dual Beam` |
| [FedCGR](fedcgr.md) | CIKM’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `C-Beam` |
