# CARD

*Non-Uniform Quantization of Visual Semantic Unit for Generative Recommendation* — Wei et al. · arXiv’26

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2604.26427) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`NU-RQ`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `NU-RQ`: Non-uniform RQ variant.
- `Enc-Dec`: Encoder-decoder.
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

把文本、图像和协同信号统一成视觉语义单元，再用非均匀 RQ-VAE 缓解码字分布不均。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
