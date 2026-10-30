# DACT: Drift-Aware Continual Tokenization for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2603.29705`)](https://arxiv.org/abs/2603.29705) · [Source Record (`data/papers/dact.yaml`)](../../data/papers/dact.yaml)

> **Summary**: 给完整 SID 生成模型提供持续更新编号器的新设计，在 TIGER 与 LC-Rec 验证。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Feng et al. (2026) | Published / posted in `SIGIR’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec / Dec-Only` | Evaluated on both Encoder-Decoder and Decoder-Only backbones. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `VI. Generalization` × `Tokenization` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` | `OPQ` | `Encoder` | `Fixed` | `Discrim.` | `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` | `Unified RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` | `Tree` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` | `CART` | `Dec-Only` | `Altern.` | `NTP + Aux.` | `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` | `RQ+LoRA` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` | `RQ` | `Dec-Only` | `Fixed†` | `NTP + Aux.` | `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` | `R-KM` | `Lazy Dec-Only` | `Fixed` | `NTP + RL` | `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` | `TokenMoE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
