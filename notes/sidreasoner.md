## At a Glance

Limitation: The RL reward scores only the generated Semantic ID, by its longest correct prefix and whether it maps to a catalog item, and not the reasoning text (Sec. 3.3.2).

### 1. Why This Paper Matters

LLM-based generative recommenders already share one token space for language and Semantic IDs (SIDs), but reasoning over SIDs is hard: itemic tokens carry no native meaning for an LLM, and recommendation reasoning has little high-quality supervision (Abstract). SIDReasoner strengthens SID-language alignment first, so that the LLM's general reasoning can carry over to recommendation without many recommendation-specific reasoning traces.

> "Stronger SID–language alignment can help general reasoning abilities better generalize to recommendation tasks." (Sec. 5)

### 2. How It Works

```mermaid
flowchart LR
    A[Teacher-enriched corpus] --> B[Multi-task alignment]
    B --> C[Reasoning activation]
    C --> D[Outcome-based GRPO]
    D --> E[Reasoning text]
    E --> F[SID]
```

#### SID-Language Alignment

Multi-task training covers next-item prediction and bidirectional translation between SIDs and item titles (Sec. 3.2.2). A teacher model enriches item descriptions in item-centric and user-centric forms, and general reasoning data is mixed in (Sec. 3.2.3).

#### Reasoning Activation

A short supervised stage teaches the model to write reasoning before the recommendation (Sec. 3.3.1). The paper calls it cold-start reasoning activation; it concerns the response format, not cold-start users or items.

> "This stage mainly serves to improve the reliability of response formatting, ensuring that reasoning is consistently generated before recommendation." (Sec. 3.3.1)

#### Outcome-Based GRPO

GRPO samples groups of reasoning-and-prediction trajectories and optimizes them with rewards from recommendation accuracy (Sec. 3.3.2, Eqs. 6–8).

### 3. Experimental Findings

- Alignment strategies: adding the enriched corpus to multi-task alignment improves results, and each variant is reported before and after RL (Table 3).
- Cross-domain: after joint SID-language alignment on all domains, the paper compares RL on a single domain with RL on all domains (Sec. 4.2.2, Fig. 3).

  > "Such reasoning knowledge, once learned, can be transferred across domains." (Sec. 4.2.2)

- Reasoning length: the length of the reasoning text decreases during RL (Sec. 4.4.2, Fig. 6).

### 4. Limitations & Critical Analysis

**Our analysis.**

- LC-Rec aligns a `Dec-Only` LLM to `RQ-VAE` SIDs with `Multi-task NTP`; SIDReasoner keeps that kind of alignment and adds an RL stage (`NTP → RL`).
- TIGER predicts `RQ-VAE` SIDs with a small `Enc-Dec` generator trained by `NTP`; SIDReasoner uses the same kind of SIDs with a `Dec-Only` LLM.
