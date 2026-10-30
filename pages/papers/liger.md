# LIGER: Unifying generative and dense retrieval for sequential recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2411.18814`)](https://arxiv.org/abs/2411.18814) · [Source Record (`data/papers/liger.yaml`)](../../data/papers/liger.yaml)

> **Summary**: Abstract: "mitigating performance differences and enhancing cold-start item recommendation". Candidates: VI / none (rule: complaint fits none of the six classes; judged by the new design).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Yang et al. (2024) | Published / posted in `arXiv’24` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text+SID` | Text representation plus semantic IDs (hybrid dense and generative retrieval). |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Dense` | NTP plus dense-vector prediction. |
| **Inference Decoding** | `Hybrid` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "mitigating performance differences and enhancing cold-start item recommendation". Candidates: VI / none (rule: complaint fits none of the six classes; judged by the new design).

## Peer Methods in `VI. Generalization` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [SpecGR](specgr.md) | AAAI’26 | `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Rank` | `Hybrid` |
