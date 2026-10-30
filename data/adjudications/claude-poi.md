# A. POI 9 篇双盲打标（claude，10-28）

规则按 `材料/Table1_扩展版.md`「附：毛病与阶段的依据」：毛病先看摘要里明说、且论文为它加了新设计的抱怨；一比一时依次看新设计多数、题目、第一件设计；阶段看对付该毛病的组件装在哪，仍分不出取贡献列表第一条。Tokenizer、Objective 只用表下注的写法。

页码是 `papers-archive/B7/` 里 PDF 的物理页码（pdftotext 按换页符切分）。没有读对方的输出。

## 总表

| 方法 | 毛病 | 阶段 | Tokenizer | Objective | 拿不准的地方 | 五列要改的 |
|---|---|---|---|---|---|---|
| GNPR-SID | I | Tokenization | Fixed | NTP | 阶段备选 Representation（较弱） | 无 |
| GeoGR | I | Representation | Fixed | NTP | 阶段（备选 Tokenization）；Objective（备选 Multi-task NTP） | 无（Inference 可写 Dyn. Beam，次要） |
| Gwhere | II | Tokenization | Fixed | NTP → DPO | 毛病（备选 I）；Objective（备选 NTP → RL） | 无 |
| LGRID | I | Representation | Fixed | Discrim. | 毛病（备选 II）；阶段（备选 Tokenization） | 无 |
| LGSID | I | Representation | Fixed | Discrim. / NTP | 无 | Backbone、Inference 补判别式一套（次要）；Venue 已证实 AAAI'26 |
| OneLoc | I | Representation | Fixed | NTP → DPO | 阶段（备选 Backbone） | **Tokenization RQ-VAE → R-KM（重要）**；Representation 去掉 CF（重要）；Venue 查不到 WSDM'26 |
| ProGEO | I | Tokenization | Fixed | NTP | 无 | 无 |
| ROS | I | Tokenization | Fixed | NTP → RL | 阶段（备选 Training）；毛病（备选 III） | Venue 已证实 ACL'26 |
| Think2Go | III | Training | Fixed | NTP → RL | Objective（备选 NTP + Aux.） | Tokenization 去掉 †（次要） |

分布：I 7 篇（其中 Representation 4、Tokenization 3），II 1 篇，III 1 篇。POI 论文几乎都在修"SID 不带地理信息"。【推断】

---

## 1. GNPR-SID（arXiv 2506.01375，KDD'25）

- **毛病：I**。摘要唯一明说的抱怨是 "employ random numeric IDs for POIs, limiting the ability to model semantic relationships between similar locations"（p1），新设计是用语义和协同特征建 SID。【事实】diversity loss 针对撞号（II），但摘要没把撞号写成前人的毛病，只说 "to ensure that SIDs are uniformly distributed"（p1），按"先照摘要里的抱怨定"不取 II。【推断】
- **阶段：Tokenization**。相对所基于的 LLM4POI（随机 ID），核心改动是把 RID 换成量化得到的 SID（§4.1，p3–5；贡献第 2 条 "semantic ID construction method that maps POI into semantic ID by POI quantization"，p2）；消融 "w/o SID" 掉 7.24%（Table 3，p8）。【事实】备选 Representation：§4.1.1 的 POI 语义表示（类别、Plus Codes 区域、营业时段、常访用户 one-hot 拼接，式 (1)，p4）也是新设计，但只是特征拼接，主体在量化。【推断】
- **Tokenizer：Fixed**。先训 RQ-VAE 得到 SID，再用 LoRA 微调 LLaMA3-8B（§4.2，p6；§5，p7）。【事实】
- **Objective：NTP**。SFT 数据以真实下一 POI 的 SID 为输出（p6）。【事实】
- **五列核对**：Representation Attr+Geo+CF 对，Attr 里含营业时段 t（式 (1)，p4）；Tokenization RQ-VAE 对（式 (2)–(8)，p4–5），撞号时追加一位区分码（p5）；Backbone Dec-Only 对（LLaMA3-8B，p7）；Inference "–" 对，只报 Acc@1（式 (16)，p7），没写解码方式。Venue KDD'25 对（DOI 10.1145/3711896.3736981，p1）。【事实】

## 2. GeoGR（arXiv 2602.10411）

