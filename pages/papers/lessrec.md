# LESSRec: LESSRec: Level-Specific History Modeling for Semantic ID-Based Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.37286`)](https://arxiv.org/abs/2610.37286) · [Source Record (`data/papers/lessrec.yaml`)](../../data/papers/lessrec.yaml)

> **Summary**: Semantic ID-based recommendation represents each item as a sequence of semantic tokens obtained through residual quantization. This paradigm generates the next item's tokens autoregressively from coarse to fine, entailing each prediction attending to historical tokens at all semantic levels. However, our inference-time analysis reveals that historical tokens at the target-token's semantic level tend to be more informative, whereas other levels can introduce interference. Motivated by these findings, we propose LESSRec that separately encodes the historical token sequence at each semantic level and restricts attention over historical tokens to the sequence at the target token's semantic level during prediction. To complement these level-specific histories, LESSRec explicitly provides an item-level semantic sequence that represents each historical item's overall semantics in chronological order. The decoder accesses the level-aligned token sequence and the item-level semantic sequence through two separate cross-attention branches and fuses their contexts. We further introduce LESSRec+, which uses separate encoders for different semantic-level histories with the same total parameter count to reduce encoder computation. Extensive experiments across three public datasets and three tokenizers demonstrate the recommendation effectiveness of LESSRec and LESSRec+, with efficiency analyses highlighting the computational benefits of LESSRec+.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Yang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text / Text+CF` | Text-only setting (TIGER/RQ) vs. text plus collaborative setting (LETTER/ Vibrent vs. industrial). |
| **Tokenization** | `RQ-VAE / R-KM / LETTER` | 三种实际评估配置 |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `III. SID–Model Alignment` × `Backbone` (8 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [LLaDA-Rec](llada-rec.md) | arXiv’25 | `Text` | `Par. VQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.` |
| [DECOR](decor.md) | SIGIR’26 | `Text+CF` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [FLASH](flash.md) | NeurIPS’26 | `Text` | `SimHash` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [Latte](latte.md) | arXiv’26 | `Text+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [MDGR](mdgr.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Masked` | `Diff.+Beam` |
| [PrefixMem](prefixmem.md) | arXiv’26 | `MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [S2GR](s2gr.md) | KDD’26 | `Text+CF` | `CoBa RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [TrieRec](trierec.md) | NeurIPS’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `C-Beam` |
