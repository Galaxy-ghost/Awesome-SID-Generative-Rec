# AdaSID

*Beyond Static Collision Handling: Adaptive Semantic ID Learning for Multimodal Recommendation at Industrial Scale* — Pan et al. · arXiv’26

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2604.23522) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`RQ`** | `Dec-Only` | `Fixed / NTP` | `C-Beam` |

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

按碰撞情况自适应地学习多模态 SID，替代静态的碰撞处理。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
