# RecoChain

*Harmonizing Generative Retrieval and Ranking in Chain-of-Recommendation* — Liu and Cao · arXiv’26

`IV. Utility` · `Backbone`

[Paper](https://arxiv.org/abs/2604.25787) · [Matrix](../../README.md#iv--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | `RQ` | **`Dec-Only`** | `Fixed / NTP + Rank` | `Hybrid` |

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Backbone |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

束搜索生成候选 SID 后，再由排序头对候选打分重排。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--backbone)
