# CITE

*Contextual Item Transition Embeddings for Generative Recommendation with Parallel Semantic Identifiers* — Ma et al. · Electronics’26

`I. Informativeness` · `Inference`

[Paper](https://doi.org/10.3390/electronics15204749) · [Matrix](../../README.md#i--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Par. OPQ` | `Non-AR` | `Fixed / Discrim.` | **`Scoring`** |

- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--inference)
