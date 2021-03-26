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

serve-docs:
	@$(RUNNER) pydoc-markdown --server --open

build-docs:
	@$(RUNNER) pydoc-markdown --build --site-dir=docs

deploy-docs: build-docs
	@$(RUNNER) mkdocs gh-deploy