- **毛病：I**。摘要两条抱怨一比一："inadequate modeling of high-quality SIDs that capture cross-category spatio-temporal collaborative relationships"（I）和 "poor alignment between large language models (LLMs) and the POI recommendation task"（III）（p1）。【事实】新设计：地理约束共访对上的对比表示学习 L_P2P（I）、EM 式 SID 迭代修正（作者说为 "mutual alignment between the LLM and the SIDs"，p5，偏 III）、CPT（III）。设计数打平；题目 "Enabling Spatio-Temporal Aware ..." 点的是 I；第一件设计也是 I。按"打平：题目"取 I。【推断】
- **阶段：Representation（拿不准，备选 Tokenization）**。修 I 的组件是 L_P2P：用 NCE 损失微调 Qwen 编码器（式 (4)，p4），装在表示阶段；消融里 L_P2P 单独带来最大涨幅（Table 4，p8）。【事实】备选 Tokenization 的理由：作者把 L_P2P、RQ-Kmeans、EM 合称 "geo-aware SID tokenization pipeline"（贡献第 2 条，p2）。【事实】
- **Tokenizer：Fixed**。EM 算法里交替"微调一个 LLM 从 POI 描述预测 SID"和"用预测更新 SID"（Algorithm 1，p5），但这一步在推荐生成器训练之前完成；生成器 CPT+SFT 在定好的 SID 上训（§4.2，p5）。若把 EM 里的 LLM 视为生成器，可记 Altern.，我认为不应如此。【推断】
- **Objective：NTP（拿不准，备选 Multi-task NTP）**。CPT 用 "a mixture of text and SID hybrid data" 和多种模板，随后 SFT（p2，p5）。【事实】Table 1 把同样"继续预训练 + SFT"的 PLUM 记为 NTP，按 PLUM 记 NTP；按 LC-Rec 的口径（多种任务同一损失）则记 Multi-task NTP。两种记法要统一。【推断】
- **五列核对**：Representation Text+Geo+CF 对（e = LLM(concat(lon, lat, loc, c))，式 (3)，p4；共访对，p4）；R-KM+EM 对；Dec-Only 对（Qwen-4B，p7）；Inference Beam 对（离线 "beam search (or alternative decoding strategies)"，p6；线上 "generates 50 candidate SIDs using dynamic beam search"，p9）。若想和 FORGE 统一，可写 Dyn. Beam（次要）。Venue arXiv'26 对（v2，2026-08-31，ACM 模板占位符未填，p1）。【事实】

## 3. Gwhere（arXiv 2607.26073，RecSys'26）

- **毛病：II（拿不准，备选 I）**。摘要明说的挑战是 "redundant or colliding token assignments"（II）和 "insufficient integration of heterogeneous item signals"（I）（p1）。【事实】两条都由同一个全对比 RQ tokenizer 对付，一比一。按"新设计多数"：去掉重构损失、改用对比损失是为 "robust differentiation among items"（§3.2，p3），Gumbel 软分配的可微 RQ 也服务区分度；注意力融合服务 I。结论段写的是 "enhance token discriminability and alleviate code collision"（p8）。取 II。【推断】备选 I：§3.2.1 多模态特征抽取与融合排在方法第一节（p3），贡献第 1 条先写 "integrates heterogeneous POI signals"（p2）。【事实】
  - 另：摘要里 "produce predictions consistent with real user behavior" 和 EAKTO 对应 IV（p1，§3.4，p4），但摘要把它写成任务要求而不是前人的毛病，不计入。【推断】
- **阶段：Tokenization**。I 和 II 的设计都在 tokenizer 里（§3.2，p3）。【事实】
- **Tokenizer：Fixed**。"Based on these SIDs, Gwhere adapts LLMs"（p1），tokenizer 先训好。【事实】
- **Objective：NTP → DPO（拿不准，备选 NTP → RL）**。CPT（含 Masked SID Prediction、SID–属性匹配，p4）→ SFT（交叉熵，p4）→ EAKTO。EAKTO 基于 KTO，用 π_θ/π_ref 的对数比作隐式奖励，不做 rollout（式 (1)，p4–5），属于 DPO 一族的离线偏好优化。【事实】原文称它 "a reinforcement learning objective"（p1），按原文措辞则记 NTP → RL。【事实】
- **五列核对**：Text+Img+Geo+CF 对（BERT 文本、ViT 图像、Haversine 空间图上的 GraphSAGE、ALS 协同，§3.2.1，p3）；Contr. RQ 对；Dec-Only 对（Qwen2.5 0.5B–7B，p5）；Training CPT+SFT+EAKTO 对；Inference "–" 对，没写束搜索配置（结论提到部署用 "multi-token prediction"，p8）。Venue RecSys'26 对（p1 页眉）。【事实】

