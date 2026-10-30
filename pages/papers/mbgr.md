# MBGR: MBGR: Multi-Business Prediction for Generative Recommendation at Meituan

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2604.02684`)](https://arxiv.org/abs/2604.02684) · [Source Record (`data/papers/mbgr.yaml`)](../../data/papers/mbgr.yaml)

> **Summary**: Abstract: "a seesaw phenomenon in multi-business scenarios"; "a unified SID space causes". Candidates: VI / II (rule: judged by the abstract's complaint first).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Li et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `RQ` | Residual quantization. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed†` |  |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "a seesaw phenomenon in multi-business scenarios"; "a unified SID space causes". Candidates: VI / II (rule: judged by the abstract's complaint first).
- **`tokenizer`** (p4): SID construction not described; Fixed is inferred. Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p4): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `VI. Generalization` × `Tokenization` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` | `OPQ` | `Encoder` | `Fixed` | `Discrim.` | `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` | `Unified RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` | `Tree` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` | `CART` | `Dec-Only` | `Altern.` | `NTP + Aux.` | `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` | `RQ+LoRA` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` | `R-KM` | `Lazy Dec-Only` | `Fixed` | `NTP + RL` | `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` | `TokenMoE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
