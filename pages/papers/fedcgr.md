# FedCGR: FedCGR: Federated Cross-Domain Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2608.10929`)](https://arxiv.org/abs/2608.10929) · [Source Record (`data/papers/fedcgr.yaml`)](../../data/papers/fedcgr.yaml)

> **Summary**: BGE-base-en-v1.5 编码公共 title/category/description；本地 SASRec CF 是后加输入，不进入冻结 tokenizer。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu et al. (2026) | Published / posted in `CIKM’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `VI. Generalization` × `Backbone` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [DualGR](dualgr.md) | WWW’26 Short | `–` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Rank` | `Dual Beam` |
| [LION](lion.md) | CIKM’26 | `Text†` | `RQ-VAE†` | `Enc-Dec` | `Fixed†` | `NTP + Aux.` | `Beam` |
