## At a Glance

Key Findings: On the public dataset, Align3GR reports +17.8% in Recall@10 and +20.2% in NDCG@10 over the strongest baseline (Abstract).

### 1. Why This Paper Matters

Turning a large language model (LLM) into a recommender meets semantic and behavioral misalignment (Abstract). Earlier LLM recommenders such as LC-Rec align item tokens through supervised tasks. Align3GR treats alignment as one problem across token, behavior modeling, and preference levels.

> "To bridge this gap, we propose Align3GR, a novel framework that unifies token-level, behavior modeling-level, and preference-level alignment." (Abstract)

Based on arXiv v2.

### 2. How It Works

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

- Industrial deployment: the authors report gains in online A/B tests and full-scale deployment on an industrial recommendation platform (Abstract).

### 4. Limitations & Critical Analysis

**Our analysis.**

- The pipeline trains SCID tokenizers, multi-task SFT, and two DPO phases in sequence. This suggests that a catalog change requires repeating several stages.
- EAGER-LLM also feeds semantic and collaborative signals to a `Dec-Only` LLM, but with `Dual H-KM` codes; Align3GR uses `Dual RQ` codes and adds DPO.
