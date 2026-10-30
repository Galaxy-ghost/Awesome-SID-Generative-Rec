# GRC: Learning to Reflect and Correct: Towards Better Decoding Trajectories for Large-Scale Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.23639`)](https://arxiv.org/abs/2602.23639) · [Source Record (`data/papers/grc.yaml`)](../../data/papers/grc.yaml)

> **Summary**: §5.1仅称Qwen3-8B encode item embeddings，未列构码原始输入模态；没有点名继承文本输入配置，不能把常见Qwen文本编码经验写Text†。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Xing et al. (2026) | Published / posted in `CIKM’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → RL` | NTP, then reinforcement learning (GRPO, GBPO, etc.). |
| **Inference Decoding** | `GRC+Beam` | Generation–Reflection–Correction加束搜索，EGRS用反思熵分配固定修正预算。 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `III. SID–Model Alignment` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [PROMISE](promise.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP + Aux.` | `PRM-Beam` |
