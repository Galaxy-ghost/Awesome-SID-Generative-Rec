# Latte

*Expressiveness Limits of Autoregressive Semantic ID Generation in Generative Recommendation* — Hou et al., arXiv’26

[arXiv](https://arxiv.org/abs/2605.06331) · [Record](../../data/papers/latte.yaml) · [← Catalog](../../README.md#iii--backbone)

> Abstract: "making it difficult to distinguish among them based on user-specific preferences".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `RQ-VAE` | **`Dec-Only`** | `Fixed / NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "making it difficult to distinguish among them based on user-specific preferences".

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

指出逐码解码树限制了表达能力，在每个 SID 前插入潜 token 重塑解码空间。

## Same cell: III × Backbone (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` → `Par. VQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP` → `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` → `SimHash` → **`Non-AR`** → `Fixed / MTP + Aux.` → `Scoring` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` → `RQ-VAE / R-KM / LETTER` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` → `Par. OPQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Multi-task NTP` → `Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` → `CoBa RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed† / NTP†` → `C-Beam` |
