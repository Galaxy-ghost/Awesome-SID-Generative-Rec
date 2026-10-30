# Paper Records Schema

Each paper is stored as a single YAML file under `data/papers/<id>.yaml`.
Field names are defined once in [`schema/paper.schema.json`](paper.schema.json) and checked against [`data/vocab.yaml`](../data/vocab.yaml) by `scripts/check.py`.

## Commands

```sh
make build   # Generate README.md, pages/papers/<id>.md, llms.txt, llms-full.txt
make check   # Validate schema, vocabulary, uniqueness, Table 1 round-trip, and links
```

## Record Format

```yaml
id: tiger
name: TIGER
title: "Recommender Systems with Generative Retrieval"
authors: "Rajput et al."
year: 2023
venue: "NeurIPS’23"
links:
  arxiv: "https://arxiv.org/abs/2305.05065"
  code: null
problem: psb
stage: n/a
representation: Text
tokenization: RQ-VAE
backbone: Enc-Dec
tokenizer: Fixed
objective: NTP
inference: Beam
poi: false
summary: "Encodes item text into hierarchical RQ-VAE semantic IDs and autoregressively decodes target item codes with a T5 encoder-decoder."
evidence:
  - field: tokenization
    quote: "We use Residual-Quantized Variational AutoEncoder (RQ-VAE) to generate Semantic IDs."
    where: "§3.1, p.3"
```

- `problem`: `psb` (`Paradigms, Systems and Benchmarks`) or `I`–`VI` (`Informativeness`, `Uniqueness and Validity`, `SID–Model Alignment`, `Utility`, `Efficiency`, `Generalization`).
- `stage`: `n/a` (for `psb`) or one of `Representation`, `Tokenization`, `Backbone`, `Training`, `Inference`.
- Technical columns (`representation`, `tokenization`, `backbone`, `tokenizer`, `objective`, `inference`) are stored verbatim as in Table 1, including `†` (inferred) and `A / B` (dual-branch setups).
- Optional narrative deep dives are stored in `notes/<id>.md` and embedded into `pages/papers/<id>.md` during `make build`.
