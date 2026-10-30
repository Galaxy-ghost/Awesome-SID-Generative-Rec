# DPE-Rec: DPE-Rec: Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2610.34700`)](https://arxiv.org/abs/2610.34700) · [Source Record (`data/papers/dpe-rec.yaml`)](../../data/papers/dpe-rec.yaml)

> **Summary**: Generative bundle construction completes a partially observed bundle by generating its missing items from a large product catalog. Compared to autoregressive LLMs, diffusion LLM emerges as a natural fit for this unordered generation task. Their bidirectional attention provides an inductive bias better aligned with unordered bundle construction. Iterative denoising can reveal multiple tokens per step, potentially reducing inference latency. However, directly applying DLMs to this task presents two key challenges: 1 Despite its flexible reveal order, confidence-guided decoding tends to postpone semantic-fork decisions until refinement tokens constrain their choices, reducing bundle diversity. 2 Revealing more tokens per step can compromise recommendation quality, stifling the potential for faster inference. We introduce DPE-Rec, a diffusion framework for diversity preservation and efficient recommendation. DPE-Rec preserves diversity by introducing semantic-fork-aware GRPO, which prioritizes semantic-fork decisions via autoregressive rollouts. It improves efficiency through pseudo-trajectory distillation, which concentrates learning from the vast random corruption space onto the compact trajectory-induced subspace visited by high-quality decoding, unlocking reliable multi-token decoding. Together, these components enable diverse and accurate bundle construction with substantially fewer denoise steps. Experiments on multiple bundle construction benchmarks show that DPE-Rec improves recommendation performance by 63% on average, and its fast variant achieves 25.6$times$ faster inference on average than existing generative recommendation arts, with minimal loss in recommendation quality.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Ma et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `IV. Utility` | Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| **Primary Stage** | `Training` | The primary design change sits in the Training stage (Tokenizer update schedule or training Objective). |
| **Representation** | `– / Text+Img` | Spotify/POG原CLHE输入未在本文分解 |
| **Tokenization** | `RQ` | Residual quantization. |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Masked → RL (→ Masked KD for Fast)` | 先random-mask去噪CE，再semantic-fork-aware GRPO |
| **Inference Decoding** | `Diff.+Legalize` | 扩散解码后候选集合内精确SID匹配，非法SID重构向量后cosine最近候选匹配并去重。 |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `IV. Utility` × `Training` (21 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [APAO](apao.md) | KDD’26 | `Text` | `R-KM` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Rank` | `Beam` |
| [DASO](daso.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
| [GEM-Rec](gem-rec.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Bid-Aware Beam` |
| [GenRec-JD](genrec-jd.md) | SIGIR’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [GFlowGR](gflowgr.md) | SIGIR’26 | `Text / Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `Beam† / C-Beam†` |
| [Ghost](ghost.md) | NeurIPS’26 | `Text` | `Skeleton R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `–` |
| [HASTE](haste.md) | arXiv’26 | `Text / MM` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `–` |
| [HCGRec](hcgrec.md) | CIKM’26 | `–` | `RQ` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [IDM/CMM](idm-cmm.md) | arXiv’26 | `Text` | `Subspace RQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring` |
| [KL-MOPD](kl-mopd.md) | arXiv’26 | `CF` | `R-KM` | `Enc-Dec` | `Fixed†` | `(NTP† / (NTP + Aux.)†) → KL-weighted OPD` | `C-Beam` |
| [MuSID-KD](musid-kd.md) | arXiv’26 | `–` | `RQ-VAE` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [NAU](nau.md) | arXiv’26 | `–` | `R-KM` | `Enc-Dec†` | `Fixed` | `NTP + Aux.` | `–` |
| [OneChord](onechord.md) | arXiv’26 | `–` | `Par. OPQ` | `Non-AR` | `Fixed` | `Next-item CE + Cons. KD + Rank KD` | `Scoring` |
| [Retrieval-Grounded-Credit](retrieval-grounded-credit.md) | arXiv’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SAGE-SID](sage-sid.md) | arXiv’26 | `Text+Img†` | `R-KM†` | `Dec-Only†` | `Fixed†` | `NTP → RL` | `Beam†` |
| [SAHL](sahl.md) | arXiv’26 | `Text` | `SRBQ` | `Non-AR` | `Fixed` | `(MTP + Masked Rec.) → MTP` | `Graph` |
| [SAPO](sapo.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+C-Beam` |
| [SLIDE](slide.md) | arXiv’26 | `–` | `–` | `Dec-Only` | `Fixed` | `NTP` | `Greedy` |
| [Token-Weighted](token-weighted.md) | CIKM’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [UGR](ugr.md) | KDD’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → (RL + Rank)` | `Beam` |
| [V-STAR](v-star.md) | KDD’26 | `Text†` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `C-Beam` |
