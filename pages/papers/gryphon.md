# Gryphon: Gryphon: A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2606.08604`)](https://arxiv.org/abs/2606.08604) · [Source Record (`data/papers/gryphon.yaml`)](../../data/papers/gryphon.yaml)

> **Summary**: 有完整 SID 生成和 item-level scoring 新架构；放弃唯一 SID 并不使其成为非 SID。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Tikhonovich et al. (2026) | Published / posted in `CIKM’26 Short` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Rank` | NTP plus a ranking loss. |
| **Inference Decoding** | `Hybrid` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `IV. Utility` × `Backbone` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [DiGR](digr.md) | arXiv’26 | `–` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Discrim.` | `Scoring` |
| [RecoChain](recochain.md) | arXiv’26 | `Text+Img` | `RQ` | `Dec-Only` | `Fixed` | `NTP + Rank` | `Hybrid` |