## 4. LGRID（arXiv 2607.27944）

- **毛病：I（拿不准，备选 II）**。摘要第一条抱怨：单一表示里的 "semantic entanglement ... causing key attributes to be insufficiently preserved during quantization, degrading SID quality, and leading to severe SID collisions"；第二条是可解释性（落不进六类）（p1）。【事实】第一条的主语是"关键属性（地理、品牌、类别）没保住"，对策 SD-Block 把隐状态分到地理槽和语义槽，属 I。【推断】备选 II：摘要的头条结果是全 SID 撞号率 39.9%，对照 LGSID 的 97.0%（p1）。【事实】
- **阶段：Representation（拿不准，备选 Tokenization）**。修纠缠的组件是 SD-Block 和 Synergistic Alignment，作用在 LLM 隐状态上、量化之前（§3，Fig. 2，p3）。【事实】备选 Tokenization：DSRQ 分两路量化，也是新设计，贡献第 2 条把整条 encode → disentangle → align → quantize 当一件（p2）。【事实】
- **Tokenizer：Fixed；Objective：Discrim.**。任务定义为 "learning a scoring function to estimate the interaction probability"（§3.1，p3）；SID 作为 DIN、DIEN、SIM、HSTU 等判别式模型的特征，按 AUC 评（p5–6）。【事实】
- **五列核对**：Text+Geo、DSRQ、Disc. (DIN 等)、2-Stage、Scoring 都对。【事实】
- **收录提示**：LGRID 不生成 SID，同 Table 1 已收的 PSRQ（I × Tokenization，Discrim.，Scoring）一类；按 PSRQ 的先例可以进 Table 1。【推断】

## 5. LGSID（arXiv 2511.14221，AAAI'26）

- **毛病：I**。摘要唯一的抱怨："simply injecting location information into prompts fails to capture fine-grained spatial characteristics and real-world distance awareness among items"（p1）。两件设计（RL 地理对齐、层次地理分词）都服务它。【事实】
- **阶段：Representation**。两件设计都修 I，分不出，取贡献列表第一条："highlight the importance of aligning LLMs with domain-specific knowledge"（p2）；引言的 "key insight" 也是 "the quality and domain awareness of upstream LLMs fundamentally determine the upper bound of item tokenization performance"（p2）。G-DPO 改的是编码物品的 LLM（p4）。【事实】
- **Tokenizer：Fixed**。先对齐 LLM、建 SID，再训推荐模型（Fig. 2，p3）。【事实】
- **Objective：Discrim. / NTP**。原文两套实验：判别式模型（DIN、TWIN、ETA 等，Table 1，AUC，p5–6）和生成式模型（TIGER、OneRec，Table 2，Hit/NDCG，p5–6）；贡献第 3 条明说 "improves performance in both discriminative and generative recommendation models"（p2）。【事实】
- **五列核对**：Representation Text+Geo+CF 对（G-DPO 注入 "generalized spatial knowledge and collaborative signals"，p1）；Geo-Idx+RQ 对。Backbone 现只记生成式一套（Enc-Dec），建议按 Table 1 的 "A / B" 写法改为 Disc. / Enc-Dec，Inference 改为 Scoring / Beam†（次要）。【推断】Venue 已证实：AAAI 第 40 卷第 17 期，2026-03-14，DOI 10.1609/aaai.v40i17.38514（https://ojs.aaai.org/index.php/AAAI/article/view/38514 ）。【事实】可去掉"待核"。

## 6. OneLoc（arXiv 2508.14646）

