# 入门指南

[English](start-here.md) | 中文

本指南分三步梳理语义 ID（Semantic ID，SID）生成式推荐的核心脉络。每一步给出带完整笔记的代表论文页，以及汇总同类工作的 README 章节。

## 1. 从 TIGER 了解五阶段流程

先读 [TIGER](../pages/zh/papers/tiger.md)。TIGER 用 RQ-VAE 编号器把物品文本编码为语义 ID，训练 Transformer 编码器-解码器生成下一物品的 SID，再用束搜索解码候选物品。所有论文页都按同样的五个阶段展开：Representation、Tokenization、Backbone、Training 与 Inference。

## 2. 向编号器注入信号与约束

接着看后续工作如何改进编号器的输入信号与训练损失。[LETTER](../pages/zh/papers/letter.md) 在 RQ-VAE 编号器中加入协同对齐损失与码本多样性损失。[OneLoc](../pages/zh/papers/oneloc.md) 面向本地生活推荐，将地理上下文融入物品表征。README 的 [I. 信息量](../README.zh.md#i-信息量) 汇总了融合协同、多模态与空间信号的论文；[II. 唯一性与合法性](../README.zh.md#ii-唯一性与合法性) 汇总了解决 SID 冲突、非法前缀与码本坍缩的论文。

## 3. 沿一个研究问题深入

从 [分类总图](../README.zh.md#分类总图) 中选定一行，按阶段阅读对应论文。以 [V. 效率](../README.zh.md#v-效率) 中的 [RPG](../pages/zh/papers/rpg.md) 为例，它并行预测长 SID 各位置的码分布，并在合法物品图上搜索，省去逐位自回归束搜索。其余各行分别覆盖 [III. SID 与模型对齐](../README.zh.md#iii-sid-与模型对齐)、[IV. 实用目标](../README.zh.md#iv-实用目标) 与 [VI. 泛化](../README.zh.md#vi-泛化)。[SIDScope](../pages/zh/papers/sidscope.md) 用于在复用公开 SID 映射前检查其质量，[术语表](glossary.zh.md) 则定义了论文页中的全部符号与字段取值。
