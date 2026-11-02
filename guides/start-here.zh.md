# 入门指南

[English](start-here.md) | 中文

本指南分三步串联清单中的核心工作。每一步列出带完整精读页的代表论文，以及汇总同类工作的 README 章节。

## 1. 从 TIGER 了解五阶段流程

先读 [TIGER](../pages/zh/papers/tiger.md)。TIGER 用 RQ-VAE 编号器将物品文本编码为语义 ID（Semantic ID，SID），训练 Transformer 编码器-解码器生成下一物品的 SID，并通过束搜索解码。该页用公式和代码逐步拆解整个流程。本清单的所有论文页都按同样的五个阶段描述方法：Representation、Tokenization、Backbone、Training 与 Inference。

## 2. 向编号器注入更多信息

接着看后续工作如何改变编号器的输入信号与训练目标。[LETTER](../pages/zh/papers/letter.md) 在 RQ-VAE 编号器中加入协同对齐损失和多样性损失。[OneLoc](../pages/zh/papers/oneloc.md) 面向本地生活推荐，在物品嵌入中融入地理上下文。README 的 [I. 信息量](../README.zh.md#i-信息量) 一节汇总了引入协同、多模态或地理信号的论文；[II. 唯一性与合法性](../README.zh.md#ii-唯一性与合法性) 一节汇总了处理 SID 冲突、非法 SID 与码本利用率的论文。

## 3. 沿一个研究问题深入

然后从 [问题 × 阶段矩阵](../README.zh.md#问题--阶段矩阵) 中选定一行，按格子阅读对应论文。例如 [V. 效率](../README.zh.md#v-效率) 中的 [RPG](../pages/zh/papers/rpg.md) 并行预测长 SID，并在合法 SID 图上解码以替代自回归束搜索。其余问题行分别覆盖 [III. SID 与模型对齐](../README.zh.md#iii-sid-与模型对齐)、[IV. 实用目标](../README.zh.md#iv-实用目标) 与 [VI. 泛化](../README.zh.md#vi-泛化)。[SIDScope](../pages/zh/papers/sidscope.md) 用于在复用已发布 SID 映射前检查其质量。[术语表](glossary.zh.md) 定义了论文页中出现的全部符号与字段取值。
