# TopoGR

*Revealing and Preserving Latent Structure of Semantic ID in Generative Recommendation* — Zheng et al. · arXiv’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2607.25216) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`BDQ`** | `Non-AR` | `Fixed / MTP + Aux.` | `Scoring+Rerank` |

- `BDQ`: Bit-Decomposable Quantizer.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Aux.`: Multi-token prediction jointly optimized with auxiliary objectives.
- `Scoring+Rerank`: Score candidate items and then rerank a selected subset.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
