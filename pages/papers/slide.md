# SLIDE

*Search-to-List Item Distillation for Single-Rollout Generative Retrieval* — Zhan et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.34764) · [Record](../../data/papers/slide.yaml) · [← Catalog](../../README.md#iv--training)

> Generative retrieval (GR) typically relies on item-level beam search to retrieve candidates, leaving cross-item dependencies unmodeled and limiting direct optimization of list-level objectives. A natural alternative is to generate the entire list within a single autoregressive trajectory. However, greedy decoding with directly trained list-wise models substantially underperforms beam search. We identify two contributing factors: the broader search space explored by beam search and the positional bias of scarce positive signals, which deprives later positions of adequate supervision. To address these challenges, we propose $\textbf{SLIDE}$, a search-to-list item distillation framework that decouples offline search from online list generation. A teacher model retrieves high-quality candidates through offline item-level beam search, providing additional conversion-relevant supervision beyond sparse behavioral labels. Their Semantic IDs (SIDs) are then concatenated in beam-score order to form list-wise distillation targets. This search-to-list conversion transforms candidates retrieved along separate search paths into sequential item-generation targets within a single trajectory. Trained on these targets, the student generates the Top-$K$ list in a single greedy pass, also decoupling teacher scaling from online deployment. Experiments on FORGE and Taobao Search show that SLIDE substantially improves retrieval quality under single greedy decoding and, with stronger offline teachers, surpasses the beam-search reference. Supplementary RL experiments support the effectiveness of list-level generation.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `–` | `Dec-Only` | **`Fixed / NTP`** | `Greedy` |

- `–`: Not reported in the paper, or not applicable.
- `–`: No item SID is built, or not reported.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Greedy`: Select the highest-scoring next token at each decoding step.

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
| [OneChord](onechord.md) | arXiv’26 | `–` → `Par. OPQ` → `Non-AR` → **`Fixed / Next-item CE + Cons. KD + Rank KD`** → `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` → `R-KM†` → `Dec-Only†` → **`Fixed† / NTP → RL`** → `–` |
| [SAHL](sahl.md) | arXiv’26 | `Text` → `SRBQ` → `Non-AR` → **`Fixed / (MTP + Masked Rec.) → MTP`** → `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → (RL + Rank)`** → `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam` |
