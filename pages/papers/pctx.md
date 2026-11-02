# Pctx

*Tokenizing Personalized Context for Generative Recommendation* — Zhong et al. · CIKM’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2510.21276) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`RQ`** | `Enc-Dec` | `Fixed / NTP` | `Beam+Agg.` |

- `RQ`: Residual quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Beam+Agg.`: Beam search followed by aggregation of predictions that refer to the same item.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
