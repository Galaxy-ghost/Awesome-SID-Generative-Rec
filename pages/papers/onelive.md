# OneLive

*Dynamically Unified Generative Framework for Live-Streaming Recommendation* — Wang et al. · KDD’26 ADS

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2602.08612) · [Matrix](../../README.md#vi--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+Audio+CF` | **`R-KM`** | `Lazy Dec-Only` | `Fixed / NTP → RL` | `Beam` |

- `Text+Img+Audio+CF`: Text, visual, and audio content combined with collaborative signals.
- `R-KM`: Residual k-means.
- `Lazy Dec-Only`: A lazy decoder-only architecture that concentrates decoder computation on target generation.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--tokenization)
