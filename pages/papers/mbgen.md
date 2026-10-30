# MBGen: Multi-Behavior Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2405.16871`)](https://arxiv.org/abs/2405.16871) · [Source Record (`data/papers/mbgen.yaml`)](../../data/papers/mbgen.yaml)

> **Summary**: Abstract: "neglecting the value of integrating the target behavior type into the learning objective".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liu et al. (2024) | Published / posted in `CIKM’24` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `CF` | Collaborative filtering signal. |
| **Tokenization** | `Bal. VQ+KM` | Balanced SID: single-layer VQ plus per-prefix k-means (MBGen). |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "neglecting the value of integrating the target behavior type into the learning objective".
- **`tokenizer`** (§3.1–3.3, p3–5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§3.1–3.3, p3–5): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `I. Informativeness` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RAGR](ragr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Beam† / –` |
| [REGER](reger.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → (NTP + Aux.)` | `Beam` |
| [SynGR](syngr.md) | ICML’26 | `Text+Img` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
