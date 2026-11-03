# 术语表

[English](glossary.md) | 中文

本页由 [`data/vocab.yaml`](../data/vocab.yaml) 自动生成，定义综述 Table 1、论文详情页与各索引页中的受控词表取值。

## 表内符号

- `†`：根据论文点名沿用的基座或配置推断得到。
- `A / B`：包含两个分支或两种评测配置。
- `–`：论文未报告。
- `n/a`：不适用于该方法。

## 研究问题

- `psb`：**范式、系统与基准。** 基线范式（TIGER）、端到端多阶段工业框架、开源代码库、评测基准与诊断工具。
- `I`：**信息量。** SID 或读取它的模型是否充分携带了推荐所需的协同、多模态与时空信号？
- `II`：**唯一性与合法性。** 每个物品是否拥有无冲突的唯一 SID，生成的 SID 是否对应真实物品，码本是否均衡利用？
- `III`：**SID 与模型对齐。** 生成模型能否理解并推理离散 SID，编号器与生成器的优化目标是否一致？
- `IV`：**实用目标。** 训练目标与解码搜索是否面向用户真实偏好与平台业务价值，而非单纯拟合下一 token 似然？
- `V`：**效率。** 训练与在线服务能否满足实际的延迟、显存与吞吐预算？
- `VI`：**泛化。** 面对冷启动新物品、跨领域迁移与动态兴趣漂移时能否保持泛化？

## 表征（Representation）

- `Attr+CF`：结构化物品属性结合协同过滤信号。
- `Attr+Geo+CF`：类目等结构化属性、地理空间特征与协同过滤信号融合（POI 场景）。
- `Attr+Geo+CF†`：结构化属性、地理信息与协同信号融合（由配置推断）。
- `CF`：纯协同过滤交互信号。
- `Cross-Dom`：跨多个领域迁移或共享的物品表征。
- `Geo`：地理坐标或空间拓扑特征。
- `MM`：多模态物品表征。
- `MM+CF`：与协同过滤信号对齐的多模态物品表征。
- `Multi-Dom`：面向多领域联合构建的统一物品表征。
- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `Text + CF`：文本表征结合协同过滤信号。
- `Text + Img + CF`：文本、图像表征结合协同过滤信号。
- `Text / Audio`：不同分支或评测设置下分别采用文本或音频表征。
- `Text / MM`：不同配置下分别采用纯文本或多模态表征。
- `Text / Text+CF`：不同配置下分别采用纯文本表征或文本加协同信号。
- `Text / –`：一种配置采用文本表征，另一种配置未报告表征来源。
- `Text+Attr+Geo`：文本、结构化属性与地理空间信息融合。
- `Text+CF`：文本表征结合协同过滤信号。
- `Text+CF / Text`：不同配置下分别采用文本加协同信号或纯文本表征。
- `Text+Geo`：文本表征结合地理空间特征。
- `Text+Geo+CF`：文本表征结合地理空间特征与协同信号。
- `Text+Img`：文本与视觉图像表征。
- `Text+Img+Attr`：文本、图像与结构化物品属性。
- `Text+Img+Audio+CF`：文本、视觉、音频内容结合协同过滤信号。
- `Text+Img+CF`：文本、图像表征结合协同过滤信号。
- `Text+Img+CF†`：文本、图像与协同信号融合表征（由配置推断）。
- `Text+Img+Geo`：文本、图像与地理空间信息。
- `Text+Img+Geo+CF`：文本、图像、地理空间与协同信号融合表征。
- `Text+Img+Geo†`：文本、图像与地理空间表征（由配置推断）。
- `Text+Img†`：文本与图像多模态表征（由配置推断）。
- `Text+SID`：稠密文本表征拼接离散语义 ID（稠密与生成式混合检索）。
- `Text+Time`：文本表征结合交互时间戳信息。
- `Text†`：物品文本表征（由配置推断）。
- `n/a`：不适用于该方法。
- `–`：论文未报告。
- `– / Text+Img`：一种配置未报告表征来源，另一种配置采用文本与图像表征。

## 编号（Tokenization）

