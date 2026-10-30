# Dynamic-Single-Codebook: From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2608.21012`)](https://arxiv.org/abs/2608.21012) · [Source Record (`data/papers/dynamic-single-codebook.yaml`)](../../data/papers/dynamic-single-codebook.yaml)

> **Summary**: 有 SID 生成推荐下游和线上验证，区别于 MERGE 只做传统检索。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Xie et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `Dyn. KM+Disamb.` | 曝光加权单层k-means语义码+固定消歧码，曝光EMA动态更新 |
| **Backbone** | `Enc-Dec / Lazy Dec-Only` | 主格分别为OneRec-V1和V2公开适配 |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP†` |  |
| **Inference Decoding** | `Beam†` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Tokenization` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [SEATER](seater.md) | SIGIR-AP’24 | `CF` | `Tree-Clus.` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [JevRec](jevrec.md) | arXiv’26 | `Text` | `Freq. R-KM` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `Length-Quota Beam` |
