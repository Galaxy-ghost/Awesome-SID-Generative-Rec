# TRACER: TRACER: Token ReAssignment for Concept ERasure in Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2606.07688`)](https://arxiv.org/abs/2606.07688) · [Source Record (`data/papers/tracer.yaml`)](../../data/papers/tracer.yaml)

> **Summary**: 直接修改 SID 分配并用于自回归生成器的概念遗忘，不是单纯外部排序证据。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Chen et al. (2026) | Published / posted in `NeurIPS’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Soft Reassign. RQ` | 保留残差层级，以 softmax token selector 加轻量扰动做可微 token 重分配。 |
| **Backbone** | `Dec-Only / Enc-Dec` | Backbone：MiniOneRec 为 Qwen2.5-7B，TIGER/P5SID/LETTER/ETEGRec 为 T5。（§4 Backbones） |
| **Tokenizer Training** | `Joint` | The generator loss updates the tokenizer directly. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |
