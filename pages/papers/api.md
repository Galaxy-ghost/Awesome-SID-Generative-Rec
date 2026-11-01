# API

*The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation* — Luo et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.36763) · [Record](../../data/papers/api.yaml) · [← Catalog](../../README.md#ii--tokenization)

> Generative recommendation (GR) predicts the next item through its semantic ID (SID). Existing methods commonly fit SID vocabularies to pretrained language model (PLM) representations of item descriptions, incurring additional training costs and making vocabulary coverage dependent on the fitting domains. We observe that pretrained sparse autoencoders expose PLM features with human-interpretable semantic annotations, allowing feature indices to serve as a reusable SID vocabulary. However, reusing this vocabulary requires preserving item distinctions under compact token budgets and learning to favor target items over candidates with shared dominant features. It also requires extending feature interpretability from item content to retrieval decisions. To address these challenges, we propose API, a framework that Adapts the Pretrained Interpretable vocabulary for effective and explainable GR without additional vocabulary learning. Within API, Pretrained Interpretable IDs (PIDs) retain selected feature indices and relative activation strengths for item discrimination. With PIDs as supervision, the Semantic Prediction Adapter (SPA) learns user preferences from interaction histories through joint feature-index and strength prediction. SPA combines both predictions to score candidate items, with item-level supervision encouraging the observed next item to outrank its alternatives. API further explains candidate score differences through feature contributions paired with their pretrained semantic annotations. Extensive experiments show that API achieves competitive performance across backbones and decoding schemes, while preserving item distinctions under compact token budgets and enabling explainable retrieval.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **II. Uniqueness and Validity**: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`PID (P-SAE)`** | `Enc-Dec / Dec-Only (AR); Non-AR (PR)` | `Fixed / NTP + Rank + Aux. / MTP + Rank + Aux.` | `C-Beam / Scoring` |

- `PID (P-SAE)`: Pretrained Interpretable ID (Pretrained Sparse Autoencoder).
- `Enc-Dec / Dec-Only (AR); Non-AR (PR)`: Encoder–decoder or decoder-only autoregressive variants, and parallel non-autoregressive variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank + Aux. / MTP + Rank + Aux.`: Autoregressive or parallel token prediction jointly optimized with ranking and auxiliary objectives.
- `C-Beam / Scoring`: Constrained beam search or direct item scoring, depending on the configuration.

## Same cell: II × Tokenization (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` → **`Spectral Clus.`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` → **`Multi-Facet ID`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `FM-Index+Agg.` |
| [HiD-VAE](hid-vae.md) | arXiv’25 | `Text` → **`Hier. RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [PSI](psi.md) | arXiv’25 | `Text` → **`Post-hoc RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` → **`RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` → **`NU-RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` → **`Learn. RQ`** → `Enc-Dec` → `Joint / NTP` → `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` → **`Contr. RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` → **`QA-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` → **`Ref.-RQ`** → `–` → `Fixed / NTP` → `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+PPR`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