- `Align. RQ`：带对齐目标训练的残差量化。
- `BDQ`：比特可分解量化器（Bit-Decomposable Quantizer）。
- `Bal. VQ+KM`：结合向量量化与均衡 k-means 聚类的编号方法。
- `C-RQ`：对比学习残差量化（Contrastive RQ）。
- `CART`：协同感知精化编号（Collaborative-Aware Refined Tokenization）。
- `CF-Aligned MM RQ`：与协同信号对齐的多模态残差量化。
- `Casc. RQ`：稀疏到稠密级联残差量化。
- `CoBa RQ-VAE`：兼顾协同对齐与码本均衡的 RQ-VAE。
- `Contr. RQ`：采用对比损失训练的残差量化。
- `Cross RQ`：跨模态交互残差量化。
- `Curr. RQ`：课程式训练的层级残差量化。
- `DSRQ`：双流残差量化（Dual-Stream Residual Quantization）。
- `Direct SID Heads`：直接输出语义 ID 码位的预测头。
- `Dual H-KM`：分别在行为与语义嵌入上构建的双源层级 k-means。
- `Dual RQ`：面向双表征流或双侧实体的双路残差量化。
- `Dual RQ-VAE`：面向两条独立表征流的双路 RQ-VAE。
- `Dyn. KM+Disamb.`：动态更新的 k-means 编码加冲突消歧后缀码。
- `Flow+PQ`：归一化流表征变换后接乘积量化（PQ）。
- `Freq. R-KM`：频率感知的残差 k-means 编号。
- `GAOQ`：全局对齐正交量化（Globally Aligned Orthogonal Quantization）。
- `Geo-Idx`：基于地理网格或空间索引构建的标识符。
- `Geo-Idx+RQ`：地理空间索引前缀结合残差量化。
- `Geo-Prefix+HClus`：地理空间前缀结合层级聚类编码。
- `Geo-Prefix+RQ-VAE`：地理空间前缀结合 RQ-VAE 残差码。
- `Graph RQ-VAE`：融合图结构传播的残差量化变分自编码器。
- `H-KM`：层级 k-means 聚类（Hierarchical k-means）。
- `HARQ`：双曲空间自适应残差量化（Hyperbolic Adaptive RQ）。
- `Hier. RQ`：带多级标签监督的层级残差量化。
- `KG-RQ`：融合知识图谱结构的残差量化。
- `LLM-Vocab`：直接从大语言模型原生词表 token 组合出的物品标识符。
- `Learn. RQ`：端到端或交替更新的可学习残差量化。
- `MM-RQ`：多模态残差量化（Multimodal RQ）。
- `Masked VQ`：面向掩码协同表征的向量量化。
- `MoE-VQ`：混合专家向量量化（Mixture-of-Experts VQ）。
- `Multi-Facet ID`：同时刻画物品多个语义切面的多维标识符。
- `Multi-Path R-KM+Hash`：多路径残差 k-means 结合哈希消歧组件。
- `NU-RQ`：带可学习非均匀变换的残差量化（Non-Uniform RQ）。
- `Nested RQ`：跨嵌套表征粒度的残差量化。
- `OPQ`：优化乘积量化（Optimized Product Quantization）。
- `Orth. RQ`：带正交约束的残差量化。
- `PC-AE`：并行码本自编码器（Parallel Codebook Auto-Encoder）。
- `PID (P-SAE)`：基于预训练稀疏自编码器的可解释标识符（Pretrained Interpretable ID）。
- `Par. OPQ`：并行优化乘积量化，生成无序多子空间码。
- `Par. VQ`：无顺序残差依赖的并行多码本向量量化。
- `Post-hoc RQ`：残差量化后接无冲突全局/递归重分配。
- `Prog. RQ`：渐进式残差量化变体（Progressive RQ）。
- `QA-RQ`：资质感知残差量化（Qualification-Aware RQ-VAE）。
- `R-KM`：残差 k-means 量化（Residual k-means）。
- `R-KM+EM`：带期望最大化（EM）精化的残差 k-means。
- `R-KM+FSQ`：残差 k-means 结合有限标量量化（FSQ）。
- `R-KM+Geo-CB`：残差 k-means 结合独立地理码本。
- `R-KM+Graph`：残差 k-means 结合语义码关联图。
- `R-KM†`：残差 k-means 编号（由配置推断）。
- `RQ`：残差向量量化（Residual Quantization）。
- `RQ+IST`：残差量化结合序列内子词合并（Item-level Subword Tokenization）。
- `RQ+LoRA`：带领域自适应 LoRA 模块的残差量化。
- `RQ-KM`：残差 k-means 量化。
- `RQ-PIB`：前缀交互负载均衡残差量化（RQ with Prefix-aware Interaction Balancing）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `RQ-VAE / Learn. RQ`：不同配置下分别采用固定 RQ-VAE 或可学习残差量化。
- `RQ-VAE / Par. VQ`：不同配置下分别采用层级 RQ-VAE 或并行向量量化。
- `RQ-VAE / R-KM / LETTER`：评测涵盖 RQ-VAE、残差 k-means 与 LETTER 等多种编号器配置。
- `RQ-VAE+DINO`：RQ-VAE 结合自监督 DINO 视觉特征量化。
- `RQ-VAE+PPR`：融合个性化 PageRank 图传播信号的 RQ-VAE。
- `RQ-VAE†`：残差量化变分自编码器（由配置推断）。
- `RecDMoN / RQ-GAE`：递归 DMoN 图划分，或基于图重构损失的图自编码残差量化。
- `Ref.-RQ`：引入参考锚点向量的残差量化。
- `SRBQ`：语义残差均衡量化（Semantic Residual Balanced Quantization）。
- `Self-Imp.`：训练过程中根据生成模型内部表征周期性自优化的编号。
- `Self-Sup. ID`：通过自监督任务直接学习的离散语义标识符。
- `Shared/Spec. RQ`：由跨域共享码本与领域专有码本组成的残差量化。
- `SimHash`：基于随机超平面的局部敏感哈希（SimHash）编码。
- `Skeleton R-KM`：围绕共享语义骨架组织的残差 k-means。
- `Soft Reassign. RQ`：带可微软重分配机制的残差量化。
- `Soft-RQ`：软路由残差量化变体。
- `Spectral Clus.`：基于谱聚类的层级编号。
- `Subspace RQ`：在嵌入子空间内分别执行的残差量化。
- `Term-ID`：由物品元数据提炼的标准化文本关键词标识符。
- `TokenMoE`：包含共享专家与领域专家的混合专家编号器。
- `Tree`：树状层级码本编号。
- `Tree-Clus.`：均衡 k 叉树聚类编号。
- `Unified RQ`：多领域共享空间的统一残差量化。
- `n/a`：不适用于该方法。
- `–`：论文未报告。

