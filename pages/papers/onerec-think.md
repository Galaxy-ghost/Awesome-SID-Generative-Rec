# OneRec-Think: Onerec-think: In-text reasoning for generative recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2510.11639`)](https://arxiv.org/abs/2510.11639) · [Source Record (`data/papers/onerec-think.yaml`)](../../data/papers/onerec-think.yaml)

> **Summary**: Abstract: "critically lacking the capacity for explicit and controllable reasoning". Candidates: none / III (rule: lack of reasoning is not a class of its own).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text+Img+CF†` |  |
| **Tokenization** | `R-KM†` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `CoT` | Chain-of-thought before the SID. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "critically lacking the capacity for explicit and controllable reasoning". Candidates: none / III (rule: lack of reasoning is not a class of its own).
- **`representation`** (§3, p2; OneRec technical report §2.1.1): Paper says itemic tokens come from 'multi-modal and collaborative content' but does not name the visual inputs.
- **`tokenization`** (§3, p2; OneRec technical report (arXiv 2506.13695v4) §2.1.2, Table 11; §5.4.1, p6): Paper only says 'Following OneRec'; R-KM inferred from the OneRec technical report (RQ-Kmeans).

## Peer Methods in `III. SID–Model Alignment` × `Training` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [ETEGRec](etegrec.md) | SIGIR’25 | `CF` | `Learn. RQ` | `Enc-Dec` | `Altern.` | `NTP + Ctr.` | `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` | `RQ-KM` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [Evo-Rec](evo-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [GTI](gti.md) | arXiv’26 | `Text+CF / Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [Intent-Driven-News](intent-driven-news.md) | ACL’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+Fuzzy Match` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Beam` |