- **毛病：I**。摘要两条抱怨一比一："how to make full use of geographic information"（I）和 "how to balance multiple objectives, including user interests, the distance between user and stores, and some other business objectives"（IV）（p1）。【事实】新设计：修 I 的三件（geo-aware SID、编码器里的 geo-aware self-attention、解码器里的 neighbor-aware prompt），修 IV 的两件奖励（地理奖励、GMV 奖励）。按新设计多数取 I；题目 "Geo-Aware ..." 也点 I。【推断】
- **阶段：Representation（拿不准，备选 Backbone）**。三件 I 设计装在两处，规则里阶段没有"多数"一条，分不出就取贡献列表第一条：geo-aware tokenizer（贡献第 2 条的 (1)，p3）。它的量化器沿用 OneRec 的 res-kmeans，改动只在输入嵌入里加了位置上下文："each residual r_i^0 ... is represented as an embedding of video content and location context information, extracted by a multimodal large language model"（§2.2，p3），所以落在 Representation。【事实】备选 Backbone：三件里两件装在编码器和解码器；消融只做了 neighbor-aware prompt、geo-aware self-attention 和奖励（§4.3，p7–8），没消 geo-aware SID。【事实】
- **Tokenizer：Fixed；Objective：NTP → DPO**。预训练用 NTP 交叉熵（式 (20)–(21)，p5），之后 "we use direct preference optimization (DPO) for alignment"，偏好对由束搜索采样、两种奖励打分构造（§2.5，式 (24)，p5）。【事实】
- **五列核对（有错）**：
  - **Tokenization：RQ-VAE → R-KM（重要）**。原文 "Following OneRec [28], we use res-kmeans to generate semantic IDs"，每层对残差做 K-means（§2.2，式 (1)–(3)，p3）。【事实】Table 2 附录写的依据 "RQ-VAE（p7）"，p7 出现的 RQ-VAE 是基线 TIGER 的描述。【事实】
  - **Representation：Text+Img+Geo+CF → Text+Img+Geo（重要）**。原文只写多模态大模型提取 "video content and location context information"（p3），位置上下文含坐标、品牌、类别（§2.1，p3）。全文没有找到协同信号进入 SID 的说法（检索 collaborative、co-occur 只命中相关工作）。【事实】Img 的依据是"多模态大模型提取视频内容"，原文没逐一列模态，可标 †。【推断】
  - Backbone Enc-Dec 对（"OneLoc is with encoder-decoder structure"，p2）；Inference Beam 对（线上 "semantic token generation via beam search"，p6）。【事实】
  - **Venue：WSDM'26 查不到**。arXiv 页面只有 v1（2025-08-20），没有 comments 或 journal-ref（https://arxiv.org/abs/2508.14646 ）；PDF 的 ACM 模板占位符未填（p1）；检索 WSDM 2026 录用信息没有结果。建议改回 arXiv'25，年份改 2025。【事实】

## 7. ProGEO（arXiv 2604.23156）

- **毛病：I**。摘要唯一的抱怨："existing semantic codebooks neglect geographic constraints, often resulting in recommendations that are semantically relevant yet geographically unreachable"（p1）。引言给出量化证据："over 50% of POIs sharing the same semantic ID are geographically separated by more than 40 kilometers"（p2）。【事实】Fig. 2 说的 "invalid cross-city deliveries"（p3）指业务上不可达，不是 II 定义里"生成的 SID 不对应真实物品"。【推断】
- **阶段：Tokenization**。新设计 geo-centroid 局部坐标和 GEO-RoPE 都作用在第三层地理码本上（Fig. 2，p3；§3，p3–4）。【事实】
- **Tokenizer：Fixed；Objective：NTP**。先建码本，再训 Qwen2.5-1.5B 做生成（附录 B，p11）。【事实】
- **五列核对**：Text+Geo 对（Qwen3-Embedding-8B 文本嵌入，p11；局部坐标，p3）；R-KM+Geo-CB 对（"two standard codebook layers ... RQ-Kmeans" 加一层地理码本，Fig. 2，p3）；Dec-Only 对；Inference Beam+Geo-Filter 对（"we select the 10 POIs whose semantic IDs are closest to the user's location as the candidate set. Beam search is performed with a width of 20"，p11）。【事实】

## 8. ROS（arXiv 2601.04562，ACL'26）

