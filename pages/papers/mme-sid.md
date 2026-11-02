# MME-SID

*Empowering large language model for sequential recommendation via multimodal embeddings and semantic ids* — Wang et al. · CIKM’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2509.02017) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`MM-RQ`** | `Dec-Only` | `Fixed / NTP` | `Scoring` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

SID 只作 LLM 的输入，用输出嵌入对全物品打分，不生成 SID。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
