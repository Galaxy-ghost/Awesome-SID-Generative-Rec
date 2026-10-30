# CITE

*Contextual Item Transition Embeddings for Generative Recommendation with Parallel Semantic Identifiers* — Ma et al., Electronics’26

[arXiv](https://doi.org/10.3390/electronics15204749) · [Record](../../data/papers/cite.yaml) · [← Catalog](../../README.md#i--inference)

> CITE (Electronics’26): Inference-stage method using Par. OPQ tokenization and Non-AR backbone.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Par. OPQ` | `Non-AR` | `Fixed / Discrim.` | **`Scoring`** |

- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

## Same cell: I × Inference (1 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CAPE](cape.md) | arXiv’26 | `Text†` → `RQ-VAE†` → `Dec-Only / Enc-Dec` → `Fixed / Multi-task NTP† / NTP†` → **`Hybrid`** |
