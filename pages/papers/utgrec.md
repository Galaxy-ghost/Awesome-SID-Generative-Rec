# UTGRec

*Universal Item Tokenization for Transferable Generative Recommendation* — Zheng et al. · arXiv’25

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2504.04405) · [Code](https://github.com/RUCAIBox/UTGRec) · [Matrix](../../README.md#vi--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Multi-Dom` | **`Tree`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

UTGRec builds a universal item tokenizer from a multimodal LLM with tree-structured codebooks, text and image reconstruction, and co-occurrence alignment, and pre-trains a generator that transfers across domains.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Key Contribution | UTGRec builds a universal item tokenizer from a multimodal LLM with tree-structured codebooks, text and image reconstruction, and co-occurrence alignment, and pre-trains a generator that transfers across domains. |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2023 with 5-core filtering. Pre-training on five domains (Arts Crafts and Sewing, Baby Products, CDs and Vinyl, Cell Phones and Accessories, Software; 999,334 users / 344,412 items in total); downstream on Musical Instruments (57,439 / 24,587), Industrial and Scientific (50,985 / 25,848), Video Games (94,762 / 25,612), Office Products (223,308 / 77,551).
- **Split**: Per-user leave-one-out: latest item for test, second most recent for validation, the rest for training; the tokenizer and recommender are pre-trained on the five source domains and fine-tuned on each downstream domain.
- **Candidates**: full catalog (full-ranking evaluation over the entire item set).
- **Visibility**: warm; no unseen-item protocol is defined (downstream items are seen during fine-tuning of both tokenizer and recommender).
- **SID**: Universal item tokenizer on Qwen2-VL-2B (LoRA) with tree-structured codebooks: root codebook 256 and leaf codebook 512, identifier length 3, shared across domains. Conflicts are resolved by reassigning the last-level code to the second-nearest or a farther code instead of appending an extra code.
- **Inference budget**: Beam size 50 for all generative recommenders; tokenizer pre-training on 16 GPUs (batch 16 per GPU). Inference hardware, batch size, and latency: not reported.
- **Results from**: Table 2 (four downstream domains versus traditional, content-based, and generative baselines including TIGER, LETTER, TIGER-M); Table 3 (ablations); later figures (analyses).

<details>
<summary>Sources</summary>

- **Datasets**: Pre-training and downstream domains, 5-core: [S3.SS1.SSS1.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS1.p1); statistics: [S3.T1](https://arxiv.org/html/2504.04405v3#S3.T1).
- **Split**: Leave-one-out allocation: [S3.SS1.SSS3.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS3.p1).
- **Candidates**: Full ranking and beam 50: [S3.SS1.SSS3.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS3.p1).
- **Visibility**: Downstream domains are fine-tuned on, no unseen-item protocol: [S3.SS1.SSS1.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS1.p1) and [S3.SS1.SSS4.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS4.p1).
- **SID**: Tree-structured codebooks (root 256, leaf 512), L=3, last-level reassignment for conflicts: [S3.SS1.SSS4.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS4.p1) and [S2.SS4.SSS1.p2](https://arxiv.org/html/2504.04405v3#S2.SS4.SSS1.p2); MLLM tokenizer: [S3.SS1.SSS4.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS4.p1).
- **Inference budget**: Beam size 50: [S3.SS1.SSS3.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS3.p1); GPUs for tokenizer pre-training: [S3.SS1.SSS4.p1](https://arxiv.org/html/2504.04405v3#S3.SS1.SSS4.p1).
- **Results from**: Main: [S3.T2](https://arxiv.org/html/2504.04405v3#S3.T2); ablation: [S3.T3](https://arxiv.org/html/2504.04405v3#S3.T3).

</details>

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER trains a domain-specific RQ-VAE on text embeddings and appends an extra code for conflicts; UTGRec learns one MLLM-based tree tokenizer across domains and reassigns conflicting last-level codes.
  - Source: UTGRec v3, baselines TIGER and TIGER-M: https://arxiv.org/html/2504.04405v3#S3.SS1.SSS2.p14 and https://arxiv.org/html/2504.04405v3#S3.SS1.SSS2.p16; conflict handling: https://arxiv.org/html/2504.04405v3#S2.SS4.SSS1.p2; Table 2: https://arxiv.org/html/2504.04405v3#S3.T2.
- **Competitor** · [LETTER](letter.md): LETTER regularizes RQ-VAE with collaborative and diversity terms per domain; UTGRec injects collaborative knowledge through co-occurring item alignment in a universal tokenizer.
  - Source: UTGRec v3, baselines: https://arxiv.org/html/2504.04405v3#S3.SS1.SSS2.p15; Table 2: https://arxiv.org/html/2504.04405v3#S3.T2.
- **Competitor** · [VQ-Rec](vq-rec.md): VQ-Rec transfers text codes across domains for discriminative sequence modeling; UTGRec transfers a generative tokenizer and recommender across domains.
  - Source: UTGRec v3, content-based baselines: https://arxiv.org/html/2504.04405v3#S3.SS1.SSS2.p11; Table 2: https://arxiv.org/html/2504.04405v3#S3.T2.
- **Alternative** · [GenCDR](gencdr.md): GenCDR later cites UTGRec as single-domain-oriented tokenization and adds domain-specific adapters and routing for cross-domain generation.
  - Source: Evidence is from the later GenCDR paper, Related Work: https://arxiv.org/html/2511.08006v2#Sx2.p2.

[View all papers in this cell](../../README.md#vi--tokenization)
