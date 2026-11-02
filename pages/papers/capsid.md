# CapsID

| **Title** | *Soft-Routed Variable-Length Semantic IDs for Generative Recommendation* |
| :-- | :-- |
| **Authors** | Cheng et al. |
| **Venue** | arXiv’26 |
| **Problem × Stage** | `I. Informativeness` · `Tokenization` |
| **Links** | [Paper](https://arxiv.org/abs/2605.05096) · [Matrix](../../README.md#i--tokenization) · [中文](../zh/papers/capsid.md) |
| **Reading level** | Overview (Level 1) |

On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>Soft-RQ"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `Soft-RQ`: Soft-routed RQ variant.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> CapsID replaces hard residual quantization with capsule routing, which soft-routes each item across capsules and ends its Semantic ID once confidence is high, so ID length varies per item.

---

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | CapsID replaces hard residual quantization with capsule routing, which soft-routes each item across capsules and ends its Semantic ID once confidence is high, so ID length varies per item. |
| Modified Stage | Tokenization |

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Beauty, Sports, and Toys with 5-core filtering (users / items: 22,363 / 12,101; 35,598 / 18,357; 19,412 / 11,924). Industrial: a proprietary 35M-item catalog from a large social media platform with text, image, and behavior embeddings (331.1M interactions); filtering not reported.
  - Source: Datasets and filtering: [S4.SS1.SSS0.Px1.p1](https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px1.p1); statistics: [S4.T2](https://arxiv.org/html/2605.05096v1#S4.T2); preprocessing statement: [A2.SS5.p1](https://arxiv.org/html/2605.05096v1#A2.SS5.p1).
- **Split**: Leave-one-out with 5-core filtering on the Amazon datasets; the exact validation/test position allocation is not restated. Histories are truncated to the most recent 50 interactions. Industrial split: not reported.
  - Source: Leave-one-out: [S4.SS1.SSS0.Px1.p1](https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px1.p1) and [S4.T2](https://arxiv.org/html/2605.05096v1#S4.T2); history truncation: [A1.SS3.SSS0.Px2.p1](https://arxiv.org/html/2605.05096v1#A1.SS3.SSS0.Px2.p1).
- **Candidates**: full catalog (full-corpus ranking); decoding is constrained by a trie over item SIDs. Recall and NDCG at K=5 and 10 on Amazon, K=50 and 100 on the 35M-item catalog.
  - Source: Full-corpus ranking: [S4.SS1.SSS0.Px3.p1](https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px3.p1); trie restricted to training-item SIDs: [A1.SS3.SSS0.Px3.p1](https://arxiv.org/html/2605.05096v1#A1.SS3.SSS0.Px3.p1).
- **Visibility**: Main: warm; no unseen-item protocol is defined. Appendix B.2 isolates Beauty cold items, defined as items with fewer than 5 interactions in the training split (about 12% of items); these are low-frequency, not strictly unseen, and tokenizer exposure is not separately reported. The industrial cold-start tier is not defined.
  - Source: Cold subset definition: [A2.SS2.p1](https://arxiv.org/html/2605.05096v1#A2.SS2.p1); industrial cold-start tier without definition: [S4.SS5.SSS0.Px5.p2](https://arxiv.org/html/2605.05096v1#S4.SS5.SSS0.Px5.p2).
- **SID**: Variable-length SIDs: K=256 capsules per depth, up to L_max=6 levels, stopping on confidence (tau=0.82) or residual norm (epsilon=0.08); SemanticBPE then merges frequent code pairs (industrial: K=1024, mean length 3.3 after merging). Collision rates are reported: 13.4% on Beauty for CapsID and 19.4% for CapsID+SemanticBPE on the industrial catalog; a resolution rule for items sharing a SID is not reported.
  - Source: Capsule configuration: [A1.SS1.SSS0.Px2.p1](https://arxiv.org/html/2605.05096v1#A1.SS1.SSS0.Px2.p1); industrial K=1024: [A1.SS3.SSS0.Px2.p1](https://arxiv.org/html/2605.05096v1#A1.SS3.SSS0.Px2.p1); measured collision rates: [S4.SS5.SSS0.Px4.p1](https://arxiv.org/html/2605.05096v1#S4.SS5.SSS0.Px4.p1) and [S4.SS5.SSS0.Px5.p2](https://arxiv.org/html/2605.05096v1#S4.SS5.SSS0.Px5.p2).
- **Inference budget**: Beam size 50 with trie-based invalid-ID filtering and an end-of-item token. The industrial run uses 4 x A100-80GB; public benchmarks run on a single commodity GPU. CapsID+SemanticBPE runs at 51% of COBRA's per-query latency on the same ANN infrastructure; Table 4 reports cost normalized to TIGER beam search (B=50). Inference batch size and absolute latency: not reported.
  - Source: Beam 50, trie, end-of-item token: [A1.SS3.SSS0.Px3.p1](https://arxiv.org/html/2605.05096v1#A1.SS3.SSS0.Px3.p1); hardware: [A2.SS5.p1](https://arxiv.org/html/2605.05096v1#A2.SS5.p1); latency versus COBRA: [S4.SS5.SSS0.Px5.p2](https://arxiv.org/html/2605.05096v1#S4.SS5.SSS0.Px5.p2); normalized cost: [S4.T4](https://arxiv.org/html/2605.05096v1#S4.T4).
- **Results from**: Table 3 (Beauty, Sports, Toys; mean over three seeds); Table 4 (patching versus tokenizer-centric design, with normalized cost); Table 5 (ablations); Table 6 (35M-item industrial catalog, single run); Figure 3 (collision, purity, predictability); Table 10 (Beauty cold-item subset).
  - Source: Main table: [S4.T3](https://arxiv.org/html/2605.05096v1#S4.T3); patching comparison: [S4.T4](https://arxiv.org/html/2605.05096v1#S4.T4); ablation: [S4.T5](https://arxiv.org/html/2605.05096v1#S4.T5); industrial: [S4.T6](https://arxiv.org/html/2605.05096v1#S4.T6); cold subset: [A2.SS2.p1](https://arxiv.org/html/2605.05096v1#A2.SS2.p1).

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["CapsID"]
    P -->|competitor| A["COBRA"]
    P -->|competitor| B["TIGER"]
    P -->|competitor| C["ADC-SID"]
    P -->|competitor| D["ActionPiece"]
    P -->|competitor| E["ReSID"]
```

- **Competitor** · [COBRA](cobra.md): COBRA patches incomplete sparse IDs with a dense vector and BeamFusion at inference; CapsID instead makes the SID itself soft-routed and variable-length, without a dense path.
  - Source: CapsID v1, Section 4.1 baselines and fairness controls: https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px4.p1; Tables 3, 4, and 6: https://arxiv.org/html/2605.05096v1#S4.T3, https://arxiv.org/html/2605.05096v1#S4.T4, https://arxiv.org/html/2605.05096v1#S4.T6.
- **Competitor** · [TIGER](tiger.md): TIGER uses fixed-length hard RQ-VAE codes; CapsID routes residuals softly across capsules and stops at an item-specific length.
  - Source: CapsID v1, Section 4.1 baselines: https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px2.p1; Tables 3 and 6: https://arxiv.org/html/2605.05096v1#S4.T3 and https://arxiv.org/html/2605.05096v1#S4.T6.
- **Competitor** · [ADC-SID](adc-sid.md): CapsID labels this baseline ADA-SID and cites arXiv:2510.25622; it adapts behavior-content quantization with fixed-length codes, whereas CapsID varies code length per item.
  - Source: CapsID v1, Table 1 and Section 2 cite it as ADA-SID [34] (arXiv:2510.25622): https://arxiv.org/html/2605.05096v1#S2.T1; Section 4.1 baselines and Table 3: https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2605.05096v1#S4.T3.
- **Competitor** · [ActionPiece](actionpiece.md): ActionPiece merges feature tokens by co-occurrence frequency; CapsID's SemanticBPE uses a differentiable merge gate over learned capsule codes.
  - Source: CapsID v1, Section 2 capsule-routing and subword paragraph: https://arxiv.org/html/2605.05096v1#S2.SS0.SSS0.Px6.p1; Section 4.1 baselines and Table 3: https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2605.05096v1#S4.T3.
- **Competitor** · [ReSID](resid.md): ReSID uses adaptive semantic quantization with residual knowledge transfer; CapsID uses capsule routing with confidence-driven stopping.
  - Source: CapsID v1, Section 2: https://arxiv.org/html/2605.05096v1#S2.SS0.SSS0.Px4.p1; Section 4.1 baselines and Table 3: https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2605.05096v1#S4.T3; cold-start protocol follows ReSID: https://arxiv.org/html/2605.05096v1#A2.SS2.p1.

[View all papers in this cell](../../README.md#i--tokenization)
