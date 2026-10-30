# RecBase: Recbase: Generative foundation model pretraining for zero-shot recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2509.03131`)](https://arxiv.org/abs/2509.03131) · [Source Record (`data/papers/recbase.yaml`)](../../data/papers/recbase.yaml)

> **Summary**: Abstract: "cross-domain generalization is hindered by a fundamental mismatch between language-centric pretraining and the recommendation task".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhou et al. (2025) | Published / posted in `EMNLP’25` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text` |  |
| **Tokenization** | `Curr. RQ` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "cross-domain generalization is hindered by a fundamental mismatch between language-centric pretraining and the recommendation task".

## Peer Methods in `VI. Generalization` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AWARE](aware.md) | arXiv’26 | `Text+Geo` | `Geo-Prefix+HClus` | `Dec-Only` | `Fixed` | `NTP` | `–` |
| [CausalDPO](causaldpo.md) | ICML’26 | `Text` | `LLM-Vocab` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Scoring` |
| [CMRec](cmrec.md) | CIKM’26 Short | `Text + Img + CF` | `RQ-VAE` | `Dec-Only†` | `–` | `NTP` | `–` |
