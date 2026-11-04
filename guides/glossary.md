# Glossary

English | [中文](glossary.zh.md)

This page is generated from [`data/vocab.yaml`](../data/vocab.yaml). It defines the controlled vocabulary values used in Table 1, the paper pages, and the indexes.

## Symbols

- `†`: Inferred from the configuration the paper names.
- `A / B`: Two branches or configurations.
- `–`: Not reported.
- `n/a`: Not applicable.
- `●` / `○`: Primary Table 1 cell (`●`) and additional column with a new mechanism (`○`).

## Problems

- `psb`: **Paradigms, Systems and Benchmarks.** Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources.
- `I`: **Informativeness.** Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs?
- `II`: **Uniqueness and Validity.** Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly?
- `III`: **SID–Model Alignment.** Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal?
- `IV`: **Utility.** Are training and search aimed at what users and the platform value, rather than at token likelihood?
- `V`: **Efficiency.** Can it be trained and served within latency and cost budgets?
- `VI`: **Generalization.** Does it still work for new items, new domains, and shifting interests?

## Representation

- `Attr+CF`: Structured item attributes combined with collaborative signals.
- `Attr+Geo+CF`: Category and other attributes, plus geography, plus CF (POI).
- `Attr+Geo+CF†`: Structured item attributes, geographic information, and collaborative signals (inferred).
- `CF`: Collaborative filtering signal.
- `Cross-Dom`: Item representations transferred or shared across multiple domains.
- `Geo`: Geographic coordinates or spatial features.
- `MM`: Multimodal item representations.
- `MM+CF`: Multimodal item representations aligned with collaborative signals.
- `Multi-Dom`: Unified item representations built jointly across multiple domains.
- `Text`: Textual item metadata (titles, descriptions, categories, or prompts).
- `Text + CF`: Text representations combined with collaborative signals.
- `Text + Img + CF`: Text and image representations combined with collaborative signals.
- `Text / Audio`: Text or audio representations in different branches or evaluation settings.
- `Text / MM`: Text-only or multimodal representations in different configurations.
- `Text / Text+CF`: Text-only representations or text representations combined with collaborative signals.
- `Text / –`: Text representations in one configuration; the representation source is not reported in another.
- `Text+Attr+Geo`: Text, structured attributes, and geographic information.
- `Text+CF`: Text representations combined with collaborative signals.
- `Text+CF / Text`: Text with collaborative signals, or text-only representations, in different configurations.
- `Text+Geo`: Text representations combined with geographic or spatial features.
- `Text+Geo+CF`: Text representations combined with geographic features and collaborative signals.
- `Text+Img`: Text and visual item representations.
- `Text+Img+Attr`: Text, images, and structured item attributes.
- `Text+Img+Audio+CF`: Text, visual, and audio content combined with collaborative signals.
- `Text+Img+CF`: Text and image representations combined with collaborative signals.
- `Text+Img+CF†`: Text, image, and collaborative representations (inferred).
- `Text+Img+Geo`: Text, images, and geographic information.
- `Text+Img+Geo+CF`: Text, image, geographic, and collaborative representations.
- `Text+Img+Geo†`: Text, image, and geographic representations (inferred).
- `Text+Img†`: Text and image representations (inferred).
- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Text+Time`: Text representations combined with interaction timestamps.
- `Text†`: Textual item representations (inferred).
- `n/a`: Not applicable to this method.
- `–`: Not reported in the paper.
- `– / Text+Img`: The representation source is unreported in one configuration; text and image representations are used in another.

## Tokenization

- `Align. RQ`: Residual quantization trained with alignment objectives.
- `BDQ`: Bit-Decomposable Quantizer.
- `Bal. VQ+KM`: Balanced tokenization combining vector quantization and k-means clustering.
- `C-RQ`: Contrastive residual quantization.
- `CART`: Collaborative-Aware Refined Tokenization.
- `CF-Aligned MM RQ`: Multimodal residual quantization aligned with collaborative signals.
- `Casc. RQ`: Cascaded sparse-to-dense residual quantization.
- `CoBa RQ-VAE`: Collaborative and Balanced RQ-VAE.
- `Contr. RQ`: Residual quantization trained with contrastive objectives.
- `Cross RQ`: Cross-modal residual quantization.
- `Curr. RQ`: Curriculum-trained hierarchical residual quantization.
- `DSRQ`: Dual-stream residual quantization.
- `Direct SID Heads`: Prediction heads that directly assign semantic-ID codes.
- `Dual H-KM`: Dual-source hierarchical k-means over behavioral and semantic embeddings.
- `Dual RQ`: Dual residual quantization over two representation streams or entity types.
- `Dual RQ-VAE`: Two residual-quantized variational autoencoders for separate representation streams.
- `Dyn. KM+Disamb.`: Dynamically updated k-means codes combined with disambiguation codes.
- `Flow+PQ`: Flow-based representation transformation followed by product quantization.
- `Freq. R-KM`: Frequency-aware residual k-means tokenization.
- `GAOQ`: Globally Aligned Orthogonal Quantization.
- `Geo-Idx`: Identifiers constructed from geographic indexing.
- `Geo-Idx+RQ`: Geographic indexing combined with residual quantization.
- `Geo-Prefix+HClus`: Geographic prefixes combined with hierarchical clustering codes.
- `Geo-Prefix+RQ-VAE`: Geographic prefixes combined with residual-quantized variational codes.
- `Graph RQ-VAE`: A graph-informed residual-quantized variational autoencoder.
- `H-KM`: Hierarchical k-means.
- `HARQ`: Hyperbolic Adaptive Residual Quantization.
- `Hier. RQ`: Hierarchically supervised residual quantization.
- `KG-RQ`: Residual quantization informed by knowledge-graph structure.
- `LLM-Vocab`: Item identifiers composed directly from tokens in the language model vocabulary.
- `Learn. RQ`: End-to-end or alternatingly updated learnable residual quantization.
- `MM-RQ`: Multimodal residual quantization.
- `Masked VQ`: Masked vector quantization over collaborative representations.
- `MoE-VQ`: Mixture-of-experts vector quantization.
- `Multi-Facet ID`: Identifiers representing multiple facets of an item.
- `Multi-Path R-KM+Hash`: Multiple residual-k-means code paths combined with a hash-based identifier component.
- `NU-RQ`: Non-uniform RQ variant.
- `Nested RQ`: Residual quantization across nested representation granularities.
- `OPQ`: Optimized product quantization.
- `Orth. RQ`: Orthogonal residual quantization.
- `PC-AE`: Parallel Codebook Auto-Encoder
- `PID (P-SAE)`: Pretrained Interpretable ID (Pretrained Sparse Autoencoder).
- `Par. OPQ`: Parallel optimized product quantization into unordered sub-codes.
- `Par. VQ`: Parallel multi-codebook vector quantization without sequential residual dependency.
- `Post-hoc RQ`: Residual quantization with post-hoc collision-free code assignment.
- `Prog. RQ`: Progressive RQ variant.
- `QA-RQ`: Qualification-Aware RQ-VAE.
- `R-KM`: Residual k-means.
- `R-KM+EM`: Residual k-means with expectation-maximization-style refinement.
- `R-KM+FSQ`: Residual k-means combined with finite scalar quantization.
- `R-KM+Geo-CB`: Residual k-means combined with a geographic codebook.
- `R-KM+Graph`: Residual k-means combined with a graph over semantic codes.
- `R-KM†`: Residual k-means tokenization (inferred).
- `RQ`: Residual quantization.
- `RQ+IST`: Residual quantization combined with item-level subword tokenization.
- `RQ+LoRA`: Residual quantization adapted per domain with LoRA modules.
- `RQ-KM`: Residual k-means quantization.
- `RQ-PIB`: Residual Quantization with Prefix-aware Interaction Balancing
- `RQ-VAE`: Residual-Quantized Variational AutoEncoder.
- `RQ-VAE / Learn. RQ`: Residual-quantized variational codes or learnable residual-quantization codes in different configurations.
- `RQ-VAE / Par. VQ`: Residual-quantized variational codes or parallel vector-quantization codes in different configurations.
- `RQ-VAE / R-KM / LETTER`: RQ-VAE, residual k-means, or LETTER tokenization in different configurations.
- `RQ-VAE+DINO`: RQ-VAE combined with self-supervised DINO visual quantization.
- `RQ-VAE+PPR`: Residual-quantized variational codes informed by Personalized PageRank signals.
- `RQ-VAE†`: Residual-Quantized Variational AutoEncoder (inferred).
- `RecDMoN / RQ-GAE`: Recursive DMoN graph partitioning, or residual quantization of graph-propagated representations with a graph reconstruction loss.
- `Ref.-RQ`: Reference-vector RQ variant.
- `SRBQ`: Semantic Residual Balanced Quantization
- `Self-Imp.`: Self-improving tokenization refined iteratively from the generator's learned representations.
- `Self-Sup. ID`: Semantic identifiers learned through self-supervision.
- `Shared/Spec. RQ`: Residual quantization using shared and task-specific codebooks.
- `SimHash`: Locality-sensitive hashing with random hyperplanes.
- `Skeleton R-KM`: Residual k-means organized around a shared semantic skeleton.
- `Soft Reassign. RQ`: Residual quantization with differentiable soft code reassignment.
- `Soft-RQ`: Soft-routed RQ variant.
- `Spectral Clus.`: Spectral clustering-based tokenization.
- `Subspace RQ`: Residual quantization applied separately within embedding subspaces.
- `Term-ID`: Standardized textual keyword identifiers generated from item metadata.
- `TokenMoE`: Mixture-of-experts tokenizer with shared and domain-specific experts.
- `Tree`: Tree-structured hierarchical codebook tokenization.
- `Tree-Clus.`: Balanced k-ary tree clustering tokenization.
- `Unified RQ`: Domain-unified residual quantization.
- `n/a`: Not applicable to this method.
- `–`: Not reported in the paper.

## Backbone

- `Dec-Only`: Decoder-only.
- `Dec-Only / Enc-Dec`: Decoder-only and encoder–decoder backbone variants.
- `Dec-Only / Non-AR`: Decoder-only autoregressive and non-autoregressive prediction variants.
- `Dec-Only†`: Decoder-only autoregressive backbone (inferred).
- `Disc.`: A discriminative recommendation model that scores candidates.
- `Disc. / Enc-Dec`: Discriminative scoring and encoder–decoder generation variants.
- `Dual Enc-Dec`: Shared encoder paired with two parallel decoders for dual token streams.
- `Enc-Dec`: Encoder-decoder.
- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Enc-Dec / Dec-Only (AR); Non-AR (PR)`: Encoder–decoder or decoder-only autoregressive variants, and parallel non-autoregressive variants.
- `Enc-Dec / Lazy Dec-Only`: Encoder–decoder and lazy decoder-only backbone variants.
- `Enc-Dec†`: Encoder–decoder backbone (inferred).
- `Enc-Dec† / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Enc-Dec† / Dec-Only†`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Enc-MLP`: A history encoder followed by MLP-based prediction heads.
- `Encoder`: Bidirectional encoder backbone without autoregressive token generation.
- `Encoder (Non-AR)`: Bidirectional encoder trained for non-autoregressive parallel prediction.
- `HeterRec`: HeterRec, the named recommendation backbone used in the paper.
- `Lazy Dec-Only`: A lazy decoder-only architecture that concentrates decoder computation on target generation.
- `Lazy Dec-Only†`: A lazy decoder-only backbone inferred from the adopted model.
- `Non-AR`: Non-autoregressive.
- `Non-AR / Enc-Dec`: Non-autoregressive and encoder–decoder backbone variants.
- `n/a`: Not applicable to this method.
- `–`: Not reported in the paper.

## Tokenizer (Training)

- `Altern.`: Tokenizer and generator are updated in turns.
- `Altern.†`: Tokenizer and generator updated in alternation (inferred).
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Fixed†`: Tokenizer frozen before generator training (inferred).
- `Joint`: The generator loss updates the tokenizer directly.
- `n/a`: Not applicable to this method.
- `–`: Not reported in the paper.

