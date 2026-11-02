# TRACER

*Token ReAssignment for Concept ERasure in Generative Recommendation* — Chen et al. · NeurIPS’26

`IV. Utility` · `Tokenization`

[Paper](https://arxiv.org/abs/2606.07688) · [Matrix](../../README.md#iv--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Soft Reassign. RQ`** | `Dec-Only / Enc-Dec` | `Joint / NTP + Aux.` | `Beam` |

- `Soft Reassign. RQ`: Residual quantization with differentiable soft code reassignment.
- `Dec-Only / Enc-Dec`: Decoder-only and encoder–decoder backbone variants.
- `Joint`: The generator loss updates the tokenizer directly.
- `NTP + Aux.`: NTP plus another auxiliary loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--tokenization)
