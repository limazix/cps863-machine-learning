SHELL:=/bin/bash

RUNNER=poetry run

install:
	@poetry install

update:
	@poetry update

clean:
	@poetry cache clean

test:
	@$(RUNNER) pytest

coverage:
	@$(RUNNER) pytest --cov=tools

doc-server:
	@$(RUNNER) pydoc-markdown --server --open