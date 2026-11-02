# Dynamic-Single-Codebook

*From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook for Generative Recommendation* — Xie et al. · arXiv’26

`V. Efficiency` · `Tokenization`

[Paper](https://arxiv.org/abs/2608.21012) · [Matrix](../../README.md#v--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Dyn. KM+Disamb.`** | `Enc-Dec / Lazy Dec-Only` | `Fixed / NTP†` | `Beam†` |

- `–`: Not reported in the paper.
- `Dyn. KM+Disamb.`: Dynamically updated k-means codes combined with disambiguation codes.
- `Enc-Dec / Lazy Dec-Only`: Encoder–decoder and lazy decoder-only backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty 2014; KuaiRec 2.0 Big Matrix, watch_ratio>=1 and users with >=5 retained events; industrial data. Other filters not reported.
  - Source: Section 4.1: https://arxiv.org/html/2608.21012v1#S4.SS1.p1 and https://arxiv.org/html/2608.21012v1#S4.SS1.p2
- **Split**: Per-user chronological last/penultimate holdouts; separate KuaiRec experiment trains through September 3, validates September 4, tests September 5.
  - Source: Section 4.1 and fixed-date protocol: https://arxiv.org/html/2608.21012v1#S4.SS1.p2 and https://arxiv.org/html/2608.21012v1#S4.SS3.SSS2.p1
- **Candidates**: not reported
  - Source: Candidate protocol absent from Sections 4.1-4.5 and Appendices B-E: https://arxiv.org/html/2608.21012v1#S4.SS1
- **Visibility**: warm; no unseen-item protocol is defined. Fixed-date validation/test days are excluded from codebook fitting; leave-two-out PV weights use all viewing events. Item-level holdouts: not reported.
  - Source: Section 4.1 and fixed-date protocol: https://arxiv.org/html/2608.21012v1#S4.SS1.p2 and https://arxiv.org/html/2608.21012v1#S4.SS3.SSS2.p1
- **SID**: Public data: [1024,512], semantic plus balanced disambiguation code; baseline [256,256,256].
  - Source: Section 4.1: https://arxiv.org/html/2608.21012v1#S4.SS1.p3
- **Inference budget**: K=5/10; beam width, hardware model, inference batch size, absolute latency/QPS not reported. Single-card QPS gains: 28.57%-47.0%.
  - Source: Sections 4.1 and 4.5: https://arxiv.org/html/2608.21012v1#S4.SS1.p5 and https://arxiv.org/html/2608.21012v1#S4.SS5.p1
- **Results from**: Original Table 2, Figures 3/4/6, Tables 9-14; Section 4.5 online A/B.
  - Source: Section 4 and Appendices C-E: https://arxiv.org/html/2608.21012v1#S4 and https://arxiv.org/html/2608.21012v1#A3 and https://arxiv.org/html/2608.21012v1#A4 and https://arxiv.org/html/2608.21012v1#A5

### 5. Connections to Related Work

- **Alternative** · [RPG](rpg.md): RPG parallelizes long SIDs; this method shortens SIDs.
  - Source: Dynamic-Single-Codebook v1, Section 2.2: https://arxiv.org/html/2608.21012v1#S2.SS2.p2.
- **Alternative** · [LLaDA-Rec](llada-rec.md): LLaDA-Rec uses diffusion with adapted beam search; this method reduces token count.
  - Source: Dynamic-Single-Codebook v1, Sections 1 and 2.2: https://arxiv.org/html/2608.21012v1#S1.p4; https://arxiv.org/html/2608.21012v1#S2.SS2.p2.
- **Alternative** · [LETTER](letter.md): LETTER regularizes residual quantization; this method changes semantic codebook width and depth.
  - Source: Dynamic-Single-Codebook v1, Section 2.1: https://arxiv.org/html/2608.21012v1#S2.SS1.p2.

[View all papers in this cell](../../README.md#v--tokenization)
