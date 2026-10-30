# GMC: Generative Multi-Target Cross-Domain Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2507.12871`)](https://arxiv.org/abs/2507.12871) · [Source Record (`data/papers/gmc.yaml`)](../../data/papers/gmc.yaml)

> **Summary**: Abstract: "may be unavailable in non-overlapped recommendation scenarios".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Jin et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Cross-Dom` |  |
| **Tokenization** | `Unified RQ` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "may be unavailable in non-overlapped recommendation scenarios".

## Peer Methods in `VI. Generalization` × `Tokenization` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` | `OPQ` | `Encoder` | `Fixed` | `Discrim.` | `Scoring` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` | `Tree` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` | `CART` | `Dec-Only` | `Altern.` | `NTP + Aux.` | `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` | `RQ+LoRA` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` | `RQ` | `Dec-Only` | `Fixed†` | `NTP + Aux.` | `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` | `R-KM` | `Lazy Dec-Only` | `Fixed` | `NTP + RL` | `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` | `TokenMoE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
