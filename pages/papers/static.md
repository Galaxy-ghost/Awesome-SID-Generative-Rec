# STATIC

*Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators* — Su et al. · KDD’26 ADS

`V. Efficiency` · `Inference`

[Paper](https://arxiv.org/abs/2602.22647) · [Matrix](../../README.md#v--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Dec-Only` | `Fixed / NTP` | **`Vec. C-Beam`** |

- `–`: Not reported in the paper.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Vec. C-Beam`: Vectorized constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--inference)
