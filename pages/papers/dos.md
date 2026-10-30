# DOS

*Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan* — Yin et al., WWW’26 Short · `POI`

[arXiv](https://arxiv.org/abs/2602.04460) · [Record](../../data/papers/dos.yaml) · [← Catalog](../../README.md#iii--tokenization)

> The abstract identifies the codebook-generation gap (III) and semantic loss during quantization (I), addressed by DFI and ORQ respectively. The designs and title cover both equally; the first contribution, DFI, breaks the tie in favor of alignment.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Orth. RQ`** | `Dec-Only†` | `Fixed† / NTP` | `–` |

- `Orth. RQ`: Orthogonal residual quantization with task-relevant dimension selection and layer-wise residual coding (DOS; ORQ in the paper).
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

## Evidence

- **`problem`** (abstract, p1; contribution list, p2): The abstract identifies the codebook-generation gap (III) and semantic loss during quantization (I), addressed by DFI and ORQ respectively. The designs and title cover both equally; the first contribution, DFI, breaks the tie in favor of alignment.
- **`stage`** (contribution 1, p2; §2.1, p2; Fig. 1(a), p3): The first contribution is Dual-Flow Integration (DFI), which incorporates user-item collaborative information directly into quantization through two flows and a shared codebook. It changes SID construction, not the generation backbone.
- **`representation`** (§2.1, Eq. (1)–(5), p2): Qwen3-0.6B-embedding encodes restaurant names, categories, dishes and prices. DFI adds collaborative signals from click sequences and target items during SID construction. No explicit geographic field is reported in the prompt template.

## Same cell: III × Tokenization (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` → **`LLM-Vocab`** → `Enc-Dec` → `Altern. / NTP` → `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` → **`Self-Imp.`** → `Enc-Dec` → `Altern. / Multi-task NTP` → `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` → **`Align. RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` → **`Dual RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` → **`R-KM+Graph`** → `Dec-Only` → `Fixed / Multi-task NTP` → `CoT+C-Beam` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` → **`Multi-Path R-KM+Hash`** → `Enc-Dec` → `Fixed / NTP + PV-RSPO + Rank + Aux.` → `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` → **`Term-ID`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` → **`Nested RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `–` |
| [SST](sst.md) | CIKM’26 | `Text` → **`RQ+IST`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` → **`BDQ`** → `Non-AR` → `Fixed / MTP + Aux.` → `Scoring+Rerank` |
