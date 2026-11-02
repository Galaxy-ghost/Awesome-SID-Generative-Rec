# FlexCode

*Semantics Meet Signals: Dual Codebook Representationl Learning for Generative Recommendation* — Hui et al. · arXiv’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2511.20673) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Dual RQ-VAE`** | `–` | `Joint / NTP` | `–` |

- `Dual RQ-VAE`: Two residual-quantized variational autoencoders for separate representation streams.
- `–`: Not reported in the paper.
- `Joint`: The generator loss updates the tokenizer directly.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
