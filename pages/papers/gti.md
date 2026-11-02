# GTI

*Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation* — Chen et al. · arXiv’26

`III. SID–Model Alignment` · `Training`

[Paper](https://arxiv.org/abs/2604.02324) · [Matrix](../../README.md#iii--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF / Text` | `RQ-VAE` | `Dec-Only` | **`Fixed / Multi-task NTP`** | `–` |

- `Text+CF / Text`: Text with collaborative signals, or text-only representations, in different configurations.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `–`: Not reported in the paper.

### TL;DR

GTI maps new Semantic ID tokens to distinct locations in the pretrained embedding space with paired linguistic supervision before fine-tuning, instead of initializing them as the mean of existing embeddings.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Key Contribution | GTI maps new Semantic ID tokens to distinct locations in the pretrained embedding space with paired linguistic supervision before fine-tuning, instead of initializing them as the mean of existing embeddings. |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Industrial recruitment pairs (good matches for SFT; profiles require at least one listed attribute); Vibrent rentals; other filtering not reported.
  - Source: https://arxiv.org/html/2604.02324v1#S7.SS1
- **Split**: Vibrent: leave-one-out; validation details not reported. Industry: 200 evaluation jobs; train/test separation not reported.
  - Source: https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px3.p1
- **Candidates**: not reported; 200 retrieved candidates per industrial query does not specify the evaluation universe.
  - Source: https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px3.p1 (200 retrieved candidates is an output count, not a negative-sampling protocol).
- **Visibility**: warm; no unseen-item protocol is defined. Industrial Mistral-E5 uses engagement supervision; test-candidate exposure not reported.
  - Source: https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px4.p2 and #S4.SS1.SSS0.Px4.p3
- **SID**: RQ-VAE SIDs from 1024-d embeddings. Industry: engagement-tuned Mistral-E5 embeddings, 3 x 8192. Vibrent: Qwen3-Embedding-0.6B embeddings, 4 x 256 with 32-d codes and the Wang et al. (2024) diversity regularizer for balanced codebook use. The appendix's 4 x 256 configuration additionally uses final-layer Sinkhorn-Knopp balancing to reduce collisions; residual collision resolution is not reported.
  - Source: https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px4.p2 ; https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px4.p3 ; https://arxiv.org/html/2604.02324v1#S7.SS3.p2
- **Inference budget**: K=5/10/20/50/100. Experiments use four H100s; inference-specific hardware, beam width, batch size and latency not reported.
  - Source: https://arxiv.org/html/2604.02324v1#S4.T1 ; #S4.T3 ; #S4.SS1.SSS0.Px4.p1
- **Results from**: Original experiments: Tables 1-2 industrial relative gains; Table 3 Vibrent relative gains; Table 4 absolute metrics.
  - Source: https://arxiv.org/html/2604.02324v1#S4.T1 ; #S4.T2 ; #S4.T3 ; #S7.T4

### 5. Connections to Related Work

- **Predecessor** · [TIGER](tiger.md): GTI adopts TIGER-style RQ-VAE semantic identifiers.
  - Source: https://arxiv.org/html/2604.02324v1#S7.SS3.p2 (Appendix 7.3).
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec uses multi-task alignment; GTI adds grounding before fine-tuning.
  - Source: https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px2.p3 ; #S4.T1 ; #S7.T4.

[View all papers in this cell](../../README.md#iii--training)
