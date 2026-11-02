# Latte

*Expressiveness Limits of Autoregressive Semantic ID Generation in Generative Recommendation* — Hou et al. · arXiv’26

`III. SID–Model Alignment` · `Backbone`

[Paper](https://arxiv.org/abs/2605.06331) · [Matrix](../../README.md#iii--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `RQ-VAE` | **`Dec-Only`** | `Fixed / NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Backbone |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

指出逐码解码树限制了表达能力，在每个 SID 前插入潜 token 重塑解码空间。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--backbone)
