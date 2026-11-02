# PSRQ

*Progressive Semantic Residual Quantization for Multimodal-Joint Interest Modeling in Music Recommendation* — Wang et al. · CIKM’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2508.20359) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`Prog. RQ`** | `Encoder` | `Fixed / Discrim.` | `Scoring` |

- `Prog. RQ`: Progressive RQ variant.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### TL;DR

PSRQ generates modality-specific and modality-joint Semantic IDs that preserve prefix semantic features and models music interests with multi-codebook cross-attention, to reduce semantic drift in residual quantization.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | PSRQ generates modality-specific and modality-joint Semantic IDs that preserve prefix semantic features and models music interests with multi-codebook cross-attention, to reduce semantic drift in residual quantization. |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Baby (81,423 users / 33,652 items; ratings of 4 or more are positives), an industrial music-streaming dataset from one week of logs (4,926,656 users / 1,387,247 songs; collections are positives, played-but-not-collected are negatives), and Music4all (14,127 users / 99,596 songs; repeated plays are positives). Items with fewer than 30 interactions are marked cold-start. Further filtering: not reported.
  - Source: Datasets and labels: https://arxiv.org/html/2508.20359v1#S5.SS1.SSS1.p1, https://arxiv.org/html/2508.20359v1#S5.I2.i1.p1, https://arxiv.org/html/2508.20359v1#S5.I2.i2.p1, https://arxiv.org/html/2508.20359v1#S5.I2.i3.p1; statistics: https://arxiv.org/html/2508.20359v1#S5.T1.
- **Split**: not reported (sequences are built by timestamp and trained for one epoch, but the train/test division is not described). Online: A/B test in February 2025 on the music platform against a DLRM ranker.
  - Source: Timestamp-ordered sequences, no split rule: https://arxiv.org/html/2508.20359v1#S5.I2.i1.p1 and https://arxiv.org/html/2508.20359v1#S5.SS1.SSS2.p1; online test: https://arxiv.org/html/2508.20359v1#S5.SS3.p1.
- **Candidates**: n/a for ranking candidates: evaluation is pointwise AUC and Logloss on labeled positive and negative samples; how negatives relate to user history is defined by the labels above.
  - Source: Pointwise AUC on labeled samples: https://arxiv.org/html/2508.20359v1#S5.SS1.SSS3.p1.
- **Visibility**: warm; no unseen-item protocol is defined. 'Cold AUC' covers items with fewer than 30 interactions, which are low-frequency, not unseen.
  - Source: Cold-start = fewer than 30 interactions, not unseen: https://arxiv.org/html/2508.20359v1#S5.SS1.SSS1.p1.
- **SID**: Progressive Semantic Residual Quantization (PSRQ): layer-wise K-means over modality embeddings (text, image or audio) that preserves the prefix semantic feature, producing modal-specific and modal-joint semantic IDs; clusters per layer k = 64 (Amazon Baby), 256 (Industrial), 128 (Music4all), 3 layers. Collision handling: not reported.
  - Source: Clusters k and layers l per dataset: https://arxiv.org/html/2508.20359v1#S5.SS1.SSS2.p1; PSRQ name and modal-specific/modal-joint IDs: https://arxiv.org/html/2508.20359v1#abstract1 and https://arxiv.org/html/2508.20359v1#S4.SS1.p1.
- **Inference budget**: n/a for generation (SIDs feed a DIN-style ranker with cross-attention, MCCA). MLLM feature extractors run on NVIDIA A100 GPUs; ranker inference batch size and latency: not reported.
  - Source: Discriminative ranker, hardware for feature extraction: https://arxiv.org/html/2508.20359v1#S5.SS1.SSS2.p1.
- **Results from**: Table 2 (All AUC, Cold AUC, Logloss versus multimodal and quantization-based rankers); Table 3 (quantizers added to DIN with text only); Table 4 (MCCA ablation); Section 5.3 (online A/B: collect +2.81%, full play +0.95%).
  - Source: Main: https://arxiv.org/html/2508.20359v1#S5.T2; quantizers in DIN: https://arxiv.org/html/2508.20359v1#S5.T3; ablation: https://arxiv.org/html/2508.20359v1#S5.T4; online: https://arxiv.org/html/2508.20359v1#S5.SS3.p1.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

SID 只作音乐推荐排序模型的特征，按 AUC 评估，不生成 SID。

### 5. Connections to Related Work

- **Alternative** · [TIGER](tiger.md): TIGER introduced RQ-VAE semantic IDs for generative retrieval; PSRQ quantizes multimodal embeddings with progressive semantic residual K-means and uses the IDs as ranking features for cold-start items.
  - Source: PSRQ v1, Section 1 and Section 2.2 cite Rajput et al. (2023): https://arxiv.org/html/2508.20359v1#S1.p3 and https://arxiv.org/html/2508.20359v1#S2.SS2.p1; RQ-VAE is a quantizer baseline in Table 3: https://arxiv.org/html/2508.20359v1#S5.T3.
- **Alternative** · [VQ-Rec](vq-rec.md): VQ-Rec framed vector quantization for transferable recommenders; PSRQ adds modal-specific and modal-joint codebooks for multimodal cold-start ranking.
  - Source: PSRQ v1, Section 1 and Section 2.2: https://arxiv.org/html/2508.20359v1#S1.p3 and https://arxiv.org/html/2508.20359v1#S2.SS2.p1.
- **Alternative** · [OneRec](onerec.md): OneRec uses residual K-means SIDs inside an end-to-end generator; PSRQ keeps a discriminative ranker and feeds it multimodal SID embeddings.
  - Source: PSRQ v1, contribution list and Section 2.2 cite OneRec: https://arxiv.org/html/2508.20359v1#S1.I1.i2.p1 and https://arxiv.org/html/2508.20359v1#S2.SS2.p1.

[View all papers in this cell](../../README.md#i--tokenization)