- **毛病：I（备选 III）**。摘要唯一的抱怨："existing LLM-based recommenders remain limited in leveraging geographic signals"（p1），按"先照摘要里的抱怨定"取 I。【事实】备选 III：引言把缺口收窄为 "they do not leverage the model's reasoning capability to treat geography as a first class decision variable"（p1），题目也是 "Enabling Geographic Reasoning"；按 Table 1 对 OneRec-Think 的先例（缺推理不单开一类，归 III）可归 III。【事实】我取 I，因为摘要的抱怨对象是地理信号。【推断】
- **阶段：Tokenization（拿不准，备选 Training）**。三件设计（Hierarchical Spatial SID、Mobility CoT、spatial-guided RL）都为地理服务，分不出，取贡献列表第一条 SID（§1 末，p2）。【事实】备选 Training：三件里两件在 Training（CoT SFT 由 Qwen3-235B 教师生成轨迹，p5；GRPO，p4、p12），题目强调推理。【事实】
- **Tokenizer：Fixed；Objective：NTP → RL**。SID grounding 预训练和 CoT SFT 都是 NTP，之后 GRPO，奖励 r = r_fmt + α r_acc + β r_dist（附录 A.3，p12）。【事实】
- **五列核对**：Text+Geo 对（S2 Cell，Qwen-0.6B 编码类别描述，§2.2.1，p2）；Geo-Prefix+RQ-VAE 对，另有区分后缀 u(p)（p2）；Dec-Only 对（Qwen3-4B，p5）；Inference CoT+C-Beam 对（"first generate the rationale-augmented CoT trace, and then condition on this trace to perform constrained beam search"，p7）。【事实】
- **Venue 已证实**：ACL 2026 Long，2026.acl-long.332，pp. 7322–7336（https://aclanthology.org/2026.acl-long.332/ ）。【事实】可去掉"待核"。

## 9. Think2Go（arXiv 2607.28997，KDD'26）

- **毛病：III**。摘要两条抱怨：非推理模型 "limit the computational capacity ... to capture deep intent"（缺推理），以及 LLM "lack a deep understanding of semantic IDs (SIDs) when SIDs are trained separately"（p1）。后一条是模型读不懂 SID（III）；前一条按 Table 1 先例"缺推理不单开一类"也归 III。【事实】
- **阶段：Training**。新设计是把 SFT 和基于 RL 的推理统一在一个架构里联合优化，以及两种 advantage 加权（§4.1–4.2，p4–6）。【事实】
- **Tokenizer：Fixed**。SID 仍由 RQ-VAE 预先学好（p7），作者批评的 "training of semantic IDs is decoupled from the model itself" 是靠推理训练补，没有让生成器更新编号器（§5.8，p9）。【事实】
- **Objective：NTP → RL（拿不准，备选 NTP + Aux.）**。损失由 L_SFT 和 L_DAPO 组成，"employs SFT to ensure the model retains correct answers, while RL is used to enhance the model's ability to explore"（p4），在一个阶段里联合训，不是先 SFT 后 RL。词表里 NTP → RL 表示先后两段，NTP + Aux. 表示同时加辅助损失；两者都不完全贴切，可考虑新增写法 NTP + RL。【推断】
- **五列核对**：Representation Attr+Geo+CF† 维持推定（只写了预处理 "consistent with GNPR"，p7）；**Tokenization RQ-VAE† 可去 †**，原文写 "the correlation among semantic IDs learned through RQ-VAE"（p7）（次要）；Dec-Only 对（LLaMA3.1-8B + LoRA，p11）；CoT+Beam 对（"During inference, we employ beam search with a size of 15"，p11）。Venue KDD'26 对（DOI 10.1145/3770854.3780334，p1）。【事实】

---

## 对正文有用的三条事实（POI 进 Table 1 和正文时可用）

1. **同一 SID 的 POI 在地理上可以相距很远**：ProGEO 在美团数据上测得同一 SID 的 POI 有一半以上相距 40 km 以上（p2）；GeoGR 测得只用文本语义的 Base SID 里，共享第一位码的 POI 平均相距 483.4 km，加地理信号后降到 31.9 km（Table 5，p8）。这是 I 类毛病在 POI 上的直接度量。【事实】
2. **撞号在 POI 上特别重**：LGRID 报告 LGSID 的全 SID 撞号率 97.0%，LGRID 降到 39.9%（p1）；GNPR-SID 的 diversity loss 权重从 0 调到 0.75，NYC 上撞号 SID 数从 711 降到 554，Acc@1 先升后降（Table 4，p8）。【事实】撞号率和准确率不单调，可作边②（撞号 ↔ 物品解析与评测）的旁证。【推断】
3. **地理既可以进 SID，也可以留到推理时过滤**：ProGEO 在码本里编码地理，推理时又把候选限定在离用户最近的 10 个 POI（p11）；ROS 用地理前缀和约束束搜索（p2，p7）；OneLoc 把位置放进注意力和 prompt（p3–5）。同一个"地理信息"在 Representation、Tokenization、Backbone、Inference 四处都有人放。这正是问题 × 阶段矩阵要展示的"同一毛病不同阶段的修法"。【推断】
