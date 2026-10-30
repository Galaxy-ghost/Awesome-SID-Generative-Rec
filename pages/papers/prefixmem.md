# PrefixMem: LLMs Need Encoders for Semantic IDs Too

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2606.00324`)](https://arxiv.org/abs/2606.00324) · [Source Record (`data/papers/prefixmem.yaml`)](../../data/papers/prefixmem.yaml)

> **Summary**: 给固定SID码位加入前缀条件记忆表示，让生成器识别同一码在不同前缀下的含义。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Chen et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `MM` | 原文明确使用PinCLIP多模态物品嵌入，但未展开具体构码模态组成。 |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `III. SID–Model Alignment` × `Backbone` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` | `Par. VQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` | `SimHash` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` | `RQ-VAE / R-KM / LETTER` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.+Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` | `CoBa RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `C-Beam` |
