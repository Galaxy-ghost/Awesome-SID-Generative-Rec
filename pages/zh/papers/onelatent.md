# OneLatent

[← 问题 × 阶段矩阵](../../../README.zh.md#v--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/onelatent.md) | 中文

| **题目** | *Latent Reasoning for Efficient Foundation Recommendation Models* |
| :-- | :-- |
| **作者** | Jiang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `V. 效率` · `训练（Training）` |
| **改动** | ○ 生成骨干 · ● 训练目标 · ○ 推理 |
| **构码输入** | `MM` |
| **领域** | `广告` · `本地生活与 POI` |
| **应用场景** | `一般物品推荐` · `POI 与本地生活`；`线上实验或部署` |
| **链接** | [论文](https://arxiv.org/abs/2610.30675) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>MM"] --> T["构码 Tokenization<br/>R-KM"] --> B["生成骨干 Backbone<br/>○ Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ● Multi-task NTP"] --> I["推理 Inference<br/>○ Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class B,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `MM`：多模态物品表征。
- `R-KM`：残差 k-means 量化（Residual k-means）。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `Multi-task NTP`：在多个对齐或推荐子任务上联合优化下一 token 预测损失。
- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。

### TL;DR

> [!NOTE]
> OneLatent 通过多视图教师轨迹、分阶段对齐与课程式后训练，将显式思维链压缩为可学习隐 token，避免在推理时生成长推理文本。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Kuaishou LLM-Rec advertising and seven-day industrial local-services logs. Deduplicate user-item interactions by strongest feedback; remove samples lacking profile/target SID and history items lacking SIDs.
  - 出处：Section 4.1.1 and Appendix A.2: [S4.SS1.SSS1.p1](https://arxiv.org/html/2610.30675v1#S4.SS1.SSS1.p1) and [A1.SS2.p2](https://arxiv.org/html/2610.30675v1#A1.SS2.p2) and [A1.SS2.p4](https://arxiv.org/html/2610.30675v1#A1.SS2.p4)
- **切分**：Allocation rule: not reported. SFT/CoT/test counts: industrial 100063/59113/20393; public 60000/30000/10000. Conversion targets use at most 50 preceding interactions.
  - 出处：Table 1 and Appendix A.2: [S4.T1](https://arxiv.org/html/2610.30675v1#S4.T1) and [A1.SS2.p3](https://arxiv.org/html/2610.30675v1#A1.SS2.p3)
- **候选集**：not reported
  - 出处：Section 4.1.3 gives generation metrics without a full-catalog/sampled candidate protocol: [S4.SS1.SSS3.p1](https://arxiv.org/html/2610.30675v1#S4.SS1.SSS3.p1)
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Sections 4.1.1 and Appendix A.2 define no unseen-item evaluation: [S4.SS1.SSS1.p1](https://arxiv.org/html/2610.30675v1#S4.SS1.SSS1.p1) and [A1.SS2](https://arxiv.org/html/2610.30675v1#A1.SS2)
- **SID 规格**：Multimodal Res-Kmeans, 3 levels x 1024 codes; collision handling: not reported.
  - 出处：Section 3.3.1 and Table 10: [S3.SS3.SSS1.p1](https://arxiv.org/html/2610.30675v1#S3.SS3.SSS1.p1) and [A1.T10](https://arxiv.org/html/2610.30675v1#A1.T10)
- **推理预算**：vLLM beam search; SID/ID Hit@1/16/32/64; three fixed latent tokens, no rationale decoding. 872-instance test: total 3.17 s, 274.29 QPS. Beam width, hardware, inference batch size: not reported.
  - 出处：Sections 3.4.3, 4.1.3, 4.4.2 and Table 7: [S3.SS4.SSS3.p1](https://arxiv.org/html/2610.30675v1#S3.SS4.SSS3.p1) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2610.30675v1#S4.SS1.SSS3.p1) and [S4.SS4.SSS2.p1](https://arxiv.org/html/2610.30675v1#S4.SS4.SSS2.p1) and [S4.T7](https://arxiv.org/html/2610.30675v1#S4.T7)
- **结果来源**：Reported Tables 2/3/7/9: main, matched-size scaling, efficiency, online A/B. Table 2's final gains compare matched Think-OR, not strongest baseline; baseline borrowed/rerun provenance not reported.
  - 出处：Tables 2/3/7/9 and Section 4.2: [S4.T2](https://arxiv.org/html/2610.30675v1#S4.T2) and [S4.T3](https://arxiv.org/html/2610.30675v1#S4.T3) and [S4.T7](https://arxiv.org/html/2610.30675v1#S4.T7) and [S4.T9](https://arxiv.org/html/2610.30675v1#S4.T9) and [S4.SS2.SSS0.Px1.p1](https://arxiv.org/html/2610.30675v1#S4.SS2.SSS0.Px1.p1)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["OneLatent"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"替代方案"| B["OneRec-Think"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B peer
```

- **同期对比** · [TIGER](tiger.md): TIGER is a SID-based generative baseline in the reported comparison.
  - 出处：OneLatent v1, Section 4.1.2 and Table 2: [S4.SS1.SSS2.p1](https://arxiv.org/html/2610.30675v1#S4.SS1.SSS2.p1); [S4.T2](https://arxiv.org/html/2610.30675v1#S4.T2).
- **替代方案** · [OneRec-Think](onerec-think.md): OneRec-Think uses explicit CoT plus RL; OneLatent trains a compact latent interface.
  - 出处：OneLatent v1, Section 2.2: [S2.SS2.p1](https://arxiv.org/html/2610.30675v1#S2.SS2.p1).

[查看同格全部论文](../../../README.zh.md#v--training)
