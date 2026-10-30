# UTGRec: Universal Item Tokenization for Transferable Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2504.04405`)](https://arxiv.org/abs/2504.04405) · [Source Record (`data/papers/utgrec.yaml`)](../../data/papers/utgrec.yaml)

> **Summary**: Abstract: "typically domain-specific, limiting their ability for effective transfer or adaptation to new domains".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zheng et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Multi-Dom` |  |
| **Tokenization** | `Tree` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "typically domain-specific, limiting their ability for effective transfer or adaptation to new domains".

## Peer Methods in `VI. Generalization` × `Tokenization` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` | `OPQ` | `Encoder` | `Fixed` | `Discrim.` | `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` | `Unified RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` | `CART` | `Dec-Only` | `Altern.` | `NTP + Aux.` | `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` | `RQ+LoRA` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` | `RQ` | `Dec-Only` | `Fixed†` | `NTP + Aux.` | `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` | `R-KM` | `Lazy Dec-Only` | `Fixed` | `NTP + RL` | `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` | `TokenMoE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
