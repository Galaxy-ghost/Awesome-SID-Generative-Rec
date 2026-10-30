# NEO: A Unified Language Model for Large Scale Search, Recommendation, and Reasoning

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2603.17533`)](https://arxiv.org/abs/2603.17533) · [Source Record (`data/papers/neo.yaml`)](../../data/papers/neo.yaml)

> **Summary**: End-to-end paradigm or benchmark using R-KM tokenization and Dec-Only backbone.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | De Nadai et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `Paradigms, Systems and Benchmarks` | Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| **Primary Stage** | `n/a` | Used for Paradigms, Systems and Benchmarks (psb) rows that are not assigned to a single stage. |
| **Representation** | `Text / Audio` | 不同实体类型分别使用文本或音频嵌入与独立码本，不代表拼接两模态。 |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `Paradigms, Systems and Benchmarks` × `n/a` (12 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TIGER](tiger.md) | NeurIPS’23 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FORGE](forge.md) | KDD’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Dyn. Beam` |
| [GRID](grid.md) | CIKM’25 | `Text` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [MiniOneRec](minionerec.md) | arXiv’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [OneRec](onerec.md) | arXiv’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Sess. Beam` |
| [GR-Generalize](gr-generalize.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `Hybrid` |
| [Netflix-SID-Comparison](netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | `–` | `RQ-VAE` | `Dec-Only / Non-AR` | `Fixed` | `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` | `C-Beam / Scoring` |
| [OneMall](onemall.md) | CIKM’26 | `Text+Img+CF` | `R-KM+FSQ` | `Enc-Dec` | `–` | `(NTP + Ctr.) → (NTP + Ctr. + RL)` | `Beam` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [ReRankID](rerankid.md) | arXiv’26 | `Text` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Greedy` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` | `–` | `–` | `–` | `–` | `–` |
| [TransX-GenRet](transx-genret.md) | arXiv’26 | `–` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP → (NTP + DPO)` | `C-Beam` |
