# AdaSID

*Beyond Static Collision Handling: Adaptive Semantic ID Learning for Multimodal Recommendation at Industrial Scale* — Pan et al. · arXiv’26

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2604.23522) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`RQ`** | `Dec-Only` | `Fixed / NTP` | `C-Beam` |

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Offline: Amazon 2018 Reviews, Beauty and Toys and Games, with 5-core filtering of users and items. Sizes (users / items / interactions): Toys 19,412 / 11,924 / 905,253; Beauty 22,363 / 12,101 / 1,048,296. Industrial: Kuaishou e-commerce short-video items with multimodal features (images, text, keyframes, audio transcripts); filtering rules not reported.
  - Source: Amazon 2018 categories, 5-core filtering, leave-one-out: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS1.p1; sizes: https://arxiv.org/html/2604.23522v1#S5.T1; industrial setting: https://arxiv.org/html/2604.23522v1#S5.SS3.p1.
- **Split**: Offline: leave-one-out into training, validation, and test; the exact validation/test position allocation is not reported beyond the leave-one-out label. Industrial: 4-day online A/B test on the retrieval model and a 4-day offline study on the ranking model.
  - Source: Leave-one-out named without position allocation: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS1.p1; industrial test periods: https://arxiv.org/html/2604.23522v1#S5.SS3.p1.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates).
  - Source: Metrics and backbone only: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS2.p1.
- **Visibility**: Offline: warm; no unseen-item protocol is defined. Industrial ranking reports a cold-start CVR subset; generator/tokenizer visibility for those items is not reported.
  - Source: Offline protocol: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS1.p1; industrial cold-start CVR subset without a visibility definition: https://arxiv.org/html/2604.23522v1#S5.T3 and https://arxiv.org/html/2604.23522v1#S5.I2.i2.p1.
- **SID**: 3 residual-quantization levels x 256 codes, 32-dimensional code embeddings, 768-dimensional input features. Collisions are reduced during tokenizer training by an adaptive overlap-repulsion loss; a post-hoc disambiguation suffix or other collision-resolution rule is not reported.
  - Source: SID length 3, 256 codes, 32-dimensional code embeddings: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS4.p1; collision handled by a training-time adaptive overlap loss, with no added suffix described: https://arxiv.org/html/2604.23522v1#S4.SS4.p1 and https://arxiv.org/html/2604.23522v1#S4.SS4.p2.
- **Inference budget**: Downstream generation uses the same TIGER configuration for all tokenizers; beam width, hardware, inference batch size, and latency: not reported. Recall and NDCG at K=3 and 5.
  - Source: Downstream TIGER configuration only: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS2.p1 and https://arxiv.org/html/2604.23522v1#S5.SS1.SSS4.p1; no extra online cost claim: https://arxiv.org/html/2604.23522v1#S4.SS4.p2.
- **Results from**: Table 2 (tokenizer comparison on Toys and Beauty under a shared TIGER backbone); Table 3 (Kuaishou online retrieval A/B and offline ranking AUC); Table 4 (ablations); Figure 3 (codebook statistics); Figure 4 (hyperparameter sensitivity on Beauty).
  - Source: Main offline table: https://arxiv.org/html/2604.23522v1#S5.T2; industrial table: https://arxiv.org/html/2604.23522v1#S5.T3; ablation: https://arxiv.org/html/2604.23522v1#S5.T4; codebook statistics: https://arxiv.org/html/2604.23522v1#S5.F3.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

按碰撞情况自适应地学习多模态 SID，替代静态的碰撞处理。

### 5. Connections to Related Work

- **Predecessor** · [QuaSID](quasid.md): QuaSID applies a fixed qualification-aware collision regularizer; AdaSID instantiates its collision term following QuaSID and makes the repulsion adaptive to semantic compatibility, local load, and training progress.
  - Source: AdaSID v1, Section 4.1 follows Hu et al. (2026) for the collision term: https://arxiv.org/html/2604.23522v1#S4.SS1.p2; QuaSID is the collision-aware baseline in Section 5.1.3 and Table 2: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS3.p1 and https://arxiv.org/html/2604.23522v1#S5.T2.
- **Predecessor** · [TIGER](tiger.md): TIGER is the shared downstream generative backbone; AdaSID changes only how the SIDs are learned.
  - Source: AdaSID v1, Section 5.1.2: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS2.p1; Section 5.1.4: https://arxiv.org/html/2604.23522v1#S5.SS1.SSS4.p1.
- **Alternative** · [HiD-VAE](hid-vae.md): HiD-VAE suppresses SID overlaps with an explicit objective under a fixed standard, while AdaSID relaxes or strengthens repulsion adaptively.
  - Source: AdaSID v1, Section 1 and Section 2.2 cite Fang et al. (2025) among static overlap-aware objectives: https://arxiv.org/html/2604.23522v1#S1.p3 and https://arxiv.org/html/2604.23522v1#S2.SS2.p1; not a baseline in Table 2.
- **Alternative** · [ETEGRec](etegrec.md): ETEGRec aligns the tokenizer with downstream recommendation through end-to-end supervision, whereas AdaSID keeps a pre-trained tokenizer and regulates code overlaps adaptively.
  - Source: AdaSID v1, Section 2.2 cites Liu et al. (2025) for end-to-end downstream supervision: https://arxiv.org/html/2604.23522v1#S2.SS2.p1; not a baseline in Table 2.

[View all papers in this cell](../../README.md#ii--tokenization)
