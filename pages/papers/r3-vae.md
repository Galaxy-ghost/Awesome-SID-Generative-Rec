# R3-VAE

*Reference Vector-Guided Rating Residual Quantization VAE for Generative Recommendation* — Wan et al. · arXiv’26

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2604.11440) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Ref.-RQ`** | `–` | `Fixed / NTP` | `Beam` |

- `Ref.-RQ`: Reference-vector RQ variant.
- `–`: Not reported in the paper.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用参考向量和点积评分稳定残差量化训练，并给出不用训练生成模型的 SID 评估指标。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
