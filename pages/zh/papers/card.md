# CARD

[← 问题 × 阶段矩阵](../../../README.zh.md#ii--tokenization) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/card.md) | 中文

| **题目** | *Non-Uniform Quantization of Visual Semantic Unit for Generative Recommendation* |
| :-- | :-- |
| **作者** | Wei et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `II. 唯一性与合法性` · `构码（Tokenization）` |
| **改动** | ○ 物品表示 · ● 构码 |
| **构码输入** | `Text` + `Img` + `CF` |
| **领域** | `电商` |
| **链接** | [论文](https://arxiv.org/abs/2604.26427) · [代码](https://github.com/HAI-UESTC/CARD) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>○ Text+Img+CF"] --> T["构码 Tokenization<br/>● NU-RQ"] --> B["生成骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: NTP"] --> I["推理 Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+Img+CF`：文本、图像表征结合协同过滤信号。
- `NU-RQ`：带可学习非均匀变换的残差量化（Non-Uniform RQ）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP`：标准下一 token 预测（Next-Token Prediction）交叉熵损失；基于预训练 LLM 的指令微调（SFT）亦归入此类。
- `C-Beam`：受合法物品集合约束的束搜索（Constrained beam search）。

### TL;DR

> [!NOTE]
> CARD 在编码前将文本、图像与协同信号融合为视觉语义单元，并用带可学习非均匀变换的 NU-RQ-VAE 量化，缓解嵌入分布偏斜。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews: Grocery and Gourmet Food (Food), Cell Phones and Accessories (Phones), and Clothing, Shoes and Jewelry (Clothing), with 5-core filtering of users and items. Sizes (users / items / interactions): Food 14,681 / 8,713 / 151,254; Phones 27,879 / 10,429 / 194,439; Clothing 39,387 / 23,033 / 278,677.
  - 出处：Categories, 5-core filtering, truncation: [S4.SS1.SSS1.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS1.p1); statistics: [S4.T1](https://arxiv.org/html/2604.26427v1#S4.T1).
- **切分**：Per-user leave-one-out: most recent interaction for test, second most recent for validation, the rest for training; histories truncated or padded to the 20 most recent items.
  - 出处：Leave-one-out allocation and history length: [S4.SS1.SSS1.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS1.p1).
- **候选集**：full catalog
  - 出处：Full ranking over the entire item set: [S4.SS1.SSS2.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS2.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Standard leave-one-out with no cold-start experiment: [S4.SS1.SSS1.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS1.p1).
- **SID 规格**：4 non-uniform RQ-VAE levels x 256 codewords (dimension 32), quantizing a vision-language embedding of a 512 x 512 rendered card (item image, title, collaborative-neighbor thumbnails). Collision handling: not reported.
  - 出处：K=4 codebooks x 256 vectors of dimension 32: [S4.SS1.SSS3.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p1); non-uniform RQ-VAE over a vision-language encoding of a rendered item card: [S3.SS2.SSS1.p1](https://arxiv.org/html/2604.26427v1#S3.SS2.SSS1.p1) and [S4.SS1.SSS3.p2](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p2); no collision rule found in Sections 3-4.
- **推理预算**：Beam search over the code vocabulary; numerical beam width not reported. T5-style encoder-decoder with 4 layers each and 6 heads. Recall and NDCG at K=5, 10, and 20. Hardware, inference batch size, and latency: not reported.
  - 出处：Beam search with top-B partial sequences, no numerical B: [S3.SS3.p2](https://arxiv.org/html/2604.26427v1#S3.SS3.p2); backbone: [S4.SS1.SSS3.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p1).
- **结果来源**：Table 2 (Food, Phones, Clothing; paired t-tests against the best baseline); Tables 3-4 (ablations of the two CARD variants); Table 5 (non-uniform quantization with different quantizers); Table 6 (text-only encoding).
  - 出处：Main table: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2); ablations: [S4.T3](https://arxiv.org/html/2604.26427v1#S4.T3) and [S4.T4](https://arxiv.org/html/2604.26427v1#S4.T4); plug-in quantizers: [S4.T5](https://arxiv.org/html/2604.26427v1#S4.T5); text-only variants: [S4.T6](https://arxiv.org/html/2604.26427v1#S4.T6).

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["CARD"]
    P -->|"同期对比"| A["MACRec"]
    P -->|"同期对比"| B["MQL4GRec"]
    P -->|"同期对比"| C["LETTER"]
    P -->|"同期对比"| D["TIGER"]
    P -->|"同期对比"| E["VQ-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D,E peer
```

- **同期对比** · [MACRec](macrec.md): MACRec reduces codebook conflicts by cross-modal quantization and multi-aspect alignment of separate modalities; CARD renders image, title, and neighbors into one card and quantizes it with a non-uniform RQ-VAE.
  - 出处：CARD v1, Section 4.1.4 baselines: [S4.I1.i9.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i9.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2); Section 2.1: [S2.SS1.p1](https://arxiv.org/html/2604.26427v1#S2.SS1.p1).
- **同期对比** · [MQL4GRec](mql4grec.md): MQL4GRec quantizes each modality into its own SIDs with pre-training; CARD uses one unified visual semantic unit, and the comparison disables MQL4GRec's extra-category pre-training.
  - 出处：CARD v1, Section 4.1.4 baselines: [S4.I1.i8.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i8.p1); implementation note on pre-training: [S4.SS1.SSS3.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2).
- **同期对比** · [LETTER](letter.md): LETTER regularizes a uniform RQ-VAE with collaborative and diversity terms; CARD changes the quantizer to a non-uniform one and the input to a rendered multimodal card.
  - 出处：CARD v1, Section 4.1.4 baselines: [S4.I1.i7.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i7.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2).
- **同期对比** · [TIGER](tiger.md): TIGER quantizes text embeddings with a uniform RQ-VAE; CARD keeps the same codebook shape and generator but replaces the input and the quantization rule.
  - 出处：CARD v1, Section 4.1.4 baselines: [S4.I1.i6.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i6.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2); Table 6 text-only TIGER variants: [S4.T6](https://arxiv.org/html/2604.26427v1#S4.T6).
- **同期对比** · [VQ-Rec](vq-rec.md): VQ-Rec pools product-quantized code embeddings in a discriminative model; CARD generates hierarchical non-uniform RQ codes autoregressively.
  - 出处：CARD v1, Section 4.1.4 baselines: [S4.I1.i5.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i5.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2).

[查看同格全部论文](../../../README.zh.md#ii--tokenization)
