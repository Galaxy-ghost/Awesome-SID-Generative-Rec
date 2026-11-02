## At a Glance

Key Findings: LETTER improves both backend models, TIGER and LC-Rec, on Instruments, Beauty, and Yelp, and adding either the collaborative or the diversity regularization alone improves TIGER (Tables 1 and 2).
Limitation: The tokenizer is trained before the generator and then kept fixed, and the collaborative regularization needs embeddings from a separately trained CF model (Sec. 3.1, Sec. 3.2).

### 1. Why This Paper Matters

Earlier item identifiers, whether plain IDs, text, or codebook codes, fall short in encoding semantics, carrying collaborative signals, or handling code assignment bias (Abstract). LETTER keeps an RQ-VAE tokenizer for the semantic part and adds a collaborative regularization and a diversity regularization to it. The learned Semantic IDs (SIDs) then serve two generators, TIGER and LC-Rec (Sec. 4.1.4).

> "LETTER incorporates Residual Quantized VAE for semantic regularization, a contrastive alignment loss for collaborative regularization, and a diversity loss to mitigate code assignment bias." (Abstract)

### 2. How It Works

#### Semantic Regularization

An RQ-VAE quantizes the item's semantic embedding level by level, so the identifier keeps a coarse-to-fine semantic hierarchy (Sec. 3.1). The main configuration uses 4 levels with 256 codewords each (Sec. 4.1.4).

#### Collaborative Regularization

A contrastive alignment loss pulls each item's quantized embedding toward its embedding from a trained collaborative filtering (CF) model (Sec. 3.1, Eq. 3). The paper names LightGCN as an example CF model (Sec. 1).

> "Intuitively, collaborative regularization encourages items with similar collaborative interactions to exhibit similar code sequences." (Sec. 3.1)

#### Diversity Regularization

A diversity loss spreads the code embeddings apart, using clusters from constrained k-means (Sec. 3.1, Eq. 4). It targets code assignment bias, where some codes receive more items than others, and item generation bias (Sec. 1).

> "As illustrated in Figure 5(a), a biased code embedding distribution is more likely to cause biased code assignment in the latent space, where some codes are assigned to more items." (Sec. 3.1)

#### Training and Generation

LETTER first trains the tokenizer with the combined loss (Eq. 5), then uses it to tokenize items for training and inference of the generator (Sec. 3.2). LETTER also adds a ranking-guided generation loss to the generator's training to improve its ranking ability (Abstract, Sec. 1). At inference, a trie restricts generation to valid identifiers.

> "To ensure generating valid identifiers, we follow (Hua et al., 2023) to employ constrained generation (De Cao et al., 2020) via Trie" (Sec. 3.2.2)

### 3. Experimental Findings

- Main results: LETTER-TIGER and LETTER-LC-Rec outperform their backend models on Instruments, Beauty, and Yelp (Sec. 4.2, Table 1).
- Ablation: adding either the collaborative or the diversity regularization to TIGER improves its performance (Sec. 4.3.1, Table 2).
- Code usage: the collaborative regularization lowers the number of codes that TIGER uses, and the diversity regularization raises it again (Sec. 4.3.2, Fig. 6).

  > "Although adding collaborative regularization decreases the code utilization of TIGER (from 148 to 76), integrating diversity regularization inversely compensates for the drop in code utilization." (Sec. 4.3.2)

- Collaborative signals: Tables 3 and 4 analyze how well the identifiers carry collaborative information (Sec. 4.3.4).
- Hyperparameters: the paper varies the identifier length $`L`$, the codebook size $`N`$, the loss weights $`\alpha`$ and $`\beta`$, the cluster number $`K`$, and the temperature $`\tau`$ (Sec. 4.3.5).

### 4. Limitations & Critical Analysis

**Stated by the authors.** The authors report two settings where a larger value hurts performance (Sec. 4.3.5). Longer identifiers lower performance, which they attribute to error accumulation in autoregressive generation:

> "Continuously increasing the identifier length from 4 to 8 will inversely degrade the performance. This is reasonable because autoregressive generation suffers from error accumulation (Ren et al., 2024b)." (Sec. 4.3.5)

A larger codebook can also hurt:

> "However, 2) blindly expanding N might inversely hurt the performance, where larger codebook size might be more susceptible to noise in the item's semantic information, potentially leading to the over-fitting of some meaningless semantics." (Sec. 4.3.5)

**Our analysis.**

- The tokenizer is trained once and then fixed (`Fixed`), so a change in the catalog requires retraining the tokenizer and re-tokenizing items. ETEGRec updates the tokenizer and the generator in turns (`Altern.`), and DIGER lets the generator loss update the tokenizer directly (`Joint`).
- The collaborative regularization needs a CF embedding for every item. This suggests that items without interactions receive no collaborative signal in their identifiers.
- The collaborative and diversity terms pull code usage in opposite directions (Sec. 4.3.2), so their weights trade one property against the other.
