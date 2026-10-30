# TCBSA: From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.32098`)](https://arxiv.org/abs/2610.32098) · [Source Record (`data/papers/tcbsa.yaml`)](../../data/papers/tcbsa.yaml)

> **Summary**: 提出不重训生成器的 SID 推理新算法，属于方法设计。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Shan et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Enc-Dec† / Dec-Only†` | Evaluated on both Encoder-Decoder and Decoder-Only backbones. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP† / NTP → RL` | TIGER继承NTP目标，本文未重述故† |
| **Inference Decoding** | `CF-Guided C-Beam` | 协同评分在剪枝前逐边引导合法SID束搜索。 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `IV. Utility` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ISD](isd.md) | arXiv’26 | `Text†` | `RQ-VAE†` | `Enc-Dec†` | `Fixed` | `NTP†` | `ISD Beam` |
