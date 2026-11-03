# ETEGRec

[← 问题 × 阶段矩阵](../../../README.zh.md#iii--training) · [按阶段索引](../index/stages.md) · [按模态索引](../index/modality.md) · [English](../../papers/etegrec.md) | 中文

| **题目** | *Generative recommender with end-to-end learnable item tokenization* |
| :-- | :-- |
| **作者** | Liu et al. |
| **发表** | SIGIR’25 |
| **问题与阶段** | `III. SID 与模型对齐` · `训练（Training）` |
| **链接** | [论文](https://arxiv.org/abs/2409.05546) · [代码](https://github.com/RUCAIBox/ETEGRec) |
| **阅读级别** | 阅读笔记（第 2 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["表征 Representation<br/>CF"] --> T["编号 Tokenization<br/>Learn. RQ"] --> B["骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>Altern. / NTP + Ctr."] --> I["推理 Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `CF`：纯协同过滤交互信号。
- `Learn. RQ`：端到端或交替更新的可学习残差量化。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Altern.`：编号器与生成器在训练过程中交替迭代更新。
- `NTP + Ctr.`：下一 token 预测结合对比学习损失。
- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。

### TL;DR

> [!NOTE]
> ETEGRec 用序列-物品对齐损失与偏好-语义对齐损失交替训练物品编号器和生成器，替代先独立训练编号器再训练生成器的两阶段流程。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | III. SID 与模型对齐：生成模型能否理解并推理离散 SID，编号器与生成器的优化目标是否一致？ |
| 核心贡献 | ETEGRec 用序列-物品对齐损失与偏好-语义对齐损失交替训练物品编号器和生成器，替代先独立训练编号器再训练生成器的两阶段流程。 |
| 主要改动阶段 | 训练（Training） |
| 主要发现 | 在 Amazon Musical Instruments、Industrial and Scientific 与 Video Games 的全量目录评测中，ETEGRec 在 Recall@5/10 和 NDCG@5/10 上优于序列推荐及固定编号器生成式基线（含 TIGER、LETTER 和 CID），并在留出的未见新用户（交互最少的 5% 用户）上保持领先（Sec. 4.2，Sec. 4.4.1，Table 3，Table 4，Fig. 2）。 |
| 局限 | RQ-VAE 编号器仅读取协同物品嵌入，无历史交互的新物品无法获得离散编码，且论文未报告实测推理延迟（Sec. 3.2.1，Sec. 3.5）。 |

---

### 1. 为什么重要

两阶段生成式推荐模型先离线训练语义 ID（Semantic ID，SID）编号器并冻结物品编码，再独立训练序列生成器，导致离散编号空间与自回归推荐目标脱节（Abstract）。ETEGRec 在双编码器-解码器框架内统一物品编号器与序列生成器，通过两项对齐损失与交替优化实现协同训练。

> "To enable synergistic interaction between these components, we propose a recommendation-oriented alignment strategy, which includes two key optimization objectives: sequence-item alignment and preference-semantic alignment."（Abstract）

---

### 2. 方法

![ETEGRec architecture diagram](../../../architectures/etegrec.png)

```mermaid
flowchart LR
    subgraph Tok["物品编号器（双分支之 1）"]
        A("256 维 SASRec 协同嵌入") --> B["3×256 RQ-VAE 编号器（128 维）"]:::key
        B --> C("4 位 SID（含消歧 token）")
        B --> Z("重建的物品语义表征")
    end
    subgraph Gen["自回归生成器（双分支之 2）"]
        C --> Enc["T5 编码器（6 层）"]
        Enc --> S("序列编码隐状态")
        S --> Dec["T5 解码器（6 层）"]
        Dec --> P("解码出的用户偏好表征")
        Dec --> BM["束搜索（束宽 20）"]
    end
    S --> L1{{"序列-物品 KL 对齐（Eq. 15）"}}:::key
    A --> L1
    P --> L2{{"偏好-语义 InfoNCE 对齐（Eq. 16）"}}:::key
    Z --> L2
    L1 -.-> B
    L1 -.-> Enc
    L2 -.-> B
    L2 -.-> Dec
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 物品编号器

物品编号器读取每个物品的 256 维协同嵌入（如由 SASRec 提取），经 3 层 RQ-VAE（每层含 256 个 128 维码字）逐层残差量化，并在末尾附加 1 个唯一性消歧 token，组成 4 位 SID（Sec. 3.2.1，Sec. 4.1.4）。

> "By taking a hierarchical scheme, we essentially organize the items in a tree-structured way, which is particularly suitable for generative tasks."（Sec. 3.2.1）

#### 面向推荐的对齐

序列-物品对齐最小化生成器编码器序列隐状态与目标物品协同嵌入经量化后的 token 分布散度（Sec. 1，Eq. 15）。偏好-语义对齐则在生成器解码器输出的用户偏好表征与 RQ-VAE 解码器重建的目标物品语义表征之间施加对比学习约束（Sec. 1，Eq. 16）。

#### 交替优化

直接联合反传梯度会在生成器尚未收敛时频繁改变物品离散编码；ETEGRec 改用交替优化策略：在编号器阶段固定生成器，用量化损失与两项对齐损失更新 RQ-VAE；在生成器阶段固定 SID，用下一 token 预测损失与对齐损失更新 T5 生成器（Sec. 3.4）。

> "In order to improve the training stability, we propose an alternating optimization strategy to mutually train the item tokenizer and the generative recommender."（Sec. 3.4）

```mermaid
flowchart LR
    subgraph Ph1["阶段 1：更新编号器（固定生成器）"]
        LTok{{"VQ + SIA + PSA 损失"}} -.-> T1["更新 RQ-VAE 码本"]:::key
        T1 --> Refresh("刷新全库物品 SID")
    end
    subgraph Ph2["阶段 2：更新生成器（固定编号器）"]
        Refresh --> G1["更新 6 层 T5 编码器-解码器"]:::key
        LGen{{"NTP + SIA + PSA 损失"}} -.-> G1
    end
    G1 -->|"下一轮交替"| LTok
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon 2023 Reviews (May 1996-September 2023): Musical Instruments, Industrial and Scientific, Video Games; 5-core filtering of users and items; sequences capped at 50 items. Sizes (users / items / interactions): Instrument 57,439 / 24,587 / 511,836; Scientific 50,985 / 25,848 / 412,947; Game 94,762 / 25,612 / 814,586.
  - 出处：Amazon 2023 subsets, 5-core filter, sequence length 50: [S4.SS1.SSS1.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS1.p1); statistics: [S4.T2](https://arxiv.org/html/2409.05546v3#S4.T2).
- **切分**：Per-user leave-one-out: latest interaction for test, second most recent for validation, the rest for training. Separate generalization study on Instrument and Scientific: the 5% of users with the least history are removed from training and evaluated as unseen users.
  - 出处：Leave-one-out allocation: [S4.SS1.SSS3.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS3.p1); unseen-user experiment: [S4.SS4.SSS1.p1](https://arxiv.org/html/2409.05546v3#S4.SS4.SSS1.p1).
- **候选集**：full catalog
  - 出处：Full ranking over the entire item set: [S4.SS1.SSS3.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS3.p1).
- **可见性**：Main: warm; no unseen-item protocol is defined. The generalization study holds out users, not items: test users are unseen by both tokenizer and generator training, while item visibility is unchanged.
  - 出处：Main protocol and unseen-user study: [S4.SS1.SSS3.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS3.p1) and [S4.SS4.SSS1.p1](https://arxiv.org/html/2409.05546v3#S4.SS4.SSS1.p1).
- **SID 规格**：3-level RQ-VAE x 256 codewords (dimension 128) over 256-dimensional SASRec collaborative embeddings; following TIGER, an extra token is appended to make IDs unique. The tokenizer is trained jointly with the generator by alternating optimization.
  - 出处：3 codebooks x 256, dimension 128, extra uniqueness token: [S4.SS1.SSS4.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS4.p1); SASRec embeddings as input: [S4.SS1.SSS4.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS4.p1).
- **推理预算**：Beam size 20 for all generative models; T5 with 6 encoder and 6 decoder layers. Recall and NDCG at K=5 and 10. Hardware, inference batch size, and latency: not reported (Section 3.5 gives asymptotic complexity only).
  - 出处：Beam size 20 for all generative models: [S4.SS1.SSS3.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS3.p1); backbone: [S4.SS1.SSS5.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS5.p1); complexity analysis only: [S3.SS5.SSS2.p1](https://arxiv.org/html/2409.05546v3#S3.SS5.SSS2.p1).
- **结果来源**：Table 3 (Instrument, Scientific, Game; paired t-tests); Table 4 (alignment-loss and alternating-training ablations); Figure 2 (seen versus unseen users); Figure 4 (alignment coefficients).
  - 出处：Main: [S4.T3](https://arxiv.org/html/2409.05546v3#S4.T3); ablation: [S4.T4](https://arxiv.org/html/2409.05546v3#S4.T4); seen/unseen users: [S4.F2](https://arxiv.org/html/2409.05546v3#S4.F2); coefficients: [S4.F4](https://arxiv.org/html/2409.05546v3#S4.F4).

</details>

- 全量目录对比：在 5-core 过滤的 Amazon 2023 Musical Instruments（57,439 用户 / 24,587 物品）、Industrial and Scientific（50,985 / 25,848）与 Video Games（94,762 / 25,612）上（束宽 20），ETEGRec 在 Recall@5/10 与 NDCG@5/10 上显著优于序列推荐与生成式基线（配对 t 检验）（Abstract，Sec. 4.1，Table 2，Table 3）。
- 对齐与优化消融：移除序列-物品对齐、偏好-语义对齐或交替更新策略均会降低推荐精度，证实端到端编号器反馈优于固定编号方案（Table 4，Fig. 4）。
- 未见新用户泛化：在 Musical Instruments 和 Industrial and Scientific 上将交互最少的 5% 用户从编号器与生成器训练集中同时留出作为未见用户，ETEGRec 在已见与未见两组用户上均优于 LETTER 和 TIGER（Sec. 4.4.1，Fig. 2）。

---

### 4. 局限与分析

**Our analysis.**

- 交替训练阶段之间刷新编号器会在训练中途改变物品 SID，需要周期性重算全库物品编码以维持生成器输入一致（Sec. 3.4）。
- Sec. 3.5 仅给出渐近复杂度分析，未报告实际端到端训练耗时开销或在线推理延迟。
- LETTER 同样利用协同信号正则化 `Learn. RQ` 编码，但在生成器训练前即冻结编号器（`Fixed`）；ETEGRec 则交替更新 `Learn. RQ` 编号器与 `Enc-Dec` 生成器（`Altern.`）。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["ETEGRec"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"同期对比"| B["LETTER"]
    P -->|"同期对比"| C["CID"]
    P -->|"替代方案"| D["AdaSID"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **同期对比** · [TIGER](tiger.md): TIGER trains the RQ-VAE tokenizer once and freezes it; ETEGRec optimizes tokenizer and generator alternately with sequence-item and preference-semantic alignment losses.
  - 出处：ETEGRec v3, baselines and implementation: [S4.SS1.SSS2.p1](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS2.p1) and [S4.SS1.SSS5.p2](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS5.p2); Table 3: [S4.T3](https://arxiv.org/html/2409.05546v3#S4.T3); unseen-user comparison in Figure 2: [S4.SS4.SSS1.p1](https://arxiv.org/html/2409.05546v3#S4.SS4.SSS1.p1).
- **同期对比** · [LETTER](letter.md): LETTER regularizes the tokenizer before generator training; ETEGRec couples the two end to end during training.
  - 出处：ETEGRec v3, Table 1 comparison of methods: [S3.T1](https://arxiv.org/html/2409.05546v3#S3.T1); baselines with official implementation: [S4.SS1.SSS5.p2](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS5.p2); Table 3: [S4.T3](https://arxiv.org/html/2409.05546v3#S4.T3).
- **同期对比** · [CID](cid.md): CID and SID (Hua et al., 2023) are fixed indexing schemes for P5-style models; ETEGRec learns the tokenizer jointly with the recommender.
  - 出处：ETEGRec v3, Table 1: [S3.T1](https://arxiv.org/html/2409.05546v3#S3.T1); baselines CID and SID with official implementations: [S4.SS1.SSS5.p2](https://arxiv.org/html/2409.05546v3#S4.SS1.SSS5.p2); Table 3: [S4.T3](https://arxiv.org/html/2409.05546v3#S4.T3).
- **替代方案** · [AdaSID](adasid.md): AdaSID keeps a pre-trained tokenizer and adapts collision repulsion, contrasting with ETEGRec's end-to-end downstream supervision of the tokenizer.
  - 出处：Evidence is from the later AdaSID paper, Section 2.2: [S2.SS2.p1](https://arxiv.org/html/2604.23522v1#S2.SS2.p1).

[查看同格全部论文](../../../README.zh.md#iii--training)
