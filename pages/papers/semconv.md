# SemConv

*Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization* — Li et al., AAAI’25

[arXiv](https://arxiv.org/abs/2412.13771) · [Record](../../data/papers/semconv.yaml) · [← Catalog](../../README.md#iii--tokenization)

> Abstract: "a notable discrepancy persists between the sparse collaborative semantics typically found in recommendation systems and the dense token representations within LLMs".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Align. RQ`** | `Dec-Only` | `Fixed / Multi-task NTP` | `Beam` |

- `Align. RQ`: Residual quantization with alignment losses and no autoencoder (SemConv).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "a notable discrepancy persists between the sparse collaborative semantics typically found in recommendation systems and the dense token representations within LLMs".
- **`representation`** (Alignment Tokenization, p2–3): AAAI paper without section numbers; subsection titles used.
- **`tokenizer`** (Alignment Task, p4): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: III × Tokenization (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` → **`LLM-Vocab`** → `Enc-Dec` → `Altern. / NTP` → `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` → **`Self-Imp.`** → `Enc-Dec` → `Altern. / Multi-task NTP` → `C-Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` → **`Dual RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` → **`R-KM+Graph`** → `Dec-Only` → `Fixed / Multi-task NTP` → `CoT+C-Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` → **`Orth. RQ`** → `Dec-Only†` → `Fixed† / NTP` → `–` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` → **`Multi-Path R-KM+Hash`** → `Enc-Dec` → `Fixed / NTP + PV-RSPO + Rank + Aux.` → `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` → **`Term-ID`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` → **`Nested RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `–` |
| [SST](sst.md) | CIKM’26 | `Text` → **`RQ+IST`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` → **`BDQ`** → `Non-AR` → `Fixed / MTP + Aux.` → `Scoring+Rerank` |
