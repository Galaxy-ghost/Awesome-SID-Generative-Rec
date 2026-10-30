# DREAM: DREAM: Dynamic Refinement of Early Assignment Mappings

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2606.06947`)](https://arxiv.org/abs/2606.06947) · [Source Record (`data/papers/dream.yaml`)](../../data/papers/dream.yaml)

> **Summary**: 提出冷物品 SID 重新分配及多路径生成新方法。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Guan et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `CART` | Collaborative-Aware Refined Tokenization，协同感知码分配及候选池。 |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Altern.` | Tokenizer and generator are updated in turns. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `VI. Generalization` × `Tokenization` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` | `OPQ` | `Encoder` | `Fixed` | `Discrim.` | `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` | `Unified RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` | `Tree` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `–` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` | `RQ+LoRA` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` | `RQ` | `Dec-Only` | `Fixed†` | `NTP + Aux.` | `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` | `R-KM` | `Lazy Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` | `TokenMoE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
