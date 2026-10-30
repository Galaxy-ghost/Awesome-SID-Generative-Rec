# FLASH: Rethinking Semantic ID Construction for Generative Recommendation: SimHash with Parallel Decoding and Semantic Alignment

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.07402`)](https://arxiv.org/abs/2610.07402) · [Source Record (`data/papers/flash.yaml`)](../../data/papers/flash.yaml)

> **Summary**: 提出离散 SimHash SID 的完整生成推荐新设计。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu et al. (2026) | Published / posted in `NeurIPS’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `SimHash` | 固定随机超平面局部敏感哈希。 |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `MTP + Aux.` | 并行码位预测，加无负例负余弦语义对齐。 |
| **Inference Decoding** | `Scoring` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `III. SID–Model Alignment` × `Backbone` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` | `Par. VQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` | `RQ-VAE / R-KM / LETTER` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` | `CoBa RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `C-Beam` |
