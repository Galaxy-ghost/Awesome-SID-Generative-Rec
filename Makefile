.PHONY: build check

build:
	python3 scripts/build.py

check:
	python3 scripts/check.py
	npx --yes awesome-lint
