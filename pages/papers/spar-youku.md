# SPAR-Youku

*SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced Semantic IDs* — Zhang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.27898) · [Record](../../data/papers/spar-youku.yaml) · [← Catalog](../../README.md#i--backbone)

> Semantic ID (SID)-based generative recommendation retrieves items through successive token-level decisions, making personalization at each decoding step essential. However, existing methods insufficiently account for prefix-dependent user evidence and imbalanced historical interaction loads among candidate branches. This can cause irreversible branch-selection errors and favor popular paths. We propose SPAR, a generative recommendation framework that jointly improves stepwise personalization and SID construction. Its PATH Decoder retrieves prefix-relevant evidence from compressed long-term user memories and combines it with recent behavior, user profiles, and event context to guide each token decision. Its RQ-PIB module balances historical interaction loads among sibling branches under each parent prefix while preserving semantic structure. Experiments on large-scale Youku production data show an average relative HitRate improvement of 2.66% over the strongest baseline. SPAR also increases target-prefix retention by 5.79 percentage points and reduces the traffic-weighted largest child-branch share by 32.84% across SID levels. In a 7-day online A/B test, SPAR serves 10% of Youku's production traffic and improves average watch time per user by 3.95% and play conversion rate by 3.38%. These results demonstrate more reliable hierarchical decoding, balanced SID branches, and improved user engagement in industrial recommendation.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-PIB` | **`Dec-Only`** | `Fixed / NTP → DPO` | `C-Beam` |

- `–`: Not reported in the paper, or not applicable.
- `RQ-PIB`: Residual Quantization with Prefix-aware Interaction Balancing
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.
- `C-Beam`: Constrained beam search.

## Same cell: I × Backbone (6 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` → `H-KM` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` → `Dual H-KM` → **`Dual Enc-Dec`** → `Fixed / NTP + Ctr.` → `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` → `Casc. RQ` → **`Dec-Only`** → `Fixed / NTP + Dense` → `BeamFusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` → `RQ-VAE / Learn. RQ` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` → `Geo-Idx` → **`Dec-Only`** → `Fixed / NTP → DPO` → `Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` → `–` → **`Enc-Dec`** → `– / NTP + Rank` → `Beam` |
