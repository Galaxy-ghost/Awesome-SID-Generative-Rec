# ACERec: Unleash the Potential of Long Semantic IDs for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.13573`)](https://arxiv.org/abs/2602.13573) · [Source Record (`data/papers/acerec.yaml`)](../../data/papers/acerec.yaml)

> **Summary**: 有完整离散 SID、并行预测和全物品聚合检索，不因最终评分排除。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Xia et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Par. OPQ` |  |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `MTP + Ctr. + Aux.` | 同阶段并行码CE + in-batch ISA对比 + 潜在token重建 |
| **Inference Decoding** | `Scoring` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Backbone` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP` | `Graph` |
| [Deco](deco.md) | arXiv’26 | `Text / –` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP → (NTP + Aux.)` | `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP / NTP + Aux.` | `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `–` | `NTP → (NTP + DPO)` | `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` | `RQ-VAE†` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Dual-level Flow Ctr.` | `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
