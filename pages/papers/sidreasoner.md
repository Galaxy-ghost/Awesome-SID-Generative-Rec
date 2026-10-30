# SIDReasoner: Reasoning over Semantic IDs Enhances Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2603.23183`)](https://arxiv.org/abs/2603.23183) · [Source Record (`data/papers/sidreasoner.yaml`)](../../data/papers/sidreasoner.yaml)

> **Summary**: 本篇§3.1明确复用SIDReasoner的SID管线；另核2603.23183v2 §3.2.1 PDF p4明确item textual metadata构码，本文未重述的输入标Text†。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | He et al. (2026) | Published / posted in `KDD’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "Itemic tokens are not natively meaningful to LLMs".
- **`objective`** (§3.2.2, §3.3.1, §3.3.2, p4–5): Location from the pre-10-26 Training evidence in the appendix.
- **`inference`** (code: HappyPointer/SIDReasoner evaluate_Qwen3_think.py (commit 2575927, read statically)): Not stated in the text.

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
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Beam` |
