# TRACER

*Token ReAssignment for Concept ERasure in Generative Recommendation* — Chen et al. · NeurIPS’26

`IV. Utility` · `Tokenization`

[Paper](https://arxiv.org/abs/2606.07688) · [Matrix](../../README.md#iv--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Soft Reassign. RQ`** | `Dec-Only / Enc-Dec` | `Joint / NTP + Aux.` | `Beam` |

- `Soft Reassign. RQ`: Residual quantization with differentiable soft code reassignment.
- `Dec-Only / Enc-Dec`: Decoder-only and encoder–decoder backbone variants.
- `Joint`: The generator loss updates the tokenizer directly.
- `NTP + Aux.`: NTP plus another auxiliary loss.

### TL;DR

TRACER removes sensitive concepts from a generative recommender by reassigning concept-related items to alternative Semantic ID tokens with a coherence regularizer, instead of suppressing tokens shared with retained items.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Key Contribution | TRACER removes sensitive concepts from a generative recommender by reassigning concept-related items to alternative Semantic ID tokens with a coherence regularizer, instead of suppressing tokens shared with retained items. |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Industrial & Scientific, Sports & Outdoors and Toys & Games; remove users/items with fewer than five interactions. Amazon release year: not reported. Randomly select 5% of brands for forgetting, covering approximately 10% of interactions.
- **Split**: Chronological 80/10/10 train/validation/test. Per-user versus global allocation and history cap: not reported.
- **Candidates**: not reported; full-catalog versus sampled ranking and history-item exclusion are unspecified.
- **Visibility**: warm; no unseen-item protocol is defined. Forgetting targets training-data influence; tokenizer exposure to held-out items/interactions: not reported.
- **SID**: All backbones use three RQ-VAE levels x 256 codes, embedding dimension 64. TRACER learns soft-assignment perturbations for target-concept items while preserving other items' original SIDs. Collision handling: not reported.
- **Inference budget**: Beam search width 10; retain/forget HR and NDCG@5/10, MRR, and description-based semantic similarity. Experiments use 4x A100 GPUs. Inference batch, latency and throughput: not reported. Batch128 and 19-27 minutes concern unlearning training, not inference.
- **Results from**: This paper's unlearning comparisons: main MOR/MiniOneRec and LETTER results on Scientific/Sports; Appendix D Tables1-3 cover five backbones x three datasets, Table4 unlearning time, Table5 item-level forgetting. ELM/RMU/RepNoise/FLAT/BLUR/PISCES baselines start from the same SFT checkpoint with tuned learning rates; five-run averages. No borrowed baseline-score source is identified.

<details>
<summary>Sources</summary>

- **Datasets**: Sec.4 datasets/preprocessing and concept setup: [S4.SS0.SSS0.Px1.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px1.p1) and [S4.SS0.SSS0.Px2.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px2.p1)
- **Split**: Sec.4 datasets/preprocessing: [S4.SS0.SSS0.Px1.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px1.p1)
- **Candidates**: Evaluation metrics and Appendix D.1 do not specify catalog/sampling protocol: [S4.SS0.SSS0.Px6.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px6.p1) and [A4.SS1.p1](https://arxiv.org/html/2606.07688v1#A4.SS1.p1)
- **Visibility**: Forget set comprises previously trained interactions, not an unseen-item evaluation: [S2.SS2.p1](https://arxiv.org/html/2606.07688v1#S2.SS2.p1) and [S4.SS0.SSS0.Px2.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px2.p1)
- **SID**: Appendix D.1 and Sec.3.1: [A4.SS1.p1](https://arxiv.org/html/2606.07688v1#A4.SS1.p1) and [S3.SS1.p2](https://arxiv.org/html/2606.07688v1#S3.SS1.p2)
- **Inference budget**: Appendix D.1-D.3: [A4.SS1.p1](https://arxiv.org/html/2606.07688v1#A4.SS1.p1) and [A4.SS2.p1](https://arxiv.org/html/2606.07688v1#A4.SS2.p1) and [A4.SS3.p1](https://arxiv.org/html/2606.07688v1#A4.SS3.p1)
- **Results from**: Sec.4 models/baselines and Appendix D.1/D.2/D.4: [S4.SS0.SSS0.Px3.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px3.p1) and [S4.SS0.SSS0.Px5.p1](https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px5.p1) and [A4.SS1.p1](https://arxiv.org/html/2606.07688v1#A4.SS1.p1) and [A4.SS2.p1](https://arxiv.org/html/2606.07688v1#A4.SS2.p1) and [A4.SS4.p1](https://arxiv.org/html/2606.07688v1#A4.SS4.p1)

</details>

### 5. Connections to Related Work

- **Predecessor** · [MiniOneRec](minionerec.md): MiniOneRec supplies the Qwen2.5-7B backbone for unlearning.
  - Source: TRACER v1, Sec.4 Models/Backbones: https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px3.p1; https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px4.p1.
- **Predecessor** · [TIGER](tiger.md): TIGER is a tested separate-training backbone.
  - Source: TRACER v1, Sec.4 Models and Appendix D.2: https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px3.p1; https://arxiv.org/html/2606.07688v1#A4.SS2.p1.
- **Predecessor** · [LETTER](letter.md): LETTER supplies a tested joint-training backbone and the motivating retraining analysis.
  - Source: TRACER v1, Sec.3 motivation and Sec.4 Models: https://arxiv.org/html/2606.07688v1#S3.SS0.SSS0.Px1.p1; https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px3.p1.
- **Predecessor** · [ETEGRec](etegrec.md): ETEGRec is a tested joint-training backbone.
  - Source: TRACER v1, Sec.4 Models and Appendix D.2: https://arxiv.org/html/2606.07688v1#S4.SS0.SSS0.Px3.p1; https://arxiv.org/html/2606.07688v1#A4.SS2.p1.

[View all papers in this cell](../../README.md#iv--tokenization)
