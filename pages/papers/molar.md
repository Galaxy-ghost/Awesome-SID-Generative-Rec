# Molar

*Multimodal llms with collaborative filtering alignment for enhanced sequential recommendation* — Luo et al. · arXiv’24

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2412.18176) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img+CF`** | `n/a` | `Dec-Only` | `n/a / Discrim.` | `Scoring` |

- `n/a`: Not applicable to this method.
- `Dec-Only`: Decoder-only.
- `Discrim.`: Scores items; does not generate SIDs.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用多模态 LLM 产出用户和物品嵌入，按相似度推荐，不使用 SID。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
