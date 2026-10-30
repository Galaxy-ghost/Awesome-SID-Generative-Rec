# JevRec: JevRec: Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.36937`)](https://arxiv.org/abs/2610.36937) · [Source Record (`data/papers/jevrec.yaml`)](../../data/papers/jevrec.yaml)

> **Summary**: Generative recommendation (GR) represents items as semantic identifiers (SIDs) and autoregressively generates the next item's SID from interaction history. However, most methods assign the same SID length to all items despite highly unequal interaction frequencies. This uniform design repeatedly incurs the cost of fine-grained codes for popular items, while shortening codes to reduce this cost also compresses the semantic representations of long-tail items. Inspired by the compact forms of frequent expressions in natural language, we propose JevRec to encode items as variable-length words and generate the next item from interaction context. Linguistic encoding retains frequency-dependent semantic prefixes from shared codebooks, producing shorter SIDs for popular items and richer descriptions for long-tail items. Yet predicting a sequence-level length and generating token-level content impose different optimization requirements that may conflict under a shared output head. Our Jev-like decision modeling component therefore predicts a length distribution with a dedicated head and generates content conditioned on length through a separate head while sharing the interaction-history representation. Experiments on three public datasets show that JevRec outperforms all compared baselines across the evaluated recommendation metrics. Further analyses show lower training and inference time than TIGER and reduced gradient conflict between length and content prediction.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhong et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Freq. R-KM` | Frequency-aware residual K-means：共享残差码本按频率保留前缀，再加独立消歧码。 |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `Length-Quota Beam` | 多长度分支 beam search，按预测长度概率分配推荐名额，过滤无效完整码后跨长度联合评分。 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Tokenization` (2 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [SEATER](seater.md) | SIGIR-AP’24 | `CF` | `Tree-Clus.` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [Dynamic-Single-Codebook](dynamic-single-codebook.md) | arXiv’26 | `–` | `Dyn. KM+Disamb.` | `Enc-Dec / Lazy Dec-Only` | `Fixed` | `NTP†` | `Beam†` |
