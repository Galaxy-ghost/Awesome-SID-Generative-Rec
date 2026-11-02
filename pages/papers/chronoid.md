# ChronoID

*Infusing Explicit Temporal Signals into Semantic IDs for Generative Recommendation* — Nian et al. · arXiv’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2606.14260) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Time` | **`RQ-VAE / Par. VQ`** | `Dec-Only†` | `Fixed / NTP` | `Beam†` |

- `Text+Time`: Text representations combined with interaction timestamps.
- `RQ-VAE / Par. VQ`: Residual-quantized variational codes or parallel vector-quantization codes in different configurations.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
