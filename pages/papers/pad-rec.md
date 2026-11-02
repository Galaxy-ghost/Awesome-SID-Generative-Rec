# PAD-Rec

*Position-Aware Drafting for Inference Acceleration in LLM-Based Generative List-Wise Recommendation* — Chen et al. · arXiv’26

`V. Efficiency` · `Inference`

[Paper](https://arxiv.org/abs/2604.27747) · [Matrix](../../README.md#v--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed / Multi-task NTP†` | **`Spec. Dec.`** |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Spec. Dec.`: Speculative decoding.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Inference |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

在投机解码的草稿模型中加入 SID 位置信息，加速列表式生成。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--inference)
