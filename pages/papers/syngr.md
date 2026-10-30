# SynGR

*Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation* — Chen et al., ICML’26

[arXiv](https://arxiv.org/abs/2605.18920) · [Record](../../data/papers/syngr.yaml) · [← Catalog](../../README.md#i--training)

> Abstract: "underexplore synergistic information across modalities".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | `RQ-VAE` | `Enc-Dec` | **`Fixed / NTP + Ctr.`** | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "underexplore synergistic information across modalities".
- **`tokenizer`** (p6): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p6): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

在生成阶段显式利用文本和图像之间的协同信息。

## Same cell: I × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [MBGen](mbgen.md) | CIKM’24 | `CF` → `Bal. VQ+KM` → `Enc-Dec` → **`Fixed / NTP`** → `Beam` |
| [RAGR](ragr.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → DPO`** → `Beam† / –` |
| [REGER](reger.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → (NTP + Aux.)`** → `Beam` |
