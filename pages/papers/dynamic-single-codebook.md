# Dynamic-Single-Codebook

*From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook for Generative Recommendation* — Xie et al., arXiv’26

[arXiv](https://arxiv.org/abs/2608.21012) · [Record](../../data/papers/dynamic-single-codebook.yaml) · [← Catalog](../../README.md#v--tokenization)

> 有 SID 生成推荐下游和线上验证，区别于 MERGE 只做传统检索。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Dyn. KM+Disamb.`** | `Enc-Dec / Lazy Dec-Only` | `Fixed / NTP†` | `Beam†` |

- `–`: Not reported in the paper, or not applicable.
- `Dyn. KM+Disamb.`: 曝光加权单层k-means语义码+固定消歧码，曝光EMA动态更新
- `Enc-Dec / Lazy Dec-Only`: 主格分别为OneRec-V1和V2公开适配
- `Fixed`: SIDs are built first and not changed while the generator trains.

## Same cell: V × Tokenization (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [SEATER](seater.md) | SIGIR-AP’24 | `CF` → **`Tree-Clus.`** → `Enc-Dec` → `Fixed / NTP + Ctr.` → `C-Beam` |
| [JevRec](jevrec.md) | arXiv’26 | `Text` → **`Freq. R-KM`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `Length-Quota Beam` |
