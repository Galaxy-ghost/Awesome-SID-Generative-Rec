# VQ-Rec: Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2210.12316`)](https://arxiv.org/abs/2210.12316) · [Source Record (`data/papers/vq-rec.yaml`)](../../data/papers/vq-rec.yaml)

> **Summary**: Abstract: "exaggerating the negative impact of domain gap".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Hou et al. (2023) | Published / posted in `WWW’23` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Multi-Dom` |  |
| **Tokenization** | `OPQ` | Optimized product quantization. |
| **Backbone** | `Encoder` |  |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Discrim.` | Scores items; does not generate SIDs. |
| **Inference Decoding** | `Scoring` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "exaggerating the negative impact of domain gap".
- **`tokenizer`** (§2.3.2, p4; §2.4, p4–5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§2.3.2, p4; §2.4, p4–5): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `VI. Generalization` × `Tokenization` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` | `Unified RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` | `Tree` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` | `CART` | `Dec-Only` | `Altern.` | `NTP + Aux.` | `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` | `RQ+LoRA` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` | `RQ` | `Dec-Only` | `Fixed†` | `NTP + Aux.` | `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` | `R-KM` | `Lazy Dec-Only` | `Fixed` | `NTP + RL` | `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` | `TokenMoE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
