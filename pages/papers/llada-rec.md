# LLaDA-Rec: LLaDA-Rec: Discrete Diffusion for Parallel Semantic ID Generation in Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2511.06254`)](https://arxiv.org/abs/2511.06254) · [Source Record (`data/papers/llada-rec.yaml`)](../../data/papers/llada-rec.yaml)

> **Summary**: Abstract: "error accumulation, where the fixed left-to-right generation order causes prediction errors in early tokens to propagate".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Shi et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Par. VQ` |  |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Masked` | Masks part of the codes and reconstructs them (includes masked diffusion). |
| **Inference Decoding** | `Diff.` | Diffusion decoding. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "error accumulation, where the fixed left-to-right generation order causes prediction errors in early tokens to propagate".

## Peer Methods in `III. SID–Model Alignment` × `Backbone` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` | `SimHash` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` | `RQ-VAE / R-KM / LETTER` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` | `CoBa RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `C-Beam` |
