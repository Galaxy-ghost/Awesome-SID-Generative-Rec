# CogRec

*Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation* — Liu et al. · arXiv’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2607.24402) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`R-KM+Graph`** | `Dec-Only` | `Fixed / Multi-task NTP` | `CoT+C-Beam` |

- `R-KM+Graph`: Residual k-means combined with a graph over semantic codes.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `CoT+C-Beam`: Reasoning followed by constrained beam-search decoding.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
