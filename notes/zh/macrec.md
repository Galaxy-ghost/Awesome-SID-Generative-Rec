## At a Glance

Key Findings: MACRec 在三个数据集上的 HR@10、NDCG@5 和 NDCG@10 均领先所有基线；仅在 Games 的 HR@5 上，MISSRec 为 0.0674，MACRec 为 0.0671（Table 2）。
Limitation: MACRec 维护两套独立的 4 层 RQ-VAE 编号器，推理时需在文本和图像两个模态分别运行受约束束搜索再平均得分，且未报告束宽与推理延迟（Methodology，Table 4）。

### 1. 为什么重要

生成式推荐要求语义 ID（Semantic ID，SID）同时具备层级结构、低冲突率以及良好的可生成性。早期的多模态生成式推荐模型对各个模态独立量化，文本与图像特征在构建码本时互不交互。

> "However, existing multimodal GR models typically encode each modality separately to obtain semantic IDs for different modalities."（Related Work）

MACRec 在两个阶段引入跨模态交互：在残差码本内部加入跨模态对比量化，并在生成器训练中设计多视角跨模态对齐任务（Methodology）。

### 2. 方法

```mermaid
flowchart LR
    subgraph S1["阶段 1：跨模态残差量化（4 层 × 256）"]
        A("LLaMA 文本嵌入") --> C["文本 MLP + 4 层 RQ-VAE"]
        B("ViT-L/14 图像嵌入") --> D["图像 MLP + 4 层 RQ-VAE"]
        A -.-> PT("K-means 文本伪标签")
        B -.-> PI("K-means 图像伪标签")
        PI -.-> L1{{"逐层跨模态对比损失"}}:::key
        PT -.-> L2{{"逐层跨模态对比损失"}}:::key
        L1 -.-> C
        L2 -.-> D
        L0{{"跨模态重建 + 基于距离的冲突重分配"}} -.-> C
        L0 -.-> D
    end
    C --> E("文本 SID")
    D --> F("图像 SID")
    subgraph S2["阶段 2：多视角对齐生成（4 层 T5）"]
        E --> G["T5 编码器-解码器生成器"]
        F --> G
        L3{{"模态内 NTP + 隐式对齐 + 物品/序列级跨模态任务"}}:::key -.-> G
        G --> H["分模态受约束束搜索与分数平均"]
        H --> I("下一物品")
    end
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 双模态伪标签

MACRec 分别在 LLaMA 文本嵌入空间和 ViT-L/14 图像嵌入空间对物品聚类，用所得簇标签定义量化器中跨模态对比学习的正样本对（Dual-modality Pseudo-label Generation）。

#### 跨模态量化

每个模态依次通过各自的 MLP 编码器与 4 层 × 256 码字 RQ-VAE。在每一层残差量化上，跨模态对比损失利用另一模态的聚类伪标签监督当前模态的残差表示（Cross-modal Quantization with Contrastive Learning）。

> "More concretely, we use visual pseudo-labels to enhance the residual representations of the text modality, and conversely, use textual pseudo-labels to optimize those of the visual modality."（Cross-modal Quantization with Contrastive Learning）

跨模态重建损失与量化损失确保离散码字能够还原原始嵌入（Cross-modal Reconstruction Alignment），剩余的 ID 冲突沿用 MQL4GRec 的做法按物品到码本的距离重分配码字。

#### 多视角对齐

4 层 T5 编码器-解码器联合优化模态内下一物品预测、文本与视觉 SID 表示的隐式对比对齐，以及跨模态的物品级互译与序列级预测任务；推理时在两个模态分别执行受约束束搜索，并对两路候选得分取平均（Generative Recommendation with Multi-aspect Alignment）。

> "For sequence-level alignment, we construct a prediction task where a historical sequence of textual semantic IDs is used to predict the visual semantic ID of the next recommended item."（Explicit Alignment with Different Generation Tasks）

### 3. 实验发现

- 全库排序：在 Amazon Musical Instruments、Arts Crafts and Sewing 和 Video Games 三个数据集上，MACRec 在 HR@10、NDCG@5 和 NDCG@10 上均优于序列、多模态与生成式基线（含 TIGER、P5-CID 及未用额外类目预训练的 MQL4GRec），仅在 Games 的 HR@5 上略低于 MISSRec（0.0671 对 0.0674；Table 2）。
- 模块消融：去掉跨模态量化、隐式对齐或显式跨模态生成任务中的任一模块，三个数据集上的 HR@10 均会下降（Table 3，Figs. 3–4）。
- 重分配前冲突率：跨模态对比量化使物品 SID 冲突率低于单模态 RQ-VAE 与 MQL4GRec，例如在 Musical Instruments 上冲突重分配前的文本冲突率为 2.38%、图像冲突率为 3.23%（Table 4）。

### 4. 局限与分析

**Our analysis.**

- MQL4GRec 用独立编号器分别量化文本与图像（`Dual RQ`），仅靠生成任务建立跨模态关联；MACRec 在量化阶段将各残差层跨模态耦合（`Cross RQ`），并在生成器目标中加入对比项（`NTP + Ctr.`），同时复用了 MQL4GRec 的距离重分配去重与双模态分数平均。
- MACRec 的输入表示仅使用文本与图像（`Text+Img`），未引入协同交互信号；后续工作 CARD 进一步融合协同邻居信息（`Text+Img+CF`），并用 `NU-RQ` 量化统一的视觉卡片输入。
