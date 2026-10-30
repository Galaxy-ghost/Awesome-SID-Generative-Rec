# ISD: Understanding Semantic IDs: From Item Representation to Item Selection in Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2607.24995`)](https://arxiv.org/abs/2607.24995) · [Source Record (`data/papers/isd.yaml`)](../../data/papers/isd.yaml)

> **Summary**: 有明确推理解码新设计 ISD，不能只按标题认定纯分析。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Wang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text†` |  |
| **Tokenization** | `RQ-VAE†` |  |
| **Backbone** | `Enc-Dec†` |  |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP†` |  |
| **Inference Decoding** | `ISD Beam` | item rank在beam reduction前支持prefix，生成后同rank融合排序 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `IV. Utility` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TCBSA](tcbsa.md) | arXiv’26 | `Text` | `R-KM` | `Enc-Dec† / Dec-Only†` | `Fixed` | `NTP† / NTP → RL` | `CF-Guided C-Beam` |
