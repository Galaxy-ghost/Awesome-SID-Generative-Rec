# RecoChain: Harmonizing Generative Retrieval and Ranking in Chain-of-Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2604.25787`)](https://arxiv.org/abs/2604.25787) · [Source Record (`data/papers/recochain.yaml`)](../../data/papers/recochain.yaml)

> **Summary**: Abstract: "leading to a gap between generation and ranking performance". Candidates: IV / III (rule: IV threshold: a flawed training objective counts).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu and Cao (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+Img` |  |
| **Tokenization** | `RQ` | Residual quantization. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Rank` | NTP plus a ranking loss. |
| **Inference Decoding** | `Hybrid` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "leading to a gap between generation and ranking performance". Candidates: IV / III (rule: IV threshold: a flawed training objective counts).
- **`tokenizer`** (p3): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p3): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `IV. Utility` × `Backbone` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [DiGR](digr.md) | arXiv’26 | `–` | `RQ-VAE` | `Dec-Only` | `–` | `Discrim.` | `Scoring` |
| [Gryphon](gryphon.md) | CIKM’26 Short | `–` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP + Rank` | `Hybrid` |
