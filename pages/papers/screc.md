# SCRec

*Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation* — Dan · RecSys’26

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2609.13678) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+CF`** | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed / MTP + Ctr.` | `Scoring / Beam†` |

- `Non-AR / Enc-Dec`: Non-autoregressive and encoder–decoder backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Ctr.`: MTP plus a contrastive loss.
- `Scoring / Beam†`: Discriminative candidate scoring vs. generative beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
