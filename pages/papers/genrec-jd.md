# GenRec-JD

*GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation* — Zou et al. · SIGIR’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2604.14878) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | **`Fixed / NTP → RL`** | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### TL;DR

GenRec-JD trains a decoder-only generator with page-wise next-token prediction, compresses prompt Semantic IDs with a Token Merger, and aligns outputs with GRPO-SR under hybrid rewards.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Key Contribution | GenRec-JD trains a decoder-only generator with page-wise next-token prediction, compresses prompt Semantic IDs with a Token Merger, and aligns outputs with GRPO-SR under hybrid rewards. |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: JD.com large-scale recommender platform: about 560 million user interaction sequences over one month. Filtering rules and catalog size: not reported.
  - Source: JD.com data scope: https://arxiv.org/html/2604.14878v1#S3.SS1.p1.
- **Split**: Temporal: the last day for testing, the remaining days for training; a validation split is not reported. Online: 10% of traffic per variant for one month on JD's homepage feed.
  - Source: Last-day test split: https://arxiv.org/html/2604.14878v1#S3.SS1.p1; online test: https://arxiv.org/html/2604.14878v1#S3.SS3.p1.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); HR and NDCG at K=1, 10, 50 over beam-search outputs, plus the share of invalid SIDs.
  - Source: Metrics only, including the hallucination rate: https://arxiv.org/html/2604.14878v1#S3.SS1.p1.
- **Visibility**: warm; no unseen-item protocol is defined. Online results report long-tail item gains without a visibility definition.
  - Source: Next-day temporal test with no unseen-item protocol: https://arxiv.org/html/2604.14878v1#S3.SS1.p1; long-tail items are analyzed online only: https://arxiv.org/html/2604.14878v1#S3.SS3.p1.
- **SID**: 3-level RQ K-means over Qwen2.5-VL multimodal embeddings fine-tuned on domain collaborative pairs; codebook size per level: not reported. A linear token merger compresses each SID triplet into one input vector in the prompt. Collision handling: not reported; generated invalid SIDs are measured (HaR 4.96% for GenRec).
  - Source: Qwen2.5-VL embeddings fine-tuned on collaborative pairs, RQ K-means triplets: https://arxiv.org/html/2604.14878v1#S2.SS1.p2; token merger: https://arxiv.org/html/2604.14878v1#S2.SS2.SSS0.Px3.p1.
- **Inference budget**: Point-wise beam search returning beam-width items per query; numerical beam width not reported. Qwen2.5 decoder-only backbones of 1.5B, 3B, and 7B; training on 8 NVIDIA H100 GPUs; inference hardware, batch size, and latency: not reported.
  - Source: Point-wise beam search at serving: https://arxiv.org/html/2604.14878v1#S2.SS2.SSS0.Px2.p1; hardware: https://arxiv.org/html/2604.14878v1#S3.SS1.p1.
- **Results from**: Table 1 (page-wise SFT versus BERT4Rec, SASRec, TIGER, LC-Rec, with hallucination rate); Table 2 (model scaling); Table 3 (GRPO-SR and reward variants); Table 4 (one-month online A/B test).
  - Source: SFT table: https://arxiv.org/html/2604.14878v1#S3.T1; scaling: https://arxiv.org/html/2604.14878v1#S3.T2; RL: https://arxiv.org/html/2604.14878v1#S3.T3; online: https://arxiv.org/html/2604.14878v1#S3.T4.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

按页做下一 token 预测，压缩输入侧的多 token SID，并做偏好对齐。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER is trained with point-wise next-item prediction; GenRec trains on page-wise target lists with a decoder-only LLM and aligns it with GRPO-SR.
  - Source: GenRec v1, Section 3.1 baselines: https://arxiv.org/html/2604.14878v1#S3.SS1.p1; Table 1: https://arxiv.org/html/2604.14878v1#S3.T1.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec also fine-tunes an LLM on SIDs but with point-wise NTP; GenRec adds page-wise supervision, a token merger, and RL alignment.
  - Source: GenRec v1, Section 3.1 baselines: https://arxiv.org/html/2604.14878v1#S3.SS1.p1; Table 1: https://arxiv.org/html/2604.14878v1#S3.T1.
- **Alternative** · [LETTER](letter.md): LETTER improves the tokenizer, whereas GenRec keeps RQ K-means SIDs and changes the supervision and alignment of the generator.
  - Source: GenRec v1, Section 4 cites Wang et al. (2025), LETTER: https://arxiv.org/html/2604.14878v1#S4.p1; not a baseline in Table 1.

[View all papers in this cell](../../README.md#iv--training)
