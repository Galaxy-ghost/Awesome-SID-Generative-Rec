# API: The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.36763`)](https://arxiv.org/abs/2610.36763) · [Source Record (`data/papers/api.yaml`)](../../data/papers/api.yaml)

> **Summary**: Generative recommendation (GR) predicts the next item through its semantic ID (SID). Existing methods commonly fit SID vocabularies to pretrained language model (PLM) representations of item descriptions, incurring additional training costs and making vocabulary coverage dependent on the fitting domains. We observe that pretrained sparse autoencoders expose PLM features with human-interpretable semantic annotations, allowing feature indices to serve as a reusable SID vocabulary. However, reusing this vocabulary requires preserving item distinctions under compact token budgets and learning to favor target items over candidates with shared dominant features. It also requires extending feature interpretability from item content to retrieval decisions. To address these challenges, we propose API, a framework that Adapts the Pretrained Interpretable vocabulary for effective and explainable GR without additional vocabulary learning. Within API, Pretrained Interpretable IDs (PIDs) retain selected feature indices and relative activation strengths for item discrimination. With PIDs as supervision, the Semantic Prediction Adapter (SPA) learns user preferences from interaction histories through joint feature-index and strength prediction. SPA combines both predictions to score candidate items, with item-level supervision encouraging the observed next item to outrank its alternatives. API further explains candidate score differences through feature contributions paired with their pretrained semantic annotations. Extensive experiments show that API achieves competitive performance across backbones and decoding schemes, while preserving item distinctions under compact token budgets and enabling explainable retrieval.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Luo et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `II. Uniqueness and Validity` | Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `PID (P-SAE)` | Pretrained Interpretable ID：预训练SAE feature indices、相对activation strengths及对应语义注释 |
| **Backbone** | `Enc-Dec / Dec-Only (AR); Non-AR (PR)` | AR结构为T5/GPT-2 |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Rank + Aux. / MTP + Rank + Aux.` | AR/PR分别序列NLL/并行码预测，加candidate preference loss与Hellinger strength项，三项同阶段联合。 |
| **Inference Decoding** | `C-Beam / Scoring` | AR为catalog-constrained beam50 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `II. Uniqueness and Validity` × `Tokenization` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` | `Spectral Clus.` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` | `Multi-Facet ID` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `FM-Index+Agg.` |
| [HiD-VAE](hid-vae.md) | arXiv’25 | `Text` | `Hier. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [PSI](psi.md) | arXiv’25 | `Text` | `Post-hoc RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` | `RQ` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` | `NU-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` | `Learn. RQ` | `Enc-Dec` | `Joint` | `NTP` | `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` | `Contr. RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` | `QA-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` | `Ref.-RQ` | `–` | `Fixed` | `NTP` | `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE+PPR` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
