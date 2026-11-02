# PROMISE

*Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations* — Guo et al. · arXiv’26

`III. SID–Model Alignment` · `Inference`

[Paper](https://arxiv.org/abs/2601.04674) · [Matrix](../../README.md#iii--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed† / NTP + Aux.` | **`PRM-Beam`** |

- `Enc-Dec`: Encoder-decoder.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `PRM-Beam`: Process-reward-model guided beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Inference |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用过程奖励模型给中间解码步打分，并据此剪枝束搜索。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--inference)
