# COBRA: Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2503.02453`)](https://arxiv.org/abs/2503.02453) · [Source Record (`data/papers/cobra.yaml`)](../../data/papers/cobra.yaml)

> **Summary**: Abstract: "significant information loss due to the separation of stages such as quantization and sequence modeling".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Yang et al. (2025) | Published / posted in `NeurIPS’25` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+SID` | Text representation plus semantic IDs (hybrid dense and generative retrieval). |
| **Tokenization** | `Casc. RQ` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Dense` | NTP plus dense-vector prediction. |
| **Inference Decoding** | `BeamFusion` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "significant information loss due to the separation of stages such as quantization and sequence modeling".
- **`tokenizer`** (p5): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p5): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `I. Informativeness` × `Backbone` (6 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` | `Dual H-KM` | `Dual Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Fusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` | `Geo-Idx` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` | `RQ-PIB` | `Dec-Only` | `Fixed` | `NTP → DPO` | `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `NTP + Rank` | `Beam` |
