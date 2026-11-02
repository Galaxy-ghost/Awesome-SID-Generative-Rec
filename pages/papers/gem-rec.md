# GEM-Rec

*One Model, Two Markets: Bid-Aware Generative Recommendation* — Jiang et al. · arXiv’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2603.22231) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Enc-Dec` | **`Fixed / NTP`** | `Bid-Aware Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Bid-Aware Beam`: Beam search whose scores incorporate bid information.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用控制 token 决定是否展示广告，并在约束解码时注入实时出价。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--training)
