# TriAlignGR

*Triangular Multitask Alignment with Multimodal Deep Interest Mining for Generative Recommendation* — Zeng et al. · arXiv’26

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2605.05249) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img`** | `RQ-VAE` | `Dec-Only` | `Fixed / Multi-task NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

把视觉语义编进 SID，并用视觉描述等多任务让模型理解 SID 的含义。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
