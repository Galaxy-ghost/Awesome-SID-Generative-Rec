# SID-MLP

*MLPs are Efficient Distilled Generative Recommenders* — Guo et al., arXiv’26

[arXiv](https://arxiv.org/abs/2605.12617) · [Record](../../data/papers/sid-mlp.yaml) · [← Catalog](../../README.md#v--backbone)

> 提出可部署的新 SID 生成解码结构，含冻结教师蒸馏与编码器扩展 SID-MLP++。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE†` | **`Enc-MLP`** | `Fixed / NTP + Aux.` | `C-Beam` |

- `Enc-MLP`: 冻结T5 encoder，一次注意力上下文读出，逐码位前缀条件MLP
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

## Same cell: V × Backbone (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → **`Lazy Dec-Only`** → `Fixed / NTP → RL` → `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP` → `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP → (NTP + Aux.)` → `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP / NTP + Aux.` → `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
