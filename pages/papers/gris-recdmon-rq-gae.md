# GrIS (RecDMoN / RQ-GAE)

*Graph-Informed Semantic IDs (RecDMoN / RQ-GAE) for Generative Recommendation* — Medvedev et al. · CIKM’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2610.01533) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`RecDMoN / RQ-VAE`** | `Enc-Dec` | `Fixed / –` | `–` |

- `RecDMoN / RQ-VAE`: Recursive DMoN graph partitioning or residual-quantized variational coding.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
