# GTI

*Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation* — Chen et al. · arXiv’26

`III. SID–Model Alignment` · `Training`

[Paper](https://arxiv.org/abs/2604.02324) · [Matrix](../../README.md#iii--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF / Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `–` |

- `Text+CF / Text`: Text with collaborative signals, or text-only representations, in different configurations.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--training)
