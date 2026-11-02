# MDGR

*Masked Diffusion Generative Recommendation* — Mu et al. · arXiv’26

`III. SID–Model Alignment` · `Backbone`

[Paper](https://arxiv.org/abs/2601.19501) · [Matrix](../../README.md#iii--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `Par. OPQ` | **`Non-AR`** | `Fixed / Masked` | `Diff.+Beam` |

- `–`: Not reported in the paper.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Masked`: Masks part of the codes and reconstructs them (includes masked diffusion).
- `Diff.+Beam`: Diffusion-based decoding combined with beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--backbone)
