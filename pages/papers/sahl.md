# SAHL: Structure-Aligned History Learning with Subspace-Structured Semantic IDs for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.25093`)](https://arxiv.org/abs/2610.25093) · [Source Record (`data/papers/sahl.yaml`)](../../data/papers/sahl.yaml)

> **Summary**: Generative recommendation constructs semantic IDs for catalog items and predicts the next ID from user interaction histories. However, existing methods face limitations in both stages. First, conventional quantizers may produce imbalanced code assignments and lack coherent intermediate semantic units between individual tokens and complete items, limiting history reconstruction. Second, recommendation models remain dominated by next-item prediction, treating historical interactions mainly as conditioning context and providing limited supervision for recovering persistent preferences across the historical path, particularly when relevant preference signals are distributed over distant interactions. To address these limitations, Structure-Aligned History Learning (SAHL) reconnects the two stages by using the structure created during quantization directly for history reconstruction. Its Semantic Residual Balanced Quantization (SRBQ) forms a balanced token-subspace-item hierarchy, and SAHL reconstructs history at these same granularities. Predictive entropy prioritizes uncertain transitions, while curriculum optimization progressively shifts training to inference-aligned next-item prediction. On four Amazon Review categories, SAHL improves NDCG@10 by 18.6%-30.0% over RPG and 2.7%-6.0% over strong method MHL. Controlled analyses verify balanced code use, the benefit of following quantizer-defined groups during reconstruction, and dependence on user history. The relevant code is available at https://github.com/CQU-MM-Intelligent-Lab/SAHL.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Wei et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text` |  |
| **Tokenization** | `SRBQ` | Semantic Residual Balanced Quantization |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `(MTP + Masked Rec.) → MTP` | 并行下一物品码预测CE与多粒度历史掩码重建CE联合训练，课程最后关闭重建、保留纯下一物品预测。 |
| **Inference Decoding** | `Graph` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `IV. Utility` × `Training` (21 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [APAO](apao.md) | KDD’26 | `Text` | `R-KM` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Rank` | `Beam` |
| [DASO](daso.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
| [DPE-Rec](dpe-rec.md) | arXiv’26 | `– / Text+Img` | `RQ` | `Non-AR` | `Fixed` | `Masked → RL (→ Masked KD for Fast)` | `Diff.+Legalize` |
| [GEM-Rec](gem-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Bid-Aware Beam` |
| [GenRec-JD](genrec-jd.md) | SIGIR’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [GFlowGR](gflowgr.md) | SIGIR’26 | `Text / Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `Beam† / C-Beam†` |
| [Ghost](ghost.md) | NeurIPS’26 | `Text` | `Skeleton R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `–` |
| [HASTE](haste.md) | arXiv’26 | `Text / MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `–` |
| [HCGRec](hcgrec.md) | CIKM’26 | `–` | `RQ` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [IDM/CMM](idm-cmm.md) | arXiv’26 | `Text` | `Subspace RQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` | `R-KM` | `Enc-Dec` | `Fixed†` | `(NTP† / (NTP + Aux.)†) → KL-weighted OPD` | `C-Beam` |
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` | `RQ-VAE` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [NAU](nau.md) | arXiv’26 | `–` | `R-KM` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `–` |
| [OneChord](onechord.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Next-item CE + Cons. KD + Rank KD` | `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` | `R-KM†` | `Dec-Only†` | `Fixed†` | `NTP → RL` | `Beam†` |
| [SAPO](sapo.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` | `–` | `Dec-Only` | `Fixed` | `NTP` | `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → (RL + Rank)` | `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
