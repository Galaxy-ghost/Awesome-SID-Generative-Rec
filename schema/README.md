# Paper Records Schema

Each paper is stored as a single YAML file under `data/papers/<id>.yaml`.
Field names are defined once in [`schema/paper.schema.json`](paper.schema.json) and checked against [`data/vocab.yaml`](../data/vocab.yaml) by `scripts/check.py`.

## Commands

```sh
make build   # Generate README.md, pages/papers/<id>.md, llms.txt, llms-full.txt
make check   # Validate schema, vocabulary, uniqueness, and links; skip external Table 1 if unconfigured
```

`make build` uses the existing YAML records and never synchronizes Table 1 automatically.
To import Table 1 columns explicitly, run `python3 scripts/build.py --sync-table1 path/to/table1.md`.
Alternatively, set `TABLE1=path/to/table1.md` and run `python3 scripts/build.py --sync-table1`.
A requested synchronization with no source or a missing file fails.
Synchronization treats Table 1 as the complete corpus: records absent from it are removed.
Records are matched by name, then by canonical ID for renamed entries; other record fields are preserved.

For the external round-trip check, run `TABLE1=path/to/table1.md make check` or
`python3 scripts/check.py --table1 path/to/table1.md`. An explicit path overrides `TABLE1`.
Without a source, the check visibly skips only the external Table 1 comparison.

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

- Optional architecture diagrams are stored as `architectures/<id>.png`, matching the record ID exactly. `make build` embeds each existing diagram into its paper page; no YAML field is needed. Relative image destinations are checked by `make check`.
