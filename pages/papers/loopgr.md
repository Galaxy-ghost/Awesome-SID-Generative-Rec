# LoopGR

*Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth* — Zhang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.34157) · [Record](../../data/papers/loopgr.yaml) · [← Catalog](../../README.md#v--backbone)

> Generative recommendation formulates item recommendation as autoregressive generation rather than a discriminative scoring problem. Although empirical studies exhibit favorable scaling behavior in recommendation, unleashing the benefits of scaling remains challenging under the strict model size and inference cost constraints of real-world systems. A central challenge is to combine expressive modeling of user-item interaction histories with flexible computational depth without proportionally increasing model size. We introduce LoopGR, a parameter-efficient scaling framework for generative recommendation via recurrent depth. LoopGR employs a tailored hierarchical recurrent depth mechanism that alternates between a shared generative decoder and a lightweight context updater. For efficient inference, we further develop recurrent trajectory self-distillation that distills a low-budget student from a high-budget teacher by aligning both predictive distributions and evolution directions. Extensive experiments show that LoopGR consistently outperforms strong generative recommendation baselines. Compared with a representative encoder-decoder baseline, LoopGR achieves superior performance while reducing model size by up to 52%. These results establish recurrent depth as a new scaling dimension, offering a flexible and resource-efficient scaling path for generative recommendation.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Enc-Dec`** | `Fixed / NTP / NTP + Aux.` | `–` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP / NTP + Aux.`: full-budget LoopGR仅NTP
- `–`: Not reported in the paper.

## Same cell: V × Backbone (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → **`Lazy Dec-Only`** → `Fixed / NTP → RL` → `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP` → `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP → (NTP + Aux.)` → `C-Beam` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
