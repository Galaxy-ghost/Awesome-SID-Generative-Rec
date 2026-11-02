# PCR-CA

*Parallel Codebook Representations with Contrastive Alignment for Multiple-Category App Recommendation* — Tan et al. · KDD’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2508.18166) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`PC-AE`** | `Disc.` | `Joint / Discrim.` | `Scoring` |

- `PC-AE`: Parallel Codebook Auto-Encoder
- `Disc.`: A discriminative recommendation model that scores candidates.
- `Joint`: The generator loss updates the tokenizer directly.
- `Discrim.`: Scores items; does not generate SIDs.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
