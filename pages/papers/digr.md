# DiGR: From Token Generation to Item Ranking: Direct Generative Recommendation with Semantic IDs

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.07847`)](https://arxiv.org/abs/2602.07847) · [Source Record (`data/papers/digr.yaml`)](../../data/papers/digr.yaml)

> **Summary**: 保留真实离散 SID 并提出完整的新推荐模型，虽不逐码生成，可按已准许例外收录。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhao et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `–` | No SID is built. |
| **Training Objective** | `Discrim.` | Scores items; does not generate SIDs. |
| **Inference Decoding** | `Scoring` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `IV. Utility` × `Backbone` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Gryphon](gryphon.md) | CIKM’26 Short | `–` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP + Rank` | `Hybrid` |
| [RecoChain](recochain.md) | arXiv’26 | `Text+Img` | `RQ` | `Dec-Only` | `Fixed` | `NTP + Rank` | `Hybrid` |
