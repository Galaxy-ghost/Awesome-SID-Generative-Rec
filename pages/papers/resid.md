# ReSID

*Rethinking Generative Recommender Tokenizer: Recsys-Native Encoding and Semantic Quantization Beyond LLMs* — Liang et al. · arXiv’26

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2602.02338) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Attr+CF`** | `GAOQ` | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Attr+CF`: Structured item attributes combined with collaborative signals.
- `GAOQ`: Globally Aligned Orthogonal Quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
