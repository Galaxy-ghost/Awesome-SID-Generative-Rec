# MBGR

*Multi-Business Prediction for Generative Recommendation at Meituan* — Li et al. · arXiv’26

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2604.02684) · [Matrix](../../README.md#vi--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`RQ`** | `Dec-Only` | `Fixed† / NTP + Aux.` | `C-Beam` |

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用业务感知 SID 和多业务预测结构缓解多业务场景的跷跷板问题。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--tokenization)
