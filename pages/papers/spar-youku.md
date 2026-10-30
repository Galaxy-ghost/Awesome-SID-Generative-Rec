# SPAR-Youku: SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced Semantic IDs

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.27898`)](https://arxiv.org/abs/2610.27898) · [Source Record (`data/papers/spar-youku.yaml`)](../../data/papers/spar-youku.yaml)

> **Summary**: Semantic ID (SID)-based generative recommendation retrieves items through successive token-level decisions, making personalization at each decoding step essential. However, existing methods insufficiently account for prefix-dependent user evidence and imbalanced historical interaction loads among candidate branches. This can cause irreversible branch-selection errors and favor popular paths. We propose SPAR, a generative recommendation framework that jointly improves stepwise personalization and SID construction. Its PATH Decoder retrieves prefix-relevant evidence from compressed long-term user memories and combines it with recent behavior, user profiles, and event context to guide each token decision. Its RQ-PIB module balances historical interaction loads among sibling branches under each parent prefix while preserving semantic structure. Experiments on large-scale Youku production data show an average relative HitRate improvement of 2.66% over the strongest baseline. SPAR also increases target-prefix retention by 5.79 percentage points and reduces the traffic-weighted largest child-branch share by 32.84% across SID levels. In a 7-day online A/B test, SPAR serves 10% of Youku's production traffic and improves average watch time per user by 3.95% and play conversion rate by 3.38%. These results demonstrate more reliable hierarchical decoding, balanced SID branches, and improved user engagement in industrial recommendation.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `RQ-PIB` | Residual Quantization with Prefix-aware Interaction Balancing |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → DPO` | NTP, then preference optimization. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Backbone` (6 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` | `H-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` | `Dual H-KM` | `Dual Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` | `Casc. RQ` | `Dec-Only` | `Fixed` | `NTP + Dense` | `BeamFusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` | `Geo-Idx` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` | `–` | `Enc-Dec` | `–` | `NTP + Rank` | `Beam` |
