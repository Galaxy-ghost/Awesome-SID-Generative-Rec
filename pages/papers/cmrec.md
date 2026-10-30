# CMRec: Cross-Country Code-Mixing for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2609.28972`)](https://arxiv.org/abs/2609.28972) · [Source Record (`data/papers/cmrec.yaml`)](../../data/papers/cmrec.yaml)

> **Summary**: 文本/图像用Qwen-VL-32B编码，再跨国i2i sampled softmax对齐注入行为；动态属性仅混合筛选不计SID输入。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Gao et al. (2026) | Published / posted in `CIKM’26 Short` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text+Img+CF` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only†` |  |
| **Tokenizer Training** | `–` | No SID is built. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `VI. Generalization` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RecBase](recbase.md) | EMNLP’25 | `Text` | `Curr. RQ` | `Dec-Only` | `Fixed` | `NTP` | `Beam` |
| [AWARE](aware.md) | arXiv’26 | `Text+Geo` | `Geo-Prefix+HClus` | `Dec-Only` | `Fixed` | `NTP` | `–` |
| [CausalDPO](causaldpo.md) | ICML’26 | `Text` | `LLM-Vocab` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Scoring` |
