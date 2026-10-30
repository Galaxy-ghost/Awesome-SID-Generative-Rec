# STAMP

*Semantic Trimming and Auxiliary Multi-step Prediction for Generative Recommendation* — Zhan et al., arXiv’26

[arXiv](https://arxiv.org/abs/2604.05329) · [Record](../../data/papers/stamp.yaml) · [← Catalog](../../README.md#v--backbone)

> Abstract: "prohibitive training overhead due to sequence expansion".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Enc-Dec / Dec-Only`** | `Fixed / NTP + Aux.` | `C-Beam` |

- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "prohibitive training overhead due to sequence expansion".
- **`backbone`** (§1, p2; §5.1.4, p6): arXiv v3.
- **`tokenizer`** (p5): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

输入侧裁掉冗余 SID token，输出侧加多步预测，提高训练效率。

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
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
