# Deco

*Separating Thinking from Spelling for Efficient Generative Recommendation* — Gusak et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.32980) · [Record](../../data/papers/deco.yaml) · [← Catalog](../../README.md#v--backbone)

> Generative recommenders retrieve items by writing their semantic IDs (SIDs) code by code under trie-constrained beam search, an approach now deployed on large web platforms. Standard autoregressive interfaces pay for the SID length K twice: a history of T items enters the backbone as TK code tokens, and every beam-search step runs through the backbone, so returning B candidates costs O(BK) backbone decode tokens per user. The second cost often dominates, and it grows with the backbone, the SID depth and the candidate budget. We introduce Deco (decoding from concepts), which separates reading the history from writing the identifier. The backbone reads each history item as one fused token and condenses the history once into a compact next-item concept; a light KV-cached decoder conditioned on the concept and the generated prefix runs the entire beam search, while the identifiers, the trie and the autoregressive factorization stay unchanged. The decoder approaches full-backbone accuracy with cross-entropy alone, and distillation improves it further. On seven datasets from e-commerce, movies and music streaming, Deco achieves comparable or better accuracy than both a standard generative recommender and the full-backbone teacher with fused inputs, while delivering 3.2-8.6$\times$ their throughput under a 50 ms p95 latency budget in a production-style serving pipeline. Delegating beam search makes larger candidate pools and models practical: Deco generates 1000 candidates faster than its teacher generates 100, and with a 1.5B-parameter LLM backbone, it matches the 69M-parameter teacher's throughput while achieving higher accuracy.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text / –` | `R-KM` | **`Dec-Only`** | `Fixed / NTP + Aux.` | `C-Beam` |

- `Text / –`: 文本构码数据 / Yambda提供128维物品向量但未披露输入来源。
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

## Same cell: V × Backbone (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → **`Lazy Dec-Only`** → `Fixed / NTP → RL` → `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP` → `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring` |
| [IBA](iba.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP → (NTP + Aux.)` → `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP / NTP + Aux.` → `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
