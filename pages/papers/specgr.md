# SpecGR

*Inductive Generative Recommendation via Retrieval-based Speculation* — Ding et al., AAAI’26

[arXiv](https://arxiv.org/abs/2410.02939) · [Record](../../data/papers/specgr.yaml) · [← Catalog](../../README.md#vi--inference)

> Abstract: "struggle to recommend unseen items".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed / NTP + Rank` | **`Hybrid`** |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "struggle to recommend unseen items".
- **`tokenizer`** (p5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (p5): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: VI × Inference (1 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [LIGER](liger.md) | arXiv’24 | `Text+SID` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP + Dense` → **`Hybrid`** |
