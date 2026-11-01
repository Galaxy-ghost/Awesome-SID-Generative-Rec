# TRACER

*Token ReAssignment for Concept ERasure in Generative Recommendation* — Chen et al., NeurIPS’26

[arXiv](https://arxiv.org/abs/2606.07688) · [Record](../../data/papers/tracer.yaml) · [← Catalog](../../README.md#iv--tokenization)

> 直接修改 SID 分配并用于自回归生成器的概念遗忘，不是单纯外部排序证据。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Soft Reassign. RQ`** | `Dec-Only / Enc-Dec` | `Joint / NTP + Aux.` | `Beam` |

- `Soft Reassign. RQ`: Residual quantization with differentiable soft code reassignment.
- `Dec-Only / Enc-Dec`: Decoder-only and encoder–decoder backbone variants.
- `Joint`: The generator loss updates the tokenizer directly.
- `NTP + Aux.`: NTP plus another auxiliary loss.
