# GeoGR: GeoGR: Enabling Spatio-Temporal Aware Industrial-Scale Generative POI Recommendations

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.10411`)](https://arxiv.org/abs/2602.10411) · [Source Record (`data/papers/geogr.yaml`)](../../data/papers/geogr.yaml)

> **Summary**: Abstract: "inadequate modeling of high-quality SIDs that capture cross-category spatio-temporal collaborative relationships"; "poor alignment between large language models (LLMs) and the POI recommendation task". I and III tie, and so do the new designs; the title ("Enabling Spatio-Temporal Aware ...") names I.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Wang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Representation` | The primary design change sits in the Representation stage. |
| **Representation** | `Text+Geo+CF` |  |
| **Tokenization** | `R-KM+EM` | RQ-Kmeans refined by an EM-style algorithm (GeoGR). |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Altern.†` |  |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (abstract, p1): Abstract: "inadequate modeling of high-quality SIDs that capture cross-category spatio-temporal collaborative relationships"; "poor alignment between large language models (LLMs) and the POI recommendation task". I and III tie, and so do the new designs; the title ("Enabling Spatio-Temporal Aware ...") names I.
- **`stage`** (Eq. (4), p4): The fix for I is contrastive representation learning on geo-constrained co-visit pairs (L_P2P); the EM-style SID refinement and CPT lean to III.
- **`tokenizer`** (§4.1.3, Algorithm 1, p5; §4.2.1, p5): The EM algorithm updates the LLM and the SIDs in turns for "mutual alignment between the LLM and the SIDs"; the final recommender is retrained from the base LLM on the fixed SIDs, hence inferred.

## Peer Methods in `I. Informativeness` × `Representation` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Molar](molar.md) | arXiv’24 | `Text+Img+CF` | `–` | `Dec-Only` | `–` | `Discrim.` | `Scoring` |
| [OneLoc](oneloc.md) | arXiv’25 | `Text+Img+Geo†` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Beam` |
| [Q-BERT4Rec](q-bert4rec.md) | arXiv’25 | `Text+Img+CF` | `RQ-VAE` | `Encoder (Non-AR)` | `Fixed` | `Masked` | `Non-AR` |
| [UNGER](unger.md) | TOIS’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [HF-SID](hf-sid.md) | arXiv’26 | `Text+Attr+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LGRID](lgrid.md) | arXiv’26 | `Text+Geo` | `DSRQ` | `Disc.` | `Fixed` | `Discrim.` | `Scoring` |
| [LGSID](lgsid.md) | AAAI’26 | `Text+Geo+CF` | `Geo-Idx+RQ` | `Disc. / Enc-Dec` | `Fixed` | `Discrim. / NTP` | `Scoring / Beam†` |
| [ReSID](resid.md) | arXiv’26 | `Attr+CF` | `GAOQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [SCRec](screc.md) | RecSys’26 | `Text+CF` | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed` | `MTP + Ctr.` | `Scoring / Beam†` |
| [SPAR](spar.md) | arXiv’26 | `Text+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
