# HCGRec

*Learning from Unreachable Rewards: Hint-Conditioned Reinforcement Learning for Generative Recommendation* — Zhang et al. · CIKM’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2608.11980) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ` | `Dec-Only` | **`Fixed / NTP → RL`** | `Beam` |

- `–`: Not reported in the paper.
- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
