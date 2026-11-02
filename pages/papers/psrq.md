# PSRQ

*Progressive Semantic Residual Quantization for Multimodal-Joint Interest Modeling in Music Recommendation* — Wang et al. · CIKM’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2508.20359) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`Prog. RQ`** | `Encoder` | `Fixed / Discrim.` | `Scoring` |

- `Prog. RQ`: Progressive RQ variant.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

SID 只作音乐推荐排序模型的特征，按 AUC 评估，不生成 SID。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
