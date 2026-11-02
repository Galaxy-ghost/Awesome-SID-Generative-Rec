# Q-BERT4Rec

*Quantized Semantic-ID Representation Learning for Multimodal Recommendation* — Huang and Gai · arXiv’25

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2512.02474) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img+CF`** | `RQ-VAE` | `Encoder (Non-AR)` | `Fixed / Masked` | `Non-AR` |

- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Masked`: Masks part of the codes and reconstructs them (includes masked diffusion).

### TL;DR

Q-BERT4Rec fuses text, image, and structural features into item embeddings, quantizes them into Semantic ID tokens by residual vector quantization, and pre-trains a bidirectional encoder with several masking strategies.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | Q-BERT4Rec fuses text, image, and structural features into item embeddings, quantizes them into Semantic ID tokens by residual vector quantization, and pre-trains a bidirectional encoder with several masking strategies. |
| Modified Stage | Representation |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Reviews 2018: pre-training on six source domains (Pet, Cell, Automotive, Tools, Toys, Sports) and fine-tuning on Musical Instruments, Arts Crafts and Sewing, Video Games (same statistics table as MQL4GRec). Filtering rules: not restated.
- **Split**: Leave-one-out: most recent interaction for test, second most recent for validation, the rest for training.
- **Candidates**: not reported explicitly; at inference the masked last position is filled with the most probable semantic ID over the item set (HR and NDCG at 1, 5, 10).
- **Visibility**: warm; no unseen-item protocol is defined.
- **SID**: 4-level RQ-VAE x 256 codewords (dimension 32) over LLaMA text and CLIP-ViT image features fused by a cross-modal semantic injection module. Collisions are resolved by MQL4GRec's distance-based token reallocation.
- **Inference budget**: Bidirectional masked prediction of the last position (no beam search); 4-layer Transformer encoder. NVIDIA RTX 4090 GPUs (four for pre-training, one for fine-tuning). Table 6 reports per-sample inference latency of about 2.66-2.67 ms with under 6M parameters.
- **Results from**: Table 2 (Instruments, Arts, Games versus traditional, Transformer, multimodal, prompt-LLM, and semantic-ID baselines); Tables 3-4 (modalities and pre-training strategies); Figures 3-5 (layers, mask ratio, dropout); Table 6 (complexity and latency).

<details>
<summary>Sources</summary>

- **Datasets**: Source and target domains: [S4.SS1.p1](https://arxiv.org/html/2512.02474v2#S4.SS1.p1), [S4.SS1.p2](https://arxiv.org/html/2512.02474v2#S4.SS1.p2), [S4.SS1.p3](https://arxiv.org/html/2512.02474v2#S4.SS1.p3); statistics: [S3.T1](https://arxiv.org/html/2512.02474v2#S3.T1).
- **Split**: Leave-one-out allocation: [S4.SS1.p4](https://arxiv.org/html/2512.02474v2#S4.SS1.p4).
- **Candidates**: Argmax over item semantic IDs: [S3.SS6.p2](https://arxiv.org/html/2512.02474v2#S3.SS6.p2); metrics: [S4.SS1.p4](https://arxiv.org/html/2512.02474v2#S4.SS1.p4).
- **Visibility**: Standard split with no unseen-item protocol: [S4.SS1.p4](https://arxiv.org/html/2512.02474v2#S4.SS1.p4).
- **SID**: 4 levels x 256 x 32, MQL4GRec reallocation for collisions: [S4.SS1.p6](https://arxiv.org/html/2512.02474v2#S4.SS1.p6) and [S3.SS4.p7](https://arxiv.org/html/2512.02474v2#S3.SS4.p7).
- **Inference budget**: Masked prediction at inference: [S3.SS6.p2](https://arxiv.org/html/2512.02474v2#S3.SS6.p2); hardware: [S4.SS1.p8](https://arxiv.org/html/2512.02474v2#S4.SS1.p8); latency: [A2.T6](https://arxiv.org/html/2512.02474v2#A2.T6).
- **Results from**: Main: [S3.T2](https://arxiv.org/html/2512.02474v2#S3.T2); ablations: [S3.T3](https://arxiv.org/html/2512.02474v2#S3.T3) and [S4.T4](https://arxiv.org/html/2512.02474v2#S4.T4); sensitivity: [S4.SS4.p1](https://arxiv.org/html/2512.02474v2#S4.SS4.p1); complexity: [A2.T6](https://arxiv.org/html/2512.02474v2#A2.T6).

</details>

### 5. Connections to Related Work

- **Competitor** · [MQL4GRec](mql4grec.md): MQL4GRec generates multimodal quantitative language autoregressively; Q-BERT4Rec reuses its collision reallocation but fuses modalities before quantization and predicts masked SIDs bidirectionally.
  - Source: Q-BERT4Rec v2, collision handling follows Zhai et al. (2025): https://arxiv.org/html/2512.02474v2#S3.SS4.p7; Table 2 baseline: https://arxiv.org/html/2512.02474v2#S3.T2.
- **Competitor** · [TIGER](tiger.md): TIGER decodes SIDs left to right with an encoder-decoder; Q-BERT4Rec uses a BERT-style encoder with multi-mask pre-training.
  - Source: Q-BERT4Rec v2, Table 2 semantic-ID baseline: https://arxiv.org/html/2512.02474v2#S3.T2; Appendix A baselines: https://arxiv.org/html/2512.02474v2#A1.I5.i1.p1.
- **Competitor** · [VQ-Rec](vq-rec.md): VQ-Rec uses product-quantized text codes for transfer; Q-BERT4Rec quantizes fused text-image features with RQ-VAE and pre-trains on six source domains.
  - Source: Q-BERT4Rec v2, Table 2 VQ/multimodal baseline: https://arxiv.org/html/2512.02474v2#S3.T2.
- **Competitor** · [CID](cid.md): P5-CID uses collaborative IDs in a prompt-based LLM; Q-BERT4Rec uses multimodal semantic IDs in a small masked Transformer.
  - Source: Q-BERT4Rec v2, Table 2 prompt-LLM baseline: https://arxiv.org/html/2512.02474v2#S3.T2; Appendix A: https://arxiv.org/html/2512.02474v2#A1.I4.i1.p1.

[View all papers in this cell](../../README.md#i--representation)
