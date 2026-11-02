# JevRec

*Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation* — Zhong et al. · arXiv’26

`V. Efficiency` · `Tokenization`

[Paper](https://arxiv.org/abs/2610.36937) · [Matrix](../../README.md#v--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Freq. R-KM`** | `Enc-Dec` | `Fixed / NTP + Aux.` | `Length-Quota Beam` |

- `Freq. R-KM`: Frequency-aware residual k-means tokenization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `Length-Quota Beam`: Beam search with recommendation quotas allocated across output lengths.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--tokenization)
