# APAO

*Bridging the Training-Inference Gap in Generative Recommendation via Adaptive Prefix-Aware Optimization* — Yu et al., KDD’26

[arXiv](https://arxiv.org/abs/2603.02730) · [Record](../../data/papers/apao.yaml) · [← Catalog](../../README.md#iv--training)

> 提出固定 SID 上的前缀感知优化方法，两种骨干验证。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM` | `Enc-Dec / Dec-Only` | **`Fixed / NTP + Rank`** | `Beam` |

- `R-KM`: Residual k-means.
- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

## Same cell: IV × Training (21 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
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
| [OneChord](onechord.md) | arXiv’26 | `–` → `Par. OPQ` → `Non-AR` → **`Fixed / Next-item CE + Cons. KD + Rank KD`** → `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` → `R-KM†` → `Dec-Only†` → **`Fixed† / NTP → RL`** → `–` |
| [SAHL](sahl.md) | arXiv’26 | `Text` → `SRBQ` → `Non-AR` → **`Fixed / (MTP + Masked Rec.) → MTP`** → `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` → `–` → `Dec-Only` → **`Fixed / NTP`** → `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → (RL + Rank)`** → `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
