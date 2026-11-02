# MSCGRec

*Multimodal Generative Recommendation for Fusing Semantic and Collaborative Signals* — Vandenhirtz et al. · arXiv’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2602.03713) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`RQ-VAE+DINO`** | `Enc-Dec` | `Fixed† / NTP` | `Trie/C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用多模态语义码和协同码共同表示物品，以约束 softmax 训练，约束束搜索解码。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
