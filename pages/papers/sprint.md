# SPRINT: SPRINT: Single-Step Generative Recommendation via Average Probability Velocity

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2609.34306`)](https://arxiv.org/abs/2609.34306) · [Source Record (`data/papers/sprint.yaml`)](../../data/papers/sprint.yaml)

> **Summary**: 用 OPQ SID 并行概率生成并对有效完整 SID 融合评分，是广义 SID 混合生成而非 token-only 大目录召回。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Cai et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Par. OPQ` |  |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Dual-level Flow Ctr.` | 平均概率速度参数化的两层item-negative contrastive目标：token概率乘积构成的SID分数与whole-SID表示相似度同时优化。Eq9替代逐码hard-label CE |
| **Inference Decoding** | `Scoring` |  |
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
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` | `RQ-VAE†` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
