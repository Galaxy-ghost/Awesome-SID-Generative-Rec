# MME-SID

*Empowering large language model for sequential recommendation via multimodal embeddings and semantic ids* — Wang et al. · CIKM’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2509.02017) · [Code](https://github.com/Applied-Machine-Learning-Lab/MME-SID) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`MM-RQ`** | `Dec-Only` | `Fixed / NTP` | `Scoring` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

MME-SID feeds an LLM multimodal embeddings together with Semantic ID embeddings from MM-RQ-VAE, trained with maximum mean discrepancy and contrastive alignment, to reduce embedding collapse and forgetting.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | MME-SID feeds an LLM multimodal embeddings together with Semantic ID embeddings from MM-RQ-VAE, trained with maximum mean discrepancy and contrastive alignment, to reduce embedding collapse and forgetting. |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon 2014 5-core: Beauty (22,332 users / 12,086 items), Toys and Games (19,121 / 11,757), Sports and Outdoors (35,092 / 18,090); items lacking a title or image are removed. Positives are ratings above 3.
  - Source: 5-core Amazon 2014 and item removal: https://arxiv.org/html/2509.02017v1#S5.SS1.SSS1.p1 and https://arxiv.org/html/2509.02017v1#A2.p1; statistics: https://arxiv.org/html/2509.02017v1#S5.T1.
- **Split**: Per user, the N-th (last) item is the test target and the (N-1)-th item the training target; a validation split is not reported. Results averaged over 3 runs.
  - Source: Last and second-last item as test and training targets: https://arxiv.org/html/2509.02017v1#S5.SS1.SSS1.p1; three runs: https://arxiv.org/html/2509.02017v1#S5.SS1.SSS4.p1.
- **Candidates**: not reported (full catalog versus sampled); items are scored by dot products between the LLM output and multimodal item embeddings, with HR and nDCG at 5, 10, 20.
  - Source: Scores over target item embeddings: https://arxiv.org/html/2509.02017v1#S4.SS3.p3 and https://arxiv.org/html/2509.02017v1#S6.SS2.p1; metrics: https://arxiv.org/html/2509.02017v1#S5.SS1.SSS2.p1.
- **Visibility**: warm; no unseen-item protocol is defined. A frequency-aware fusion module reweights modalities by each item's training-set frequency.
  - Source: Standard split; frequency-aware fusion for cold versus warm items without an unseen-item protocol: https://arxiv.org/html/2509.02017v1#S5.SS1.SSS1.p1 and https://arxiv.org/html/2509.02017v1#S4.SS3.p3.
- **SID**: Separate collaborative, textual, and visual SIDs from RQ-VAEs with 4 levels x 256 codes (300 for Sports), used as LLM input embeddings alongside projected modality embeddings. The paper states that MME-SID does not need to tackle collisions because multimodal data discriminate between items; no resolution rule is described.
  - Source: 4 levels x 256 (300 for Sports) per modality: https://arxiv.org/html/2509.02017v1#A1.T4; no collision handling needed by design: https://arxiv.org/html/2509.02017v1#S4.I1.i2.p1.
- **Inference budget**: No autoregressive decoding: one forward pass of Llama3-8B-instruct, then scoring against item embeddings. All experiments on A100 GPUs; inference batch size and latency: not reported.
  - Source: Scoring instead of autoregressive decoding: https://arxiv.org/html/2509.02017v1#S6.SS2.p1; hardware: https://arxiv.org/html/2509.02017v1#S5.SS1.SSS4.p1.
- **Results from**: Table 3 (Beauty, Toys, Sports versus ID, multimodal, and SID-based baselines; t-tests); Figure 3 (embedding collapse and SR performance); Appendix Table 4 (hyperparameters).
  - Source: Main: https://arxiv.org/html/2509.02017v1#S5.T3; collapse analysis: https://arxiv.org/html/2509.02017v1#S5.SS3.p1.

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER-MM generates per-modality RQ-VAE semantic IDs autoregressively and must resolve collisions; MME-SID feeds multimodal SIDs and embeddings to an LLM and scores items directly.
  - Source: MME-SID v1, baseline TIGER-MM: https://arxiv.org/html/2509.02017v1#S5.I2.i7.p1; collision contrast: https://arxiv.org/html/2509.02017v1#S4.I1.i2.p1; Table 3: https://arxiv.org/html/2509.02017v1#S5.T3.
- **Competitor** · [LETTER](letter.md): LETTER regularizes the tokenizer for generative retrieval on a TIGER backbone; MME-SID avoids generation and aligns modalities with an MMD loss.
  - Source: MME-SID v1, baseline LETTER implemented on TIGER: https://arxiv.org/html/2509.02017v1#S5.I2.i9.p1; Table 3: https://arxiv.org/html/2509.02017v1#S5.T3.
- **Alternative** · [LC-Rec](lc-rec.md): LC-Rec aligns an LLM to item indices but decodes autoregressively; MME-SID scores items from the LLM output for lower latency.
  - Source: MME-SID v1, Section 6.2: https://arxiv.org/html/2509.02017v1#S6.SS2.p1.
- **Alternative** · [ADC-SID](adc-sid.md): ADC-SID later compares against MM-RQ-VAE (MME-SID's tokenizer) and adds adaptive behavior-content alignment.
  - Source: Evidence is from the later ADC-SID paper: MM-RQ-VAE baseline and Table 2: https://arxiv.org/html/2510.25622v3#S4.I3.i6.p1 and https://arxiv.org/html/2510.25622v3#S4.T2.

[View all papers in this cell](../../README.md#i--tokenization)
