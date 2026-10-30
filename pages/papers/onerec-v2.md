# OneRec-V2: OneRec-V2 Technical Report

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2508.20900`)](https://arxiv.org/abs/2508.20900) · [Source Record (`data/papers/onerec-v2.yaml`)](../../data/papers/onerec-v2.yaml)

> **Summary**: §4.1明确OneRec-V2 PTQ不改架构或训练；其§2.2.2点名沿用OneRec-V1 tokenizer。另核OneRec-V1 §2.1.1，caption/tag/ASR/OCR/cover/frames进入MiniCPM-V，再用协同物品对对齐。仅通过该两跳继承链报告，故标†。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhou et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+Img+CF†` |  |
| **Tokenization** | `R-KM†` |  |
| **Backbone** | `Lazy Dec-Only` | The paper's Lazy Decoder-Only architecture (OneRec-V2). |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "inefficient computational allocation where 97.66% of resources are consumed by sequence encoding rather than generation"; "limitations in reinforcement learning relying solely on reward models". Candidates: V / IV (rule: tie broken by the first new design).
- **`representation`** (§2.2.2, p8): Paper only says the tokenizer is as in OneRec-V1; inferred from the OneRec technical report, as for OneRec-Think.
- **`tokenization`** (§2.2.2, p8): Paper only says the tokenizer is as in OneRec-V1; inferred from the OneRec technical report, as for OneRec-Think.

## Peer Methods in `V. Efficiency` × `Backbone` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RPG](rpg.md) | KDD’25 | `Text+Img` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP` | `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP + Ctr. + Aux.` | `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP → (NTP + Aux.)` | `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP / NTP + Aux.` | `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `–` | `NTP → (NTP + DPO)` | `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` | `RQ-VAE†` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Dual-level Flow Ctr.` | `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
