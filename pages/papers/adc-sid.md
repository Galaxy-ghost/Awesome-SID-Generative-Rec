# ADC-SID

*Taming the Long Tail: Denoising Collaborative Information for Robust Semantic ID Generation* — Xu et al., arXiv’25

[arXiv](https://arxiv.org/abs/2510.25622) · [Record](../../data/papers/adc-sid.yaml) · [← Catalog](../../README.md#i--tokenization)

> Abstract: "leading to the loss of critical multimodal information". The arXiv API abstract is truncated; judged on the visible part.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`MoE-VQ`** | `Enc-Dec` | `Fixed† / NTP` | `–` |

- `Enc-Dec`: Encoder-decoder.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

## Architecture

![ADC-SID architecture diagram](../../architectures/adc-sid.png)

## Evidence

- **`problem`** (arXiv abstract): Abstract: "leading to the loss of critical multimodal information". The arXiv API abstract is truncated; judged on the visible part.
- **`tokenizer`** (p7; p8): Not stated whether the generator updates the tokenizer; Fixed is inferred. Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p7; p8): Location from the 10-26 'Training split' table in the appendix.

## 旧卡片说明

迁自 `d61aa6c:papers/mmqv2.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

以下说明与架构图来自旧版 MMQ-v2（arXiv 2510.25622）；该论文自 v3 起改名为 ADC-SID。它与 MMQ（arXiv 2508.15281）是不同论文，旧版说明不覆盖 v3 的全部变更。

### MMQ-v2：自适应行为挖掘语义标识学习

> MMQ-v2 以 ADA-SID 为核心，通过稀疏混合专家自适应融合内容与行为信号，学习更稳健的语义标识。

### 研究动机与问题定义

内容型 SID 难以表达协同偏好，而直接加入行为又可能引入噪声和流行度偏置。ADA-SID 试图根据物品和行为状态动态决定内容与协同信号的融合方式。

### TL;DR（核心摘要）

`文本/图像与行为 → 自适应路由量化 → ADA-SID → 生成模型 → 推荐物品`

方法使用稀疏 MoE 量化网络，把共享专家和模态/行为特定专家结合起来；路由器依据信号选择专家，并通过对齐、去噪和放大机制优化 SID。论文在生成式推荐设置中用生成模型直接预测 SID。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 文本、图像、交互和行为统计 |
| 信息融入位置 | 自适应量化网络与 SID 学习目标 |
| 语义标识结构 | 多级离散序列 |
| 适用场景 | 多模态生成式推荐 |

### 方法设计

#### 3.1 行为-内容混合量化
ADA-SID 使用内容编码器和行为/协同编码器获得多源表示，再通过稀疏 MoE 量化网络分配共享专家与模态特定专家。量化结果形成多级 SID，兼顾内容语义和交互结构。

#### 3.2 自适应行为-内容对齐
模型通过对齐目标让内容表示与行为表示互相约束，并用去噪机制抑制噪声行为、流行度和异常交互。放大机制进一步增强对推荐有效行为的利用。

#### 3.3 动态行为路由
动态路由器根据物品和行为状态决定专家组合，使不同物品不必采用同一种内容-行为融合比例。稀疏性正则控制激活专家数量和码本使用。

#### 3.4 下游生成推荐
生成式推荐器使用学习到的 SID 作为目标序列直接预测下一物品。论文也比较判别式下游任务，并通过工业数据、消融和流行度分层分析验证 ADA-SID。

### 实验结论

- 自适应行为路由优于固定融合策略。
- 去噪和对齐模块对长尾物品表现有帮助。

### 局限性与研究定位

#### 局限性
- 稀疏专家和多模态编码增加了训练与部署复杂度。
- 生成任务与判别任务共用 SID 时的统一服务成本仍未充分报告。

#### 研究定位
MMQ-v2 的核心贡献是让行为信号以自适应方式参与 SID 学习，适合放在“行为增强的语义标识学习”章节。

### 标签

`多模态` · `稀疏MoE` · `行为挖掘` · `语义标识`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：自适应融合行为与内容。
- 使用场景：多模态推荐。

## Same cell: I × Tokenization (33 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CoST](cost.md) | RecSys’24 | `Text` → **`C-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [LETTER](letter.md) | CIKM’24 | `Text+CF` → **`Learn. RQ`** → `Enc-Dec` → `Fixed / NTP + Rank` → `C-Beam` |
| [LMIndexer](lmindexer.md) | ICML’24 | `Text` → **`Self-Sup. ID`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [ActionPiece](actionpiece.md) | ICML’25 | `Text` → **`OPQ`** → `Enc-Dec` → `Fixed / NTP` → `Ensemble` |
| [DAS](das.md) | CIKM’25 | `Text+CF` → **`Dual RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [EAGER-LLM](eager-llm.md) | WWW’25 | `Text+CF` → **`Dual H-KM`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [FlexCode](flexcode.md) | arXiv’25 | `Text+CF` → **`Dual RQ-VAE`** → `–` → `Joint / NTP` → `–` |
| [GenSAR](gensar.md) | RecSys’25 | `Text+CF` → **`Shared/Spec. RQ`** → `Enc-Dec` → `Fixed / Multi-task NTP` → `C-Beam` |
| [GNPR-SID](gnpr-sid.md) | KDD’25 | `Attr+Geo+CF` → **`RQ-VAE`** → `Dec-Only` → `Fixed / NTP` → `–` |
| [GRAM](gram.md) | ACL’25 | `Text+CF` → **`H-KM`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [KGTB](kgtb.md) | arXiv’25 | `Attr+Geo+CF` → **`KG-RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `–` |
| [MME-SID](mme-sid.md) | CIKM’25 | `Text+Img+CF` → **`MM-RQ`** → `Dec-Only` → `Fixed / NTP` → `Scoring` |
| [MQL4GRec](mql4grec.md) | ICLR’25 | `Text+Img` → **`Dual RQ`** → `Enc-Dec` → `Fixed / Multi-task NTP` → `Beam` |
| [PSRQ](psrq.md) | CIKM’25 | `Text+Img` → **`Prog. RQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [QT-Mob](qt-mob.md) | KDD’25 | `Text+Geo` → **`RQ-VAE`** → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam` |
| [TokenRec](tokenrec.md) | TKDE’25 | `CF` → **`Masked VQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [CapsID](capsid.md) | arXiv’26 | `Text+CF` → **`Soft-RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [ChronoID](chronoid.md) | arXiv’26 | `Text+Time` → **`RQ-VAE / Par. VQ`** → `Dec-Only†` → `Fixed / NTP` → `Beam†` |
| [GrIS (RecDMoN / RQ-GAE)](gris-recdmon-rq-gae.md) | CIKM’26 | `Text+CF` → **`RecDMoN / RQ-VAE`** → `Enc-Dec` → `Fixed / –` → `–` |
| [MACRec](macrec.md) | AAAI’26 | `Text+Img` → **`Cross RQ`** → `Enc-Dec` → `Fixed / NTP + Ctr.` → `C-Beam` |
| [MMGRec](mmgrec.md) | TOMM’26 | `Text+Img+CF` → **`Graph RQ-VAE`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [MMQ](mmq.md) | WSDM’26 | `Text+Img` → **`MoE-VQ`** → `HeterRec` → `Joint / MTP` → `–` |
| [MSCGRec](mscgrec.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+DINO`** → `Enc-Dec` → `Fixed† / NTP` → `Trie/C-Beam` |
| [PCR-CA](pcr-ca.md) | KDD’26 | `Text+CF` → **`PC-AE`** → `Disc.` → `Joint / Discrim.` → `Scoring` |
| [Pctx](pctx.md) | CIKM’26 | `Text+CF` → **`RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam+Agg.` |
| [ProGEO](progeo.md) | arXiv’26 | `Text+Geo` → **`R-KM+Geo-CB`** → `Dec-Only` → `Fixed / NTP` → `Beam+Geo-Filter` |
| [RoFiGR](rofigr.md) | arXiv’26 | `Text+Img+CF` → **`CF-Aligned MM RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam` |
| [ROS](ros.md) | ACL’26 | `Text+Geo` → **`Geo-Prefix+RQ-VAE`** → `Dec-Only` → `Fixed / NTP → RL` → `CoT+C-Beam` |
| [SPRIG](sprig.md) | CIKM’26 Short | `Text / Audio` → **`R-KM`** → `Dec-Only` → `Fixed / NTP` → `Div. Beam` |
| [Tlow](tlow.md) | CIKM’26 Applied | `Text` → **`Flow+PQ`** → `Non-AR` → `Fixed / MTP + Rel.MSE` → `Scoring` |
| [UniRec](unirec.md) | arXiv’26 | `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `C-Beam` |
| [UniSID](unisid.md) | arXiv’26 | `Text+Img+Attr` → **`Direct SID Heads`** → `–` → `– / –` → `–` |
| [VarLenRec (TIGER)](varlenrec-tiger.md) | arXiv’26 | `Text` → **`HARQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam` |
