# PROMISE

*Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations* — Guo et al., arXiv’26

[arXiv](https://arxiv.org/abs/2601.04674) · [Record](../../data/papers/promise.yaml) · [← Catalog](../../README.md#iii--inference)

> Abstract: "errors in early, high-level tokens irreversibly divert the generation trajectory".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed† / NTP + Aux.` | **`PRM-Beam`** |

- `Enc-Dec`: Encoder-decoder.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `PRM-Beam`: Process-reward-model guided beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "errors in early, high-level tokens irreversibly divert the generation trajectory".
- **`tokenizer`** (p4): SID construction not described; Fixed inferred from the usual pipeline. Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p4): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用过程奖励模型给中间解码步打分，并据此剪枝束搜索。

## Same cell: III × Inference (1 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [GRC](grc.md) | CIKM’26 | `–` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP → RL` → **`GRC+Beam`** |
