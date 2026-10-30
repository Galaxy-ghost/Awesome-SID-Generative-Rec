# DECOR

*Learning Decomposed Contextual Token Representations from Pretrained and Collaborative Signals for Generative Recommendation* — Liu et al., SIGIR’26

[arXiv](https://arxiv.org/abs/2509.10468) · [Record](../../data/papers/decor.yaml) · [← Catalog](../../README.md#iii--backbone)

> Abstract: "suboptimal static tokenization"; "discarded pretrained semantics". Candidates: I / III (rule: tie broken by the first new design).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `RQ-VAE` | **`Enc-Dec`** | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "suboptimal static tokenization"; "discarded pretrained semantics". Candidates: I / III (rule: tie broken by the first new design).
- **`tokenizer`** (Fig. 2, p4): Location from the pre-10-26 Training evidence in the appendix.
- **`inference`** (§4.8, p9; Table 5, p10): No prefix constraint reported.

## Same cell: III × Backbone (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` → `Par. VQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` → `SimHash` → **`Non-AR`** → `Fixed / MTP + Aux.` → `Scoring` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [LESSRec](lessrec.md) | arXiv’26 | `Text / Text+CF` → `RQ-VAE / R-KM / LETTER` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` → `Par. OPQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Multi-task NTP` → `Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` → `CoBa RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed† / NTP†` → `C-Beam` |
