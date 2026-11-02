# Dynamic-Single-Codebook

*From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook for Generative Recommendation* — Xie et al. · arXiv’26

`V. Efficiency` · `Tokenization`

[Paper](https://arxiv.org/abs/2608.21012) · [Matrix](../../README.md#v--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Dyn. KM+Disamb.`** | `Enc-Dec / Lazy Dec-Only` | `Fixed / NTP†` | `Beam†` |

- `–`: Not reported in the paper.
- `Dyn. KM+Disamb.`: Dynamically updated k-means codes combined with disambiguation codes.
- `Enc-Dec / Lazy Dec-Only`: Encoder–decoder and lazy decoder-only backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--tokenization)
