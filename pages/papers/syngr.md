# SynGR

*Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation* — Chen et al. · ICML’26

`I. Informativeness` · `Training`

[Paper](https://arxiv.org/abs/2605.18920) · [Matrix](../../README.md#i--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | `RQ-VAE` | `Enc-Dec` | **`Fixed / NTP + Ctr.`** | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Training |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

在生成阶段显式利用文本和图像之间的协同信息。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--training)
