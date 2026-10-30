# HiD-VAE: HiD-VAE: Interpretable Generative Recommendation via Hierarchical and Disentangled Semantic IDs

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2508.04618`)](https://arxiv.org/abs/2508.04618) · [Source Record (`data/papers/hid-vae.yaml`)](../../data/papers/hid-vae.yaml)

> **Summary**: Abstract: "semantically flat and uninterpretable, lacking a coherent hierarchy"; "prone to representation entanglement (i.e., ``ID collisions'')". Candidates: I / II (rule: tie broken by the majority of new designs).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Fang et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `II. Uniqueness and Validity` | Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Hier. RQ` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "semantically flat and uninterpretable, lacking a coherent hierarchy"; "prone to representation entanglement (i.e., ``ID collisions'')". Candidates: I / II (rule: tie broken by the majority of new designs).
- **`tokenizer`** (§3.8, p5): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `II. Uniqueness and Validity` × `Tokenization` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` | `Spectral Clus.` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` | `Multi-Facet ID` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP` | `FM-Index+Agg.` |
| [PSI](psi.md) | arXiv’25 | `Text` | `Post-hoc RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` | `RQ` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [API](api.md) | arXiv’26 | `Text` | `PID (P-SAE)` | `Enc-Dec / Dec-Only (AR); Non-AR (PR)` | `Fixed` | `NTP + Rank + Aux. / MTP + Rank + Aux.` | `C-Beam / Scoring` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` | `NU-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` | `Learn. RQ` | `Enc-Dec` | `Joint` | `NTP` | `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` | `Contr. RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` | `QA-RQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` | `Ref.-RQ` | `–` | `Fixed` | `NTP` | `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE+PPR` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
