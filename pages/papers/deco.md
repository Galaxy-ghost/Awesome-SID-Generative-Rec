# Deco: Separating Thinking from Spelling for Efficient Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.32980`)](https://arxiv.org/abs/2610.32980) · [Source Record (`data/papers/deco.yaml`)](../../data/papers/deco.yaml)

> **Summary**: Generative recommenders retrieve items by writing their semantic IDs (SIDs) code by code under trie-constrained beam search, an approach now deployed on large web platforms. Standard autoregressive interfaces pay for the SID length K twice: a history of T items enters the backbone as TK code tokens, and every beam-search step runs through the backbone, so returning B candidates costs O(BK) backbone decode tokens per user. The second cost often dominates, and it grows with the backbone, the SID depth and the candidate budget. We introduce Deco (decoding from concepts), which separates reading the history from writing the identifier. The backbone reads each history item as one fused token and condenses the history once into a compact next-item concept; a light KV-cached decoder conditioned on the concept and the generated prefix runs the entire beam search, while the identifiers, the trie and the autoregressive factorization stay unchanged. The decoder approaches full-backbone accuracy with cross-entropy alone, and distillation improves it further. On seven datasets from e-commerce, movies and music streaming, Deco achieves comparable or better accuracy than both a standard generative recommender and the full-backbone teacher with fused inputs, while delivering 3.2-8.6$\times$ their throughput under a 50 ms p95 latency budget in a production-style serving pipeline. Delegating beam search makes larger candidate pools and models practical: Deco generates 1000 candidates faster than its teacher generates 100, and with a 1.5B-parameter LLM backbone, it matches the 69M-parameter teacher's throughput while achieving higher accuracy.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Gusak et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text / –` | 文本构码数据 / Yambda提供128维物品向量但未披露输入来源。 |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Backbone` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [RPG](rpg.md) | KDD’25 | `Text+Img` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP` | `Graph` |
| [ACERec](acerec.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP + Ctr. + Aux.` | `Scoring` |
| [IBA](iba.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP → (NTP + Aux.)` | `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP / NTP + Aux.` | `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `–` | `NTP → DPO` | `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` | `RQ-VAE†` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Dual-level Flow Ctr.` | `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
