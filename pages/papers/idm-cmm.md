# IDM/CMM: Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.32943`)](https://arxiv.org/abs/2610.32943) · [Source Record (`data/papers/idm-cmm.yaml`)](../../data/papers/idm-cmm.yaml)

> **Summary**: Generative recommendation with semantic IDs represents each item as a sequence of discrete codes derived from its semantic representation and predicts these codes to generate recommendations. Existing semantic-ID recommenders are typically trained with hard labels for the observed next item. Although such supervision identifies the target, it provides no explicit distributional information about alternative items conditioned on the same user history. Sequential recommenders can supply this item-level predictive knowledge, but transferring it to semantic-ID generation is challenging because the teacher and student operate in item and code spaces, respectively. We propose two complementary knowledge-distillation objectives for parallel semantic-ID recommenders, which predict all code positions simultaneously without autoregressive prefix conditioning. Item Distribution Matching (IDM) reconstructs a catalogue-level item distribution from the student's parallel code predictions and aligns it with the teacher's item distribution. Code Marginal Matching (CMM) projects the teacher's item probabilities onto each code position using fixed item-to-code assignments, then matches the resulting code marginals to the corresponding student heads. Both objectives transfer the teacher's soft distributional knowledge while preserving the student's parallel prediction structure. Experiments on benchmark datasets show that both methods consistently outperform existing state-of-the-art approaches. On average, IDM improves Recall@10 by 15.39%, while CMM improves NDCG@10 by 8.28%. These results demonstrate that distillation in either reconstructed item space or code-marginal space can substantially strengthen hard-label supervision for parallel generative recommendation.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Xu et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text` |  |
| **Tokenization** | `Subspace RQ` | 16个量化子空间，每空间3残差层，48个并行码头 |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `MTP + Aux.` | 并行码位预测，加无负例负余弦语义对齐。 |
| **Inference Decoding** | `Scoring` |  |
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
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` | `R-KM` | `Enc-Dec` | `Fixed†` | `(NTP† / (NTP + Aux.)†) → KL-weighted OPD` | `C-Beam` |
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