## 生成骨干（Backbone）

- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Dec-Only / Enc-Dec`：涵盖仅解码器与编码器-解码器两种骨干变体。
- `Dec-Only / Non-AR`：涵盖仅解码器自回归与非自回归并行预测两种变体。
- `Dec-Only†`：仅解码器自回归架构（由配置推断）。
- `Disc.`：对候选物品打分的判别式推荐骨干。
- `Disc. / Enc-Dec`：涵盖判别式打分与编码器-解码器生成两种变体。
- `Dual Enc-Dec`：共享编码器配合双并行解码器的双流架构。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Enc-Dec / Dec-Only`：同时在编码器-解码器与仅解码器两种骨干上验证。
- `Enc-Dec / Dec-Only (AR); Non-AR (PR)`：自回归分支采用编码器-解码器或仅解码器，并行分支采用非自回归骨干。
- `Enc-Dec / Lazy Dec-Only`：涵盖编码器-解码器与延迟解码（Lazy Decoder-only）两种变体。
- `Enc-Dec†`：编码器-解码器架构（由配置推断）。
- `Enc-Dec† / Dec-Only`：同时在推断的编码器-解码器与仅解码器骨干上验证。
- `Enc-Dec† / Dec-Only†`：同时在编码器-解码器与仅解码器骨干上验证（由配置推断）。
- `Enc-MLP`：序列历史编码器后接多层感知机（MLP）预测头。
- `Encoder`：双向编码器骨干，不进行逐位自回归解码。
- `Encoder (Non-AR)`：面向非自回归并行预测训练的双向编码器。
- `HeterRec`：论文命名的异构推荐骨干网络 HeterRec。
- `Lazy Dec-Only`：将计算集中在目标生成阶段的延迟仅解码器架构。
- `Lazy Dec-Only†`：由所沿用基座推断的延迟仅解码器架构。
- `Non-AR`：非自回归（Non-autoregressive）并行预测架构。
- `Non-AR / Enc-Dec`：涵盖非自回归与编码器-解码器两种骨干变体。
- `n/a`：不适用于该方法。
- `–`：论文未报告。

