# Contributing

To add or update a paper in two steps:

1. Create or edit `data/papers/<id>.yaml` following [`schema/paper.schema.json`](schema/paper.schema.json) and [`data/vocab.yaml`](data/vocab.yaml) (optionally add a technical walkthrough in `notes/<id>.md`).
2. Run `make build && make check` to regenerate `README.md`, `pages/papers/<id>.md`, and `llms.txt` and verify all checks pass.
