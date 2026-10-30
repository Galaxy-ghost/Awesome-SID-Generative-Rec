# EAGER: EAGER: Two-Stream Generative Recommender with Behavior-Semantic Collaboration

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2406.14017`)](https://arxiv.org/abs/2406.14017) · [Source Record (`data/papers/eager.yaml`)](../../data/papers/eager.yaml)

> **Summary**: Abstract: "focus solely on either behavioral or semantic aspects of item information".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Wang et al. (2024) | Published / posted in `KDD’24` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `Dual H-KM` |  |
| **Backbone** | `Dual Enc-Dec` |  |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Ctr.` | NTP plus a contrastive loss. |
| **Inference Decoding** | `Fusion` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | [`https://github.com/yewzz/EAGER`](https://github.com/yewzz/EAGER) | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "focus solely on either behavioral or semantic aspects of item information".
- **`tokenizer`** (p5): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p5): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `I. Informativeness` × `Backbone` (6 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` | `Casc. RQ` | `Dec-Only` | `Fixed` | `NTP + Dense` | `BeamFusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` | `Geo-Idx` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` | `RQ-PIB` | `Dec-Only` | `Fixed` | `NTP → DPO` | `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `NTP + Rank` | `Beam` |
