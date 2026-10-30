# LoopGR: LoopGR: Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.34157`)](https://arxiv.org/abs/2610.34157) · [Source Record (`data/papers/loopgr.yaml`)](../../data/papers/loopgr.yaml)

> **Summary**: Generative recommendation formulates item recommendation as autoregressive generation rather than a discriminative scoring problem. Although empirical studies exhibit favorable scaling behavior in recommendation, unleashing the benefits of scaling remains challenging under the strict model size and inference cost constraints of real-world systems. A central challenge is to combine expressive modeling of user-item interaction histories with flexible computational depth without proportionally increasing model size. We introduce LoopGR, a parameter-efficient scaling framework for generative recommendation via recurrent depth. LoopGR employs a tailored hierarchical recurrent depth mechanism that alternates between a shared generative decoder and a lightweight context updater. For efficient inference, we further develop recurrent trajectory self-distillation that distills a low-budget student from a high-budget teacher by aligning both predictive distributions and evolution directions. Extensive experiments show that LoopGR consistently outperforms strong generative recommendation baselines. Compared with a representative encoder-decoder baseline, LoopGR achieves superior performance while reducing model size by up to 52%. These results establish recurrent depth as a new scaling dimension, offering a flexible and resource-efficient scaling path for generative recommendation.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `–` | No SID is built. |
| **Training Objective** | `NTP / NTP + Aux.` | full-budget LoopGR仅NTP |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Backbone` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP` | `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP + Ctr. + Aux.` | `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP → (NTP + Aux.)` | `C-Beam` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `–` | `NTP → (NTP + DPO)` | `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` | `RQ-VAE†` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Dual-level Flow Ctr.` | `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
