# PSI

*Purely Semantic Indexing for LLM-based Generative Recommendation and Retrieval* — Zhang et al. · arXiv’25

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2509.16446) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Post-hoc RQ`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

放宽最近质心分配，不追加非语义 token 也能得到唯一 SID。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
