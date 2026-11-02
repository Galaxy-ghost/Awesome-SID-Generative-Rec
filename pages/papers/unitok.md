# UniTok

*Tokenize Once, Recommend Anywhere: Unified Item Tokenization for Multi-domain LLM-based Recommendation* — Hou and Shin · AAAI’26

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2511.12922) · [Matrix](../../README.md#vi--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Multi-Dom` | **`TokenMoE`** | `Enc-Dec` | `Fixed / NTP` | `Beam†` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用共享专家和领域专家码本，把多个领域的物品统一分词。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--tokenization)
