# NEZHA

*A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations* — Wang et al. · WWW’26 Industry

`V. Efficiency` · `Inference`

[Paper](https://arxiv.org/abs/2511.18793) · [Matrix](../../README.md#v--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Dec-Only` | `Fixed / NTP` | **`Self-Draft+Hash`** |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Self-Draft+Hash`: Self-drafted candidate generation with hash-set validity checking.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--inference)
