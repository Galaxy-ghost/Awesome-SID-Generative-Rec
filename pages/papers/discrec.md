# DiscRec

*Disentangled Semantic-Collaborative Modeling for Generative Recommendation* — Liu et al. · arXiv’25

`I. Informativeness` · `Backbone`

[Paper](https://arxiv.org/abs/2506.15576) · [Code](https://github.com/Ten-Mao/DiscRec) · [Matrix](../../README.md#i--backbone)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `RQ-VAE / Learn. RQ` | **`Enc-Dec`** | `Fixed / NTP` | `C-Beam` |

- `RQ-VAE / Learn. RQ`: Residual-quantized variational codes or learnable residual-quantization codes in different configurations.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

DiscRec adds item-level position embeddings and splits semantic and collaborative signals into two gated branches, one with attention inside each item, instead of fusing them in one embedding space.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | DiscRec adds item-level position embeddings and splits semantic and collaborative signals into two gated branches, one with attention inside each item, instead of fusing them in one embedding space. |
| Modified Stage | Backbone |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Review subsets Beauty, Musical Instruments, Arts, Toys; remove users/items with fewer than 5 interactions; keep latest 20 history items, padding shorter histories.
- **Split**: Main per-user chronological leave-one-out: most recent item test, second-most-recent validation, remaining interactions training. Additional Beauty user-level random split: train/validation/test 8:1:1, with all models retrained from scratch.
- **Candidates**: full catalog; reported full-ranking evaluation over the entire item set, with prefix-tree-constrained generation; history exclusion not reported.
- **Visibility**: warm; no unseen-item protocol is defined. Beauty additionally evaluates held-out users and low-popularity targets; LETTER uses pretrained SASRec embeddings, whose test-item exposure is not reported.
- **SID**: 4 RQ-VAE codebooks, 256 entries/level, 32 dimensions/entry, from LLaMA2-7B title/description representations. DiscRec-T uses TIGER tokenization; DiscRec-L uses LETTER collaborative/diversity regularization with pretrained SASRec embeddings. Tokenizer trained before recommender; collision handling not reported.
- **Inference budget**: Prefix-tree-constrained autoregressive decoding, beam 20; Recall/NDCG@5/10; inference hardware, batch size and measured latency not reported. The paper gives theoretical complexity rather than serving measurements.
- **Results from**: Own DiscRec-T/DiscRec-L comparisons, ablations and Beauty generalization studies. Baselines follow referenced implementations under a unified generative configuration; EAGER is resized to dimension 128 and its histories are correctly sorted chronologically. No copied baseline result scores stated; run counts/variance not reported.

<details>
<summary>Sources</summary>

- **Datasets**: [S4.SS1.SSS1.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS1.p1)
- **Split**: [S4.SS1.SSS1.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS1.p1) ; [S4.SS5.p2](https://arxiv.org/html/2506.15576v2#S4.SS5.p2)
- **Candidates**: [S4.SS1.SSS3.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS3.p1)
- **Visibility**: [S4.SS1.SSS1.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS1.p1) ; [S4.SS1.SSS4.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p1) ; [S4.SS5.p2](https://arxiv.org/html/2506.15576v2#S4.SS5.p2)
- **SID**: [S4.SS1.SSS4.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p1) ; [S4.SS1.SSS4.p2](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p2) ; [S3.SS2.p2](https://arxiv.org/html/2506.15576v2#S3.SS2.p2)
- **Inference budget**: [S4.SS1.SSS3.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS3.p1) ; [S3.SS3.p4](https://arxiv.org/html/2506.15576v2#S3.SS3.p4)
- **Results from**: [S4.SS1.SSS4.p1](https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p1) ; [S4.T2](https://arxiv.org/html/2506.15576v2#S4.T2) ; [S4.SS5.p2](https://arxiv.org/html/2506.15576v2#S4.SS5.p2)

</details>

### 5. Connections to Related Work

- **Predecessor** · [TIGER](tiger.md): DiscRec-T inserts disentangled modeling into TIGER.
  - Source: https://arxiv.org/html/2506.15576v2#S1.p5 ; https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p2
- **Predecessor** · [LETTER](letter.md): DiscRec-L uses LETTER's collaboratively regularized tokenizer.
  - Source: https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p1 ; https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p2
- **Competitor** · [EAGER](eager.md): Two-stream baseline compared with DiscRec's single-workflow disentanglement.
  - Source: https://arxiv.org/html/2506.15576v2#S4.SS1.SSS2.p2 ; https://arxiv.org/html/2506.15576v2#S4.SS1.SSS4.p1

[View all papers in this cell](../../README.md#i--backbone)
