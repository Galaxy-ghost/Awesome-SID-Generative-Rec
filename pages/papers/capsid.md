# CapsID

*Soft-Routed Variable-Length Semantic IDs for Generative Recommendation* — Cheng et al. · arXiv’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2605.05096) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Soft-RQ`** | `Dec-Only` | `Fixed / NTP` | `C-Beam` |

- `Soft-RQ`: Soft-routed RQ variant.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用胶囊路由替代硬残差量化，按置信度决定 SID 长度，再用 Semantic BPE 合并相邻 token。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
