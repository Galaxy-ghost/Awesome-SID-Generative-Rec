# SynGR: SynGR: Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2605.18920`)](https://arxiv.org/abs/2605.18920) · [Source Record (`data/papers/syngr.yaml`)](../../data/papers/syngr.yaml)

> **Summary**: Abstract: "underexplore synergistic information across modalities".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Chen et al. (2026) | Published / posted in `ICML’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text+Img` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Ctr.` | NTP plus a contrastive loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "underexplore synergistic information across modalities".
- **`tokenizer`** (p6): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p6): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `I. Informativeness` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [MBGen](mbgen.md) | CIKM’24 | `CF` | `Bal. VQ+KM` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [RAGR](ragr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Beam† / –` |
| [REGER](reger.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → (NTP + Aux.)` | `Beam` |
