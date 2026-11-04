# CausalDPO

[← 问题 × 阶段矩阵](../../../README.zh.md#vi--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/causaldpo.md) | 中文

| **题目** | *Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation* |
| :-- | :-- |
| **作者** | Zhao et al. |
| **发表** | ICML’26 |
| **问题与阶段** | `VI. 泛化` · `训练（Training）` |
| **改动** | ● 训练目标 |
| **构码输入** | `n/a` |
| **领域** | `本地生活与 POI` · `电影` · `图书与有声书` |
| **链接** | [论文](https://arxiv.org/abs/2603.22335) · [代码](https://github.com/user683/CausalDPO) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text"] --> T["构码 Tokenization<br/>LLM-Vocab"] --> B["生成骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ● NTP → DPO"] --> I["推理 Inference<br/>Scoring"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `LLM-Vocab`：直接从大语言模型原生词表 token 组合出的物品标识符。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP → DPO`：先进行下一 token 预测微调，再执行直接偏好优化（DPO）。
- `Scoring`：直接计算候选物品得分，不逐位生成 SID。

### TL;DR

> [!NOTE]
> CausalDPO 为基于 LLM 的推荐扩展 DPO，加入后门调整、隐环境软聚类与不变性约束，消除分布偏移下被 DPO 放大的虚假相关。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Yelp2018, MovieLens-10M, and Book-Crossing. Users with at least 40 interactions (Yelp2018) or 20 interactions (ML-10M, Book-Crossing) are kept; ratings above 4 (ML-10M, Yelp2018) or above 7 (Book-Crossing) are positives. Sizes (sequences / items / interactions): ML-10M 71,567 / 10,681 / 10,000,054; Yelp2018 31,668 / 38,048 / 1,561,406; Book-Crossing 278,858 / 271,379 / 1,149,780.
  - 出处：Dataset list: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1); user thresholds and positive-rating rules: [A2.SS1.p1](https://arxiv.org/html/2603.22335v2#A2.SS1.p1); statistics: [A2.T2](https://arxiv.org/html/2603.22335v2#A2.T2).
- **切分**：Distribution-shift splits: popularity shift (Yelp2018) samples 20% of interactions as a popularity-balanced OOD test set; temporal shift (ML-10M) takes each user's latest 20% of interactions; exposure shift (Book-Crossing) takes the most recent 20% and imputes a fully exposed test set by matrix factorization; mixed shift (Yelp2018) samples 80% popularity-shift and 20% temporal-shift test interactions. The remainder is split 7:1:2 into training, validation, and IID test.
  - 出处：Shift constructions: [A2.I2.i1.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i1.p1), [A2.I2.i2.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i2.p1), [A2.I2.i3.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i3.p1), and [A2.I2.i4.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i4.p1).
- **候选集**：full catalog (generated items are scored and ranked over the entire item space and mapped to dataset items).
  - 出处：Scoring and ranking over the entire item space: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1).
- **可见性**：warm; no unseen-item protocol is defined. The distribution shifts concern popularity, time, and exposure of user-item interactions, not unseen items; tokenizer n/a.
  - 出处：OOD shifts concern popularity, time, and exposure, not unseen items: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1) and [A2.I2.i1.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i1.p1).
- **SID 规格**：n/a (items are generated as text by the LLM and mapped to dataset items; no semantic IDs).
  - 出处：Prompts generate items as text: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1); the item is represented through text in the prompt formulation: [S2.p1](https://arxiv.org/html/2603.22335v2#S2.p1).
- **推理预算**：Llama-3.1-8B; decoding strategy and width: not reported. Experiments run on one node with 8 NVIDIA A800 80GB GPUs; inference batch size and latency: not reported. Table 6 reports training time per epoch (CausalDPO 2,971 s versus DPO 2,482 s). HR and NDCG at K=10 and 20.
  - 出处：Hardware: [A2.SS3.p1](https://arxiv.org/html/2603.22335v2#A2.SS3.p1); training time per epoch: [A2.T6](https://arxiv.org/html/2603.22335v2#A2.T6).
- **结果来源**：Table 1 (popularity, temporal, and exposure shifts on Yelp2018, ML-10M, Book-Crossing); Table 4 (mixed shift); Table 3 (IID test sets); Table 5 (causal regularizer added to other DPO variants); Table 8 (ablations); Table 9 (model sizes).
  - 出处：OOD table: [S3.T1](https://arxiv.org/html/2603.22335v2#S3.T1); IID: [A2.T3](https://arxiv.org/html/2603.22335v2#A2.T3); mixed shift: [A2.T4](https://arxiv.org/html/2603.22335v2#A2.T4); regularizer transfer: [A2.T5](https://arxiv.org/html/2603.22335v2#A2.T5); ablation: [A2.T8](https://arxiv.org/html/2603.22335v2#A2.T8); model sizes: [A2.T9](https://arxiv.org/html/2603.22335v2#A2.T9).

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["CausalDPO"]
    P -->|"替代方案"| A["OneRec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A peer
```

- **替代方案** · [OneRec](onerec.md): OneRec uses iterative preference alignment for a generative recommender with semantic IDs; CausalDPO adds backdoor adjustment over latent environments to DPO for text-generating LLM recommenders under distribution shift.
  - 出处：CausalDPO v2, Section 4 cites Deng et al. (2025), OneRec, among DPO adoptions in recommendation: [S4.p2](https://arxiv.org/html/2603.22335v2#S4.p2); not a baseline in Table 1.

[查看同格全部论文](../../../README.zh.md#vi--training)
