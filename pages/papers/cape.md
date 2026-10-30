# CAPE: Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval and Ranking

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.29298`)](https://arxiv.org/abs/2610.29298) · [Source Record (`data/papers/cape.yaml`)](../../data/papers/cape.yaml)

> **Summary**: Generative recommenders replace the retrieve-then-rank cascade with a single model: beam search over semantic item identifiers performs retrieval, and the same likelihood performs ranking. We show that this shared score makes them forget long-tail items twice. In retrieval, beam search keeps identifier prefixes by the probability mass of their subtrees, so tail items are pruned early, and a wider beam admits few more of them. In ranking, the likelihood places tail items below head items even when they are admitted, so expanding retrieval alone brings little or no gain. Both failures reflect missing item-level memorization (i.e., direct recall of which items co-occur), which collaborative filtering provides and shared-prefix generation lacks. To this end, we propose CAPE (Co-occurrence-Aware Pool Expansion), a training-free plug-in that restores memorization at both stages: (i) a memorization channel retrieves co-occurrence-supported tail items outside the beam and scores them with the frozen generator, and (ii) memorization-calibrated ranking fuses the generator likelihood with co-occurrence evidence while keeping the generator's first item. Experiments with two generative backbones on product and music domains show that CAPE significantly improves long-tail accuracy over the backbones and over re-ranking baselines that share its candidates, preserves or improves overall accuracy, and adds a small fraction of the latency.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Huang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `Text†` |  |
| **Tokenization** | `RQ-VAE†` |  |
| **Backbone** | `Dec-Only / Enc-Dec` | Backbone：MiniOneRec 为 Qwen2.5-7B，TIGER/P5SID/LETTER/ETEGRec 为 T5。（§4 Backbones） |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP† / NTP†` | 分别MiniOneRec发布的SFT checkpoint（recommendation+SID-text alignment）与TIGER逐码预测 |
| **Inference Decoding** | `Hybrid` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Inference` (1 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [CITE](cite.md) | Electronics’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Discrim.` | `Scoring` |
