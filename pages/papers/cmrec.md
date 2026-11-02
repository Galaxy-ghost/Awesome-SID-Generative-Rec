# CMRec

*Cross-Country Code-Mixing for Generative Recommendation* — Gao et al. · CIKM’26 Short

`VI. Generalization` · `Training`

[Paper](https://arxiv.org/abs/2609.28972) · [Matrix](../../README.md#vi--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | `Dec-Only†` | **`– / NTP`** | `–` |

- `–`: Not reported in the paper.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--training)