## Objective (Training)

- `(MTP + Masked Rec.) → MTP`: Joint multi-token prediction and masked reconstruction, followed by multi-token prediction alone.
- `(NTP + Ctr.) → RL`: Joint next-token and contrastive training, followed by a reinforcement-learning stage; retained losses are specified per paper.
- `(NTP† / (NTP + Aux.)†) → KL-weighted OPD`: Inferred next-token-based initialization variants followed by KL-weighted on-policy distillation.
- `Discrim.`: Scores items; does not generate SIDs.
- `Discrim. / NTP`: Discriminative scoring or next-token prediction in different configurations.
- `Dual-level Flow Ctr.`: Contrastive training at token and complete-identifier levels in a flow-based model.
- `MTP`: Predicts several codes in parallel at once.
- `MTP + Aux.`: Multi-token prediction jointly optimized with auxiliary objectives.
- `MTP + Ctr.`: MTP plus a contrastive loss.
- `MTP + Ctr. + Aux.`: Multi-token prediction jointly optimized with contrastive and auxiliary objectives.
- `MTP + Rel.MSE`: Multi-token prediction jointly optimized with a mean-squared-error objective on relations.
- `Masked`: Masks part of the codes and reconstructs them (includes masked diffusion).
- `Masked → RL (→ Masked KD for Fast)`: Masked-prediction pretraining, followed by reinforcement learning and optional masked-prediction distillation for a faster variant.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT`: Multi-task next-token prediction, or text next-token prediction with multi-token and ranking objectives; language-task reinforcement learning follows supervised fine-tuning.
- `Multi-task NTP†`: Multi-task next-token prediction (inferred).
- `Multi-task NTP† / NTP`: Inferred multi-task next-token prediction or standard next-token prediction across variants.
- `Multi-task NTP† / NTP†`: Inferred multi-task or single-task next-token-prediction initialization in different backbones.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `NTP + Dense`: NTP plus dense-vector prediction.
- `NTP + PV-RSPO + Rank + Aux.`: Next-token prediction jointly optimized with prefix-value RSPO, ranking, and auxiliary objectives.
- `NTP + RL`: Next-token prediction jointly optimized with reinforcement learning.
- `NTP + Rank`: NTP plus a ranking loss.
- `NTP + Rank + Aux. / MTP + Rank + Aux.`: Autoregressive or parallel token prediction jointly optimized with ranking and auxiliary objectives.
- `NTP / NTP + Aux.`: Next-token prediction alone or jointly optimized with auxiliary objectives.
- `NTP → (NTP + Aux.)`: Next-token prediction, followed by joint optimization of next-token prediction and auxiliary objectives.
- `NTP → (NTP + DPO)`: Next-token prediction, followed by joint next-token prediction and direct preference optimization.
- `NTP → (RL + Rank)`: Next-token prediction, followed by joint reinforcement-learning and ranking objectives.
- `NTP → DPO`: NTP, then preference optimization.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `NTP → RL†`: Next-token prediction followed by reinforcement learning (inferred).
- `NTP†`: Next-token prediction loss (inferred).
- `NTP† / NTP → RL`: Inferred next-token training in one configuration, or next-token training followed by reinforcement learning in another.
- `Next-item CE + Cons. KD + Rank KD`: Next-item cross-entropy jointly optimized with consistency and ranking distillation.
- `n/a`: Not applicable to this method.
- `–`: Not reported in the paper.

## Inference

- `Beam`: Autoregressive beam search over Semantic ID tokens.
- `Beam+Agg.`: Beam search followed by aggregation of predictions that refer to the same item.
- `Beam+Geo-Filter`: Beam search with geographically restricted candidates.
- `BeamFusion`: Joint decoding combining autoregressive SID beam search with dense nearest-neighbor scoring.
- `Beam†`: Autoregressive beam search (inferred).
- `Beam† / C-Beam`: Inherited beam search or prefix-constrained beam search across configurations.
- `Beam† / C-Beam†`: Beam search or constrained beam search in the respective inherited configurations.
- `Beam† / –`: Inherited beam search in one configuration; decoding not reported in the other.
- `Bid-Aware Beam`: Beam search whose scores incorporate bid information.
- `C-Beam`: Constrained beam search.
- `C-Beam / Scoring`: Constrained beam search or direct item scoring, depending on the configuration.
- `CF-Guided C-Beam`: Constrained beam search guided by collaborative signals.
- `CoT`: Chain-of-thought before the SID.
- `CoT+Beam`: Reasoning followed by beam-search decoding.
- `CoT+C-Beam`: Reasoning followed by constrained beam-search decoding.
- `CoT+Fuzzy Match`: Reasoning-guided identifier generation followed by fuzzy matching to available items.
- `CoT+Greedy`: Reasoning with greedy decoding.
- `Diff.`: Diffusion decoding.
- `Diff.+Beam`: Diffusion-based decoding combined with beam search.
- `Diff.+Legalize`: Diffusion-based decoding followed by mapping generated codes to valid items.
- `Div. Beam`: Beam search with an explicit diversity mechanism.
- `Div. C-Beam`: Constrained beam search with an explicit diversity mechanism.
- `Dual Beam`: Beam-search decoding in two branches with merged candidates.
- `Dyn. Beam`: Dynamic beam search.
- `Ensemble`: Score aggregation across multiple randomized token segmentations or decoding paths.
- `FM-Index+Agg.`: FM-index-constrained generation followed by identifier-to-item score aggregation.
- `FP8+RecoGEM`: FP8 inference with the RecoGEM execution framework.
- `Fusion`: Fusion of candidate scores decoded from parallel token branches.
- `GRC+Beam`: Generation, reflection and correction combined with beam search.
- `Graph`: Iterative decoding over a proximity graph of valid item Semantic IDs.
- `Greedy`: Select the highest-scoring next token at each decoding step.
- `Hybrid`: Hybrid retrieval combining generative SID decoding with dense or co-occurrence retrieval.
- `ISD Beam`: Item-supported beam search.
- `Length-Quota Beam`: Beam search with recommendation quotas allocated across output lengths.
- `Non-AR`: Single-pass non-autoregressive parallel decoding.
- `PRM-Beam`: Process-reward-model guided beam search.
- `PV-Beam+Rerank`: Prefix-value-guided beam search followed by reranking.
- `Scoring`: Direct candidate scoring without step-by-step SID generation.
- `Scoring / Beam`: Direct candidate scoring or autoregressive beam search across configurations.
- `Scoring / Beam†`: Discriminative candidate scoring vs. generative beam search.
- `Scoring+Rerank`: Score candidate items and then rerank a selected subset.
- `Self-Draft+Hash`: Self-drafted candidate generation with hash-set validity checking.
- `Sess. Beam`: Session-wise beam search generating a multi-item slate in one pass.
- `Spec. Dec.`: Speculative decoding.
- `Trie/C-Beam`: Prefix-tree (trie) constrained beam search restricted to valid catalog SIDs.
- `Vec. C-Beam`: Vectorized constrained beam search.
- `n/a`: Not applicable to this method.
- `–`: Not reported in the paper.

## SID Input Modalities

- `Text`: Textual item metadata, titles, descriptions, categories, or text-formatted attributes fed to the tokenizer.
- `Img`: Visual item images or image frames fed to the tokenizer.
- `Audio`: Audio tracks or acoustic spectrograms fed to the tokenizer.
- `Video`: Video streams or video-level representations fed to the tokenizer.
- `MM`: Multimodal item representations whose specific constituent modalities are not disaggregated in the paper.
- `CF`: Collaborative filtering or user–item interaction signals fed to the tokenizer.
- `Attr`: Structured tabular or categorical item attributes fed to the tokenizer without text serialization.
- `Geo`: Geographic coordinates, spatial grids, or location features fed to the tokenizer.
- `Time`: Interaction timestamps or temporal features fed to the tokenizer.
- `n/a`: No discrete SID tokenizer is built (items are represented as continuous vectors or plain text).
- `Other`: Tokenizer input outside the signals above, or not stated in the paper; `modality_other` says what it is.

## Domains

- `E-commerce`: E-commerce product recommendation (including all Amazon review subsets, Taobao, JD, etc.).
- `POI / Local`: Point-of-interest, check-in, and local-life service recommendation (including Yelp, Gowalla, Foursquare, etc.).
- `Short video / Live`: Short-video feed and live-streaming recommendation (including Kuaishou, KuaiRand, Douyin, etc.).
- `Ads`: Online advertising and sponsored recommendation.
- `Movie`: Movie recommendation (including MovieLens, Douban Movie, Netflix, etc.).
- `Music`: Music track and artist recommendation (including Last.fm, Spotify, etc.).
- `Search`: Product search, content search, and joint search–recommendation.
- `News`: News article recommendation (including MIND, etc.).
- `Book`: Book and audiobook recommendation (including Douban Book, Goodreads, etc.).
- `Games`: Video game platform recommendation (including Steam).
- `Podcast`: Podcast show and episode recommendation.
- `Long video`: Long-form video platform recommendation.
- `Video`: General video platform recommendation.
- `Image / Article`: Image discovery and article content recommendation.
- `Apps`: Mobile application recommendation.
- `Food / Recipe`: Food and recipe recommendation.
- `Travel / Hotel`: Travel and hotel accommodation recommendation.
- `Recruitment`: Job and recruitment recommendation.
- `Other`: Data from a business the domains above do not cover, or one the paper does not name; each entry says what the paper states.

## Evaluation Settings

- `cold-start`: Dedicated evaluation on zero-interaction users (`scope: user`), zero-interaction items (`scope: item`), or simulated history removal.
- `cross-domain`: Cross-domain transfer, cross-city transfer, or unseen-domain zero-shot evaluation.
- `catalog-change`: Evaluation of identifier maintenance or recommendation after item catalog additions, deletions, or updates.
