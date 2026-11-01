# Ghost

*Echoes in Filter Bubble: Diagnosing and Curing Popularity Bias in Generative Recommenders* — Yin et al., NeurIPS’26

[arXiv](https://arxiv.org/abs/2605.16825) · [Record](../../data/papers/ghost.yaml) · [← Catalog](../../README.md#iv--training)

> 既有诊断也提出 Ghost 新方法，不能按纯分析排除。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Skeleton R-KM` | `Dec-Only` | **`Fixed / NTP + Aux.`** | `–` |

- `Skeleton R-KM`: Residual k-means organized around a shared semantic skeleton.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `–`: Not reported in the paper.

## Same cell: IV × Training (21 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [APAO](apao.md) | KDD’26 | `Text` → `R-KM` → `Enc-Dec / Dec-Only` → **`Fixed / NTP + Rank`** → `Beam` |
| [DASO](daso.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
| [DPE-Rec](dpe-rec.md) | arXiv’26 | `– / Text+Img` → `RQ` → `Non-AR` → **`Fixed / Masked → RL (→ Masked KD for Fast)`** → `Diff.+Legalize` |
| [GEM-Rec](gem-rec.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `Bid-Aware Beam` |
| [GenRec-JD](genrec-jd.md) | SIGIR’26 | `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [GFlowGR](gflowgr.md) | SIGIR’26 | `Text / Text+CF` → `RQ-VAE / Learn. RQ` → `Enc-Dec†` → **`Fixed / NTP + Aux.`** → `Beam† / C-Beam†` |
| [HASTE](haste.md) | arXiv’26 | `Text / MM` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–` |
| [HCGRec](hcgrec.md) | CIKM’26 | `–` → `RQ` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [IDM/CMM](idm-cmm.md) | arXiv’26 | `Text` → `Subspace RQ` → `Non-AR` → **`Fixed / MTP + Aux.`** → `Scoring` |
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` → `R-KM` → `Enc-Dec` → **`Fixed† / (NTP† / (NTP + Aux.)†) → KL-weighted OPD`** → `C-Beam` |
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` → `RQ-VAE` → `Enc-MLP` → **`Fixed / NTP + Aux.`** → `C-Beam` |
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
