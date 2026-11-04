# MiniOneRec

[← 问题 × 阶段矩阵](../../../README.zh.md#范式系统与基准) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/minionerec.md) | 中文

| **题目** | *An Open-Source Framework for Scaling Generative Recommendation* |
| :-- | :-- |
| **作者** | Kong et al. |
| **发表** | arXiv’25 |
| **问题与阶段** | `范式、系统与基准` · `无单一阶段` |
| **改动** | ○ 训练目标 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **特殊设置** | `跨域迁移` |
| **应用场景** | `一般物品推荐`；`公开数据` |
| **链接** | [论文](https://arxiv.org/abs/2510.24431) · [代码](https://github.com/AkaliKong/MiniOneRec) |
| **阅读级别** | 阅读笔记（第 2 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text"] --> T["构码 Tokenization<br/>RQ-VAE"] --> B["生成骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ NTP → RL"] --> I["推理 Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP → RL`：先进行下一 token 预测微调，再执行强化学习（如 GRPO、GBPO 等）。
- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。

### TL;DR

> [!NOTE]
> MiniOneRec 是覆盖 RQ-VAE SID 构建、Qwen 骨干监督微调与受约束解码强化学习的开源框架，用于在公开基准上检验生成式扩展规律。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 主要发现 | 将 Qwen2.5 骨干从 0.5B 扩展至 7B 参数时训练损失与评估损失单调下降，结合全流程 SID 对齐、约束束采样与 GRPO 后在 Amazon Industrial 与 Office 上全面超越传统、生成式与 LLM 基线（Abstract，Sec. 5.2，Table 1，Fig. 1）。 |
| 局限 | 扩展定律实验仅度量模型增大时的训练损失与评估损失，未直接报告排序指标随规模的变化曲线（Sec. 5.2，Fig. 1）。 |

---

### 1. 为什么重要

用语义 ID（Semantic ID，SID）序列替代海量嵌入表的工业级生成式推荐器大多闭源，公开基准上模型参数扩展定律是否成立、怎样的最小后训练配方即可获得强竞争力仍缺乏系统验证。

> "Yet most industrial deployments remain proprietary, leaving two fundamental questions open: (1) Do the expected scaling laws hold on public benchmarks? (2) What is the minimal post-training recipe that enables competitive performance?"（Abstract）

MiniOneRec 开源复现了覆盖 RQ-VAE 物品编号、监督微调（SFT）全流程 SID 对齐与 GRPO 强化学习（RL）的完整流水线，并公开多尺寸模型代码、训练脚本与权重检查点（Sec. 1）。

---

### 2. 方法

![MiniOneRec architecture diagram](../../../architectures/minionerec.png)

```mermaid
flowchart LR
    subgraph TOK["阶段 1：物品离散编号"]
        A("物品标题与描述") --> B["冻结 Qwen3-Embedding-4B"]
        B --> C["3 层 × 256 RQ-VAE"]
        C --> D("SID token 扩充至 Qwen2.5 词表")
    end
    subgraph SFT_STAGE["阶段 2：全流程对齐 SFT"]
        D --> E["Qwen2.5-Instruct（0.5B–7B）微调"]
        L1{{"下一物品 NTP + 标题/描述 <-> SID 互译对齐"}} -.-> E
    end
    subgraph RL_STAGE["阶段 3：强化偏好优化"]
        E --> R["约束束搜索采样（束宽 16）"]
        R --> F["GRPO 策略更新"]:::key
        L1 -.-> F
        L2{{"二元命中奖励 + 困难负例软排序奖励"}}:::key -.-> F
    end
    F --> G["约束束搜索解码"]
    G --> H("Top-K 下一物品")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 物品编号

冻结的 Qwen3-Embedding-4B 文本编码器提取物品标题与描述嵌入，3 层 × 256 码字的 RQ-VAE 将每个物品量化为 3 位层级 SID（Sec. 3.2，Sec. 4）。

> "The codebooks, the encoder and the decoder are trained jointly, while the text encoder remains frozen."（Sec. 3.2）

#### 全流程 SID 对齐

三层共 3 × 256 个 SID token 直接追加进 Qwen2.5-Instruct 词表。下一物品 SID 预测与双向语言-SID 对齐任务（标题/描述与 SID 互译）贯穿 SFT 与后续 RL 全程联合优化，不在预热后丢弃（Sec. 3.3，Sec. 6）。

#### 强化偏好优化

RL 阶段采用 GRPO，以束宽为 16 的约束束搜索替代无约束多项式采样，确保每条提示采样出 16 个互异且合法的候选 SID（Sec. 3.4.1，Sec. 5.5.2）。混合奖励由精确命中的二元正确性奖励与拉大困难负例差距的软排序惩罚项组成（Sec. 3.4.2）。

> "The mixed reward discussed combines binary correctness with a soft ranking term, helping the LLM tell hard negatives apart."（Sec. 3.4.2）

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2023: Industrial and Scientific, Office Products. Trimming follows Bao et al. (2024): users and items with fewer than 5 interactions removed; events limited to October 1996-November 2018 for Industrial; histories truncated to at most 10 items. Retained sizes: in Appendix B (not restated here).
  - 出处：Datasets and trimming: [S5.SS1.p1](https://arxiv.org/html/2510.24431v1#S5.SS1.p1) and [A2.p1](https://arxiv.org/html/2510.24431v1#A2.p1).
- **切分**：Chronological 8:1:1 split into training, validation, and test. OOD study: train only on Industrial and evaluate on Office without tuning.
  - 出处：Chronological 8:1:1: [A2.p1](https://arxiv.org/html/2510.24431v1#A2.p1); OOD transfer: [S5.SS4.p1](https://arxiv.org/html/2510.24431v1#S5.SS4.p1).
- **候选集**：not reported explicitly (the policy predicts among all catalog candidates and returns the top-k beams; whether metrics are full-catalog is not stated).
  - 出处：Ranking among all catalog items via beam search: [S3.SS1.p2](https://arxiv.org/html/2510.24431v1#S3.SS1.p2).
- **可见性**：In-domain: warm; no unseen-item protocol is defined. OOD: Office items are unseen by the generator (trained only on Industrial); whether the RQ-VAE was fit on Office items: not reported.
  - 出处：In-domain chronological split; OOD on a never-seen domain: [S5.SS4.p1](https://arxiv.org/html/2510.24431v1#S5.SS4.p1) and [S5.SS4.p2](https://arxiv.org/html/2510.24431v1#S5.SS4.p2).
- **SID 规格**：3-level RQ-VAE x 256 codewords over Qwen3-Embedding-4B text embeddings; the three layers of 256 SID tokens are appended to the Qwen2.5-Instruct tokenizer vocabulary. Collision handling: not reported.
  - 出处：L=3 x K=256 RQ-VAE over Qwen3-Embedding-4B, SID tokens added to vocabulary: [S3.I1.i3.p1](https://arxiv.org/html/2510.24431v1#S3.I1.i3.p1), [S4.p1](https://arxiv.org/html/2510.24431v1#S4.p1), [A1.SS1.p2](https://arxiv.org/html/2510.24431v1#A1.SS1.p2); no collision rule found.
- **推理预算**：Constrained beam search returns the top-k list; the numerical width at evaluation is not reported (RL rollouts use beam width 16). SFT on 8 NVIDIA H100 GPUs; inference batch size and latency: not reported.
  - 出处：Beam search for recommendation lists and RL rollouts (width 16): [S3.SS1.p2](https://arxiv.org/html/2510.24431v1#S3.SS1.p2), [S3.SS4.SSS1.p4](https://arxiv.org/html/2510.24431v1#S3.SS4.SSS1.p4), [S5.SS5.SSS2.p1](https://arxiv.org/html/2510.24431v1#S5.SS5.SSS2.p1); hardware: [S4.p1](https://arxiv.org/html/2510.24431v1#S4.p1).
- **结果来源**：Table 1 (Industrial and Office versus traditional, generative, and LLM-based baselines); Table 2 (unseen Office domain); Table 3 (pre-trained versus random initialization); Figures 1 and 4 (scaling and rollout strategies).
  - 出处：Main: [S5.T1](https://arxiv.org/html/2510.24431v1#S5.T1); OOD: [S5.T2](https://arxiv.org/html/2510.24431v1#S5.T2); pre-training effect: [S5.T3](https://arxiv.org/html/2510.24431v1#S5.T3); rollout strategies: [S5.SS5.SSS2.p2](https://arxiv.org/html/2510.24431v1#S5.SS5.SSS2.p2).

</details>

- 规模扩展与主基准：Qwen2.5 骨干从 0.5B 增至 7B 时训练与评估损失单调下降（Sec. 5.2，Fig. 1），MiniOneRec 在 Amazon Industrial and Scientific 与 Office Products 上优于传统序列模型、SID 生成模型（TIGER、LC-Rec）及 LLM 推荐基线（Table 1）。
- 对齐策略与采样消融：在 SFT 与 RL 全程保留语言-SID 辅助对齐的变体在各项指标上均显著高于仅做早期对齐的变体（Sec. 5.5.1，Fig. 4a）；GRPO 训练中束宽 16 的约束束采样也稳定优于无约束采样（Sec. 5.5.2，Fig. 4）。
- 跨域迁移与预训练先验：仅在 Industrial 域训练后直接零样本评测未见过的 Office 域（Sec. 5.4，Table 2），以及从预训练 Qwen2.5 权重初始化对比从零随机初始化（Sec. 5.6，Table 3），均取得一致的排序收益。

---

### 4. 局限与分析

**Our analysis.**

- LC-Rec 仅通过 `Multi-task NTP` SFT 将 `Dec-Only` LLM 对齐到 `RQ-VAE` SID；MiniOneRec 将双向对齐任务一直保留至带约束束采样的 GRPO 强化学习阶段（`NTP → RL`）。
- 工业版 OneRec 使用 `R-KM` 从多模态与协同信号（`MM+CF`）构建 SID，而 MiniOneRec 仅用纯文本（`Text`）训练 `RQ-VAE`，未报告额外的冲突后缀消歧规则。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["MiniOneRec"]
    P -->|"前序工作"| A["OneRec"]
    P -->|"同期对比"| B["TIGER"]
    P -->|"同期对比"| C["LC-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **前序工作** · [OneRec](onerec.md): MiniOneRec is an open-source reproduction of the OneRec-style pipeline: SID construction, SFT, and RL with constrained beam rollouts on public data.
  - 出处：MiniOneRec v1, Section 1 positions it against OneRec: [S1.p1](https://arxiv.org/html/2510.24431v1#S1.p1) and [S1.p3](https://arxiv.org/html/2510.24431v1#S1.p3); Section 3.3: [S3.SS3.p1](https://arxiv.org/html/2510.24431v1#S3.SS3.p1).
- **同期对比** · [TIGER](tiger.md): TIGER trains a small generator with next-token prediction only; MiniOneRec uses an LLM with SID alignment tasks and GRPO.
  - 出处：MiniOneRec v1, Table 1 generative baselines: [S5.T1](https://arxiv.org/html/2510.24431v1#S5.T1).
- **同期对比** · [LC-Rec](lc-rec.md): LC-Rec aligns an LLM to SIDs with SFT tasks; MiniOneRec keeps such alignment throughout SFT and RL and adds reinforced preference optimization.
  - 出处：MiniOneRec v1, Table 1 generative baselines (LCRec): [S5.T1](https://arxiv.org/html/2510.24431v1#S5.T1); related work: [S2.SS1.p2](https://arxiv.org/html/2510.24431v1#S2.SS1.p2).

[查看同格全部论文](../../../README.zh.md#范式系统与基准)
