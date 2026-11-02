# LESSRec

*Level-Specific History Modeling for Semantic ID-Based Recommendation* — Yang et al. · arXiv’26

`III. SID–Model Alignment` · `Backbone`

[Paper](https://arxiv.org/abs/2610.37286) · [Matrix](../../README.md#iii--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text / Text+CF` | `RQ-VAE / R-KM / LETTER` | **`Enc-Dec`** | `Fixed / NTP` | `C-Beam` |

- `Text / Text+CF`: Text-only representations or text representations combined with collaborative signals.
- `RQ-VAE / R-KM / LETTER`: RQ-VAE, residual k-means, or LETTER tokenization in different configurations.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--backbone)
