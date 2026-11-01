# OneChord

*Distill What You Rank, Recommend in One Pass* — Li et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.25805) · [Record](../../data/papers/onechord.yaml) · [← Catalog](../../README.md#iv--training)

> Accurate product discovery on the Web requires recommendation models that rank catalog candidates within tight inference budgets. In semantic-ID recommendation, deployment can fuse code probabilities with item similarities, making the final ranking depend on their normalization and relative weights. This motivates a direct training principle: \emph{distill what you rank}. We present OneChord, which uses one learned, catalog-normalized fusion for next-item supervision, refinement distillation, and inference. A shared parallel decoder produces joint SID evidence and item-matching scores. During training, a frozen denoiser supplies legal partial SIDs; the student evaluates these states to construct refined fused targets. Matching direct and refined predictions on shared hard candidates transfers refinement into one-pass recommendation. We characterize the fusion weights induced by candidate conditioning and establish sufficient conditions for preserving the refined predictor's full-catalog Top-$K$ selection. Across six Amazon datasets, OneChord achieves the highest Recall@5 and NDCG@5 among the compared methods on every dataset, with average relative gains of 6.30\% and 7.12\% over the strongest baseline. It also achieves a 1.04--1.18$\times$ full-test generation speedup over the fastest baseline. OneChord makes the served ranking distribution the common object of recommendation learning and distillation.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `Par. OPQ` | `Non-AR` | **`Fixed / Next-item CE + Cons. KD + Rank KD`** | `Scoring` |

- `–`: Not reported in the paper, or not applicable.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Next-item CE + Cons. KD + Rank KD`: Next-item cross-entropy jointly optimized with consistency and ranking distillation.

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
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` → `RQ-VAE` → `Enc-MLP` → **`Fixed / NTP + Aux.`** → `C-Beam` |
| [NAU](nau.md) | arXiv’26 | `–` → `R-KM` → `Enc-Dec†` → **`Fixed / NTP + Aux.`** → `–` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` → `R-KM†` → `Dec-Only†` → **`Fixed† / NTP → RL`** → `–` |
| [SAHL](sahl.md) | arXiv’26 | `Text` → `SRBQ` → `Non-AR` → **`Fixed / (MTP + Masked Rec.) → MTP`** → `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` → `–` → `Dec-Only` → **`Fixed / NTP`** → `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → (RL + Rank)`** → `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
