# TrieRec

*Trie-Aware Transformers for Generative Recommendation* — Xu et al. · NeurIPS’26

`III. SID–Model Alignment` · `Backbone`

[Paper](https://arxiv.org/abs/2602.21677) · [Matrix](../../README.md#iii--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Enc-Dec`** | `Fixed† / NTP†` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--backbone)
