# AtSpeed

| **题目** | *Efficient Inference for Large Language Model-based Generative Recommendation* |
| :-- | :-- |
| **作者** | Lin et al. |
| **会议** | ICLR’25 |
| **问题与阶段** | `V. 效率` · `Inference` |
| **链接** | [论文](https://arxiv.org/abs/2410.05165) · [代码](https://github.com/Linxyhaha/AtSpeed) · [矩阵](../../../README.zh.md#v--inference) · [English](../../papers/atspeed.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>Spec. Dec."]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class I main
```

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Spec. Dec.`: Speculative decoding.

### TL;DR

> [!NOTE]
> AtSpeed 在 top-K 序列上对齐草稿模型与目标 LLM，并放宽投机解码的验证条件，以加速 LLM 生成式推荐中 top-K 物品的束搜索解码。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | V. 效率：Can it be trained and served within latency and cost budgets? |
| 核心贡献 | AtSpeed 在 top-K 序列上对齐草稿模型与目标 LLM，并放宽投机解码的验证条件，以加速 LLM 生成式推荐中 top-K 物品的束搜索解码。 |
| 主要改动阶段 | Inference |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty and Games (main), plus MovieLens-1M and Goodreads in Appendix Table 6. Filtering rules: not restated; statistics in Appendix Table 2.
  - 出处：Datasets: [S4.SS1.p1](https://arxiv.org/html/2410.05165v3#S4.SS1.p1); split and identifier length: [A1.SS3.SSS1.p1](https://arxiv.org/html/2410.05165v3#A1.SS3.SSS1.p1).
- **切分**：All interactions sorted by global timestamp and split 8:1:1 into training, validation, and test.
  - 出处：Global-timestamp 8:1:1 split: [A1.SS3.SSS1.p1](https://arxiv.org/html/2410.05165v3#A1.SS3.SSS1.p1).
- **候选集**：not reported (full catalog versus sampled); top-K (K = 1, 3, 5, 10, 20) from beam search of the target LLM, evaluated by Recall and NDCG plus walltime speedup.
  - 出处：Metrics: [S4.SS1.p3](https://arxiv.org/html/2410.05165v3#S4.SS1.p3).
- **可见性**：warm; no unseen-item protocol is defined (global temporal split, so test items may include items not seen in training, but this is not analyzed).
  - 出处：Global temporal split with no unseen-item protocol: [A1.SS3.SSS1.p1](https://arxiv.org/html/2410.05165v3#A1.SS3.SSS1.p1).
- **SID 规格**：RQ-VAE item identifiers following LC-Rec, length L=4; codebook size and collision handling: not reported.
  - 出处：RQ-VAE identifiers following LC-Rec, length 4: [S4.SS1.p1](https://arxiv.org/html/2410.05165v3#S4.SS1.p1) and [A1.SS3.SSS1.p1](https://arxiv.org/html/2410.05165v3#A1.SS3.SSS1.p1).
- **推理预算**：Speculative beam decoding: LLaMA-68M draft model with draft length 4 and draft beam size N=40 verifying top-K beams (K up to 20) of a LLaMA-7B LC-Rec target with tree-based attention. Figure 1 measures LC-Rec inference time on one NVIDIA A5000; draft training on 4 A5000 GPUs; speedup reported as walltime ratio (WS@K).
  - 出处：Draft settings and hardware: [S4.SS1.p4](https://arxiv.org/html/2410.05165v3#S4.SS1.p4) and [A1.SS3.SSS1.p2](https://arxiv.org/html/2410.05165v3#A1.SS3.SSS1.p2); target inference cost figure: [S1.F1](https://arxiv.org/html/2410.05165v3#S1.F1).
- **结果来源**：Table 1 (walltime speedup and accepted steps versus SFT, WordKD, SeqKD, TVDKD, DARE drafts); Appendix Table 5 (Recall and NDCG on Beauty and Games for the target LLM, the baselines, and AtSpeed instantiated on LC-Rec with LLaMA-7B); Appendix Tables 6-7 (MovieLens-1M, Goodreads, alignment-data cost).
  - 出处：Main: [S4.T1](https://arxiv.org/html/2410.05165v3#S4.T1); ranking results: [A1.T5](https://arxiv.org/html/2410.05165v3#A1.T5); appendix datasets and cost: [A1.T6](https://arxiv.org/html/2410.05165v3#A1.T6) and [A1.T7](https://arxiv.org/html/2410.05165v3#A1.T7).

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["AtSpeed"]
    P -->|predecessor| A["LC-Rec"]
    P -->|alternative| B["SpecGR"]
    P -->|alternative| C["PAD-Rec"]
```

- **前序工作** · [LC-Rec](lc-rec.md): AtSpeed accelerates an LC-Rec target model: it trains a small draft model aligned to LC-Rec's top-K beams and verifies drafted beams in parallel.
  - 出处：AtSpeed v3, instantiated on LC-Rec: https://arxiv.org/html/2410.05165v3#S4.SS1.p1 and https://arxiv.org/html/2410.05165v3#S4.SS1.p4; Figure 1 inference cost of LC-Rec: https://arxiv.org/html/2410.05165v3#S1.F1.
- **替代方案** · [SpecGR](specgr.md): SpecGR uses speculative drafting to recommend new items inductively, whereas AtSpeed uses it only to speed up decoding while keeping the target model's top-K.
  - 出处：AtSpeed v3, Section 5 related work cites SpecGR: https://arxiv.org/html/2410.05165v3#S5.p1.
- **替代方案** · [PAD-Rec](pad-rec.md): PAD-Rec later also applies speculative decoding to LLM generative recommendation, targeting list-wise generation with position-aware drafts.
  - 出处：Evidence is from the later PAD-Rec paper, Sections 1 and 2.3: https://arxiv.org/html/2604.27747v1#S1.p2 and https://arxiv.org/html/2604.27747v1#S2.SS3.p1.

[查看同格全部论文](../../../README.zh.md#v--inference)
