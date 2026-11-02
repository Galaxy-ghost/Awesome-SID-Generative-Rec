# UTGRec

*Universal Item Tokenization for Transferable Generative Recommendation* — Zheng et al. · arXiv’25

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2504.04405) · [Matrix](../../README.md#vi--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Multi-Dom` | **`Tree`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

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

用多模态大模型和树状码本构造跨领域通用的物品标识。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--tokenization)
