# REGER

*Modeling inter-item Relations with Semantic IDs for Generative Recommendation* — Huang et al. · arXiv’26

`I. Informativeness` · `Training`

[Paper](https://arxiv.org/abs/2610.37584) · [Matrix](../../README.md#i--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Enc-Dec` | **`Fixed / NTP → (NTP + Aux.)`** | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → (NTP + Aux.)`: Next-token prediction, followed by joint optimization of next-token prediction and auxiliary objectives.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--training)
