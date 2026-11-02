# Intent-Driven-News

*Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation* — Su et al. · ACL’26 Industry

`III. SID–Model Alignment` · `Training`

[Paper](https://arxiv.org/abs/2605.07613) · [Matrix](../../README.md#iii--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `CoT+Fuzzy Match` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `CoT+Fuzzy Match`: Reasoning-guided identifier generation followed by fuzzy matching to available items.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--training)
