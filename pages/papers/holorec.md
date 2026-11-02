# HoloRec

*Holistic Encoding and Interleaved Reasoning for Generative Recommendation* — Zhao et al. · arXiv’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2606.15331) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Nested RQ`** | `Enc-Dec` | `Fixed / NTP + Aux.` | `–` |

- `–`: Not reported in the paper.
- `Nested RQ`: Residual quantization across nested representation granularities.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
