# PinGER

*Token-Efficient Generative Retrieval with Semantic IDs* — Li et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.33435) · [Record](../../data/papers/pinger.yaml) · [← Catalog](../../README.md#v--backbone)

> Generative retrieval replaces nearest-neighbor search with token-by-token decoding of an item's semantic ID (SID). But existing SID-based methods primarily use L levels of tokens sequentially to represent each item in the input history. As a result, a fixed context window holds L times fewer items than it would with one embedding per item. We present PinGER, a generative retriever deployed at Pinterest that retains SID outputs while making input histories compact, built on three ideas. (1) An asymmetric attention mask over interleaved SID and dense tokens lets later items attend only to the dense ones, so the model is supervised at every SID position in training yet serves one token per item while computing the same function. (2) Generation is controllable through goal-conditioned outputs, reinforcement learning, and a prefix-diversity penalty, which together steer retrieval toward surface-specific goals and diverse candidates. (3) A serving stack built for efficient wide-beam generation is paired with decoding constrained to valid identifiers and candidate resolution from a host-local index. Deployed in Related Pins, PinGER lifts saves of fresh Pins by 3.60% and overall saves by 0.62%, while reducing the surface's end-to-end latency by 0.7% and eliminating the cost of the nearest-neighbor search it replaces.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | **`Dec-Only`** | `– / NTP → DPO` | `Div. C-Beam` |

- `Dec-Only`: Decoder-only.
- `–`: No SID is built.
- `NTP → DPO`: NTP, then preference optimization.
- `Div. C-Beam`: Constrained beam search with an explicit diversity mechanism.

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
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
