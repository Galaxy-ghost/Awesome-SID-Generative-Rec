# GRID: GRID: Generative Recommendation via Inpainting Diffusion

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2507.22224`)](https://arxiv.org/abs/2507.22224) · [Source Record (`data/papers/grid.yaml`)](../../data/papers/grid.yaml)

> **Summary**: Abstract: "the absence of an open-source, unified framework hinders systematic benchmarking and extension".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Ju et al. (2025) | Published / posted in `CIKM’25` |
| **Problem Band** | `Paradigms, Systems and Benchmarks` | Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| **Primary Stage** | `n/a` | Used for Paradigms, Systems and Benchmarks (psb) rows that are not assigned to a single stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "the absence of an open-source, unified framework hinders systematic benchmarking and extension".
- **`stage`** (arXiv abstract): Appendix tentatively places the new design in Backbone.
- **`tokenization`** (§4.1, p3): R-KM is the paper's RK-Means, (L, W) = (3, 256).

## Peer Methods in `Paradigms, Systems and Benchmarks` × `n/a` (12 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TIGER](tiger.md) | NeurIPS’23 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FORGE](forge.md) | KDD’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Dyn. Beam` |
| [MiniOneRec](minionerec.md) | arXiv’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [OneRec](onerec.md) | arXiv’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Sess. Beam` |
| [GR-Generalize](gr-generalize.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `Hybrid` |
| [NEO](neo.md) | arXiv’26 | `Text / Audio` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
| [Netflix-SID-Comparison](netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | `–` | `RQ-VAE` | `Dec-Only / Non-AR` | `Fixed` | `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` | `C-Beam / Scoring` |
| [OneMall](onemall.md) | CIKM’26 | `Text+Img+CF` | `R-KM+FSQ` | `Enc-Dec` | `–` | `(NTP + Ctr.) → (NTP + Ctr. + RL)` | `Beam` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [ReRankID](rerankid.md) | arXiv’26 | `Text` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Greedy` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` | `–` | `–` | `–` | `–` | `–` |
| [TransX-GenRet](transx-genret.md) | arXiv’26 | `–` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP → (NTP + DPO)` | `C-Beam` |
