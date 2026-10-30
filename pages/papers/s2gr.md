# S2GR: S2GR: Stepwise Semantic-Guided Reasoning in Latent Space for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2601.18664`)](https://arxiv.org/abs/2601.18664) · [Source Record (`data/papers/s2gr.yaml`)](../../data/papers/s2gr.yaml)

> **Summary**: Abstract: "degrading quality for SID codes". Candidates: III / none (rule: judged by the abstract's complaint first).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Guo et al. (2026) | Published / posted in `KDD’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `CoBa RQ-VAE` | Collaborative and Balanced RQ-VAE: item co-occurrence signal, codebook uniformity and load balancing (S2GR). |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Ctr.` | NTP plus a contrastive loss. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "degrading quality for SID codes". Candidates: III / none (rule: judged by the abstract's complaint first).
- **`representation`** (§5.1.3, p7; §4.2.1, p4, Eq. 3–5): Public-data (Beauty) setting; industrial data uses video frames.
- **`tokenizer`** (§5.1.3, p7; §5.3, p7): Location from the pre-10-26 Training evidence in the appendix.

## Peer Methods in `III. SID–Model Alignment` × `Backbone` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` | `Par. VQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` | `SimHash` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` | `RQ-VAE / R-KM / LETTER` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `C-Beam` |
