# CoST

*Contrastive quantization based semantic tokenization for generative recommendation* — Zhu et al. · RecSys’24

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2404.14774) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`C-RQ`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

CoST trains the item tokenizer with a contrastive quantization objective that captures neighborhood relationships between items, instead of the reconstruction loss used by RQ-VAE.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | CoST trains the item tokenizer with a contrastive quantization objective that captures neighborhood relationships between items, instead of the reconstruction loss used by RQ-VAE. |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: MIND news (preprocessing following Feng et al. 2022: interactions with at least 15 users kept, sequences capped at 70; 29,207 users / 12,251 items) and Amazon Office (users with fewer than 5 interactions removed), split by item count into Office (S) (2,868 users / 14,618 items) and Office (L) (16,696 users / 37,347 items).
  - Source: Datasets and filters: https://arxiv.org/html/2404.14774v2#S4.SS1.p1; statistics: https://arxiv.org/html/2404.14774v2#S3.T1.
- **Split**: Leave-one-out: last item for test, penultimate for validation, the remaining items for training.
  - Source: Leave-one-out allocation: https://arxiv.org/html/2404.14774v2#S4.SS1.p3.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates).
  - Source: Metrics only: https://arxiv.org/html/2404.14774v2#S4.SS1.p3.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard leave-one-out with no cold-start experiment: https://arxiv.org/html/2404.14774v2#S4.SS1.p3.
- **SID**: 3 residual-quantization levels with a codebook of size 64 shared across levels, 96-dimensional latent; Sentence-T5 768-dimensional input. The paper states each item receives a unique 3-tuple, but the mechanism that guarantees uniqueness is not reported.
  - Source: 3 shared codebooks of size 64, 96-dimensional latent, unique 3-tuples: https://arxiv.org/html/2404.14774v2#S4.SS1.p2; sensitivity: https://arxiv.org/html/2404.14774v2#S4.F4.
- **Inference budget**: TIGER-style encoder-decoder; decoding method and beam width not reported. Recall and NDCG at K=5, 10, 20, 40 (MIND) and 10, 20 (Office). Hardware, inference batch size, and latency: not reported.
  - Source: Generator follows TIGER's structure, no decoding settings: https://arxiv.org/html/2404.14774v2#S4.SS1.p2 and https://arxiv.org/html/2404.14774v2#S3.SS2.p1.
- **Results from**: Table 2 (MIND) and Table 3 (Office (S) and Office (L)), comparing random hashing, reconstruction-only RQ-VAE, contrastive-only, and combined losses; Figures 3-4 (temperature, epochs, codebook size, number of codebooks, embedding dimension).
  - Source: MIND: https://arxiv.org/html/2404.14774v2#S4.T2; Office: https://arxiv.org/html/2404.14774v2#S4.T3; sensitivity: https://arxiv.org/html/2404.14774v2#S4.F3 and https://arxiv.org/html/2404.14774v2#S4.F4.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

在量化中加入对比学习，让 SID 保留物品之间的邻域关系。

### 5. Connections to Related Work

- **Predecessor** · [TIGER](tiger.md): TIGER's RQ-VAE is trained only with reconstruction loss; CoST keeps TIGER's generator and adds a contrastive loss so that neighboring items get distinguishable codes.
  - Source: CoST v2, Section 1 identifies RQ-VAE from TIGER as the starting point: https://arxiv.org/html/2404.14774v2#S1.p3; Section 3.2 follows TIGER's architecture: https://arxiv.org/html/2404.14774v2#S3.SS2.p1; the reconstruction-only row in Tables 2-3 is the TIGER-style tokenizer: https://arxiv.org/html/2404.14774v2#S4.T2 and https://arxiv.org/html/2404.14774v2#S4.T3.
- **Alternative** · [EAGER](eager.md): EAGER tokenizes items by hierarchical k-means and also integrates collaborative information, whereas CoST trains a residual quantizer with a contrastive objective over item neighborhoods.
  - Source: CoST v2, Section 1 and Section 2 cite Wang et al. (2024b), EAGER, for hierarchical k-means and semantic-collaborative tokenization: https://arxiv.org/html/2404.14774v2#S1.p3 and https://arxiv.org/html/2404.14774v2#S2.p2; not compared in Tables 2-3.
- **Alternative** · [LETTER](letter.md): LETTER integrates collaborative signals into the RQ-VAE tokenizer, while CoST uses contrastive quantization on semantic embeddings.
  - Source: CoST v2, Section 2 cites LETTER among semantic-collaborative tokenizers: https://arxiv.org/html/2404.14774v2#S2.p2; not compared in Tables 2-3.
- **Alternative** · [TokenRec](tokenrec.md): TokenRec also combines semantic and collaborative information when tokenizing items; CoST relies on contrastive learning over semantic embeddings.
  - Source: CoST v2, Section 2 cites Qu et al. (2024), TokenRec: https://arxiv.org/html/2404.14774v2#S2.p2; not compared in Tables 2-3.

[View all papers in this cell](../../README.md#i--tokenization)
