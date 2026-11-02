# GenRec-JD

*GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation* — Zou et al. · SIGIR’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2604.14878) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | **`Fixed / NTP → RL`** | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

按页做下一 token 预测，压缩输入侧的多 token SID，并做偏好对齐。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
