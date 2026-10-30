# KL-MOPD: KL-MOPD: Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.36973`)](https://arxiv.org/abs/2610.36973) · [Source Record (`data/papers/kl-mopd.yaml`)](../../data/papers/kl-mopd.yaml)

> **Summary**: Coordinating multiple recommendation objectives (e.g., click and conversion) is critical for real-world generative recommendation (GR). However, since a positive item in GR can be retrieved only when its tokens are successively selected at every decoding step, traditional item-wise methods lack fine-grained token-wise supervision to guide intermediate steps. Motivated by its success in foundation models, we consider introducing multi-objective on-policy distillation (MOPD) into GR to distill two single-objective teachers into a student at each token. Yet, we find that in vanilla MOPD, (i) teachers exhibit unequal distillation difficulty at each token (i.e., token-level imbalance), and (ii) the harder-to-distill teacher varies across tokens (i.e., cross-token inconsistency), leaving each objective poorly learned at certain steps and hindering positive item retrieval for both objectives, leading to suboptimal performance. To address this challenge, we propose KL-MOPD (KL-Weighted Multi-Objective On-Policy Distillation), a simple yet effective distillation method that allocates token-wise teacher weights proportional to the initial student-teacher token-wise KL divergences, thereby strengthening supervision for the harder-to-distill teacher at every decoding step. Despite its simplicity, we theoretically prove that KL-MOPD strictly outperforms vanilla MOPD in the additive joint recommendation objective under mild conditions. Moreover, KL-MOPD is plug-and-play and computationally efficient, requiring only a one-time pre-training weight calibration with negligible training overhead. Extensive experiments on three public benchmarks, a billion-scale industrial dataset, and online A/B tests on our e-commerce advertising platform demonstrate that KL-MOPD significantly improves both individual and joint recommendation performance. The anonymous code is provided for peer review.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Yang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `CF` | Collaborative filtering signal. |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed†` |  |
| **Training Objective** | `(NTP† / (NTP + Aux.)†) → KL-weighted OPD` | 初始化A/B=TIGER/REG4Rec：前者NTP、后者NTP+category辅助监督，按点名继承标† |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
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
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` | `RQ-VAE` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [NAU](nau.md) | arXiv’26 | `–` | `R-KM` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `–` |
| [OneChord](onechord.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Next-item CE + Cons. KD + Rank KD` | `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` | `R-KM†` | `Dec-Only†` | `Fixed†` | `NTP → RL` | `Beam†` |
| [SAHL](sahl.md) | arXiv’26 | `Text` | `SRBQ` | `Non-AR` | `Fixed` | `(MTP + Masked Rec.) → MTP` | `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` | `–` | `Dec-Only` | `Fixed` | `NTP` | `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → (RL + Rank)` | `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
