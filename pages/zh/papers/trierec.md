# TrieRec

[← 问题 × 阶段矩阵](../../../README.zh.md#iii--backbone) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/trierec.md) | 中文

| **题目** | *Trie-Aware Transformers for Generative Recommendation* |
| :-- | :-- |
| **作者** | Xu et al. |
| **发表** | NeurIPS’26 |
| **问题与阶段** | `III. SID 与模型对齐` · `生成骨干（Backbone）` |
| **改动** | ● 生成骨干 |
| **构码输入** | `Text` |
| **领域** | `电商` · `电影` |
| **链接** | [论文](https://arxiv.org/abs/2602.21677) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text"] --> T["构码 Tokenization<br/>RQ-VAE"] --> B["生成骨干 Backbone<br/>● Enc-Dec"] --> TR["训练 Training<br/>编号器更新: Fixed†<br/>训练目标: NTP†"] --> I["推理 Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed†`：生成器训练期间冻结编号器（由配置推断）。
- `NTP†`：下一 token 预测损失（由配置推断）。
- `C-Beam`：受合法物品集合约束的束搜索（Constrained beam search）。

### TL;DR

> [!NOTE]
> TrieRec 为 Transformer 生成器加入前缀树感知绝对位置编码与拓扑感知相对位置编码，使注意力反映 SID 前缀树结构而非扁平 token 流。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty, Toys, Food; MovieLens-1M. Standard 5-core filtering, histories retain the most recent 20 interactions.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2602.21677v1#S4.SS1.SSS1.p1)
- **切分**：Per-user most recent interaction test, penultimate validation, earlier interactions training.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2602.21677v1#S4.SS1.SSS1.p1)
- **候选集**：Traditional models: full catalog; generative candidate universe not explicitly reported beyond a valid-item trie.
  - 出处：Section 4.1.2: [S4.SS1.SSS2.p1](https://arxiv.org/html/2602.21677v1#S4.SS1.SSS2.p1)
- **可见性**：warm; no unseen-item protocol is defined. Tokenizer/collaborative encoder exposure to test items not reported.
  - 出处：Section 4.1 defines no unseen-item holdout: [S4.SS1](https://arxiv.org/html/2602.21677v1#S4.SS1)
- **SID 规格**：Sentence-T5-base text features; RQ-VAE: 3 semantic levels x 256 codes, dimension 32, plus a fourth collision token. Select lowest-collision tokenizer checkpoint before appending the uniqueness digit; collision-token vocabulary size not reported.
  - 出处：Section 4.1.4 and Appendix A: [S4.SS1.SSS4.p1](https://arxiv.org/html/2602.21677v1#S4.SS1.SSS4.p1) and [A1.p1](https://arxiv.org/html/2602.21677v1#A1.p1)
- **推理预算**：Constrained beam 10; Recall/NDCG@5/10. Hardware and inference batch size not reported. Figure 3 plots inference time on Beauty/Toy, but the inference panel lacks explicit units and numeric bar labels.
  - 出处：Sections 4.1.2/4.4 and Figure 3: [S4.SS1.SSS2.p1](https://arxiv.org/html/2602.21677v1#S4.SS1.SSS2.p1) and [S4.F3](https://arxiv.org/html/2602.21677v1#S4.F3)
- **结果来源**：Original Tables 2/4: TrieRec on TIGER, CoST, LETTER and competing positional/structure encodings. Table 3: LETTER-based ablations.
  - 出处：Section 4.2, Tables 2/4: [S4.SS2.p1](https://arxiv.org/html/2602.21677v1#S4.SS2.p1) and [S4.T2](https://arxiv.org/html/2602.21677v1#S4.T2) and [S4.T4](https://arxiv.org/html/2602.21677v1#S4.T4) and [S4.T3](https://arxiv.org/html/2602.21677v1#S4.T3)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["TrieRec"]
    P -->|"前序工作"| A["TIGER"]
    P -->|"前序工作"| B["CoST"]
    P -->|"前序工作"| C["LETTER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **前序工作** · [TIGER](tiger.md): TrieRec adds trie-aware positional encodings to TIGER.
  - 出处：TrieRec v1, Sections 1/4.1: [S1.p5](https://arxiv.org/html/2602.21677v1#S1.p5); [S4.SS1.SSS4.p1](https://arxiv.org/html/2602.21677v1#S4.SS1.SSS4.p1).
- **前序工作** · [CoST](cost.md): CoST is the contrastive-tokenization backbone augmented by TrieRec.
  - 出处：TrieRec v1, Section 4.2 and Related Work: [S4.SS2.p2](https://arxiv.org/html/2602.21677v1#S4.SS2.p2); [S5.p3](https://arxiv.org/html/2602.21677v1#S5.p3).
- **前序工作** · [LETTER](letter.md): LETTER supplies the backbone for TrieRec's main ablations and efficiency comparison.
  - 出处：TrieRec v1, Table 3 and Section 4.4: [S4.T3](https://arxiv.org/html/2602.21677v1#S4.T3); [S4.SS4.p1](https://arxiv.org/html/2602.21677v1#S4.SS4.p1).

[查看同格全部论文](../../../README.zh.md#iii--backbone)
