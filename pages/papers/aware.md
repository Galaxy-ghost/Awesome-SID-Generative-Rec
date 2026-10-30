# AWARE: Why Users Go There: World Knowledge-Augmented Generative Next POI Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2605.11807`)](https://arxiv.org/abs/2605.11807) · [Source Record (`data/papers/aware.yaml`)](../../data/papers/aware.yaml)

> **Summary**: 沿用ROS的SID生成骨干，增量是有原文机制和实验支撑的世界知识获取及历史选择。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Ding et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text+Geo` |  |
| **Tokenization** | `Geo-Prefix+HClus` | S2地理前缀加层次聚类 |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `VI. Generalization` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RecBase](recbase.md) | EMNLP’25 | `Text` | `Curr. RQ` | `Dec-Only` | `Fixed` | `NTP` | `Beam` |
| [CausalDPO](causaldpo.md) | ICML’26 | `Text` | `LLM-Vocab` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Scoring` |
| [CMRec](cmrec.md) | CIKM’26 Short | `Text + Img + CF` | `RQ-VAE` | `Dec-Only†` | `–` | `NTP` | `–` |
