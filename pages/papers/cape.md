# CAPE

*Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval and Ranking* — Huang et al. · arXiv’26

`I. Informativeness` · `Inference`

[Paper](https://arxiv.org/abs/2610.29298) · [Matrix](../../README.md#i--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE†` | `Dec-Only / Enc-Dec` | `Fixed / Multi-task NTP† / NTP†` | **`Hybrid`** |

- `Dec-Only / Enc-Dec`: Decoder-only and encoder–decoder backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP† / NTP†`: Inferred multi-task or single-task next-token-prediction initialization in different backbones.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Inference |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Industrial & Scientific, Office Products and Beauty (5-core), plus LastFM-1K (987 users, 40429 tracks). LastFM filtering thresholds: not reported. Histories contain the latest ten items.
  - Source: Sec.5.1 and Appendix B: https://arxiv.org/html/2610.29298v1#S5.SS1.p2 and https://arxiv.org/html/2610.29298v1#A2.p1
- **Split**: I&S/Office: chronological 80/10/10; per-user versus global allocation not reported. LastFM/Beauty: last user interaction test, penultimate validation, earlier interactions training.
  - Source: Sec.5.1 and Appendix B: https://arxiv.org/html/2610.29298v1#S5.SS1.p2 and https://arxiv.org/html/2610.29298v1#A2.p1
- **Candidates**: Reported ranking pool: 75 retrieved items, comprising 50 beam outputs plus the 25 highest-co-occurrence tail items outside the beam; not a sampled-negative pool. Full-catalog versus sampled-negative evaluation label and history-item exclusion: not reported. Tail metrics count all tail test cases, including unretrieved targets.
  - Source: Sec.4.1, Sec.2.1 and Appendix B: https://arxiv.org/html/2610.29298v1#S4.SS1.p1 and https://arxiv.org/html/2610.29298v1#S2.SS1.p2 and https://arxiv.org/html/2610.29298v1#A2.p3
- **Visibility**: warm; no unseen-item protocol is defined. Tail is the bottom 80% by training frequency. Frequency, tail partition and user/event co-occurrence matrices use training data only; tokenizer exposure to test items: not reported.
  - Source: Sec.2.1 and Appendix B: https://arxiv.org/html/2610.29298v1#S2.SS1.p2 and https://arxiv.org/html/2610.29298v1#A2.p1
- **SID**: Inherited frozen backbone identifiers: three tokens/item, with a fourth collision-resolution token for a small number of LastFM items. TIGER uses residual-quantized identifiers. Numerical codebook sizes and MiniOneRec tokenizer construction: not reported. CAPE leaves tokenization unchanged.
  - Source: Sec.5.1 and Appendix B: https://arxiv.org/html/2610.29298v1#S5.SS1.p1 and https://arxiv.org/html/2610.29298v1#A2.p2
- **Inference budget**: Beam50 +25 co-occurrence tail candidates, one batched teacher-forcing pass, calibrated ranking with fixed top1; HR/NDCG@5/10. Validation-selected lambda=0.5 on I&S/Office and 5 on LastFM. FP32 on one A40; full-request means over first128 test users: 1.20s I&S, 1.22s Office, 1.55s LastFM-MiniOneRec, 0.19s LastFM-TIGER. Timing includes input preparation, beam, retrieval, teacher forcing, evidence and ranking after two-user warm-up; one-time loading takes 5-16s separately. Request batch size: not reported.
  - Source: Sec.4.1/4.3, Sec.5.1, Table4 and Appendix B: https://arxiv.org/html/2610.29298v1#S4.SS1.p3 and https://arxiv.org/html/2610.29298v1#S4.SS3.p2 and https://arxiv.org/html/2610.29298v1#S5.SS1.p1 and https://arxiv.org/html/2610.29298v1#S5.T4 and https://arxiv.org/html/2610.29298v1#A2.p4 and https://arxiv.org/html/2610.29298v1#A2.T7 and https://arxiv.org/html/2610.29298v1#S5.SS1.p4
- **Results from**: Paper's frozen-checkpoint inference comparisons/ablations. Released Amazon MiniOneRec checkpoints; LastFM continues SFT from that checkpoint; TIGER is trained from scratch with seeds42/43/44. Table2 main comparisons; Table3 Amazon TIGER evaluated after CAPE was frozen. Re-rankers share the 75-item pool/top1 and validation rule; 10000 user-bootstrap replicates quantify paired differences. No borrowed baseline scores are identified.
  - Source: Sec.5.1, Tables2/3 and Appendix B: https://arxiv.org/html/2610.29298v1#S5.SS1.p2 and https://arxiv.org/html/2610.29298v1#S5.T2 and https://arxiv.org/html/2610.29298v1#S5.T3 and https://arxiv.org/html/2610.29298v1#A2.p2 and https://arxiv.org/html/2610.29298v1#A2.p4

### 5. Connections to Related Work

- **Predecessor** · [MiniOneRec](minionerec.md): MiniOneRec supplies a frozen backbone and released Amazon checkpoints.
  - Source: CAPE v1, Sec.5.1 and Appendix B: https://arxiv.org/html/2610.29298v1#S5.SS1.p1; https://arxiv.org/html/2610.29298v1#A2.p2.
- **Predecessor** · [TIGER](tiger.md): TIGER supplies the second backbone for cross-architecture evaluation.
  - Source: CAPE v1, Sec.5.1 and Table3: https://arxiv.org/html/2610.29298v1#S5.SS1.p1; https://arxiv.org/html/2610.29298v1#S5.T3.
- **Alternative** · [LIGER](liger.md): LIGER is contrasted as a trained hybrid retrieval approach.
  - Source: CAPE v1, Sec.6: https://arxiv.org/html/2610.29298v1#S6.p1.

[View all papers in this cell](../../README.md#i--inference)
