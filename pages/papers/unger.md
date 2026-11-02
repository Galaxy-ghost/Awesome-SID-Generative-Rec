# UNGER

*Generative Recommendation with A Unified Code via Semantic and Collaborative Integration* — Xiao et al. · TOIS’25

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2502.06269) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+CF`** | `R-KM` | `Enc-Dec` | `Fixed / NTP + Ctr.` | `Beam` |

- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
