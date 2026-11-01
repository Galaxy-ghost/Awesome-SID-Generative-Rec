# GR4AD-X

*Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for Large-Scale Advertising* — Xiao et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.38378) · [Record](../../data/papers/gr4ad-x.yaml) · [← Catalog](../../README.md#iii--tokenization)

> Generative recommendation (GR) reformulates item retrieval as autoregressive generation of discrete semantic identifiers (SIDs), offering a unified paradigm for personalized recommendation. GR4AD, as an industrial generative recommendation framework, has greatly improved advertising revenue while enabling efficient real-time serving in Kuaishou.However, continued deployment has exposed three limitations: deterministic SID assignment remains sensitive to semantic boundaries; conventional backbone scaling provides diminishing revenue gains under strict serving constraints; and sequence-level value optimization provides limited credit assignment to intermediate SID decisions, causing likelihood-based beam search to prematurely prune potentially high-value candidates. We present GR4AD-X, which addresses these limitations through reliable SID construction, serving-efficient capacity scaling, and unified value alignment. Specifically, GR4AD-X improves SID reliability through Multi-Path assignment. It expands model capacity along multiple complementary dimensions rather than relying solely on wider or deeper backbones, achieving a better effectiveness-efficiency trade-off under strict serving constraints. Finally, Unified Value-Guided Generation and Discrimination (UniVGD) aligns generation with commercial value through prefix-level reward optimization, value-guided beam pruning, and discriminative reranking within a unified model. Large-scale online A/B tests on the Kuaishou advertising platform demonstrate that GR4AD-X achieves a cumulative revenue improvement of 3.07% over the deployed GR4AD baseline while satisfying strict latency and throughput constraints.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Multi-Path R-KM+Hash`** | `Enc-Dec` | `Fixed / NTP + PV-RSPO + Rank + Aux.` | `PV-Beam+Rerank` |

- `–`: Not reported in the paper, or not applicable.
- `Multi-Path R-KM+Hash`: Multiple residual-k-means code paths combined with a hash-based identifier component.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + PV-RSPO + Rank + Aux.`: Next-token prediction jointly optimized with prefix-value RSPO, ranking, and auxiliary objectives.
- `PV-Beam+Rerank`: Prefix-value-guided beam search followed by reranking.

## Same cell: III × Tokenization (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` → **`LLM-Vocab`** → `Enc-Dec` → `Altern. / NTP` → `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` → **`Self-Imp.`** → `Enc-Dec` → `Altern. / Multi-task NTP` → `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` → **`Align. RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` → **`Dual RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` → **`R-KM+Graph`** → `Dec-Only` → `Fixed / Multi-task NTP` → `CoT+C-Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` → **`Orth. RQ`** → `Dec-Only†` → `Fixed† / NTP` → `–` |
| [GRLM](grlm.md) | arXiv’26 | `Text` → **`Term-ID`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` → **`Nested RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `–` |
| [SST](sst.md) | CIKM’26 | `Text` → **`RQ+IST`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` → **`BDQ`** → `Non-AR` → `Fixed / MTP + Aux.` → `Scoring+Rerank` |
