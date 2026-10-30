# CausalDPO: Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2603.22335`)](https://arxiv.org/abs/2603.22335) · [Source Record (`data/papers/causaldpo.yaml`)](../../data/papers/causaldpo.yaml)

> **Summary**: Abstract: "significantly undermining the generalization capability of LLM-based generative recommendation methods in out of distribution (OOD) scenarios".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhao et al. (2026) | Published / posted in `ICML’26` |
| **Problem Band** | `VI. Generalization` | Does it still work for new items, new domains, and shifting interests? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `Text` |  |
| **Tokenization** | `LLM-Vocab` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → DPO` | NTP, then preference optimization. |
| **Inference Decoding** | `Scoring` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "significantly undermining the generalization capability of LLM-based generative recommendation methods in out of distribution (OOD) scenarios".

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

生成物品标题文本，再对全物品打分映射到物品；当前记录将标题标识归为 LLM-Vocab。

## Peer Methods in `VI. Generalization` × `Training` (3 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [RecBase](recbase.md) | EMNLP’25 | `Text` | `Curr. RQ` | `Dec-Only` | `Fixed` | `NTP` | `Beam` |
| [AWARE](aware.md) | arXiv’26 | `Text+Geo` | `Geo-Prefix+HClus` | `Dec-Only` | `Fixed` | `NTP` | `–` |
| [CMRec](cmrec.md) | CIKM’26 Short | `Text+Img+CF` | `RQ-VAE` | `Dec-Only†` | `–` | `NTP` | `–` |
