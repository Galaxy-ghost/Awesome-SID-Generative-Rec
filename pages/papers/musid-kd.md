# MuSID-KD

*Multigranularity Knowledge Distillation for Generative Recommendation with Semantic IDs* — Zhang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.35218) · [Record](../../data/papers/musid-kd.yaml) · [← Catalog](../../README.md#iv--training)

> Generative recommendation with semantic IDs (SIDs) represents each item as a sequence of discrete tokens and autoregressively predicts the next item's SID. Despite strong recommendation performance, repeated decoding over multiple SID positions incurs substantial inference cost. Knowledge distillation transfers knowledge from a powerful generative teacher to a lightweight student, yet conventional objectives do not fully account for multi-token SID generation. We identify two limitations: item-level distribution alignment may not adequately preserve the teacher's ranking of candidate groups sharing SID prefixes, while uniform alignment across SID positions may affect final item ranking differently. We propose MuSID-KD, which combines Hierarchical Candidate Distribution Alignment (HCDA) and Ranking Impact Guided Levelwise Distillation (RIGD). HCDA aggregates item probabilities according to shared SID prefixes and aligns candidate distributions at successive levels, from candidate groups to individual items. RIGD evaluates the reduction in pairwise ranking surrogate loss when one student score contribution is replaced with the teacher's contribution, and allocates supervision accordingly. Experiments on real-world recommendation datasets using three lightweight student architectures demonstrate improved recommendation accuracy and better alignment of prefix marginal distributions and pairwise item rankings, without modifying the student's online inference architecture. Code is available at https://anonymous.4open.science/r/m7k2-review-83f9/.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Enc-MLP` | **`Fixed / NTP + Aux.`** | `C-Beam` |

- `–`: Not reported in the paper, or not applicable.
- `Enc-MLP`: A history encoder followed by MLP-based prediction heads.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

## Same cell: IV × Training (21 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [APAO](apao.md) | KDD’26 | `Text` → `R-KM` → `Enc-Dec / Dec-Only` → **`Fixed / NTP + Rank`** → `Beam` |
| [DASO](daso.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
| [DPE-Rec](dpe-rec.md) | arXiv’26 | `– / Text+Img` → `RQ` → `Non-AR` → **`Fixed / Masked → RL (→ Masked KD for Fast)`** → `Diff.+Legalize` |
| [GEM-Rec](gem-rec.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `Bid-Aware Beam` |
| [GenRec-JD](genrec-jd.md) | SIGIR’26 | `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [GFlowGR](gflowgr.md) | SIGIR’26 | `Text / Text+CF` → `RQ-VAE / Learn. RQ` → `Enc-Dec†` → **`Fixed / NTP + Aux.`** → `Beam† / C-Beam†` |
| [Ghost](ghost.md) | NeurIPS’26 | `Text` → `Skeleton R-KM` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–` |
| [HASTE](haste.md) | arXiv’26 | `Text / MM` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–` |
| [HCGRec](hcgrec.md) | CIKM’26 | `–` → `RQ` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [IDM/CMM](idm-cmm.md) | arXiv’26 | `Text` → `Subspace RQ` → `Non-AR` → **`Fixed / MTP + Aux.`** → `Scoring` |
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` → `R-KM` → `Enc-Dec` → **`Fixed† / (NTP† / (NTP + Aux.)†) → KL-weighted OPD`** → `C-Beam` |
| [NAU](nau.md) | arXiv’26 | `–` → `R-KM` → `Enc-Dec†` → **`Fixed / NTP + Aux.`** → `–` |
| [OneChord](onechord.md) | arXiv’26 | `–` → `Par. OPQ` → `Non-AR` → **`Fixed / Next-item CE + Cons. KD + Rank KD`** → `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` → `R-KM†` → `Dec-Only†` → **`Fixed† / NTP → RL`** → `–` |
| [SAHL](sahl.md) | arXiv’26 | `Text` → `SRBQ` → `Non-AR` → **`Fixed / (MTP + Masked Rec.) → MTP`** → `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` → `–` → `Dec-Only` → **`Fixed / NTP`** → `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → (RL + Rank)`** → `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
