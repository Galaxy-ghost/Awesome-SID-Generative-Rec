# RAGR: RAGR: Review-Augmented Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2605.17267`)](https://arxiv.org/abs/2605.17267) · [Source Record (`data/papers/ragr.yaml`)](../../data/papers/ragr.yaml)

> **Summary**: 评论 SID 作为上下文与生成监督，目标仍是物品 SID，属于新推荐训练设计。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → DPO` | NTP, then preference optimization. |
| **Inference Decoding** | `Beam† / –` | TIGER+RAGR 沿用 TIGER 的束搜索 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [MBGen](mbgen.md) | CIKM’24 | `CF` | `Bal. VQ+KM` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [REGER](reger.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → (NTP + Aux.)` | `Beam` |
| [SynGR](syngr.md) | ICML’26 | `Text+Img` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
