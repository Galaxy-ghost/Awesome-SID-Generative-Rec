# Think2Go: Think2Go: Generative Next POI Recommendation with LLM Reasoning

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2607.28997`)](https://arxiv.org/abs/2607.28997) · [Source Record (`data/papers/think2go.yaml`)](../../data/papers/think2go.yaml)

> **Summary**: Abstract: non-reasoning models "limit the computational capacity ... to capture deep intent"; LLMs "lack a deep understanding of semantic IDs (SIDs) when SIDs are trained separately". The second is III; the first is III too, since missing reasoning does not form a problem of its own.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhuang et al. (2026) | Published / posted in `KDD’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Attr+Geo+CF†` | Attr 为类别等结构化属性，Geo 为区域/邻接，CF 为用户访问。 |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `CoT+Beam` | Think, self-correct, answer, then beam search (Think2Go). |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (abstract, p1): Abstract: non-reasoning models "limit the computational capacity ... to capture deep intent"; LLMs "lack a deep understanding of semantic IDs (SIDs) when SIDs are trained separately". The second is III; the first is III too, since missing reasoning does not form a problem of its own.
- **`stage`** (§4.1–4.2, p4–6): SFT and RL-based reasoning are optimized jointly in one architecture, with two advantage weightings.
- **`representation`** (p7): Inferred from GNPR-SID, whose data processing the paper follows.

## Peer Methods in `III. SID–Model Alignment` × `Training` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [ETEGRec](etegrec.md) | SIGIR’25 | `CF` | `Learn. RQ` | `Enc-Dec` | `Altern.` | `NTP + Ctr.` | `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` | `RQ-KM` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [OneRec-Think](onerec-think.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT` |
| [Evo-Rec](evo-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [GTI](gti.md) | arXiv’26 | `Text+CF / Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [Intent-Driven-News](intent-driven-news.md) | ACL’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+Fuzzy Match` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
