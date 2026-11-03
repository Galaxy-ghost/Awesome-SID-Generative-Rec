# Start Here

English | [中文](start-here.zh.md)

This guide maps a three-step reading route through Semantic ID (SID) generative recommendation. Each step links representative paper pages with full notes and the README sections that collect related work.

## 1. Learn the Five-Stage Pipeline with TIGER

Start with [TIGER](../pages/papers/tiger.md). TIGER encodes item text into Semantic IDs with an RQ-VAE tokenizer, trains a Transformer encoder-decoder to generate the next item's SID, and decodes candidates with beam search. Every paper page follows the same five stages: Representation, Tokenization, Backbone, Training, and Inference.

## 2. Enrich the Tokenizer

Next, compare how follow-up work changes what the tokenizer sees and how it learns. [LETTER](../pages/papers/letter.md) adds collaborative alignment and diversity losses to an RQ-VAE tokenizer. [OneLoc](../pages/papers/oneloc.md) incorporates geographic context into item embeddings for local-life recommendation. In the README, [I. Informativeness](../README.md#i-informativeness) collects papers that inject collaborative, multimodal, or spatial signals, while [II. Uniqueness and Validity](../README.md#ii-uniqueness-and-validity) covers SID collisions, invalid prefixes, and codebook usage.

## 3. Follow a Research Problem

Pick one row of the [Problem × Stage Matrix](../README.md#problem--stage-matrix) and read the papers in its cells. For example, [RPG](../pages/papers/rpg.md) under [V. Efficiency](../README.md#v-efficiency) predicts long SIDs in parallel and decodes over a graph of valid items instead of running autoregressive beam search. The remaining rows cover [III. SID–Model Alignment](../README.md#iii-sidmodel-alignment), [IV. Utility](../README.md#iv-utility), and [VI. Generalization](../README.md#vi-generalization). [SIDScope](../pages/papers/sidscope.md) audits released SID mappings before reuse, and the [glossary](glossary.md) defines every symbol and column value on the paper pages.
