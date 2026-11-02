# CausalDPO

*Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation* — Zhao et al. · ICML’26

`VI. Generalization` · `Training`

[Paper](https://arxiv.org/abs/2603.22335) · [Matrix](../../README.md#vi--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `LLM-Vocab` | `Dec-Only` | **`Fixed / NTP → DPO`** | `Scoring` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Training |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

生成物品标题文本，再对全物品打分映射到物品；当前记录将标题标识归为 LLM-Vocab。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--training)
