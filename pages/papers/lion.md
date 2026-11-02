# LION

*Self-Evolving Memory for Generative Recommendation* — Lin et al. · CIKM’26

`VI. Generalization` · `Backbone`

[Paper](https://arxiv.org/abs/2609.15598) · [Matrix](../../README.md#vi--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE†` | **`Enc-Dec`** | `Fixed† / NTP + Aux.` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `NTP + Aux.`: NTP plus another auxiliary loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--backbone)
