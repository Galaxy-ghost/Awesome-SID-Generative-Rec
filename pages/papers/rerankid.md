# ReRankID: Reasoning Reranking with Semantic IDs as the Sole Item Representation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.22797`)](https://arxiv.org/abs/2610.22797) · [Source Record (`data/papers/rerankid.yaml`)](../../data/papers/rerankid.yaml)

> **Summary**: End-to-end paradigm or benchmark using R-KM† tokenization and Dec-Only backbone.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Tang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `Paradigms, Systems and Benchmarks` | Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| **Primary Stage** | `n/a` | Used for Paradigms, Systems and Benchmarks (psb) rows that are not assigned to a single stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `R-KM†` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `CoT+Greedy` | 贪心生成自然语言推理与候选索引排序，失败时追加结构化抽取。 |
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
| [NEO](neo.md) | arXiv’26 | `Text / Audio` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
| [Netflix-SID-Comparison](netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | `–` | `RQ-VAE` | `Dec-Only / Non-AR` | `Fixed` | `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` | `C-Beam / Scoring` |
| [OneMall](onemall.md) | CIKM’26 | `Text+Img+CF` | `R-KM+FSQ` | `Enc-Dec` | `–` | `(NTP + Ctr.) → (NTP + Ctr. + RL)` | `Beam` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` | `–` | `–` | `–` | `–` | `–` |
| [TransX-GenRet](transx-genret.md) | arXiv’26 | `–` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP → (NTP + DPO)` | `C-Beam` |
