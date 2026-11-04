# SAPO

[← 问题 × 阶段矩阵](../../../README.zh.md#iv--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/sapo.md) | 中文

| **题目** | *Step-Aligned Policy Optimization for Reasoning-Based Generative Recommendation* |
| :-- | :-- |
| **作者** | Zheng et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `训练（Training）` |
| **改动** | ● 训练目标 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **链接** | [论文](https://arxiv.org/abs/2605.17648) · [代码](https://github.com/zhengzaiyi/SAPO) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text"] --> T["构码 Tokenization<br/>RQ-VAE"] --> B["生成骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ● NTP → RL"] --> I["推理 Inference<br/>CoT+C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP → RL`：先进行下一 token 预测微调，再执行强化学习（如 GRPO、GBPO 等）。
- `CoT+C-Beam`：显式推理后接合法前缀约束束搜索。

### TL;DR

> [!NOTE]
> SAPO 以一个思考块加一个 SID token 为一步，为每个推理步单独计算组相对优势，替代将单一精确匹配优势广播到整段回复的做法。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews Office Products, Video Games, Industrial & Scientific; October 2016-November 2018; 5-core users/items. Further history truncation not reported.
  - 出处：[S5.SS1.p1](https://arxiv.org/html/2605.17648v1#S5.SS1.p1) ; #A8.p1
- **切分**：Per-user chronological leave-one-out: last item test, second last validation, remaining prefix training; all valid sliding-window history/target pairs used for training.
  - 出处：[A8.p1](https://arxiv.org/html/2605.17648v1#A8.p1)
- **候选集**：not reported
  - 出处：[S5.SS1](https://arxiv.org/html/2605.17648v1#S5.SS1) ; #S5.SS2.p1 ; #A8
- **可见性**：warm; no unseen-item protocol is defined. Tokenizer fitting exposure to test items not explicitly separated.
  - 出处：[A8.p1](https://arxiv.org/html/2605.17648v1#A8.p1) ; #A8.p3
- **SID 规格**：RQ-VAE: 3 x 256 over title/category/brand/description embeddings. Paper reports training until every item has a unique tuple, with no extra collision suffix; a separate collision-assignment rule is not reported.
  - 出处：[A8.p3](https://arxiv.org/html/2605.17648v1#A8.p3)
- **推理预算**：Qwen3-1.7B generates three thinking blocks followed by three contiguous SID tokens, enabling trie-constrained beam decoding and KV reuse; Recall/NDCG@5/10. Test beam width, reasoning cap, hardware allocation, batch size and latency not reported. The 16 rollouts/prompt, 1024-token cap and 4 H100s are training settings.
  - 出处：[A6.p2](https://arxiv.org/html/2605.17648v1#A6.p2) ; #A9.SS2.p1 ; #A10.p1 ; #A11.p2
- **结果来源**：Original Table 1: main comparison; SIDReasoner uses author checkpoints evaluated by this paper, all other baselines reimplemented. Table 2: SAPO component ablations; Table 7: training overhead, not inference latency.
  - 出处：[S5.T1](https://arxiv.org/html/2605.17648v1#S5.T1) ; #S5.T2 ; #S5.SS1.p2 ; #A12.T7

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["SAPO"]
    P -->|"前序工作"| A["SIDReasoner"]
    P -->|"同期对比"| B["OneRec-Think"]
    P -->|"同期对比"| C["TIGER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **前序工作** · [SIDReasoner](sidreasoner.md): SAPO shares SIDReasoner Stage 1/2 checkpoints but replaces rollout-level Stage 3 credit with rewards and advantages for thinking-block/SID-token pairs.
  - 出处：SAPO v1, Appendix G and Section 5.2: [A7.p3](https://arxiv.org/html/2605.17648v1#A7.p3); [S5.SS2.p2](https://arxiv.org/html/2605.17648v1#S5.SS2.p2).
- **同期对比** · [OneRec-Think](onerec-think.md): OneRec-Think is a reasoning-based generative baseline with outcome-level feedback; SAPO localizes RL credit to individual SID reasoning steps.
  - 出处：SAPO v1, Appendix G and Table 1: [A7.p3](https://arxiv.org/html/2605.17648v1#A7.p3); [S5.T1](https://arxiv.org/html/2605.17648v1#S5.T1).
- **同期对比** · [TIGER](tiger.md): TIGER is the non-reasoning residual-SID generation baseline; SAPO adds structured reasoning and step-aligned policy optimization.
  - 出处：SAPO v1, Appendix G and Table 1: [A7.p2](https://arxiv.org/html/2605.17648v1#A7.p2); [S5.T1](https://arxiv.org/html/2605.17648v1#S5.T1).

[查看同格全部论文](../../../README.zh.md#iv--training)
