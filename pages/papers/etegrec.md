# ETEGRec: Generative recommender with end-to-end learnable item tokenization

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2409.05546`)](https://arxiv.org/abs/2409.05546) · [Source Record (`data/papers/etegrec.yaml`)](../../data/papers/etegrec.yaml)

> **Summary**: Abstract: "treat item tokenization and generative recommendation training as separate processes".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu et al. (2025) | Published / posted in `SIGIR’25` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `CF` | Collaborative filtering signal. |
| **Tokenization** | `Learn. RQ` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Altern.` | Tokenizer and generator are updated in turns. |
| **Training Objective** | `NTP + Ctr.` | NTP plus a contrastive loss. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "treat item tokenization and generative recommendation training as separate processes".

## Peer Methods in `III. SID–Model Alignment` × `Training` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` | `RQ-KM` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [OneRec-Think](onerec-think.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT` |
| [Evo-Rec](evo-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [GTI](gti.md) | arXiv’26 | `Text+CF / Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [Intent-Driven-News](intent-driven-news.md) | ACL’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+Fuzzy Match` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Beam` |
