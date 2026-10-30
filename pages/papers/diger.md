# DIGER: Differentiable Semantic ID for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2601.19711`)](https://arxiv.org/abs/2601.19711) · [Source Record (`data/papers/diger.yaml`)](../../data/papers/diger.yaml)

> **Summary**: Abstract: "This leads to an objective mismatch"; "this often causes codebook collapse, where only a few codes are used". Candidates: III / II (rule: tie broken by the majority of new designs).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Fu et al. (2026) | Published / posted in `SIGIR’26` |
| **Problem Band** | `II. Uniqueness and Validity` | Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Learn. RQ` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Joint` | The generator loss updates the tokenizer directly. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Beam†` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "This leads to an objective mismatch"; "this often causes codebook collapse, where only a few codes are used". Candidates: III / II (rule: tie broken by the majority of new designs).
- **`tokenizer`** (§6.1, p6; Table 2, p7): Location from the pre-10-26 Training evidence in the appendix.
- **`inference`** (§3, p3; p6): Decoding not stated; implementation 'followed the settings in [29]' (ETEGRec); inferred from ETEGRec (Beam in Table 1).

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
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` | `Contr. RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` | `QA-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` | `Ref.-RQ` | `–` | `Fixed` | `NTP` | `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE+PPR` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
