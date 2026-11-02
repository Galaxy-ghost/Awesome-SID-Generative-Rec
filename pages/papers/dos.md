# DOS

*Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan* — Yin et al. · WWW’26 Short

`III. SID–Model Alignment` · `Tokenization` · `POI`

[Paper](https://arxiv.org/abs/2602.04460) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Orth. RQ`** | `Dec-Only†` | `Fixed† / NTP` | `–` |

- `Orth. RQ`: Orthogonal residual quantization.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
