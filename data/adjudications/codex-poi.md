# A. POI 九篇独立打标（Codex）

日期：2026-10-28。依据 B7 本地 PDF，页码均为 PDF 物理页码；与本轮其他窗口独立。只提交建议，不修改 Table 1/2。

Tokenizer 列指训练关系（如 Fixed/Joint），与五阶段配置中的 Tokenization 算法列分开；Objective 列记录目标，不把 CPT/SFT 这类阶段名直接当目标。来源位置后的事实和判定推断分开标记。

## 1. GNPR-SID

原文：[arXiv v2](https://arxiv.org/abs/2506.01375)，本地 `GNPR-SID_2506.01375.pdf`。【事实】以下依据来自本地全文。【事实】

- **毛病：I（信息不够），次候选 II** p1 摘要首先明确批评随机编号无法表达地点语义；p3–4 §4.1.1 将类别、区域、营业时间及共访用户引入表示；p5–6 §4.1.3 又用 diversity loss 改善码本利用与冲突。【事实】按摘要的主要抱怨，建议 I；如果把“新增设计”只数为 diversity loss，则 II 有理由，不能把这条边界抹掉。【推断】
- **改动阶段：Tokenization** p2 贡献及 §4.1 的新设计集中在 semantic ID construction，生成侧主要是已有 LLM 的微调。【事实】编码模块横跨 Representation 与 Tokenization，按贡献整体及新量化损失取后者。【推断】
- **Tokenizer：Fixed** p6 §4.2 在前面已经构造出的 SIDs 上建立 SFT 数据，p7 分别给出 RQ-VAE 和 LLaMA 微调设置，没有生成器回传更新码本的路径。【事实】由顺序流程判 Fixed，而不是将文中的 end-to-end 直接读作 Joint。【推断】
- **Objective：NTP†** p6 §4.2.2 以真实下一 POI 的 SID 作输出监督；未找到生成器目标的完整公式。【事实】NTP 是依据 SFT 输出任务的推定，量化的 reconstruction/quantization/diversity 三项不应混进生成器 Objective 列。【推断】
- **五列核对：** `Attr+Geo+CF / RQ-VAE / Dec-Only / 2-Stage / –` 基本成立：p3–4 §4.1.1 是 one-hot 类别、Plus Codes 区域、时间与协同特征；p4–6 §4.1.2–3 是 RQ-VAE；p7 §5.2 是 LLaMA3-8B；p6 是先编号再微调；正文未给解码算法，保留 `–`，含义为未报告。【事实】旧 Training 拆成上面两列。【推断】
- **可供后续分析的反例：** p8 Table 4 中 NYC 的 λ 从 0.25 增至 0.75，Unique 从 3,259 增至 3,313，但 Acc@1 从 0.3618 降至 0.3368；这里只能说明该消融中唯一性代理与准确率不单调。【事实】

## 2. GeoGR

原文：[arXiv v2](https://arxiv.org/abs/2602.10411)，本地 `GeoGR_2602.10411.pdf`。【事实】

- **毛病：I，III 为明确并列候选** p1 摘要的两条抱怨分别是 SID 缺少跨类别时空协同关系，以及 LLM 与 POI 任务对齐不足。【事实】按首项设计是 geo-aware SID pipeline，暂取 I；这不是单凭使用 LLM 就归 III。【推断】
- **改动阶段：Representation（备选 Tokenization）** p4 §4.1.1 用地理约束共访对训练语义编码器；p5 §4.1.3 则用生成预测反过来修 SID。【事实】针对 I 的直接组件是前者，因此取 Representation；若 leader 最终把主毛病定 III，阶段应重审为 Tokenization/Training，不能只改主标签。【推断】
- **Tokenizer：拿不准，`Altern.` / `Fixed`** p5 Algorithm 1 与 §4.1.3 明确交替固定 SID 微调 LLM、固定 LLM 更新 SID，不能遗漏；但 Fig.2 将这部分放在 SID 构建阶段，§4.2 又单列最终推荐器的 CPT/SFT。【事实】全流程口径应记 `Altern.`；若本列严格限定“最终推荐生成器训练期间”，则 `Fixed`。【推断】原文没有充分说明 EM 的 LLM 与最终推荐器权重是否同一条持续训练链，建议表格用 `Altern.†` 并保留此脚注，待深度轮核源码。【推断】
- **Objective：Multi-task NTP** p5 §4.2.1 式(9)是多种模板的 next-token likelihood；p5–6 §4.2.2 是下一 POI 的 SFT。【事实】按现有词表记 Multi-task NTP；EM 是更新流程，不能作为另一个损失名称。【推断】
- **五列核对：** `Text+Geo+CF / R-KM+EM / Dec-Only / CPT+SFT / Beam` 的表示、编号、骨干和解码成立：p4 Eq.(3)与共访 NCE，p5 Eq.(5–8)及 Algorithm 1，§4.2 Qwen-4B，p9 服务段 dynamic beam search。【事实】旧 Training 漏掉了构码时交替优化，拆列时必须说明；不能仅凭 CPT+SFT 转成 Fixed。【推断】

## 3. Gwhere

原文：[arXiv v1](https://arxiv.org/abs/2607.26073)，本地 `Gwhere_2607.26073.pdf`。【事实】

- **毛病：拿不准，II / I；暂倾向 II** p1 摘要并列冗余/碰撞与异质信号整合不足；p2 第一条贡献是全对比 tokenizer，p3 §3.2 明说 reconstruction 与区分物品的目标不一致，并替换为对比学习。【事实】按新设计和贡献顺序，II 更合适；多模态融合则支持 I。【推断】EAKTO 虽重要，却不能使全篇自动归 IV。【推断】
- **改动阶段：Tokenization** p3 §3.2.2 的 soft RQ、contrastive objective 是针对区分性和碰撞的主要改动；§3.3–4 是后续 LLM 训练。【事实】按选定毛病取 Tokenization。【推断】
- **Tokenizer：Fixed†** p6 Fig.1 明确先离线构建 SID，再 CPT、SFT、偏好对齐；没有展示推荐损失回传码本。【事实】这支持 Fixed，但原文未用 freeze 明说，保留 †；“end-to-end industrial framework”不是 Joint 的充分依据。【推断】
- **Objective：NTP + Aux. + KTO（EAKTO）** p4 §3.3.1 包含 masked SID prediction 与匹配/错配 triplet 判别，§3.3.2 为 cross-entropy，§3.4 为 EAKTO。【事实】现有 12 值词表没有 KTO，不能把它直接换成 DPO 或 GRPO；建议先保留 `NTP + Aux. → EAKTO` 的原文描述，合并时决定是否扩展受控词表，不直接新增源表值。【推断】
- **五列核对：** `Text+Img+Geo+CF / Contr. RQ / Dec-Only / CPT+SFT+EAKTO / –` 基本成立：p3 §3.2.1 和 p5 §4.1.2 明确四种模态；p3 soft RQ；p5 §4.1.4 使用 Qwen2.5 的 0.5B–7B 版本；p6 Fig.1 为训练顺序。【事实】未找到明确的 beam 配置，`–` 保留未报告含义；p8 总结提及 multi-token prediction/prefill-decoding 工程优化，不足以据此填 Beam。【事实】
## 4. LGRID

原文：[arXiv v1](https://arxiv.org/abs/2607.27944)，本地 `LGRID_2607.27944.pdf`。【事实】

- **毛病：I；II 是结果层面的次标签** p1 的核心抱怨是单一表示中属性纠缠造成关键信息损失及不透明，碰撞是其后果；p3 §3.2 直接把干预定位为 representation-construction。【事实】按根因而非最大数字取 I。【推断】
- **改动阶段：Representation** p3–5 §3.3–3.5 的联合编码、slot disentanglement、属性解码和对比正则先产生可解释槽位，然后 §3.6 才量化。【事实】按首次核心干预取 Representation。【推断】
- **Tokenizer：Fixed（相对下游推荐器）** p5 §3.6.2 明确 slot 表示收敛并固定后再训 DSRQ；§3.6.3 说明全部 SID 离线生成、在线查表。【事实】这不是 Joint，也不是 LLM 直接逐 token 生成推荐对象。【推断】
- **Objective：Discrim.；具体下游损失拿不准** p5 §3.1/§3.6.3 定义 scoring function 并把 SID 嵌入与 item-ID 拼接；p6 Table 1 用多种判别模型和 AUC。【事实】不能把上游属性解码 NTP+Ctr. 填成推荐器目标；具体 BCE/BPR 等随 backbone 变化，原文未统一给出，取现有概括标签 Discrim.。【推断】
- **五列核对：** `Text+Geo / DSRQ / Disc. (DIN 等) / 2-Stage / Scoring` 成立，证据为 p3 §3.3、p5 §3.6、p6 Table 1、p8 Efficiency。【事实】“2-Stage”指上游学习顺序不够精确，拆列后按 Fixed / Discrim. 记录；即便用户已决定 POI 收录，也需显式标为“SID 用作特征”，不要将它的 AUC 结果当逐码生成的证据。【推断】

## 5. LGSID

原文：[arXiv v1](https://arxiv.org/abs/2511.14221)，本地 `LGSID_2511.14221.pdf`。【事实】

- **毛病：I** p1 摘要抱怨仅把位置写进 prompt 不能保留精细空间属性及距离；G-DPO 是为编码器注入地理/协同知识。【事实】这里的 “alignment” 对象是物品表示的领域知识，不自动等于 SID–generator alignment。【推断】
- **改动阶段：Representation** p2 第一项实质模块及 p3–4 “RL-based Geographic LLM Alignment”训练 list-wise reward model，再用 G-DPO 改编码 LLM 的表示；地理分层量化是后续模块。【事实】按主毛病和干预顺序取 Representation，备选 Tokenization 的理由是标题与第二个核心模块均强调构码，需保留边界。【推断】
- **Tokenizer：Fixed†** p4 构码发生在 LLM 表示对齐之后，p6 Table 2 将这些码分别接 TIGER/OneRec；没有写生成器反向更新编号器。【事实】因此 Fixed 是流程推定。【推断】
- **Objective：NTP†（TIGER）；OneRec 分支拿不准 NTP / NTP+DPO** p6 Table 2 指明两个生成器，但未在该实验处说明 OneRec 是否复现其偏好优化。【事实】不能把上游 G-DPO 放到生成器 Objective，也不能把另文 OneRec 的完整训练直接搬来；建议主表 `NTP†`，脚注注明 OneRec 目标未详述。【推断】
- **五列核对：** `Text+Geo+CF / Geo-Idx+RQ / Enc-Dec / 2-Stage / Beam†` 对应 p1、p3–4 的协同/地理混合偏好对与编码，p4 离散空间和内容属性首码、对齐向量的残差码，p6 TIGER/OneRec。【事实】Enc-Dec 仅代表生成式分支，p6 Table 1 另有判别模型；Beam 仍仅按 TIGER 推定，原文未报告解码配置，不应去掉 †。【推断】

## 6. OneLoc

原文：[arXiv v1](https://arxiv.org/abs/2508.14646)，本地 `OneLoc_2508.14646.pdf`。【事实】

- **毛病：建议放“范式、系统与基准”；备选 I** p1 摘要先说 local-life 尚缺端到端生成推荐，再提出三处地理设计和多目标奖励；p3 贡献第一项是整套 local-life generative system。【事实】按现有“整体新范式/系统”的规则放顶块；若 leader 认为这只是 OneRec 的领域适配而非整体范式，则三处地理设计对两类奖励，I 比 IV 更有主标签理由。【推断】
- **改动阶段：Generative Backbone（若顶块仍要求五选一）** p2、Fig.2 与 §2.3–2.4 的 geo-aware encoder attention、neighbor-aware decoder prompt 是系统结构中的主要新组件。【事实】该标签仅作配置定位；顶块不硬配毛病。【推断】
- **Tokenizer：Fixed** p3 §2.2 先在多模态视频/位置嵌入上作残差聚类，p5 Eq.(21)、(25–26)单独训练推荐器，没有码本梯度更新。【事实】按流程判 Fixed。【推断】
- **Objective：`NTP → DPO`（按现有受控词表；DPO 阶段仍混合 NTP）** p5 Eq.(26)显式相加，地理距离与 GMV 奖励用于构造偏好对。【事实】
- **五列核对与确定更正：**
  - **Tokenization `RQ-VAE` → `R-KM`** p3 §2.2 “Geo-aware Semantic IDs”明写 res-kmeans，Eq.(1) 是 K-means；p7 出现 RQ-VAE 的位置是 TIGER baseline 描述，不能作为 OneLoc 的依据。【事实】
  - **Representation `Text+Img+Geo+CF` → `Multimodal+Geo`（或 `Text+Img+Geo†`）** p3 §2.2 只明确多模态 LLM 提取视频内容与位置上下文，未给出 CF 训练信号进入 tokenizer 输入的证据；用户交互序列输入推荐器不等于 SID 表示用了 CF。【事实】文本描述在 p2 明写，视频的视觉模态合理，但原文未明确拆成静态 Img，建议保留 Multimodal 而不是强填 Img+CF。【推断】
  - **Backbone `Enc-Dec`**：p2 与 Fig.2、§2.3–2.4 明确，保留。【事实】
  - **Training `NTP+DPO`**：与 Eq.(26)一致，拆为 Fixed / NTP → DPO，并注明 Eq.(26) 的混合目标。【事实】
  - **Inference `Beam` → `Beam+Reward-Rank/Filter`（服务口径）** p6 §3 的 Video Mapping Server 后接 GMV score estimation 与 rule-based filtering，最后 TopK；若表只记录生成器解码，Beam 可以保留，但正文必须注明外部后处理。【事实】

## 7. ProGEO（原文名 Pro-GEO）

原文：[arXiv v1](https://arxiv.org/abs/2604.23156)，本地 `ProGEO_2604.23156.pdf`。【事实】

- **毛病：I，备选 II** p1 摘要的抱怨是语义 codebook 忽视地理，导致不可到达的推荐；解决方式是把相对地理关系显式编码。【事实】这里的地理不可达不同于“SID 不指向真实物品”，因此按当前 II 定义不能直接归 II；首选 I，若未来 II 扩为情境可行性须全表一致改规则。【推断】
- **改动阶段：Tokenization** p3–5 §3 设计局部坐标与 Geo-RoPE，并在残差聚类中形成 geo-codebook；不是仅给生成器附加经纬度。【事实】按组件安装位置取 Tokenization。【推断】
- **Tokenizer：Fixed†** p11 §B.2.1 分别给 item tokenization 与生成器训练，未见联合更新；R-Kmeans 构码随后作为固定目标。【事实】按流程推定 Fixed。【推断】
- **Objective：NTP†** p11 给 Qwen2.5-1.5B 的 instruction/output SID list 训练与优化器，未找到与主表完全对应的显式生成器损失公式。【事实】只能按自回归监督微调推定 NTP，不应记 RL。【推断】
- **五列核对：** `Text+Geo / R-KM+Geo-CB / Dec-Only / 2-Stage / Beam+Geo-Filter` 大体成立：p3–5 构码，p11 Qwen3-Embedding-8B 与 Qwen2.5-1.5B，p11 Appendix B.2 给候选地理筛选和 beam width=20。【事实】该附录同时写候选仅 10 个、正文报告 Hit@50/100，计分候选范围存在需要作者/代码解释的张力；本轮只标“协议待核”，不擅自认定实验错误。【推断】公开集还使用 Layer-4 hard ID，表注宜区分工业与公开配置。【推断】

## 8. ROS

原文：[arXiv v2](https://arxiv.org/abs/2601.04562)，本地 `ROS_2601.04562.pdf`。【事实】

- **毛病：I（备选 III）** p1 摘要和引言反复批评地理信息虽作为特征输入，却没有成为 reasoning 的决策变量；p2–4 把空间 SID、Mobility CoT、空间奖励连起来。【事实】这是模型没有用好地理信号，按现有 I 的问句可容纳；若把核心抱怨读成“模型不能 reasoning over SID”则 III 也合理，不能仅因有 GRPO 就判 IV。【推断】
- **改动阶段：Training** p3 §2.3 是 CoT traces 的 SFT；p4 §2.4 是空间引导 GRPO，骨干仍是已有 Qwen。【事实】主要干预改变模型学习的推理/空间行为，取 Training；Tokenization 是次阶段。【推断】
- **Tokenizer：Fixed** p2 §2.2 先构造 SID，随后 grounding pretraining；p12 §A.3 分别描述地理编码、语义量化与后续三阶段模型训练。【事实】按顺序判 Fixed。【推断】
- **Objective：`NTP → RL`（前段为 Multi-task NTP，后段为 GRPO）** p2–3 有双向 text↔SID 与序列预测，p3 CoT SFT，p4/p12 有 GRPO 与 format/SID/distance reward。【事实】
- **五列核对：** `Text+Geo / Geo-Prefix+RQ-VAE / Dec-Only / PT+SFT+GRPO / CoT+C-Beam` 主要成立：p2 §2.2.1 的 S2 地理前缀、Qwen-0.6B 类别文本、RQ-VAE 语义锚点、区分后缀；p12 学生 Qwen3-4B，教师 Qwen3-235B。【事实】**推理必须限缩口径**：p7 “Top-K Recommendation via Two-Stage Inference”明确它是扩展实验，主实验为 HR@1；因此建议 `CoT（Top-1）；CoT+C-Beam（Top-K）`，不能说所有结果都来自 C-Beam。【事实】

## 9. Think2Go

原文：[arXiv v1](https://arxiv.org/abs/2607.28997)，本地 `Think2Go_2607.28997.pdf`。【事实】

- **毛病：III** p1 摘要明确说 SID 独立训练导致 LLM 理解不足，p2 再把 decoupled training 与 SID comprehension 联系；主要方案把记忆式 SFT 和探索式 RL 结合。【事实】按明确抱怨归 III；优势估计虽改优化，不足以把主标签变成 IV。【推断】
- **改动阶段：Training** p5 Fig.2 是 Think→Go token 的策略优化与 Answer token 的 SFT；§4.2 修改 advantage 的 uncertainty/reward-gap 权重。【事实】取 Training，不把“single architecture”误读为新 backbone。【推断】
- **Tokenizer：Fixed†** p2 讨论 pretrained SID，p7 说明 RQ-VAE SID；Fig.2 的联合优化发生在推理与答案 token，没有 tokenizer 更新分支。【事实】因此 Fixed 为推定，“joint”不能据此填 Joint。【推断】
- **Objective：`NTP → RL`（RL 阶段联合保留 Answer-SFT；DAPO-style，带 STEU/DRG 修正）** p4 先列 DAPO 目标，p5–6 给修改后的 advantage，Answer 部分为 SFT；不是可直接记成标准 GRPO 的复现。【事实】主表用既定 NTP → RL；脚注保留训练中联合 NTP 的事实与具体 RL 变体，箭头只概括阶段顺序。【推断】
- **五列核对：** `Attr+Geo+CF† / RQ-VAE† / Dec-Only / SFT+RL / CoT+Beam`：p7 明确 RQ-VAE，可去掉该算法的 †，但码表构造细节仍不完备；p6–7 数据处理沿 GNPR 不足以严格证明所有输入字段与 CF 相同，Representation 的 † 保留。【事实】p11 Appendix A 明确 LLaMA3.1-8B 与 inference beam=15，CoT+Beam 成立；训练 rollout beam=10 与 inference beam=15 要分开。【事实】

## 汇总与合并提醒

| 方法 | 毛病建议 | 主阶段建议 | Tokenizer | Objective |
|---|---|---|---|---|
| GNPR-SID | I（边界 II） | Tokenization | Fixed | NTP† |
| GeoGR | I（边界 III） | Representation（边界 Tokenization） | Altern.† / Fixed，拿不准 | Multi-task NTP |
| Gwhere | II / I，拿不准 | Tokenization | Fixed† | 现词表无法无损表达：NTP + Aux. → EAKTO |
| LGRID | I | Representation | Fixed | Discrim. |
| LGSID | I | Representation | Fixed† | NTP†；OneRec 分支目标待核 |
| OneLoc | 范式、系统与基准（备选 I） | Generative Backbone | Fixed | NTP → DPO（后段混合 NTP） |
| ProGEO | I | Tokenization | Fixed† | NTP† |
| ROS | I（边界 III） | Training | Fixed | NTP → RL（Multi-task NTP；GRPO） |
| Think2Go | III | Training | Fixed† | NTP → RL（联合 Answer-SFT） |

表内均为本轮依照规则作出的判定建议，不构成论文作者自报分类。【推断】

确定需要修的旧值是 OneLoc 的 RQ-VAE；其 Representation 的 CF 缺证据，ROS 的 C-Beam 仅适用于 Top-K 扩展，GeoGR 的 EM 交替构码不可从训练描述中漏掉。【事实】POI 范围决定仍服从 10-27 新要求；旧 Table 2 中“暂缓进 Table 1”已失效，但本轮不直接改源表。【事实】

局限：本次核对的是列出的本地版本与 arXiv 摘要，没有运行作者源码；† 和“拿不准”都保留到深度轮。【事实】发表场所不是本轮四项打标的判定依据，未因版权页占位信息补填 venue。【事实】

最终核对补充：现有 Objective 词表只允许 12 种写法，顺序偏好优化/RL 用箭头；本轮已统一 OneLoc、ROS、Think2Go 的建议表值，Gwhere 的 EAKTO 是真实词表缺口，留待合并决策，不把二元反馈 KTO 擅写成 DPO。【事实】【推断】
