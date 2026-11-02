# TransRec

*Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation* — Lin et al. · KDD’24

`II. 唯一性与合法性` · `Tokenization` · [论文](https://arxiv.org/abs/2310.06491) · [代码](https://github.com/Linxyhaha/TransRec/) · [矩阵](../../../README.zh.md#ii--tokenization) · [English](../../papers/transrec.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>Multi-Facet ID"] --> B["Backbone<br/>Enc-Dec / Dec-Only"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>FM-Index+Agg."]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `Multi-Facet ID`: Identifiers representing multiple facets of an item.
- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `FM-Index+Agg.`: FM-index-constrained generation followed by identifier-to-item score aggregation.

### TL;DR

> [!NOTE]
> TransRec 用结合 ID、标题与属性的多面标识索引物品，通过 FM-index 子串索引约束生成，并聚合生成的标识为物品库打分排序。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | II. 唯一性与合法性：Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| 核心贡献 | TransRec 用结合 ID、标题与属性的多面标识索引物品，通过 FM-index 子串索引约束生成，并聚合生成的标识为物品库打分排序。 |
| 主要改动阶段 | Tokenization |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty and Toys, plus Yelp. Release year and filtering thresholds: not reported. Items use random unique numeric IDs, titles and categories.
  - 出处：Sec.4.1 Datasets and Appendix Table9: [S4.SS1.SSS1.p1](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS1.p1) and [A1.T9](https://arxiv.org/html/2310.06491v2#A1.T9)
- **切分**：Per-user leave-one-out: last item test, penultimate validation, remainder training. Full training uses all training users; few-shot selects 1024/2048 users. Discard oldest history items until input fits 1024 tokens (BART) or 512 (LLaMA).
  - 出处：Sec.4.1 Datasets/Implementation and Sec.4.3.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS1.p1) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS3.p1) and [S4.SS3.SSS1.p1](https://arxiv.org/html/2310.06491v2#S4.SS3.SSS1.p1)
- **候选集**：not reported: full-catalog versus sampled evaluation and history-item exclusion are unspecified. Generated facet identifiers are aggregated into scores for in-corpus items.
  - 出处：Sec.3.2 aggregated grounding and Sec.4.1 evaluation: [S3.SS2.SSS2.p1](https://arxiv.org/html/2310.06491v2#S3.SS2.SSS2.p1) and [S3.SS2.SSS2.p3](https://arxiv.org/html/2310.06491v2#S3.SS2.SSS2.p3) and [S4.SS1.SSS2.p2](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS2.p2)
- **可见性**：Full-training item-level visibility: not reported. Few-shot tests the N training users plus N unseen users; warm requires both user and item warm, otherwise cold. Cold items are unseen by generator training, but the cold subset also includes unseen-user cases. Identifier construction reportedly uses only warm items; learned SID tokenizer n/a for manual facets. Cold-item exposure through the FM-index is not reported.
  - 出处：Sec.4.2 and Sec.4.3.1 explicitly distinguish warm/cold users and items: [S4.SS2.p1](https://arxiv.org/html/2310.06491v2#S4.SS2.p1) and [S4.SS3.SSS1.p1](https://arxiv.org/html/2310.06491v2#S4.SS3.SSS1.p1) and [S4.SS3.SSS1.p2](https://arxiv.org/html/2310.06491v2#S4.SS3.SSS1.p2)
- **SID 规格**：Three separate facets: unique random numeric ID, title and categories. Variable text-token lengths; codebook size n/a. Numeric IDs provide uniqueness while titles/attributes can be shared. Training samples five title substrings per sequence and uses each category separately; this is not a quantized SID.
  - 出处：Sec.3.1.1-3.1.2 and Appendix A.2: [S3.SS1.SSS1.p2](https://arxiv.org/html/2310.06491v2#S3.SS1.SSS1.p2) and [S3.SS1.SSS1.p5](https://arxiv.org/html/2310.06491v2#S3.SS1.SSS1.p5) and [S3.SS1.SSS2.p2](https://arxiv.org/html/2310.06491v2#S3.SS1.SSS2.p2) and [A1.SS2.p1](https://arxiv.org/html/2310.06491v2#A1.SS2.p1)
- **推理预算**：FM-index-constrained beam20 for TransRec and LLM baselines; generate each facet, then aggregate grounding scores. Recall/NDCG@5/10. Table3 reports 218.43s grounding per 5000 Beauty users, not end-to-end request latency. Inference batch, hardware and generated-length cap: not reported; four RTX A5000 GPUs are explicitly the training setup.
  - 出处：Sec.3.2 generation, Sec.4.1 implementation/evaluation and Table3: [S3.SS2.SSS1.p3](https://arxiv.org/html/2310.06491v2#S3.SS2.SSS1.p3) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS3.p1) and [S4.SS1.SSS2.p2](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS2.p2) and [S4.T3](https://arxiv.org/html/2310.06491v2#S4.T3)
- **结果来源**：This paper's Table1 full-training BART comparison, Table2 Beauty few-shot warm/cold comparison, Table3 grounding ablation, and appendix analyses. P5 is explicitly trained on sequential tasks with randomized IDs; Appendix A.3 implements indexing baselines and TransRec with the same T5-small backbone/single prompt. Borrowed-score attribution and run/seed counts: not reported.
  - 出处：Tables1-3 and Appendix A.3/A.6: [S4.T1](https://arxiv.org/html/2310.06491v2#S4.T1) and [S4.T2](https://arxiv.org/html/2310.06491v2#S4.T2) and [S4.T3](https://arxiv.org/html/2310.06491v2#S4.T3) and [S4.SS1.SSS2.p1](https://arxiv.org/html/2310.06491v2#S4.SS1.SSS2.p1) and [A1.SS3.p1](https://arxiv.org/html/2310.06491v2#A1.SS3.p1) and [A1.SS6.p1](https://arxiv.org/html/2310.06491v2#A1.SS6.p1)

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["TransRec"]
    P -->|competitor| A["CID"]
    P -->|competitor| B["TIGER"]
```

- **同期对比** · [CID](cid.md): CID+IID and the other Hua et al. indexing variants are compared baselines.
  - 出处：TransRec v2, Sec.4.1 Baselines and Appendix A.3: https://arxiv.org/html/2310.06491v2#S4.SS1.SSS2.p1; https://arxiv.org/html/2310.06491v2#A1.SS3.p1.
- **同期对比** · [TIGER](tiger.md): TIGER is compared as a quantized semantic-identifier baseline.
  - 出处：TransRec v2, Sec.4.1 Baselines and Sec.4.2: https://arxiv.org/html/2310.06491v2#S4.SS1.SSS2.p1; https://arxiv.org/html/2310.06491v2#S4.SS2.p1.

[查看同格全部论文](../../../README.zh.md#ii--tokenization)
