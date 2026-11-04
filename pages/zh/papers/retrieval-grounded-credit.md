# Retrieval-Grounded-Credit

[← 问题 × 阶段矩阵](../../../README.zh.md#iv--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/retrieval-grounded-credit.md) | 中文

| **题目** | *From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative Recommendation* |
| :-- | :-- |
| **作者** | Zhu et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `训练（Training）` |
| **改动** | ● 训练目标 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **链接** | [论文](https://arxiv.org/abs/2609.29983) · [代码](https://github.com/YuFan-Microsoft/Retrieval-Grounded-Credit-Assignment-for-Generative-Recommendation) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text†"] --> T["构码 Tokenization<br/>RQ-VAE"] --> B["生成骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ● NTP → RL"] --> I["推理 Inference<br/>CoT+C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `Text†`：物品文本表征（由配置推断）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP → RL`：先进行下一 token 预测微调，再执行强化学习（如 GRPO、GBPO 等）。
- `CoT+C-Beam`：显式推理后接合法前缀约束束搜索。

### TL;DR

> [!NOTE]
> Retrieval-Grounded-Credit 将每条推理轨迹拆为多个兴趣假设，分别作为查询送入冻结检索器，对命中目标的假设直接给予奖励而非仅奖励最终解码的 SID。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Video Games, Office Products, Industrial and Scientific; October 2016-November 2018 interactions, 5-core filtering, histories capped at 10 items.
  - 出处：v1 Section 4.1, pp. 5-6: [page=5](https://arxiv.org/pdf/2609.29983v1#page=5)
- **切分**：Per-user chronological last interaction test, penultimate validation; earlier interactions form sliding-window training pairs.
  - 出处：v1 Section 4.1, pp. 5-6: [page=5](https://arxiv.org/pdf/2609.29983v1#page=5)
- **候选集**：full catalog; trie contains all catalog SIDs, no sampled negatives.
  - 出处：v1 Section 4.1, p. 6: [page=6](https://arxiv.org/pdf/2609.29983v1#page=6)
- **可见性**：warm; no unseen-item protocol is defined. SIDReasoner tokenizers/mappings reused and frozen; tokenizer exposure to test items not reported.
  - 出处：v1 Sections 3.1/4.1, pp. 3/5-6 define no unseen-item holdout: [page=3](https://arxiv.org/pdf/2609.29983v1#page=3) and [page=5](https://arxiv.org/pdf/2609.29983v1#page=5)
- **SID 规格**：Domain-specific RQ-VAE: 3 levels x 256 codes; collision handling not reported.
  - 出处：v1 Section 3.1, p. 3: [page=3](https://arxiv.org/pdf/2609.29983v1#page=3)
- **推理预算**：Qwen3-1.7B; constrained beam returns 10 valid SIDs, metrics @5/10. Interests average 3.8/query set, each retrieves top-50 by frozen Qwen3-Embedding-4B exact cosine search. Hardware, inference batch size, latency not reported; training samples 16 trajectories/prompt, distinct from evaluation.
  - 出处：v1 Section 4.1, p. 6, Figure 5, p. 9: [page=6](https://arxiv.org/pdf/2609.29983v1#page=6) and [page=9](https://arxiv.org/pdf/2609.29983v1#page=9)
- **结果来源**：Original Table 4 RL controls/ours; external baselines are reported SIDReasoner results. Ours and SID-plus-trace control average three training seeds. Figure 5 interest-conditioned decoding includes target-aware oracle upper bounds.
  - 出处：v1 Section 4.1/Table 4, p. 6, Figure 5, p. 9: [page=6](https://arxiv.org/pdf/2609.29983v1#page=6) and [page=9](https://arxiv.org/pdf/2609.29983v1#page=9)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["Retrieval-Grounded-Credit"]
    P -->|"前序工作"| A["SIDReasoner"]
    P -->|"替代方案"| B["PROMISE"]
    P -->|"替代方案"| C["SAPO"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **前序工作** · [SIDReasoner](sidreasoner.md): Reuses SIDReasoner's tokenizer, alignment data, and evaluator; adds retrieval-grounded trace credit.
  - 出处：Retrieval-Grounded-Credit v1, Sections 3.1/3.2 and 4.1, pp. 3/6: [page=3](https://arxiv.org/pdf/2609.29983v1#page=3); [page=6](https://arxiv.org/pdf/2609.29983v1#page=6).
- **替代方案** · [PROMISE](promise.md): PROMISE rewards intermediate SID paths; this method verifies language interests through retrieval.
  - 出处：Retrieval-Grounded-Credit v1, Section 2.3, p. 3: [page=3](https://arxiv.org/pdf/2609.29983v1#page=3).
- **替代方案** · [SAPO](sapo.md): SAPO aligns reasoning blocks with SID tokens; this method attributes query hits to interest lines.
  - 出处：Retrieval-Grounded-Credit v1, Section 2.3, p. 3: [page=3](https://arxiv.org/pdf/2609.29983v1#page=3).

[查看同格全部论文](../../../README.zh.md#iv--training)
