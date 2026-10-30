# DualGR: DualGR: Generative Retrieval with Long and Short-Term Interests Modeling

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2511.12518`)](https://arxiv.org/abs/2511.12518) · [Source Record (`data/papers/dualgr.yaml`)](../../data/papers/dualgr.yaml)

> **Summary**: Abstract: "long-short interest interference, context-induced noise in hierarchical SID generation, and the lack of explicit learning from exposed-but-unclicked feedback". Candidates: I / III / VI (rule: tie broken by the title).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Yi et al. (2026) | Published / posted in `WWW’26 Short` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Rank` | NTP plus a ranking loss. |
| **Inference Decoding** | `Dual Beam` | Two-branch beam search, then merge (DualGR). |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "long-short interest interference, context-induced noise in hierarchical SID generation, and the lack of explicit learning from exposed-but-unclicked feedback". Candidates: I / III / VI (rule: tie broken by the title).
- **`tokenizer`** (§2.5, p3): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§2.5, p3): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `VI. Generalization` × `Backbone` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [FedCGR](fedcgr.md) | CIKM’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [LION](lion.md) | CIKM’26 | `Text†` | `RQ-VAE†` | `Enc-Dec` | `Fixed†` | `NTP + Aux.` | `Beam` |
