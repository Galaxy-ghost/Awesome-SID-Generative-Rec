# MuSID-KD

*Multigranularity Knowledge Distillation for Generative Recommendation with Semantic IDs* — Zhang et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.35218) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Enc-MLP` | **`Fixed / NTP + Aux.`** | `C-Beam` |

- `–`: Not reported in the paper.
- `Enc-MLP`: A history encoder followed by MLP-based prediction heads.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
