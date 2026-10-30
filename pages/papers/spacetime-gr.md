# Spacetime-GR: Spacetime-GR: A Spacetime-Aware Generative Model for Large Scale Online POI Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2508.16126`)](https://arxiv.org/abs/2508.16126) · [Source Record (`data/papers/spacetime-gr.yaml`)](../../data/papers/spacetime-gr.yaml)

> **Summary**: 工业版本以二元地理标识生成完整POI，映射原文明确一一对应；表值限生成推荐分支。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Lin et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Geo` | Geographic coordinates and spatial index features (Spacetime-GR). |
| **Tokenization** | `Geo-Idx` | 地理块+块内序号的两token层次索引，沿用LGSID的Geo-Idx写法。 |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → DPO` | NTP, then preference optimization. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Backbone` (6 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` | `Dual H-KM` | `Dual Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` | `Casc. RQ` | `Dec-Only` | `Fixed` | `NTP + Dense` | `BeamFusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` | `RQ-PIB` | `Dec-Only` | `Fixed` | `NTP → DPO` | `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `NTP + Rank` | `Beam` |
