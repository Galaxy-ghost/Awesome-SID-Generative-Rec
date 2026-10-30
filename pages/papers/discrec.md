# DiscRec: DiscRec: Disentangled Semantic-Collaborative Modeling for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2506.15576`)](https://arxiv.org/abs/2506.15576) · [Source Record (`data/papers/discrec.yaml`)](../../data/papers/discrec.yaml)

> **Summary**: Abstract: "token-item misalignment"; "semantic-collaborative signal entanglement". Candidates: I / III (rule: tie broken by the title).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `RQ-VAE / Learn. RQ` | Evaluated on both standard RQ-VAE (TIGER) and learnable collaborative RQ (LETTER). |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "token-item misalignment"; "semantic-collaborative signal entanglement". Candidates: I / III (rule: tie broken by the title).
- **`tokenization`** (§I, p2; §IV-A, p7): Settings A/B take the TIGER and LETTER rows of Table 1.
- **`tokenizer`** (§II-A–B, p3): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `I. Informativeness` × `Backbone` (6 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` | `Dual H-KM` | `Dual Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` | `Casc. RQ` | `Dec-Only` | `Fixed` | `NTP + Dense` | `BeamFusion` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` | `Geo-Idx` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` | `RQ-PIB` | `Dec-Only` | `Fixed` | `NTP → DPO` | `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `NTP + Rank` | `Beam` |
