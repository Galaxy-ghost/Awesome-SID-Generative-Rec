# OneLatent: OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.30675`)](https://arxiv.org/abs/2610.30675) · [Source Record (`data/papers/onelatent.yaml`)](../../data/papers/onelatent.yaml)

> **Summary**: 明确生成Res-Kmeans三位SID；首次2026-10-22在补搜窗口，提出新的latent对齐训练与高效推荐方法。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Jiang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `MM` | 原文明确使用PinCLIP多模态物品嵌入，但未展开具体构码模态组成。 |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |
