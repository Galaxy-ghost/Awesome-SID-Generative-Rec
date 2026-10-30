# SID-MLP: MLPs are Efficient Distilled Generative Recommenders

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2605.12617`)](https://arxiv.org/abs/2605.12617) · [Source Record (`data/papers/sid-mlp.yaml`)](../../data/papers/sid-mlp.yaml)

> **Summary**: 提出可部署的新 SID 生成解码结构，含冻结教师蒸馏与编码器扩展 SID-MLP++。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Guo et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE†` |  |
| **Backbone** | `Enc-MLP` | 冻结T5 encoder，一次注意力上下文读出，逐码位前缀条件MLP |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Backbone` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP` | `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP + Ctr. + Aux.` | `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP → (NTP + Aux.)` | `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP / NTP + Aux.` | `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `–` | `NTP → (NTP + DPO)` | `Div. C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Dual-level Flow Ctr.` | `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
