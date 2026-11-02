# DAS

*Dual-Aligned Semantic IDs Empowered Industrial Recommender System* — Ye et al. · CIKM’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2508.10584) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Dual RQ`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

单阶段同时优化量化和协同对齐，让用户侧与广告侧的 SID 互相对齐。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
