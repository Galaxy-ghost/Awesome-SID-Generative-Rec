# GRLM

*Unleashing the Native Recommendation Potential: LLM-Based Generative Recommendation via Structured Term Identifiers* — Zhang et al. · arXiv’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2601.06798) · [Code](https://github.com/ZY0025/GRLM) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Term-ID`** | `Dec-Only` | `Fixed / Multi-task NTP` | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 2. How It Works

![GRLM architecture diagram](../../architectures/grlm.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: In-domain: Amazon Beauty, Sports, Toys (5-core, following TIGER and OneRec-Think; 22,363 / 12,101, 35,598 / 18,357, 19,412 / 11,924 users / items). Cross-domain pairs Sports-Clothing and Phones-Electronics, built per GenCDR by merging overlapping users' interactions chronologically. Appendix: ten Amazon 2014 categories merged.
  - Source: In-domain and cross-domain datasets: https://arxiv.org/html/2601.06798v1#S4.p3 and https://arxiv.org/html/2601.06798v1#S4.p4; statistics: https://arxiv.org/html/2601.06798v1#S4.T1; ten-dataset appendix: https://arxiv.org/html/2601.06798v1#A1.T6.
- **Split**: Leave-one-out (allocation not restated beyond the label); in the cross-domain setting the last interaction in each domain of the pair is predicted separately.
  - Source: Leave-one-out and cross-domain evaluation: https://arxiv.org/html/2601.06798v1#S4.p3 and https://arxiv.org/html/2601.06798v1#S4.p4.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); validity of generated Term IDs is measured separately (Table 5).
  - Source: Metrics only: https://arxiv.org/html/2601.06798v1#S4.p5.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2601.06798v1#S4.p3.
- **SID**: Term IDs: 5 natural-language terms per item from Qwen3-4B's native vocabulary, produced by context-aware term generation (7 and 10 terms tested). Collision handling: not reported beyond relying on a large term space; an optional K-means compression maps 54,255 raw terms to K core terms (3,000-8,000).
  - Source: Term IDs of length 5 from the LLM vocabulary: https://arxiv.org/html/2601.06798v1#S4.p5; length study: https://arxiv.org/html/2601.06798v1#A2.T8; collision discussion and compression: https://arxiv.org/html/2601.06798v1#A2.p1, https://arxiv.org/html/2601.06798v1#A4.p4, https://arxiv.org/html/2601.06798v1#A4.T9.
- **Inference budget**: Beam search with generation max length 30 tokens; beam width not reported. Qwen3-4B backbone; hardware, inference batch size, and latency: not reported. Valid rate at 10 is 0.989-0.998 (Table 5).
  - Source: Beam search, max length 30: https://arxiv.org/html/2601.06798v1#S4.p5; training batch: https://arxiv.org/html/2601.06798v1#A1.p2; validity: https://arxiv.org/html/2601.06798v1#S5.T5.
- **Results from**: Table 2 (in-domain), Table 3 (cross-domain), Table 4 (ablations), Table 5 (Term ID validity), Appendix Tables 7-9 (ten-dataset results, Term ID length, vocabulary compression).
  - Source: Results: https://arxiv.org/html/2601.06798v1#S5.T2, https://arxiv.org/html/2601.06798v1#S5.T3, https://arxiv.org/html/2601.06798v1#S5.T4, https://arxiv.org/html/2601.06798v1#S5.T5, https://arxiv.org/html/2601.06798v1#A1.T7, https://arxiv.org/html/2601.06798v1#A2.T8, https://arxiv.org/html/2601.06798v1#A4.T9.

## 旧卡片说明

迁自 `d61aa6c:papers/grlm.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### GRLM：基于结构化术语标识的原生 LLM 生成推荐

> GRLM 用原生语言词表构造结构化 Term IDs，使 LLM 直接生成语义丰富的物品术语标识。

### 研究动机与问题定义

数值 SID 通常需要扩展词表和额外对齐，文本标识又容易出现同义词分裂和幻觉。GRLM 以原生 LLM token 构造 Term IDs，并通过邻域上下文提升一致性与区分性。

### TL;DR（核心摘要）

`物品元信息与相似邻域 → 上下文术语生成 → IIFT → Term ID生成 → EIG落地物品`

上下文术语生成从相似物品邻域中抽取标准化且有区分度的关键词。IIFT 联合训练术语内化和用户行为预测；推理时生成 Term ID。若无法精确匹配，EIG 会对候选库进行结构化匹配评分，因此最终物品仍依赖外部标识落地机制。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 物品元信息、相似邻域和用户交互 |
| 信息融入位置 | 术语生成、LLM 训练和候选落地 |
| 语义标识结构 | 变长术语序列 |
| 适用场景 | 跨域、长尾和文本信息丰富的推荐 |

### 方法设计

#### 3.1 上下文术语生成（CTG）
GRLM 先用嵌入模型检索与目标物品相似的邻域，再把目标元信息和邻域元信息一起交给 LLM。提示要求共享属性使用一致术语，同时保留能区分相似物品的细粒度关键词，得到 Term ID。

#### 3.2 综合指令微调（IIFT）
IIFT 联合训练术语内化和用户行为序列预测。术语内化要求模型从元信息恢复标准 Term ID，行为任务则使用历史 Term ID 与标题预测后续物品，从而让 LLM 同时理解标识结构和用户偏好。

#### 3.3 弹性标识落地（EIG）
推理时先尝试 Term ID 的精确字符串匹配；若失败，再按术语位置和衰减权重对候选库进行结构化匹配评分。该后置步骤负责将生成的术语标识落到候选物品。

#### 3.4 实验分析
论文分别评估域内、跨域、消融、规模扩展和术语幻觉，分析上下文邻域对一致性、区分性和可落地性的影响。

### 实验结论

- GRLM 在域内和跨域设置中报告了较强推荐效果。
- 上下文术语生成降低了标识碎片化与幻觉。
- 论文报告了随模型规模扩大而提升的趋势。

### 局限性与研究定位

#### 局限性
- EIG 的结构化匹配依赖候选库和后置评分，不是纯 SID 直达。
- 术语生成、候选库更新和多级匹配增加工程复杂度。
- 代码公开状态未报告。

#### 研究定位
GRLM 的主要贡献是利用 LLM 原生词表构造可解释 Term ID；它适合放在“文本标识与生成推荐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2601.06798)

### 标签

`术语标识` · `上下文术语生成` · `LLM推荐` · `标识落地`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 检索方式补充

迁自 `d61aa6c:tables/boundary-and-excluded-methods.md` 的机制说明。

Term ID 无法精确匹配时，仍通过候选库结构化评分完成物品落地。

旧表的“核心／边界／排除”分组已由当前问题与阶段分类取代。

### 5. Connections to Related Work

- **Competitor** · [OneRec-Think](onerec-think.md): OneRec-Think reasons over numeric SIDs with an LLM; GRLM replaces SIDs with Term IDs drawn from the LLM's own vocabulary.
  - Source: GRLM v1, LLM-based baselines and preprocessing: https://arxiv.org/html/2601.06798v1#S4.I1.i3.p1 and https://arxiv.org/html/2601.06798v1#S4.p3; Table 2: https://arxiv.org/html/2601.06798v1#S5.T2.
- **Competitor** · [IDGenRec](idgenrec.md): IDGenRec generates free textual IDs; GRLM extracts a fixed number of standardized terms with context-aware generation to limit synonym ambiguity.
  - Source: GRLM v1, LLM-based baselines: https://arxiv.org/html/2601.06798v1#S4.I1.i3.p1; Table 2: https://arxiv.org/html/2601.06798v1#S5.T2; case study: https://arxiv.org/html/2601.06798v1#A3.p1.
- **Competitor** · [TIGER](tiger.md): TIGER uses numeric RQ-VAE semantic IDs; GRLM uses natural-language term IDs.
  - Source: GRLM v1, generative baselines: https://arxiv.org/html/2601.06798v1#S4.I1.i2.p1; Tables 2 and 3: https://arxiv.org/html/2601.06798v1#S5.T2 and https://arxiv.org/html/2601.06798v1#S5.T3.
- **Competitor** · [GenCDR](gencdr.md): GenCDR adapts semantic-ID tokenization per domain; GRLM transfers across domains through shared vocabulary terms.
  - Source: GRLM v1, cross-domain baselines and protocol: https://arxiv.org/html/2601.06798v1#S4.I1.i4.p1 and https://arxiv.org/html/2601.06798v1#S4.p4; Table 3: https://arxiv.org/html/2601.06798v1#S5.T3.

[View all papers in this cell](../../README.md#iii--tokenization)
