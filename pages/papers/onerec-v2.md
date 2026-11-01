# OneRec-V2

*Technical Report* — Zhou et al., arXiv’25

[arXiv](https://arxiv.org/abs/2508.20900) · [Record](../../data/papers/onerec-v2.yaml) · [← Catalog](../../README.md#v--backbone)

> §4.1明确OneRec-V2 PTQ不改架构或训练；其§2.2.2点名沿用OneRec-V1 tokenizer。另核OneRec-V1 §2.1.1，caption/tag/ASR/OCR/cover/frames进入MiniCPM-V，再用协同物品对对齐。仅通过该两跳继承链报告，故标†。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF†` | `R-KM†` | **`Lazy Dec-Only`** | `Fixed / NTP → RL` | `Beam` |

- `Lazy Dec-Only`: A lazy decoder-only architecture that concentrates decoder computation on target generation.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

## Evidence

- **`problem`** (arXiv abstract): Abstract: "inefficient computational allocation where 97.66% of resources are consumed by sequence encoding rather than generation"; "limitations in reinforcement learning relying solely on reward models". Candidates: V / IV (rule: tie broken by the first new design).
- **`representation`** (§2.2.2, p8): Paper only says the tokenizer is as in OneRec-V1; inferred from the OneRec technical report, as for OneRec-Think.
- **`tokenization`** (§2.2.2, p8): Paper only says the tokenizer is as in OneRec-V1; inferred from the OneRec technical report, as for OneRec-Think.

## Same cell: V × Backbone (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [RPG](rpg.md) | KDD’25 | `Text+Img` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP` → `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP → (NTP + Aux.)` → `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP / NTP + Aux.` → `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
