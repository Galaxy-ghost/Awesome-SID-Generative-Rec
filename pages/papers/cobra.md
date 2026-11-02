# COBRA

*Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations* — Yang et al. · NeurIPS’25

`I. Informativeness` · `Backbone`

[Paper](https://arxiv.org/abs/2503.02453) · [Matrix](../../README.md#i--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `Casc. RQ` | **`Dec-Only`** | `Fixed / NTP + Dense` | `BeamFusion` |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Dense`: NTP plus dense-vector prediction.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Backbone |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

先生成稀疏 ID，再生成稠密向量并在该 ID 下做近邻检索，用 BeamFusion 融合两种分数排序。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--backbone)
