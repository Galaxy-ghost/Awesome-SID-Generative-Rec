# DPE-Rec

*Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction* — Ma et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2610.34700) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `– / Text+Img` | `RQ` | `Non-AR` | **`Fixed / Masked → RL (→ Masked KD for Fast)`** | `Diff.+Legalize` |

- `– / Text+Img`: The representation source is unreported in one configuration; text and image representations are used in another.
- `RQ`: Residual quantization.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Masked → RL (→ Masked KD for Fast)`: Masked-prediction pretraining, followed by reinforcement learning and optional masked-prediction distillation for a faster variant.
- `Diff.+Legalize`: Diffusion-based decoding followed by mapping generated codes to valid items.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
