# STAMP

*Semantic Trimming and Auxiliary Multi-step Prediction for Generative Recommendation* — Zhan et al. · arXiv’26

`V. Efficiency` · `Backbone`

[Paper](https://arxiv.org/abs/2604.05329) · [Matrix](../../README.md#v--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Enc-Dec / Dec-Only`** | `Fixed / NTP + Aux.` | `C-Beam` |

- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Backbone |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

输入侧裁掉冗余 SID token，输出侧加多步预测，提高训练效率。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--backbone)
