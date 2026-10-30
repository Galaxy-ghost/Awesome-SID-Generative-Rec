# IBA

*Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based Generative Recommendation* — Yang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2607.12425) · [Record](../../data/papers/iba.yaml) · [← Catalog](../../README.md#v--backbone)

> 新增隐式精炼模块与预算预测器，并给出训练和约束解码。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Enc-Dec`** | `Fixed / NTP → (NTP + Aux.)` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → (NTP + Aux.)`: 先uniform refinement CE，再主CE联合lookahead token CE及gain regression。
- `C-Beam`: Constrained beam search.

## Same cell: V × Backbone (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → **`Lazy Dec-Only`** → `Fixed / NTP → RL` → `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP` → `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP / NTP + Aux.` → `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
