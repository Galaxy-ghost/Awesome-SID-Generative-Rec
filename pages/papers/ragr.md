# RAGR

*Review-Augmented Generative Recommendation* — Zhang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2605.17267) · [Record](../../data/papers/ragr.yaml) · [← Catalog](../../README.md#i--training)

> 评论 SID 作为上下文与生成监督，目标仍是物品 SID，属于新推荐训练设计。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Enc-Dec` | **`Fixed / NTP → DPO`** | `Beam† / –` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.
- `Beam† / –`: TIGER+RAGR 沿用 TIGER 的束搜索

## Same cell: I × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [MBGen](mbgen.md) | CIKM’24 | `CF` → `Bal. VQ+KM` → `Enc-Dec` → **`Fixed / NTP`** → `Beam` |
| [REGER](reger.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → (NTP + Aux.)`** → `Beam` |
| [SynGR](syngr.md) | ICML’26 | `Text+Img` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP + Ctr.`** → `C-Beam` |
