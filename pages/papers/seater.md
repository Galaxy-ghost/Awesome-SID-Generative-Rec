# SEATER

*Generative retrieval with semantic tree-structured identifiers and contrastive learning* — Si et al., SIGIR-AP’24

[arXiv](https://arxiv.org/abs/2309.13375) · [Record](../../data/papers/seater.yaml) · [← Catalog](../../README.md#v--tokenization)

> Abstract: "these methods fall short in efficiency and effectiveness for large-scale recommendations". Candidates: V / III (rule: judged by the abstract's complaint first).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | **`Tree-Clus.`** | `Enc-Dec` | `Fixed / NTP + Ctr.` | `C-Beam` |

- `CF`: Collaborative filtering signal.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "these methods fall short in efficiency and effectiveness for large-scale recommendations". Candidates: V / III (rule: judged by the abstract's complaint first).

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

构造等长的平衡树状标识，并用对比学习建模标识结构。

## Same cell: V × Tokenization (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [Dynamic-Single-Codebook](dynamic-single-codebook.md) | arXiv’26 | `–` → **`Dyn. KM+Disamb.`** → `Enc-Dec / Lazy Dec-Only` → `Fixed / NTP†` → `Beam†` |
| [JevRec](jevrec.md) | arXiv’26 | `Text` → **`Freq. R-KM`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `Length-Quota Beam` |
