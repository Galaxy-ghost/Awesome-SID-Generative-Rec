# CITE: CITE: Contextual Item Transition Embeddings for Generative Recommendation with Parallel Semantic Identifiers

[Back to Catalog](../../README.md) · [Paper (`https://doi.org/10.3390/electronics15204749`)](https://doi.org/10.3390/electronics15204749) · [Source Record (`data/papers/cite.yaml`)](../../data/papers/cite.yaml)

> **Summary**: CITE (Electronics’26): Inference-stage method using Par. OPQ tokenization and Non-AR backbone.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Ma et al. (2026) | Published / posted in `Electronics’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Par. OPQ` |  |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Discrim.` | Scores items; does not generate SIDs. |
| **Inference Decoding** | `Scoring` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CAPE](cape.md) | arXiv’26 | `Text†` | `RQ-VAE†` | `Dec-Only / Enc-Dec` | `Fixed` | `Multi-task NTP† / NTP†` | `Hybrid` |
