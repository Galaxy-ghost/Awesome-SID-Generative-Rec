# PFA: PFA: Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.39273`)](https://arxiv.org/abs/2610.39273) · [Source Record (`data/papers/pfa.yaml`)](../../data/papers/pfa.yaml)

> **Summary**: Long user behavioral sequences improve the performance of generative recommendation (GR), but computing full attention over long histories during autoregressive beam search decoding incurs substantial online inference latency. To accelerate long-sequence decoding, existing approaches typically rely on static history compression or dynamic top-k sparse attention; however, the former risks losing critical semantics, whereas the latter incurs significant overhead from repeated token selection and non-contiguous memory access. In this work, we thoroughly analyze attention patterns during GR decoding and reveal two key properties: (i) progressive attention focusing, where attention progressively focuses on a small subset of critical historical tokens; and (ii) cross-step ranking consistency, where their importance rankings remain relatively stable across subsequent decoding steps. Motivated by these observations, we propose Progressively Focused Attention (PFA), an efficient sparse decoding framework for long-sequence GR. PFA retains full attention at the initial decoding step to explore global historical preferences. It then establishes a shared importance ranking through cross-beam weighted aggregation and reorders the key-value cache of the selected tokens into a contiguous memory layout. Subsequent decoding steps reuse this ranking and geometrically reduce the token budget, preserving critical semantics while lowering computational and memory access overhead. Extensive experiments on two public benchmarks and a large-scale industrial dataset demonstrate that PFA outperforms state-of-the-art baselines. A 7-day online A/B test on a large-scale e-commerce advertising platform further confirms that PFA delivers substantial business gains while maintaining low inference latency. Our code is publicly available at https://anonymous.4open.science/r/PFA-review-088D.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhou et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Inference` | The primary design change sits in the Inference stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `–` | No item SID is built, or not reported. |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `–` | No SID is built. |
| **Training Objective** | `–` |  |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `V. Efficiency` × `Inference` (5 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Spec. Dec.` |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Self-Draft+Hash` |
| [OneRec-V2-Quantized](onerec-v2-quantized.md) | arXiv’26 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed†` | `NTP → RL†` | `FP8+RecoGEM` |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP†` | `Spec. Dec.` |
| [STATIC](static.md) | KDD’26 ADS | `–` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `Vec. C-Beam` |
