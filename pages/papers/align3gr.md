# Align3GR

*Align$^3$GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation* — Ye et al. · AAAI’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2511.11255) · [Matrix](../../README.md#iii--tokenization)

Reading level: Reading Notes (Level 2) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [1. Why This Paper Matters](#1-why-this-paper-matters) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [4. Limitations & Critical Analysis](#4-limitations--critical-analysis) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Dual RQ`** | `Dec-Only` | `Fixed / NTP → DPO` | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

### TL;DR

Align3GR aligns an LLM recommender at three levels, with dual semantic and collaborative tokenization, bidirectional semantic alignment in behavior modeling, and progressive DPO from self-play and real-world feedback.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Key Contribution | Align3GR aligns an LLM recommender at three levels, with dual semantic and collaborative tokenization, bidirectional semantic alignment in behavior modeling, and progressive DPO from self-play and real-world feedback. |
| Modified Stage | Tokenization |
| Key Findings | On the public dataset, Align3GR reports +17.8% in Recall@10 and +20.2% in NDCG@10 over the strongest baseline (Abstract). |

### 1. Why This Paper Matters

Turning a large language model (LLM) into a recommender meets semantic and behavioral misalignment (Abstract). Earlier LLM recommenders such as LC-Rec align item tokens through supervised tasks. Align3GR treats alignment as one problem across token, behavior modeling, and preference levels.

> "To bridge this gap, we propose Align3GR, a novel framework that unifies token-level, behavior modeling-level, and preference-level alignment." (Abstract)

Based on arXiv v2.

### 2. How It Works

![Align3GR architecture diagram](../../architectures/align3gr.png)

*Figure source: Fig. 2, original paper.*

```mermaid
flowchart LR
    A[Users and items] --> B[Dual SC encoders]
    B --> C[SCIDs]
    C --> D[Multi-task SFT]
    D --> E[SP-DPO]
    E --> F[RF-DPO]
```

#### Token-Level Alignment

Dual semantic-collaborative (SC) encoders and RQ-VAEs build SCIDs for both users and items (Fig. 2 caption). The LLM vocabulary is expanded with these tokens.

> "Following previous work (Zheng et al. 2024), we first expand the LLM vocabulary to include the SCID tokens of the user and the item, thus avoiding out-of-vocabulary issues and ensuring smooth integration with autoregressive generation tasks." (Behavior Modeling-level Alignment)

#### Behavior Modeling-Level Alignment

Supervised fine-tuning (SFT) follows LC-Rec with four tasks: sequential item prediction, asymmetric item prediction, item prediction based on user intention, and personalized preference inference (Multi-task SFT). The user's SCID token appears in every task prompt, and one task reconstructs the user profile text from the user SCID (Multi-task SFT).

#### Preference-Level Alignment

Self-play DPO (SP-DPO) runs in Easy, Medium, and Hard stages defined by prefix n-gram match over the hierarchical SCID (Preference-level Alignment). Real-feedback DPO (RF-DPO) then uses feedback labeled disliked, neutral, or liked (Preference-level Alignment).

> "Specifically, considering the hierarchical nature of SCID, we divide progressive SP-DPO learning into three stages: Easy, Medium, and Hard, using a prefix-ngram match metric (Zheng et al. 2025)" (Preference-level Alignment)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Instruments, Amazon Beauty, and Yelp; users and items with fewer than 5 interactions are filtered. Retained corpus sizes: not reported in the body. Industrial: internal data from a large-scale advertising recommendation platform; filtering not reported.
  - Source: Datasets, 5-interaction filter, leave-one-out, history cap: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p1; industrial platform: https://arxiv.org/html/2511.11255v2#Sx4.SSx3.p1.
- **Split**: Leave-one-out into training, validation, and test; histories capped at the 20 most recent items. The exact position allocation is not reported beyond the leave-one-out label. Online: 10% of traffic (about 40+ million users) over multiple weeks.
  - Source: Leave-one-out and 20-item cap: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p1 and https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3; online traffic: https://arxiv.org/html/2511.11255v2#Sx4.SSx3.p1.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); industrial retrieval reports Recall@100.
  - Source: Metrics and beam width only: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard leave-one-out with no cold-start experiment: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p1.
- **SID**: Item SCID: 3-level RQ-VAE x 256 codewords (dimension 32) over concatenated semantic (T5) and collaborative (DIN) embeddings; users receive their own SCIDs from a separate user RQ-VAE. Both are added to the LLM vocabulary. Collision handling: not reported.
  - Source: 3-level RQ-VAE x 256 codes of dimension 32, user and item SCIDs added to the vocabulary: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p4; dual user/item tokenizer: https://arxiv.org/html/2511.11255v2#Sx3.SSx2.p2 and https://arxiv.org/html/2511.11255v2#Sx3.SSx2.p4.
- **Inference budget**: Beam search with beam width 20 for generative methods (following EAGER-LLM); Recall and NDCG at K=5 and 10. All experiments use 4 NVIDIA GPUs (model not stated); inference batch size and latency: not reported. Backbone: Llama2-7B with LoRA.
  - Source: Beam width 20 following EAGER-LLM: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3; 4 GPUs for all experiments: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p4.
- **Results from**: Table 1 (Instruments, Beauty, Yelp; averages over five seeds); Table 2 (industrial Recall@100 and online revenue versus a two-tower baseline and TIGER); Tables 3-5 and Figure 4 (tokenization, SFT-task, and DPO ablations).
  - Source: Main table: https://arxiv.org/html/2511.11255v2#Sx3.T1; industrial: https://arxiv.org/html/2511.11255v2#Sx4.T2; ablations: https://arxiv.org/html/2511.11255v2#Sx4.T3, https://arxiv.org/html/2511.11255v2#Sx4.T4, https://arxiv.org/html/2511.11255v2#Sx4.T5; five seeds: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p4.

- Industrial deployment: the authors report gains in online A/B tests and full-scale deployment on an industrial recommendation platform (Abstract).

### 4. Limitations & Critical Analysis

**Our analysis.**

- The pipeline trains SCID tokenizers, multi-task SFT, and two DPO phases in sequence. This suggests that a catalog change requires repeating several stages.
- EAGER-LLM also feeds semantic and collaborative signals to a `Dec-Only` LLM, but with `Dual H-KM` codes; Align3GR uses `Dual RQ` codes and adds DPO.

### 5. Connections to Related Work

- **Competitor** · [EAGER-LLM](eager-llm.md): EAGER-LLM aligns item tokens with collaborative signals; Align3GR also tokenizes users and adds progressive self-play and real-feedback DPO.
  - Source: Align3GR v2, Experimental Settings baselines (13) and beam-width protocol: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2 and https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec aligns LLMs to item codes with auxiliary tasks; Align3GR adds dual user-item SCIDs and preference-level DPO on top of multi-task SFT.
  - Source: Align3GR v2, baselines (11): https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1.
- **Competitor** · [LETTER](letter.md): LETTER learns a regularized item tokenizer; Align3GR fuses semantic and collaborative features for both users and items through a U2I loss.
  - Source: Align3GR v2, baselines (12): https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1.
- **Competitor** · [TIGER](tiger.md): TIGER uses content-only RQ-VAE item codes with a small Transformer; Align3GR uses an LLM backbone with dual SCIDs and DPO.
  - Source: Align3GR v2, baselines (10): https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1; industrial Table 2: https://arxiv.org/html/2511.11255v2#Sx4.T2.

[View all papers in this cell](../../README.md#iii--tokenization)
