# POI 9 篇打标：两家对照和 leader 裁决（10-28）

两家各自打标、互不知情。规则见 `材料/Table1_扩展版.md`「附：毛病与阶段的依据」，写法见同文件表下注（Objective 只有 12 种写法）。下面"核过"指 leader 打开了原文。

## 裁决后的四项

| 方法 | 毛病 | 阶段 | Tokenizer | Objective | 两家是否一致 |
|---|---|---|---|---|---|
| GNPR-SID | I | Tokenization | Fixed | NTP | 一致 |
| GeoGR | I | Representation | Altern.† | Multi-task NTP | 毛病、阶段一致；后两项按下文裁 |
| Gwhere | II | Tokenization | Fixed | NTP → DPO | 毛病、阶段一致（两家都标拿不准，备选 I）；Objective 按下文裁 |
| LGRID | I | Representation | Fixed | Discrim. | 一致 |
| LGSID | I | Representation | Fixed | Discrim. / NTP | 毛病、阶段一致；Objective 按下文裁 |
| OneLoc | I | Representation | Fixed | NTP → DPO | **毛病、阶段都不一致**，按下文裁 |
| ProGEO | I | Tokenization | Fixed | NTP | 一致 |
| ROS | I | Tokenization | Fixed | NTP → RL | **阶段不一致**，按下文裁 |
| Think2Go | III | Training | Fixed | NTP → RL | 一致 |

## 分歧怎么裁的

1. **OneLoc 的毛病：I，不放"范式、系统与基准"。**
   - Codex 认为它是整套本地生活生成式系统，应放进最上面一块。Claude 取 I。
   - 摘要明说两条挑战："how to make full use of geographic information"（I）和 "how to balance multiple objectives"（IV）（p1，核过）。修 I 的设计有三件（geo-aware SID、编码器里的 geo-aware self-attention、解码器里的 neighbor-aware prompt），修 IV 的有两件（两种奖励）。
   - 规则是"先照摘要里的抱怨定"。OneRec 放进最上面一块，是因为它的摘要只抱怨级联框架；OneLoc 的抱怨落得进六类，所以按多数取 I。

2. **OneLoc、ROS 的阶段：按现行规则取贡献列表第一条，分别是 Representation 和 Tokenization。**
   - 两篇都是三件设计修同一个毛病，分装在两个阶段：
     - OneLoc：geo-aware SID 一件在 Representation，attention 和 prompt 两件在 Backbone；
     - ROS：空间 SID 一件在 Tokenization，Mobility CoT 和空间 RL 两件在 Training。
   - Codex 按"多数设计所在的阶段"，取 Backbone 和 Training。Claude 按现行规则"几处时取对付该毛病的那一处；仍分不出，取贡献列表第一条"。
   - 两篇的第一条贡献都是 SID（ROS 引言第 (1) 条是 Hierarchical Spatial SID，核过）。OneLoc 沿用 OneRec 的 res-kmeans，改动只在输入嵌入里加了位置上下文（§2.2，p3），所以落在 Representation。
   - **这是规则的空档，留给本人定**：阶段规则要不要加一条"多数"？加了，这两篇就改成 Backbone 和 Training。已有的 84 行要不要按新规则重查，也要一起定。

3. **GeoGR 的 Tokenizer：Altern.†，不记 Fixed。**
   - §4.1.3 的 EM 算法里，LLM 做的就是下一 POI 预测：真实下一 POI 的 SID 不在 beam 候选里时，用最高概率的候选替换。它和 SID 轮流更新，作者说是为了 "mutual alignment between the LLM and the SIDs"（核过）。这符合 Altern. 的定义"编号器和生成器轮流更新"。
   - 最终的推荐器从基座 θ0 重新做 CPT 加 SFT（§4.2.1），所以加 †，脚注写明"交替发生在构码阶段，最终生成器在定好的 SID 上训"。

