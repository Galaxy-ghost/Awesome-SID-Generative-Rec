# DECOR

[← Problem × Stage Matrix](../../README.md#iii--backbone) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/decor.md)

| **Title** | *Learning Decomposed Contextual Token Representations from Pretrained and Collaborative Signals for Generative Recommendation* |
| :-- | :-- |
| **Authors** | Liu et al. |
| **Venue** | SIGIR’26 |
| **Problem × Stage** | `III. SID–Model Alignment` · `Backbone` |
| **Changes** | ● Backbone |
| **SID inputs** | `Text` |
| **Domain** | `E-commerce` |
| **Scenario** | `General Item Recommendation`; `Public Benchmarks` |
| **Links** | [Paper](https://arxiv.org/abs/2509.10468) · [Code](https://github.com/yliuaa/DECOR.git) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>● Enc-Dec"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: NTP"] --> I["Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text+CF`: Text representations combined with collaborative signals.
- `RQ-VAE`: Residual-Quantized Variational AutoEncoder.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Beam`: Autoregressive beam search over Semantic ID tokens.

### TL;DR

> [!NOTE]
> DECOR refines Semantic ID token embeddings by interaction context and fuses pretrained codebook embeddings with learned collaborative embeddings, instead of static token assignments that overwrite pretrained semantics.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Scientific, Instrument and Game (paper labels); user/item 5-core filtering; chronological histories capped at 20 items.
  - Source: Section 4.1.1 and Table 1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS1.p1) ; [S3.T1](https://arxiv.org/html/2509.10468v2#S3.T1)
- **Split**: Per-user chronological leave-one-out: last interaction test, penultimate validation, remaining interactions training.
  - Source: Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS1.p1)
- **Candidates**: full catalog; full-ranking evaluation without sampling.
  - Source: Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS1.p1)
- **Visibility**: warm; no unseen-item protocol is defined. RQ-VAE/text-encoder exposure to test items not reported; collaborative embeddings are learned from recommendation sequences.
  - Source: Sections 3.2/3.3/4.1 define no item holdout: [S3.SS2.p1](https://arxiv.org/html/2509.10468v2#S3.SS2.p1) ; [S3.SS3.p2](https://arxiv.org/html/2509.10468v2#S3.SS3.p2) ; [S4.SS1.SSS1.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS1.p1)
- **SID**: Sentence-T5 embeddings; frozen RQ-VAE with 3 levels x 256 entries, plus an incremental index token resolving identical 3-token prefixes: 4-token IDs. Token assignments remain fixed while embeddings are contextually composed and fused with learned collaborative embeddings.
  - Source: Sections 3.2/3.3/4.1.2: [S3.SS2.p2](https://arxiv.org/html/2509.10468v2#S3.SS2.p2) ; [S3.SS3.p2](https://arxiv.org/html/2509.10468v2#S3.SS3.p2) ; [S4.SS1.SSS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS2.p1)
- **Inference budget**: Beam 50; Recall/NDCG@5/10; experiments on one Tesla A40. Table 5 batches 8/16/32/64/128: DECOR 4.49-4.70 ms/sample, 213-223 samples/s; batch 128 adds 0.85 ms over TIGER. Prefix constraints not reported.
  - Source: Section 4.1.2/4.8 and Table 5: [S4.SS1.SSS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS2.p1) ; [S4.SS8.p1](https://arxiv.org/html/2509.10468v2#S4.SS8.p1) ; [S4.T5](https://arxiv.org/html/2509.10468v2#S4.T5)
- **Results from**: Original Table 2 test results use seed 2025; significance tested across five seeds. Generative baselines rerun from official code; other baselines adapted or quoted when protocols match. Table 5 measures inference cost; Figure 5 measures convergence, excluding ETEGRec tokenizer-update epochs.
  - Source: Sections 4.1.2/4.2/4.7 and Tables 2/5: [S4.SS1.SSS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS2.p1) ; [S4.SS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS2.p1) ; [S3.T2](https://arxiv.org/html/2509.10468v2#S3.T2) ; [S4.T5](https://arxiv.org/html/2509.10468v2#S4.T5) ; [S4.SS7.p1](https://arxiv.org/html/2509.10468v2#S4.SS7.p1)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["DECOR"]
    P -->|"predecessor"| A["TIGER"]
    P -->|"alternative"| B["ETEGRec"]
    P -->|"competitor"| C["LETTER"]
    P -->|"competitor"| D["CID"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **Predecessor** · [TIGER](tiger.md): DECOR augments TIGER's fixed tokenization with contextual token embeddings.
  - Source: DECOR v2, Sections 3.2/4.1.2 and Table 2: [S3.SS2.p1](https://arxiv.org/html/2509.10468v2#S3.SS2.p1) ; [S4.SS1.SSS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS1.SSS2.p1) ; [S3.T2](https://arxiv.org/html/2509.10468v2#S3.T2).
- **Alternative** · [ETEGRec](etegrec.md): DECOR adapts embeddings without ETEGRec's repeated re-tokenization.
  - Source: DECOR v2, Sections 3.4/4.7: [S3.SS4.p2](https://arxiv.org/html/2509.10468v2#S3.SS4.p2) ; [S4.SS7.p1](https://arxiv.org/html/2509.10468v2#S4.SS7.p1).
- **Competitor** · [LETTER](letter.md): LETTER is a tokenizer-enhancement baseline in the shared evaluation.
  - Source: DECOR v2, Sections 1/4.2 and Table 2: [S1.p6](https://arxiv.org/html/2509.10468v2#S1.p6) ; [S4.SS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS2.p1) ; [S3.T2](https://arxiv.org/html/2509.10468v2#S3.T2).
- **Competitor** · [CID](cid.md): P5-CID is a collaborative-indexing baseline.
  - Source: DECOR v2, Section 4.2 and Table 2: [S4.SS2.p1](https://arxiv.org/html/2509.10468v2#S4.SS2.p1) ; [S3.T2](https://arxiv.org/html/2509.10468v2#S3.T2).

[View all papers in this cell](../../README.md#iii--backbone)
