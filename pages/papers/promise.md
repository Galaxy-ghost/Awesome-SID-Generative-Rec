# PROMISE: PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2601.04674`)](https://arxiv.org/abs/2601.04674) · [Source Record (`data/papers/promise.yaml`)](../../data/papers/promise.yaml)

> **Summary**: Abstract: "errors in early, high-level tokens irreversibly divert the generation trajectory".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Guo et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed†` |  |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `PRM-Beam` | Process-reward-model guided beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "errors in early, high-level tokens irreversibly divert the generation trajectory".
- **`tokenizer`** (p4): SID construction not described; Fixed inferred from the usual pipeline. Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p4): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用过程奖励模型给中间解码步打分，并据此剪枝束搜索。

## Peer Methods in `III. SID–Model Alignment` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [GRC](grc.md) | CIKM’26 | `–` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → RL` | `GRC+Beam` |