4. **GeoGR 的 Objective：Multi-task NTP。**
   - 原文写 "multi-task CPT datasets with various prompt templates"（§4.2.1，核过），符合 LC-Rec 的口径"同一损失训多种任务"。
   - Claude 提醒的一致性问题要另外处理：Table 1 里同样做"继续预训练 + SFT"的 PLUM 记的是 NTP。这次不改 PLUM，列进待办，回 PLUM 原文看它的 CPT 是不是多任务。

5. **Gwhere 的 Objective：NTP → DPO。**
   - 词表里"NTP → DPO"的定义是"之后再做偏好优化"。EAKTO 是 KTO 的变体，也属于偏好优化。
   - Codex 指出 CPT 里还有遮蔽 SID 预测和匹配判别两个辅助任务，可是词表没有"NTP + Aux. → DPO"这样的组合写法，所以写进脚注。

6. **LGSID 的 Objective：Discrim. / NTP，五列相应改成 A / B 写法。**
   - 原文判别式（DIN 等，Table 1）和生成式（TIGER、OneRec，Table 2）各做了一套实验，贡献第 3 条也明说两边都提升。按 Table 1 现有的 "A / B" 写法：Backbone 改为 Disc. / Enc-Dec，Inference 改为 Scoring / Beam†。
   - Codex 记了 NTP†，只看了生成式那一支。

7. **Objective 的写法统一到词表**：Codex 写的 "NTP+DPO""Multi-task NTP+GRPO""NTP+RL" 不在 12 种写法里，分别改为 NTP → DPO、NTP → RL、NTP → RL。

## 已有五列要改的（交给 exec-repo 和 Table 1 编辑源）

| 方法 | 列 | 原值 → 改为 | 依据 | 几家查到 |
|---|---|---|---|---|
| OneLoc | Tokenization | RQ-VAE → R-KM | §2.2，p3 "Following OneRec, we use res-kmeans"；p7 的 RQ-VAE 是基线 TIGER 的描述 | 两家各自查到 |
| OneLoc | Representation | Text+Img+Geo+CF → Text+Img+Geo† | 全文没有协同信号进 SID 的说法；Img 是从"多模态大模型提取视频内容"推定的 | 两家各自查到 |
| OneLoc | Venue | WSDM'26（待核）→ arXiv'25 | arXiv 只有 v1（2025-08-20），没有 comments 和 journal-ref（leader 核过）；Claude 检索 WSDM 2026 录用信息也没有结果 | Claude，leader 复核 |
| LGSID | Venue | AAAI'26（待核）→ AAAI'26 | AAAI 第 40 卷第 17 期，DOI 10.1609/aaai.v40i17.38514 | Claude |
| ROS | Venue | ACL'26（待核）→ ACL'26 | 2026.acl-long.332 | Claude |
| LGSID | Backbone / Inference | Enc-Dec → Disc. / Enc-Dec；Beam† → Scoring / Beam† | 见上第 6 条 | Claude |
| ROS | Inference | 保留 CoT+C-Beam，加脚注 | 主实验只报 HR@1，用 CoT；C-Beam 只用在 Top-K 扩展实验（§ "Top-K Recommendation via Two-Stage Inference"，p7） | Codex |
| Think2Go | Tokenization | RQ-VAE† 去掉 † | p7 "the correlation among semantic IDs learned through RQ-VAE" | Claude（次要） |

## 正文可用的三条事实（Claude 整理，数字的出处见 claude-poi.md 文末）

1. 同一个 SID 的 POI 在地理上可以相距很远。ProGEO 报告一半以上相距超过 40 km；GeoGR 报告共享第一位码的 POI 平均相距 483.4 km，加地理信号后降到 31.9 km。
2. 撞号在 POI 上很重。LGRID 报告 LGSID 的全 SID 撞号率是 97.0%。
3. 同一份"地理信息"，在 Representation、Tokenization、Backbone、Inference 四个阶段都有人放。这正好可以作为问题 × 阶段矩阵的例子。
