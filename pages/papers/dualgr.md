# DualGR

*Generative Retrieval with Long and Short-Term Interests Modeling* — Yi et al., WWW’26 Short

[arXiv](https://arxiv.org/abs/2511.12518) · [Record](../../data/papers/dualgr.yaml) · [← Catalog](../../README.md#vi--backbone)

> Abstract: "long-short interest interference, context-induced noise in hierarchical SID generation, and the lack of explicit learning from exposed-but-unclicked feedback". Candidates: I / III / VI (rule: tie broken by the title).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `R-KM` | **`Dec-Only`** | `Fixed / NTP + Rank` | `Dual Beam` |

- `–`: Not reported in the paper, or not applicable.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.
- `Dual Beam`: Two-branch beam search, then merge (DualGR).

## Evidence

- **`problem`** (arXiv abstract): Abstract: "long-short interest interference, context-induced noise in hierarchical SID generation, and the lack of explicit learning from exposed-but-unclicked feedback". Candidates: I / III / VI (rule: tie broken by the title).
- **`tokenizer`** (§2.5, p3): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§2.5, p3): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: VI × Backbone (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [FedCGR](fedcgr.md) | CIKM’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [LION](lion.md) | CIKM’26 | `Text†` → `RQ-VAE†` → **`Enc-Dec`** → `Fixed† / NTP + Aux.` → `Beam` |
