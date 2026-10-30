# CID: How to Index Item IDs for Recommendation Foundation Models

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2305.06569`)](https://arxiv.org/abs/2305.06569) · [Source Record (`data/papers/cid.yaml`)](../../data/papers/cid.yaml)

> **Summary**: Abstract: "To avoid generating excessively long text and hallucinated recommendations"; "creating LLM-compatible item IDs to uniquely identify each item is essential". Candidates: II / I (rule: judged by the abstract's complaint first).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Hua et al. (2023) | Published / posted in `SIGIR-AP’23` |
| **Problem Band** | `II. Uniqueness and Validity` | Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `CF` | Collaborative filtering signal. |
| **Tokenization** | `Spectral Clus.` | Recursive spectral clustering on the co-occurrence graph (CID). |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "To avoid generating excessively long text and hallucinated recommendations"; "creating LLM-compatible item IDs to uniquely identify each item is essential". Candidates: II / I (rule: judged by the abstract's complaint first).
- **`tokenizer`** (p2; §5.2): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (p2; §5.2): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `II. Uniqueness and Validity` × `Tokenization` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TransRec](transrec.md) | KDD’24 | `Text` | `Multi-Facet ID` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `FM-Index+Agg.` |
| [HiD-VAE](hid-vae.md) | arXiv’25 | `Text` | `Hier. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [PSI](psi.md) | arXiv’25 | `Text` | `Post-hoc RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` | `RQ` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [API](api.md) | arXiv’26 | `Text` | `PID (P-SAE)` | `Enc-Dec / Dec-Only (AR); Non-AR (PR)` | `Fixed` | `NTP + Rank + Aux. / MTP + Rank + Aux.` | `C-Beam / Scoring` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` | `NU-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` | `Learn. RQ` | `Enc-Dec` | `Joint` | `NTP` | `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` | `Contr. RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` | `QA-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` | `Ref.-RQ` | `–` | `Fixed` | `NTP` | `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE+PPR` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
