# SIIT

*Enhancing item tokenization for generative recommendation through self-improvement* — Chen et al. · arXiv’24

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2412.17171) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Self-Imp.`** | `Enc-Dec` | `Altern. / Multi-task NTP` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Altern.`: Tokenizer and generator are updated in turns.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

让 LLM 在训练中迭代修正自己的物品分词。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
