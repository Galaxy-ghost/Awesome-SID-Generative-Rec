# SEATER: Generative retrieval with semantic tree-structured identifiers and contrastive learning

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2309.13375`)](https://arxiv.org/abs/2309.13375) · [Source Record (`data/papers/seater.yaml`)](../../data/papers/seater.yaml)

> **Summary**: Abstract: "these methods fall short in efficiency and effectiveness for large-scale recommendations". Candidates: V / III (rule: judged by the abstract's complaint first).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Si et al. (2024) | Published / posted in `SIGIR-AP’24` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `CF` | Collaborative filtering signal. |
| **Tokenization** | `Tree-Clus.` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Ctr.` | NTP plus a contrastive loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "these methods fall short in efficiency and effectiveness for large-scale recommendations". Candidates: V / III (rule: judged by the abstract's complaint first).

## Peer Methods in `V. Efficiency` × `Tokenization` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Dynamic-Single-Codebook](dynamic-single-codebook.md) | arXiv’26 | `–` | `Dyn. KM+Disamb.` | `Enc-Dec / Lazy Dec-Only` | `Fixed` | `NTP†` | `Beam†` |
| [JevRec](jevrec.md) | arXiv’26 | `Text` | `Freq. R-KM` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `Length-Quota Beam` |
