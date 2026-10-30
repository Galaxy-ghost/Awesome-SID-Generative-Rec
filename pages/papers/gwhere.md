# Gwhere: Guess Where You Go: Generative Next Point-of-Interest Recommendation in Amap

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2607.26073`)](https://arxiv.org/abs/2607.26073) · [Source Record (`data/papers/gwhere.yaml`)](../../data/papers/gwhere.yaml)

> **Summary**: Abstract: "redundant or colliding token assignments"; "insufficient integration of heterogeneous item signals". II and I tie; most of the tokenizer design (contrastive instead of reconstruction loss; "alleviate code collision", p8) serves II. Both labelings were unsure (alternative I).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhai et al. (2026) | Published / posted in `RecSys’26` |
| **Problem Band** | `II. Uniqueness and Validity` | Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text+Img+Geo+CF` |  |
| **Tokenization** | `Contr. RQ` | Fully contrastive residual-quantization tokenizer (Gwhere). |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → DPO` | NTP, then preference optimization. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | [`https://github.com/alibaba/SimCIT`](https://github.com/alibaba/SimCIT) | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (abstract, p1): Abstract: "redundant or colliding token assignments"; "insufficient integration of heterogeneous item signals". II and I tie; most of the tokenizer design (contrastive instead of reconstruction loss; "alleviate code collision", p8) serves II. Both labelings were unsure (alternative I).
- **`stage`** (§3.2, p3): The designs for both complaints sit in the tokenizer.
- **`tokenizer`** (p1; Fig. 1, p6): "Based on these SIDs, Gwhere adapts LLMs"; SIDs are built offline before LLM training.

## Peer Methods in `II. Uniqueness and Validity` × `Tokenization` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` | `Spectral Clus.` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` | `Multi-Facet ID` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `FM-Index+Agg.` |
| [HiD-VAE](hid-vae.md) | arXiv’25 | `Text` | `Hier. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [PSI](psi.md) | arXiv’25 | `Text` | `Post-hoc RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` | `RQ` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [API](api.md) | arXiv’26 | `Text` | `PID (P-SAE)` | `Enc-Dec / Dec-Only (AR); Non-AR (PR)` | `Fixed` | `NTP + Rank + Aux. / MTP + Rank + Aux.` | `C-Beam / Scoring` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` | `NU-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` | `Learn. RQ` | `Enc-Dec` | `Joint` | `NTP` | `Beam†` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` | `QA-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` | `Ref.-RQ` | `–` | `Fixed` | `NTP` | `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE+PPR` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
