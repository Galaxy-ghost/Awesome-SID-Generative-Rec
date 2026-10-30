# COBRA

*Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations* — Yang et al., NeurIPS’25

[arXiv](https://arxiv.org/abs/2503.02453) · [Record](../../data/papers/cobra.yaml) · [← Catalog](../../README.md#i--backbone)

> Abstract: "significant information loss due to the separation of stages such as quantization and sequence modeling".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `Casc. RQ` | **`Dec-Only`** | `Fixed / NTP + Dense` | `BeamFusion` |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Dense`: NTP plus dense-vector prediction.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "significant information loss due to the separation of stages such as quantization and sequence modeling".
- **`tokenizer`** (p5): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p5): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

先生成稀疏 ID，再生成稠密向量并在该 ID 下做近邻检索，用 BeamFusion 融合两种分数排序。

## Same cell: I × Backbone (6 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` → `H-KM` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` → `Dual H-KM` → **`Dual Enc-Dec`** → `Fixed / NTP + Ctr.` → `Fusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` → `RQ-VAE / Learn. RQ` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` → `Geo-Idx` → **`Dec-Only`** → `Fixed / NTP → DPO` → `Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` → `RQ-PIB` → **`Dec-Only`** → `Fixed / NTP → DPO` → `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` → `–` → **`Enc-Dec`** → `– / NTP + Rank` → `Beam` |
