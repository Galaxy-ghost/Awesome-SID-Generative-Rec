# Spacetime-GR

*A Spacetime-Aware Generative Model for Large Scale Online POI Recommendation* — Lin et al., arXiv’25 · `POI`

[arXiv](https://arxiv.org/abs/2508.16126) · [Record](../../data/papers/spacetime-gr.yaml) · [← Catalog](../../README.md#i--backbone)

> 工业版本以二元地理标识生成完整POI，映射原文明确一一对应；表值限生成推荐分支。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Geo` | `Geo-Idx` | **`Dec-Only`** | `Fixed / NTP → DPO` | `Beam` |

- `Geo`: Geographic coordinates or spatial features.
- `Geo-Idx`: Identifiers constructed from geographic indexing.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

## Same cell: I × Backbone (6 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` → `H-KM` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` → `Dual H-KM` → **`Dual Enc-Dec`** → `Fixed / NTP + Ctr.` → `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` → `Casc. RQ` → **`Dec-Only`** → `Fixed / NTP + Dense` → `BeamFusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` → `RQ-VAE / Learn. RQ` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` → `RQ-PIB` → **`Dec-Only`** → `Fixed / NTP → DPO` → `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` → `–` → **`Enc-Dec`** → `– / NTP + Rank` → `Beam` |
