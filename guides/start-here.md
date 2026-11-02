# Start Here

This guide gives a reading route through the list in three steps. Each step names papers with full pages and the README sections that collect related work.

## 1. Learn the Pipeline with TIGER

Start with [TIGER](../pages/papers/tiger.md). TIGER encodes item text into Semantic IDs (SIDs) with an RQ-VAE tokenizer, trains a Transformer encoder-decoder to generate the SID of the next item, and decodes with beam search. Its page walks through each step with formulas and code. Every paper page in this list describes a method by the same five stages: Representation, Tokenization, Backbone, Training, and Inference.

## 2. Add Information to the Tokenizer

Next, read how later papers change what the tokenizer sees and how it learns. [LETTER](../pages/papers/letter.md) adds a collaborative alignment loss and a diversity loss to an RQ-VAE tokenizer. [OneLoc](../pages/papers/oneloc.md) adds geographic context to the item embedding for local-life recommendation. The README band [I. Informativeness](../README.md#i-informativeness) collects papers that add collaborative, multimodal, or geographic signals. The band [II. Uniqueness and Validity](../README.md#ii-uniqueness-and-validity) collects papers on SID collisions, invalid SIDs, and codebook use.

## 3. Follow One Research Problem

Then pick one row of the [Problem × Stage Matrix](../README.md#problem--stage-matrix) and read the papers in its cells. [RPG](../pages/papers/rpg.md) is an example from [V. Efficiency](../README.md#v-efficiency): it predicts long SIDs in parallel and decodes over a graph of valid SIDs instead of running beam search. The other bands cover [SID–model alignment](../README.md#iii-sidmodel-alignment), [utility](../README.md#iv-utility), and [generalization](../README.md#vi-generalization). [SIDScope](../pages/papers/sidscope.md) checks released SID mappings before they are reused. The [glossary](glossary.md) defines every value in the paper pages.
