# RecBase

*Generative foundation model pretraining for zero-shot recommendation* — Zhou et al. · EMNLP’25

`VI. Generalization` · `Training`

[Paper](https://arxiv.org/abs/2509.03131) · [Matrix](../../README.md#vi--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Curr. RQ` | `Dec-Only` | **`Fixed / NTP`** | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Training |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

推理时可逐位生成概念 ID，但实验按 AUC 对候选物品打分排序。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--training)
