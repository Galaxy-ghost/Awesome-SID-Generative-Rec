# SEATER

*Generative retrieval with semantic tree-structured identifiers and contrastive learning* — Si et al. · SIGIR-AP’24

`V. Efficiency` · `Tokenization`

[Paper](https://arxiv.org/abs/2309.13375) · [Matrix](../../README.md#v--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | **`Tree-Clus.`** | `Enc-Dec` | `Fixed / NTP + Ctr.` | `C-Beam` |

- `CF`: Collaborative filtering signal.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

构造等长的平衡树状标识，并用对比学习建模标识结构。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--tokenization)
