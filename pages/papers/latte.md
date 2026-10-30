# Latte: Expressiveness Limits of Autoregressive Semantic ID Generation in Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2605.06331`)](https://arxiv.org/abs/2605.06331) · [Source Record (`data/papers/latte.yaml`)](../../data/papers/latte.yaml)

> **Summary**: Abstract: "making it difficult to distinguish among them based on user-specific preferences".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Hou et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "making it difficult to distinguish among them based on user-specific preferences".

## Peer Methods in `III. SID–Model Alignment` × `Backbone` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` | `Par. VQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` | `SimHash` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` | `RQ-VAE / R-KM / LETTER` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` | `CoBa RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `C-Beam` |
