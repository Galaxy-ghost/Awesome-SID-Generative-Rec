# NAU

*Neighborhood-Aware Unlearning for Generative Recommendation* — Lubitzsch et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.27232) · [Record](../../data/papers/nau.yaml) · [← Catalog](../../README.md#iv--training)

> Generative recommendation predicts items by autoregressively generating semantic identifiers (SIDs), whose tokens are shared across semantically related items. With this paradigm gaining adoption, the question of how to support unlearning in it has become pressing. If training interactions must later be removed, such as injected spam or interactions with items a user no longer wants, this sharing lets an unlearning update unintentionally affect the predictions for the interactions' neighbors. We show that this effect is locally structured and hidden by global metrics: unlearning can leave recommendation utility on the whole test set nearly unchanged while substantially degrading it on neighborhoods of the forgotten interactions' SIDs. We propose Neighborhood-Aware Unlearning (NAU), which augments interaction-level unlearning with explicit control over the probability mass assigned to the forgotten items' neighborhoods. Across three datasets and four SID tokenizers, NAU restores spam-induced exposure toward the retrained reference while retaining more than 95% of retrained utility, and recovers the neighborhood utility that forget-and-repair unlearning loses at no global cost. We identify local probability redistribution as an important failure mode of unlearning in SID-based generative recommenders and show that explicitly controlling this redistribution can mitigate its effects.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `R-KM` | `Enc-Dec†` | **`Fixed / NTP + Aux.`** | `–` |

- `–`: Not reported in the paper, or not applicable.
- `R-KM`: Residual k-means.
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
| [Ghost](ghost.md) | NeurIPS’26 | `Text` → `Skeleton R-KM` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–` |
| [HASTE](haste.md) | arXiv’26 | `Text / MM` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–` |
| [HCGRec](hcgrec.md) | CIKM’26 | `–` → `RQ` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam` |
| [IDM/CMM](idm-cmm.md) | arXiv’26 | `Text` → `Subspace RQ` → `Non-AR` → **`Fixed / MTP + Aux.`** → `Scoring` |
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` → `R-KM` → `Enc-Dec` → **`Fixed† / (NTP† / (NTP + Aux.)†) → KL-weighted OPD`** → `C-Beam` |
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` → `RQ-VAE` → `Enc-MLP` → **`Fixed / NTP + Aux.`** → `C-Beam` |
| [OneChord](onechord.md) | arXiv’26 | `–` → `Par. OPQ` → `Non-AR` → **`Fixed / Next-item CE + Cons. KD + Rank KD`** → `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` → `R-KM†` → `Dec-Only†` → **`Fixed† / NTP → RL`** → `–` |
| [SAHL](sahl.md) | arXiv’26 | `Text` → `SRBQ` → `Non-AR` → **`Fixed / (MTP + Masked Rec.) → MTP`** → `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` → `–` → `Dec-Only` → **`Fixed / NTP`** → `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → (RL + Rank)`** → `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
