# FlexCode

[← 问题 × 阶段矩阵](../../../README.zh.md#i--tokenization) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/flexcode.md) | 中文

| **题目** | *Semantics Meet Signals: Dual Codebook Representationl Learning for Generative Recommendation* |
| :-- | :-- |
| **作者** | Hui et al. |
| **发表** | arXiv’25 |
| **问题与阶段** | `I. 信息量` · `构码（Tokenization）` |
| **改动** | ● 构码 · ○ 编号器更新 · ○ 训练目标 |
| **构码输入** | semantic: `Text` + `CF` · collaborative: `CF` |
| **领域** | `电商` · `短视频与直播` · `其他`（未具名商业平台的内部数据） |
| **应用场景** | `一般物品推荐`；`工业数据离线` |
| **链接** | [论文](https://arxiv.org/abs/2511.20673) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text+CF"] --> T["构码 Tokenization<br/>● Dual RQ-VAE"] --> B["生成骨干 Backbone<br/>–"] --> TR["训练 Training<br/>编号器更新: ○ Joint<br/>训练目标: ○ NTP"] --> I["推理 Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+CF`：文本表征结合协同过滤信号。
- `Dual RQ-VAE`：面向两条独立表征流的双路 RQ-VAE。
- `Joint`：推荐生成损失通过可微路径直接反传更新编号器。
- `NTP`：标准下一 token 预测（Next-Token Prediction）交叉熵损失；基于预训练 LLM 的指令微调（SFT）亦归入此类。

### TL;DR

> [!NOTE]
> FlexCode 通过轻量 MoE 按物品流行度在协同码本与语义码本之间分配固定 token 预算，替代所有物品共用单一码本的做法。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon-Beauty, Amazon-Sports and Outdoors, KuaiRand-1K; 5-core filtering; proprietary industrial interactions.
  - 出处：Sections 4.1.1 and Public Benchmarks: [S4.SS1.SSS1.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS1.p1) and [S4.SS1.SSS1.Px1.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS1.Px1.p1)
- **切分**：Public: chronological last item test, penultimate validation; industrial: last logged day evaluation, validation not reported.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS1.p1) and [S4.SS1.SSS1.Px2.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS1.Px2.p1)
- **候选集**：not reported
  - 出处：Candidate protocol absent from Section 4.1: [S4.SS1](https://arxiv.org/html/2511.20673v1#S4.SS1)
- **可见性**：warm; no unseen-item protocol is defined. Head/tail evaluation concerns popularity; tokenizer and collaborative-encoder item exposure: not reported.
  - 出处：Sections 4.1.1 and 4.3.2: [S4.SS1.SSS1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS1) and [S4.SS3.SSS2.p1](https://arxiv.org/html/2511.20673v1#S4.SS3.SSS2.p1)
- **SID 规格**：Dual RQ-VAE; total token budgets 3/4/5/6, popularity-dependent allocation; base K=512. Main-experiment depth and collision handling not reported.
  - 出处：Sections 3.1/3.3 and Tables 4-5: [S3.SS1](https://arxiv.org/html/2511.20673v1#S3.SS1) and [S3.SS3.p3](https://arxiv.org/html/2511.20673v1#S3.SS3.p3) and [S5.T4](https://arxiv.org/html/2511.20673v1#S5.T4) and [S5.T5](https://arxiv.org/html/2511.20673v1#S5.T5)
- **推理预算**：Recall/NDCG@5/10; beam width, hardware, inference batch size, latency not reported.
  - 出处：Sections 3.4 and 4.1.3: [S3.SS4](https://arxiv.org/html/2511.20673v1#S3.SS4) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS3.p1)
- **结果来源**：Original Table 1: public benchmarks; Figure 2: industrial overall and head/tail results.
  - 出处：Table 1 and Figure 2: [S4.T1](https://arxiv.org/html/2511.20673v1#S4.T1) and [S4.F2](https://arxiv.org/html/2511.20673v1#S4.F2)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["FlexCode"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"同期对比"| B["LC-Rec"]
    P -->|"同期对比"| C["COBRA"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **同期对比** · [TIGER](tiger.md): Compared semantic-ID baseline; FlexCode separates semantic and collaborative codebooks.
  - 出处：FlexCode v1, Section 4.1.2 and Table 1: [S4.SS1.SSS2.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS2.p1); [S4.T1](https://arxiv.org/html/2511.20673v1#S4.T1).
- **同期对比** · [LC-Rec](lc-rec.md): Compared semantic-ID baseline; FlexCode allocates tokens by item popularity.
  - 出处：FlexCode v1, Section 4.1.2 and Table 1: [S4.SS1.SSS2.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS2.p1); [S4.T1](https://arxiv.org/html/2511.20673v1#S4.T1).
- **同期对比** · [COBRA](cobra.md): Compared semantic-ID baseline; FlexCode combines dual codebooks with adaptive routing.
  - 出处：FlexCode v1, Section 4.1.2 and Table 1: [S4.SS1.SSS2.p1](https://arxiv.org/html/2511.20673v1#S4.SS1.SSS2.p1); [S4.T1](https://arxiv.org/html/2511.20673v1#S4.T1).

[查看同格全部论文](../../../README.zh.md#i--tokenization)