## 编号器更新（Training）

- `Altern.`：编号器与生成器在训练过程中交替迭代更新。
- `Altern.†`：编号器与生成器交替迭代更新（由配置推断）。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `Fixed†`：生成器训练期间冻结编号器（由配置推断）。
- `Joint`：推荐生成损失通过可微路径直接反传更新编号器。
- `n/a`：不适用于该方法。
- `–`：论文未报告。

## 训练目标（Training）

- `(MTP + Masked Rec.) → MTP`：先联合训练多 token 预测与掩码重构，再单独微调多 token 预测。
- `(NTP + Ctr.) → RL`：先联合训练下一 token 预测与对比损失，再执行强化学习后训练。
- `(NTP† / (NTP + Aux.)†) → KL-weighted OPD`：先进行下一 token 预训练初始化，再执行 KL 加权的同策略蒸馏（OPD）。
- `Discrim.`：判别式候选物品打分损失，不直接生成 SID。
- `Discrim. / NTP`：不同配置下分别采用判别式打分损失或下一 token 预测损失。
- `Dual-level Flow Ctr.`：流模型中在 token 级与完整标识符级同时施加的双层对比损失。
- `MTP`：多 token 并行预测损失（Multi-Token Prediction），一次前向同时预测多个码位。
- `MTP + Aux.`：多 token 预测与辅助损失联合优化。
- `MTP + Ctr.`：多 token 预测结合对比学习损失。
- `MTP + Ctr. + Aux.`：多 token 预测、对比损失与辅助目标联合优化。
- `MTP + Rel.MSE`：多 token 预测结合关系均方误差（MSE）损失。
- `Masked`：掩码部分码位并重构（含离散掩码扩散目标）。
- `Masked → RL (→ Masked KD for Fast)`：先做掩码预测预训练，再接强化学习对齐，快速变体进一步做掩码蒸馏。
- `Multi-task NTP`：在多个对齐或推荐子任务上联合优化下一 token 预测损失。
- `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT`：多任务下一 token 预测，或文本 NTP 加多 token 预测与排序损失；SFT 后接语言任务强化学习。
- `Multi-task NTP†`：多任务下一 token 预测（由配置推断）。
- `Multi-task NTP† / NTP`：不同变体下采用推断的多任务下一 token 预测或标准下一 token 预测。
- `Multi-task NTP† / NTP†`：不同骨干下采用推断的多任务或单任务下一 token 预测初始化。
- `NTP`：标准下一 token 预测（Next-Token Prediction）交叉熵损失；基于预训练 LLM 的指令微调（SFT）亦归入此类。
- `NTP + Aux.`：下一 token 预测结合辅助正则或对齐损失。
- `NTP + Ctr.`：下一 token 预测结合对比学习损失。
- `NTP + Dense`：离散 SID 的下一 token 预测结合稠密向量回归/对比损失。
- `NTP + PV-RSPO + Rank + Aux.`：下一 token 预测联合前缀价值 RSPO、排序损失与辅助损失。
- `NTP + RL`：下一 token 预测与强化学习目标联合训练。
- `NTP + Rank`：下一 token 预测结合显式排序损失。
- `NTP + Rank + Aux. / MTP + Rank + Aux.`：自回归或并行 token 预测联合排序损失与辅助损失。
- `NTP / NTP + Aux.`：单独使用下一 token 预测，或与辅助损失联合优化。
- `NTP → (NTP + Aux.)`：先进行下一 token 预测预训练，再联合优化下一 token 预测与辅助目标。
- `NTP → (NTP + DPO)`：先进行下一 token 预测微调，再联合优化下一 token 预测与直接偏好优化（DPO）。
- `NTP → (RL + Rank)`：先进行下一 token 预测微调，再联合优化强化学习与排序目标。
- `NTP → DPO`：先进行下一 token 预测微调，再执行直接偏好优化（DPO）。
- `NTP → RL`：先进行下一 token 预测微调，再执行强化学习（如 GRPO、GBPO 等）。
- `NTP → RL†`：先进行下一 token 预测微调，再执行强化学习（由配置推断）。
- `NTP†`：下一 token 预测损失（由配置推断）。
- `NTP† / NTP → RL`：一种配置采用下一 token 预测，另一种配置后接强化学习微调。
- `Next-item CE + Cons. KD + Rank KD`：下一物品交叉熵联合一致性知识蒸馏与排序蒸馏。
- `n/a`：不适用于该方法。
- `–`：论文未报告。

