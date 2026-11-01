# JevRec

*Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation* — Zhong et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.36937) · [Record](../../data/papers/jevrec.yaml) · [← Catalog](../../README.md#v--tokenization)

> Generative recommendation (GR) represents items as semantic identifiers (SIDs) and autoregressively generates the next item's SID from interaction history. However, most methods assign the same SID length to all items despite highly unequal interaction frequencies. This uniform design repeatedly incurs the cost of fine-grained codes for popular items, while shortening codes to reduce this cost also compresses the semantic representations of long-tail items. Inspired by the compact forms of frequent expressions in natural language, we propose JevRec to encode items as variable-length words and generate the next item from interaction context. Linguistic encoding retains frequency-dependent semantic prefixes from shared codebooks, producing shorter SIDs for popular items and richer descriptions for long-tail items. Yet predicting a sequence-level length and generating token-level content impose different optimization requirements that may conflict under a shared output head. Our Jev-like decision modeling component therefore predicts a length distribution with a dedicated head and generates content conditioned on length through a separate head while sharing the interaction-history representation. Experiments on three public datasets show that JevRec outperforms all compared baselines across the evaluated recommendation metrics. Further analyses show lower training and inference time than TIGER and reduced gradient conflict between length and content prediction.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Freq. R-KM`** | `Enc-Dec` | `Fixed / NTP + Aux.` | `Length-Quota Beam` |

- `Freq. R-KM`: Frequency-aware residual k-means tokenization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `Length-Quota Beam`: Beam search with recommendation quotas allocated across output lengths.

## Same cell: V × Tokenization (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [SEATER](seater.md) | SIGIR-AP’24 | `CF` → **`Tree-Clus.`** → `Enc-Dec` → `Fixed / NTP + Ctr.` → `C-Beam` |
| [Dynamic-Single-Codebook](dynamic-single-codebook.md) | arXiv’26 | `–` → **`Dyn. KM+Disamb.`** → `Enc-Dec / Lazy Dec-Only` → `Fixed / NTP†` → `Beam†` |
