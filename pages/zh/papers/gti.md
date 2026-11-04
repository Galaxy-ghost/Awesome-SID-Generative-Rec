# GTI

[← 问题 × 阶段矩阵](../../../README.zh.md#iii--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/gti.md) | 中文

| **题目** | *Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation* |
| :-- | :-- |
| **作者** | Chen et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `III. SID 与模型对齐` · `训练（Training）` |
| **改动** | ● 训练目标 |
| **构码输入** | A: `Text` + `CF` · B: `Text` |
| **领域** | `招聘` · `电商` |
| **应用场景** | `一般物品推荐`；`工业数据离线` |
| **链接** | [论文](https://arxiv.org/abs/2604.02324) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text+CF / Text"] --> T["构码 Tokenization<br/>RQ-VAE"] --> B["生成骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ● Multi-task NTP"] --> I["推理 Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `Text+CF / Text`：不同配置下分别采用文本加协同信号或纯文本表征。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `Multi-task NTP`：在多个对齐或推荐子任务上联合优化下一 token 预测损失。

### TL;DR

> [!NOTE]
> GTI 在微调前借助配对语言监督，把新增 SID token 映射到预训练嵌入空间中的区分性位置，而非用已有嵌入的均值初始化。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Industrial recruitment pairs (good matches for SFT; profiles require at least one listed attribute); Vibrent rentals; other filtering not reported.
  - 出处：[S7.SS1](https://arxiv.org/html/2604.02324v1#S7.SS1)
- **切分**：Vibrent: leave-one-out; validation details not reported. Industry: 200 evaluation jobs; train/test separation not reported.
  - 出处：[S4.SS1.SSS0.Px3.p1](https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px3.p1)
- **候选集**：not reported; 200 retrieved candidates per industrial query does not specify the evaluation universe.
  - 出处：[S4.SS1.SSS0.Px3.p1](https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px3.p1) (200 retrieved candidates is an output count, not a negative-sampling protocol).
- **可见性**：warm; no unseen-item protocol is defined. Industrial Mistral-E5 uses engagement supervision; test-candidate exposure not reported.
  - 出处：[S4.SS1.SSS0.Px4.p2](https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px4.p2) and #S4.SS1.SSS0.Px4.p3
- **SID 规格**：RQ-VAE SIDs from 1024-d embeddings. Industry: engagement-tuned Mistral-E5 embeddings, 3 x 8192. Vibrent: Qwen3-Embedding-0.6B embeddings, 4 x 256 with 32-d codes and the Wang et al. (2024) diversity regularizer for balanced codebook use. The appendix's 4 x 256 configuration additionally uses final-layer Sinkhorn-Knopp balancing to reduce collisions; residual collision resolution is not reported.
  - 出处：[S4.SS1.SSS0.Px4.p2](https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px4.p2) ; [S4.SS1.SSS0.Px4.p3](https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px4.p3) ; [S7.SS3.p2](https://arxiv.org/html/2604.02324v1#S7.SS3.p2)
- **推理预算**：K=5/10/20/50/100. Experiments use four H100s; inference-specific hardware, beam width, batch size and latency not reported.
  - 出处：[S4.T1](https://arxiv.org/html/2604.02324v1#S4.T1) ; #S4.T3 ; #S4.SS1.SSS0.Px4.p1
- **结果来源**：Original experiments: Tables 1-2 industrial relative gains; Table 3 Vibrent relative gains; Table 4 absolute metrics.
  - 出处：[S4.T1](https://arxiv.org/html/2604.02324v1#S4.T1) ; #S4.T2 ; #S4.T3 ; #S7.T4

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["GTI"]
    P -->|"前序工作"| A["TIGER"]
    P -->|"同期对比"| B["LC-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B peer
```

- **前序工作** · [TIGER](tiger.md): GTI adopts TIGER-style RQ-VAE semantic identifiers.
  - 出处：[S7.SS3.p2](https://arxiv.org/html/2604.02324v1#S7.SS3.p2) (Appendix 7.3).
- **同期对比** · [LC-Rec](lc-rec.md): LC-Rec uses multi-task alignment; GTI adds grounding before fine-tuning.
  - 出处：[S4.SS1.SSS0.Px2.p3](https://arxiv.org/html/2604.02324v1#S4.SS1.SSS0.Px2.p3) ; #S4.T1 ; #S7.T4.

[查看同格全部论文](../../../README.zh.md#iii--training)
