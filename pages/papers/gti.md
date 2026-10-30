# GTI: Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2604.02324`)](https://arxiv.org/abs/2604.02324) · [Source Record (`data/papers/gti.yaml`)](../../data/papers/gti.yaml)

> **Summary**: 提出明确可复用的词嵌入 grounding 训练阶段，并在真实离散 RQ-VAE SID 推荐中验证。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Chen et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text+CF / Text` | Representation：工业招聘候选用 Mistral-E5 加 recruiter engagement 两塔微调 |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `III. SID–Model Alignment` × `Training` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LC-Rec](lc-rec.md) | ICDE’24 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [ETEGRec](etegrec.md) | SIGIR’25 | `CF` | `Learn. RQ` | `Enc-Dec` | `Altern.` | `NTP + Ctr.` | `Beam` |
| [GREAM](gream.md) | arXiv’25 | `Text+CF` | `RQ-KM` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [OneRec-Think](onerec-think.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT` |
| [Evo-Rec](evo-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [Intent-Driven-News](intent-driven-news.md) | ACL’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+Fuzzy Match` |
| [SIDReasoner](sidreasoner.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
| [Think2Go](think2go.md) | KDD’26 | `Attr+Geo+CF†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Beam` |
