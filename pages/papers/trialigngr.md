# TriAlignGR

*Triangular Multitask Alignment with Multimodal Deep Interest Mining for Generative Recommendation* — Zeng et al. · arXiv’26

`I. Informativeness` · `Representation`

[Paper](https://arxiv.org/abs/2605.05249) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img`** | `RQ-VAE` | `Dec-Only` | `Fixed / Multi-task NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `C-Beam`: Constrained beam search.

### TL;DR

TriAlignGR adds visual content and LLM-mined user intents to Semantic ID construction and trains several generation tasks linking Semantic IDs, text, and images under one autoregressive loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | TriAlignGR adds visual content and LLM-mined user intents to Semantic ID construction and trains several generation tasks linking Semantic IDs, text, and images under one autoregressive loss. |
| Modified Stage | Representation |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty, Sports and Outdoors, Musical Instruments with 5-core filtering (22K-36K users, 10K-18K items, 198K-296K interactions in total ranges; per-dataset counts not separated in the text).
  - Source: Datasets and protocol: https://arxiv.org/html/2605.05249v3#A1.p1.
- **Split**: Leave-last-out protocol (allocation not restated beyond the label); results averaged over three seeds.
  - Source: Leave-last-out: https://arxiv.org/html/2605.05249v3#A1.p1; three seeds: https://arxiv.org/html/2605.05249v3#S4.SS1.p1.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); top-K from beam search with beam size 20.
  - Source: Metrics and beam: https://arxiv.org/html/2605.05249v3#A1.p2.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2605.05249v3#A1.p1.
- **SID**: 3-level RQ-VAE with codebook sizes 4,096, 2,048, and 1,024 over gme-Qwen2-VL multimodal embeddings enriched with image captions (CMSA) and mined user interests (MDIM). Collision rates are reported: 3.1% of Beauty items share a full SID (5.1% for text-only RQ-VAE); a resolution rule is not reported.
  - Source: 3-level RQ-VAE with 4096/2048/1024 over gme-Qwen2-VL embeddings: https://arxiv.org/html/2605.05249v3#A1.p3; collision diagnostics: https://arxiv.org/html/2605.05249v3#A3.T6.
- **Inference budget**: Beam size 20; Qwen2.5-7B-Instruct backbone; experiments on NVIDIA A100 GPUs; inference batch size and latency: not reported.
  - Source: Beam 20, backbone, GPUs: https://arxiv.org/html/2605.05249v3#A1.p2 and https://arxiv.org/html/2605.05249v3#A1.p3.
- **Results from**: Table 2 (Beauty, Sports, Instruments versus sequential, generative, LLM, and reasoning baselines; three seeds); Tables 3-5 (component, SID-versus-task, and task-combination ablations); Appendix Tables 6-8 (SID diagnostics, semantic probing, SID construction versus MiniOneRec).
  - Source: Main: https://arxiv.org/html/2605.05249v3#S4.T2; ablations: https://arxiv.org/html/2605.05249v3#S4.T3, https://arxiv.org/html/2605.05249v3#S4.T4, https://arxiv.org/html/2605.05249v3#S4.T5; SID diagnostics: https://arxiv.org/html/2605.05249v3#A3.T6; probing: https://arxiv.org/html/2605.05249v3#A4.T7; vs MiniOneRec: https://arxiv.org/html/2605.05249v3#A5.T8.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

把视觉语义编进 SID，并用视觉描述等多任务让模型理解 SID 的含义。

### 5. Connections to Related Work

- **Competitor** · [SIDReasoner](sidreasoner.md): SIDReasoner is the strongest baseline, aligning SIDs and language through enriched corpora and RL; TriAlignGR adds visual captions and mined interests before quantization and eight alignment tasks.
  - Source: TriAlignGR v3, Section 4.1: https://arxiv.org/html/2605.05249v3#S4.SS1.p1; Table 2: https://arxiv.org/html/2605.05249v3#S4.T2.
- **Predecessor** · [MiniOneRec](minionerec.md): TriAlignGR shares MiniOneRec's backbone, training protocol, and RQ-VAE configuration and isolates the effect of its SID enrichment against it.
  - Source: TriAlignGR v3, Section 4.1 comparison: https://arxiv.org/html/2605.05249v3#S4.SS1.p3; Appendix Table 8: https://arxiv.org/html/2605.05249v3#A5.T8.
- **Competitor** · [LETTER](letter.md): LETTER regularizes a text tokenizer; TriAlignGR changes the tokenizer input to multimodal, interest-enriched embeddings.
  - Source: TriAlignGR v3, Table 2 baseline: https://arxiv.org/html/2605.05249v3#S4.T2.
- **Competitor** · [ETEGRec](etegrec.md): ETEGRec trains tokenizer and generator jointly; TriAlignGR keeps a fixed tokenizer and adds multitask alignment.
  - Source: TriAlignGR v3, Table 2 baseline: https://arxiv.org/html/2605.05249v3#S4.T2.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec uses text-only SIDs with alignment tasks; TriAlignGR extends the task set with visual-semantic tasks.
  - Source: TriAlignGR v3, Table 2 baseline: https://arxiv.org/html/2605.05249v3#S4.T2.

[View all papers in this cell](../../README.md#i--representation)
