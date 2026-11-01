.PHONY: build check

build:
	python3 scripts/build.py

check:
	python3 scripts/check.py $(if $(TABLE1),--table1 $(TABLE1))
	npx --yes awesome-lint