## 推理解码（Inference）

- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。
- `Beam+Agg.`：束搜索后对指向同一物品的多条标识符预测聚合得分。
- `Beam+Geo-Filter`：结合地理位置范围过滤候选的束搜索。
- `BeamFusion`：融合自回归 SID 束搜索得分与稠密最近邻检索得分的联合解码。
- `Beam†`：自回归束搜索（由配置推断）。
- `Beam† / C-Beam`：不同配置下采用自回归束搜索或前缀约束束搜索。
- `Beam† / C-Beam†`：所沿用基座中的束搜索或约束束搜索。
- `Beam† / –`：一种配置沿用束搜索，另一种配置未报告解码方式。
- `Bid-Aware Beam`：在束搜索打分中融合广告出价（Bid）信息的解码。
- `C-Beam`：受合法物品集合约束的束搜索（Constrained beam search）。
- `C-Beam / Scoring`：依配置采用约束束搜索或直接候选打分。
- `CF-Guided C-Beam`：由协同过滤信号引导剪枝与打分的约束束搜索。
- `CoT`：先生成思维链（Chain-of-Thought）推理文本，再输出目标 SID。
- `CoT+Beam`：显式推理后接束搜索解码。
- `CoT+C-Beam`：显式推理后接合法前缀约束束搜索。
- `CoT+Fuzzy Match`：推理引导生成标识符后通过模糊匹配映射至真实物品。
- `CoT+Greedy`：显式推理配合贪心解码。
- `Diff.`：迭代去噪扩散解码。
- `Diff.+Beam`：离散扩散解码结合束搜索。
- `Diff.+Legalize`：扩散生成码序列后映射合法化为目录中的真实物品。
- `Div. Beam`：引入显式多样性重排或惩罚项的束搜索。
- `Div. C-Beam`：引入显式多样性机制的约束束搜索。
- `Dual Beam`：在双分支上分别束搜索并融合候选结果。
- `Dyn. Beam`：按步或按样本动态调整束宽的束搜索。
- `Ensemble`：对同一历史的多种随机切分或多路径解码结果聚合排序。
- `FM-Index+Agg.`：基于 FM-index 约束生成并聚合指向同一物品的多标识符得分。
- `FP8+RecoGEM`：采用 FP8 低精度量化与 RecoGEM 推理引擎部署解码。
- `Fusion`：融合并行双解码分支输出的候选得分。
- `GRC+Beam`：生成-反思-修正（GRC）配合束搜索解码。
- `Graph`：在合法物品 SID 近邻图上做迭代图搜索解码。
- `Greedy`：每步直接选取概率最高 token 的贪心解码。
- `Hybrid`：结合生成式 SID 解码与稠密/共现检索的混合召回。
- `ISD Beam`：由用户侧物品打分支撑前缀保留的束搜索（Item-Supported Beam）。
- `Length-Quota Beam`：按可变 SID 长度分配候选配额的束搜索。
- `Non-AR`：单次前向非自回归并行解码。
- `PRM-Beam`：由过程奖励模型（PRM）逐步引导的束搜索。
- `PV-Beam+Rerank`：前缀价值引导束搜索后接候选重排。
- `Scoring`：直接计算候选物品得分，不逐位生成 SID。
- `Scoring / Beam`：不同配置下采用候选直接打分或自回归束搜索。
- `Scoring / Beam†`：判别式候选打分与生成式束搜索对比。
- `Scoring+Rerank`：先对候选集打分筛选，再对头部子集精细重排。
- `Self-Draft+Hash`：自草稿投机生成配合哈希集合合法性校验。
- `Sess. Beam`：单次生成包含多个物品的整段会话列表（Session-wise beam search）。
- `Spec. Dec.`：草稿模型与目标模型协同的投机解码（Speculative decoding）。
- `Trie/C-Beam`：基于前缀树（Trie）约束的束搜索，仅允许解码真实存在的物品前缀。
- `Vec. C-Beam`：向量化并行前缀约束束搜索。
- `n/a`：不适用于该方法。
- `–`：论文未报告。
