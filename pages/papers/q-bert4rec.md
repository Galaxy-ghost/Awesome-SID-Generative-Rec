# Q-BERT4Rec

*Quantized Semantic-ID Representation Learning for Multimodal Recommendation* — Huang and Gai · arXiv’25

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2512.02474) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img+CF`** | `RQ-VAE` | `Encoder (Non-AR)` | `Fixed / Masked` | `Non-AR` |

- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Masked`: Masks part of the codes and reconstructs them (includes masked diffusion).

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

掩码预测下一物品的 SID，推理时在物品集合上取概率最大者，原文没有给出生成或解码 SID 的过程。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
