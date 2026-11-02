# DIGER

*Differentiable Semantic ID for Generative Recommendation* — Fu et al. · SIGIR’26

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2601.19711) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Learn. RQ`** | `Enc-Dec` | `Joint / NTP` | `Beam†` |

- `Enc-Dec`: Encoder-decoder.
- `Joint`: The generator loss updates the tokenizer directly.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
