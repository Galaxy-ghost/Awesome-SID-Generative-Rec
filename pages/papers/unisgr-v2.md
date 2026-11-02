# UniSGR-V2

*Stepwise Target-Side Feature Anticipation and Crossing for Generative Recommendation* — Yang et al. · arXiv’26

`I. Informativeness` · `Backbone`

[Paper](https://arxiv.org/abs/2610.16132) · [Matrix](../../README.md#i--backbone)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `–` | **`Enc-Dec`** | `– / NTP + Rank` | `Beam` |

- `–`: Not reported in the paper.
- `Enc-Dec`: Encoder-decoder.
- `NTP + Rank`: NTP plus a ranking loss.

### TL;DR

UniSGR-V2 anticipates a continuous target-side feature vector before each codeword and crosses it with the semantic prefix and user behavior inside the decoder, using it for generation and ranking.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | UniSGR-V2 anticipates a continuous target-side feature vector before each codeword and crosses it with the semantic prefix and user behavior inside the decoder, using it for generation and ranking. |
| Modified Stage | Backbone |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Lazada recommendation logs with impression, click, add-to-cart and pay behaviors; training: 2.42 billion samples, 6.46 million users, 7.53 million items.
- **Split**: Chronological: first 30 days training, following day testing; validation split not reported.
- **Candidates**: not reported; full-catalog versus sampled retrieval evaluation and history exclusion are unspecified; ranking sample construction not reported.
- **Visibility**: warm; no unseen-item protocol is defined.
- **SID**: 3-level semantic IDs with 2,048 codewords per level; tokenizer inputs, quantization algorithm, training visibility and collision handling not reported.
- **Inference budget**: Beam search width not reported; paired prediction/code execution uses 3 sequential decoder calls; maximum history 1,024. Full TacGR: 701 QPS, mean latency 75.6 ms, P99 83.8 ms under matched production hardware/load; hardware specification, batch size and numerical memory-funnel schedule not reported; anchoring tower is training-only.
- **Results from**: Own Lazada offline comparison, ablations and serving benchmarks; Table 1 averages 5 seeds. UniRec CoA reproduced on the same backbone; other baseline implementation provenance not reported. Own 40-day online A/B test on 10% traffic replaces UniSGR in one retrieval channel: IPV +0.79%, Order +5.55%, GMV +3.09%; other channels and downstream ranking retained.

<details>
<summary>Sources</summary>

- **Datasets**: [S4.SS1.p1](https://arxiv.org/html/2610.16132v2#S4.SS1.p1)
- **Split**: [S4.SS1.p1](https://arxiv.org/html/2610.16132v2#S4.SS1.p1)
- **Candidates**: [S4.SS1.p3](https://arxiv.org/html/2610.16132v2#S4.SS1.p3) ; HR@100/500 are output cutoffs, not a stated evaluation pool.
- **Visibility**: [S4.SS1.p1](https://arxiv.org/html/2610.16132v2#S4.SS1.p1) ; Appendix A's cold-start prediction refers to the initial anticipation slot.
- **SID**: [S4.SS1.p4](https://arxiv.org/html/2610.16132v2#S4.SS1.p4)
- **Inference budget**: [S3.SS5.SSS4.p1](https://arxiv.org/html/2610.16132v2#S3.SS5.SSS4.p1) ; [S4.SS1.p4](https://arxiv.org/html/2610.16132v2#S4.SS1.p4) ; [A2.T5](https://arxiv.org/html/2610.16132v2#A2.T5) ; [S3.SS4.SSS2.p3](https://arxiv.org/html/2610.16132v2#S3.SS4.SSS2.p3) ; [S3.SS7.SSS2](https://arxiv.org/html/2610.16132v2#S3.SS7.SSS2)
- **Results from**: [S4.SS1.p2](https://arxiv.org/html/2610.16132v2#S4.SS1.p2) ; [S4.T1](https://arxiv.org/html/2610.16132v2#S4.T1) ; [S4.SS5.p1](https://arxiv.org/html/2610.16132v2#S4.SS5.p1) ; [A2.p1](https://arxiv.org/html/2610.16132v2#A2.p1)

</details>

### 5. Connections to Related Work

- **Predecessor** · [UniRec](unirec.md): Its discrete attribute chain is the closest motivation and a same-backbone baseline.
  - Source: https://arxiv.org/html/2610.16132v2#S1.p5 ; https://arxiv.org/html/2610.16132v2#S4.SS1.p2
- **Competitor** · [OneRec-V2](onerec-v2.md): Industrial generative retrieval baseline in Table 1.
  - Source: https://arxiv.org/html/2610.16132v2#S4.SS1.p2 ; bibliography identifies Zhou et al. (2025) as arXiv:2508.20900.
- **Competitor** · [TIGER](tiger.md): Semantic-ID generative retrieval baseline in Table 1.
  - Source: https://arxiv.org/html/2610.16132v2#S4.SS1.p2 ; https://arxiv.org/html/2610.16132v2#S4.T1

[View all papers in this cell](../../README.md#i--backbone)
