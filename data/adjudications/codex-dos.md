# DOS 双盲打标（Codex，2026-10-30）

本稿由 Codex 独立核读原文并打标，未读取另一方的 DOS 稿件，未派子代理。只提交本稿及完成标记，不改 Table 1、Table 2 或论文正文。【事实】

## 来源与口径

- 论文：DOS: Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan，Junwei Yin et al.；[arXiv 条目](https://arxiv.org/abs/2602.04460)明确注明 WWW 2026 short paper，故 Venue 取 `WWW’26 Short`，年份取 2026。【事实】
- 主证据：[本地 PDF](papers-archive/B2/DOS_2602.04460.pdf)，arXiv v1，共 4 页；下文页码均为 PDF 物理页码，已读摘要、§1–4、Fig. 1 和 Tables 1–3；另打开了 [arXiv HTML v1](https://arxiv.org/html/2602.04460v1)核对。【事实】
- 毛病按[现行判定规则](data/references/Table1_snapshot_94.md:165)，阶段按[本轮简报](data/references/taxonomy-and-tensions.yaml:833)指定的贡献列表第一条判定；`†` 表示原文没有直接写明、由上下文推定的值。【事实】

## 八项打标

建议归入 **III SID–Model Alignment × Tokenization**；其余列以 §3.2.2、Table 2 的 HSTU-DOS 生成实验为填写对象，编号器内部的判别训练另作说明。【推断】

| 字段 | 取值 | 原文位置与理由 |
| --- | --- | --- |
| 毛病 | III SID–Model Alignment | [摘要，p1；§1，p1–2](https://arxiv.org/html/2602.04460v1)：两条抱怨是码本空间与生成空间脱节、量化造成语义损失，分别对应 DFI 与 ORQ。【事实】按规则先得 III / I 各一条；两件设计各修一条，标题也各点名一件，最后由第一件 DFI 的对齐目标破平，取 III，不归「范式、系统与基准」。【推断】 |
| 改动阶段 | Tokenization | [§1 贡献第 1 条、§2.1，p2；Fig. 1(a)，p3](https://arxiv.org/html/2602.04460v1)：第一项贡献为 DFI，通过用户与物品两路及共享码本，把协同关系直接融入量化。【事实】DFI 改变 SID 的构建和码本学习，归 Tokenization；此判断依据第一项 DFI，而非第二项 ORQ，也不把构码用的双塔误认作生成 Backbone。【推断】 |
| Tokenizer | 拿不准：Fixed† / Joint；暂取 Fixed† | [§2.2 式 (11)、§3.1.1，p3；§3.2.2，p4](https://arxiv.org/html/2602.04460v1)：论文分别说明 DOS 的量化训练及生成出的 SID 在 HSTU 中的评估；未说明 HSTU 训练时是否冻结或反传更新编号器。【事实】两段流程支持 Fixed†；式 (11) 的内部联合优化容易被读成 Joint，但没有生成器损失回传的证据，两个候选的边界见下文。【推断】 |
| Objective | NTP | [§3.2.2，p4，Table 2](https://arxiv.org/html/2602.04460v1)：原文将 HSTU-DOS 实验明确列为下一 token 预测，并用 Hit@10 评价。【事实】对应生成器的 Objective 记 NTP；式 (11) 的 BCE、正交、互信息、重构和 VQ 损失属于 DOS 编号器训练，不据此写成 NTP + Aux.。【推断】 |
| Representation | Text+CF | [§2.1，p2，提示模板及式 (1)–(5)](https://arxiv.org/html/2602.04460v1)：餐厅名、类别、菜品、价格等文本经 Qwen3-0.6B-embedding 编码，点击序列与目标物品的协同关系在 DFI 中融入 SID 学习。【事实】按表内信号口径记 Text+CF；CF 不表示初始 LLM 嵌入已含协同信息，模板未报告坐标或地址，不因本地生活场景补 Geo。【推断】 |
| Tokenization | ORQ | [§2.2，p2–3，式 (6)–(11)、Fig. 1(b)](https://arxiv.org/html/2602.04460v1)：正交变换后选择任务相关维度作残差量化，将其残差与其余维度送入下一层。【事实】采用原文模块名 ORQ，即 Orthogonal Residual Quantization，作为本表新写法；用户与物品两路共享码本的 DFI 在阶段依据中说明。【推断】 |
| Backbone | HSTU；归并架构类别拿不准：HSTU / Dec-Only† | [§3.2.2、Table 2，p4](https://arxiv.org/html/2602.04460v1)明确将生成实验骨干写为 HSTU，但没有给出该实例的注意力掩码、层配置或 SID 输出结构。【事实】暂保留 HSTU 为新写法；Dec-Only† 可由 HSTU 原作的因果自回归设置推定，不能作为 DOS 直接报告的架构类别，详见下文。【推断】 |
| Inference | – | [§3.1.2、§3.2.2，p3–4](https://arxiv.org/html/2602.04460v1)，只给生成任务指标和 HSTU-DOS 的 Hit@10；检查 §2–4、Fig. 1 及表注，未找到 beam、greedy、sampling 或约束解码的具体说明。【事实】沿用表下注的 `–`，表示未报告，不表示没有推断环节；不由 Hit@10 反推 Beam。【推断】 |

## 两处拿不准的边界

1. **Tokenizer：Fixed† / Joint。** `Fixed†` 的理由：DOS 有独立量化数据和损失，§3.2.2 再拿其产生的 SID 评估 HSTU，符合先构码再训生成器的读法，但没有冻结声明。【推断】`Joint` 的局部依据：式 (11) 联合优化 BCE 与量化相关损失，Fig. 1 的预测器和量化模块同属 DOS。【事实】不过该预测器是式 (4) 的 MLP，不是 HSTU；按现行定义，内部联合优化不足以判定「生成器损失直接更新编号器」，故暂取 Fixed†，保留未核实项。[DOS §2.1–2.2、§3.2.2，p2–4](https://arxiv.org/html/2602.04460v1)【推断】

2. **Backbone：HSTU / Dec-Only†。** `HSTU` 的理由：DOS §3.2.2、Table 2 直接点名，能够忠实保留已知实现；本稿暂取此值，并将其作为新写法说明。【推断】`Dec-Only†` 的理由：[HSTU 原作 §2.2–3](https://arxiv.org/html/2402.17152v1)采用因果掩码的自回归设置，并以 HSTU 层构成自注意力序列网络。【事实】这可支持归入因果生成骨干，但 DOS 没交代具体改造；若 leader 统一为 Dec-Only，需保留 †。[DOS §3.2.2，p4](https://arxiv.org/html/2602.04460v1)【推断】

## 合并时需要保留的口径

- **按生成实验填行，不把量化评测当成另一套生成骨干。** §3.1.2 明说 AUC、F1 对应量化任务，Hit@10 对应生成任务；§3.2.2、Table 2 确有 HSTU-DOS 的生成实验。[DOS p3–4](https://arxiv.org/html/2602.04460v1)【事实】因此本行采用 HSTU 与 NTP，不能仅因 Table 1 的 BCE/AUC 就改成 Disc.、Discrim.、Scoring，也不把编号器内部 MLP 另列为一套下游推荐实验。【推断】
- **POI 身份不自动带来 Geo，LLM 编码器不等于生成器。** §2.1 中 Qwen 的用途是文本嵌入，模板没有显式地理字段；§3.2.2 的生成实验用 HSTU。[DOS p2、p4](https://arxiv.org/html/2602.04460v1)【事实】因此不填 Text+Geo，也不以 Qwen 的架构替代 HSTU。【推断】
- **线上实验不用于补足未知的推断设置。** §3.4 仅说明给原有模型加入 SID、其余架构不变，未命名线上骨干或解码算法。[DOS p4](https://arxiv.org/html/2602.04460v1)【事实】不能据此认定线上系统就是离线 HSTU，或补写 Beam。【推断】

供合并的暂定行如下；`Fixed†` 保留不确定性，HSTU 与 ORQ 的新写法含义见上表。【推断】

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ★ DOS (Yin et al., 2026) | WWW’26 Short | Text+CF | **ORQ** | HSTU | Fixed† | NTP | – |

## 检索与核对记录

| 查询词或来源 | 打开的来源 | 收获 |
| --- | --- | --- |
| 本地 backlog 中 DOS / 2602.04460 | `papers-archive/B2/DOS_2602.04460.pdf` | 找到并通读 4 页原文，定位 DFI、ORQ、HSTU 实验及未报告项。 |
| arXiv 编号及 HTML | [条目](https://arxiv.org/abs/2602.04460)、[HTML v1](https://arxiv.org/html/2602.04460v1) | 核对题名、作者、年份、Short track 和正文。 |
| DOI 10.1145/3774904.3792845 | [DOI 入口](https://doi.org/10.1145/3774904.3792845) | 浏览工具未能打开落地页；DOI 字符串见 PDF p1，会议及 track 依据 arXiv 条目。 |
| DOS 参考文献 [9]：HSTU | [HSTU 原作 HTML v1](https://arxiv.org/html/2402.17152v1) | 核对 §2.2 的因果自回归设置及 §3 的网络结构；仅用于讨论 Backbone 的归并候选，不替 DOS 补训练或推断配置。 |
