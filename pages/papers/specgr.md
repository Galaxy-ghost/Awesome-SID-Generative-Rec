# SpecGR: Inductive Generative Recommendation via Retrieval-based Speculation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2410.02939`)](https://arxiv.org/abs/2410.02939) · [Source Record (`data/papers/specgr.yaml`)](../../data/papers/specgr.yaml)

> **Summary**: Abstract: "struggle to recommend unseen items".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Ding et al. (2026) | Published / posted in `AAAI’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text+SID` | Text representation plus semantic IDs (hybrid dense and generative retrieval). |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Rank` | NTP plus a ranking loss. |
| **Inference Decoding** | `Hybrid` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "struggle to recommend unseen items".
- **`tokenizer`** (p5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (p5): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `VI. Generalization` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LIGER](liger.md) | arXiv’24 | `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Dense` | `Hybrid` |
