# PLUM: PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2510.07784`)](https://arxiv.org/abs/2510.07784) · [Source Record (`data/papers/plum.yaml`)](../../data/papers/plum.yaml)

> **Summary**: Abstract: "a framework designed to adapt pre-trained LLMs for industry-scale recommendation tasks".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | He et al. (2026) | Published / posted in `WWW’26` |
| **Problem Band** | `Paradigms, Systems and Benchmarks` | Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| **Primary Stage** | `n/a` | Used for Paradigms, Systems and Benchmarks (psb) rows that are not assigned to a single stage. |
| **Representation** | `Text+Img+CF` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "a framework designed to adapt pre-trained LLMs for industry-scale recommendation tasks".
- **`stage`** (arXiv abstract): Appendix tentatively places the new design in Training.
- **`tokenizer`** (§2.2, p4; §2.3, p4–5): Location from the pre-10-26 Training evidence in the appendix.

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
| [ReRankID](rerankid.md) | arXiv’26 | `Text` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Greedy` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` | `–` | `–` | `–` | `–` | `–` |
| [TransX-GenRet](transx-genret.md) | arXiv’26 | `–` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP → (NTP + DPO)` | `C-Beam` |
