SHELL:=/bin/bash
RUNNER=poetry run

PYTHON_TOOLS=tools
PYTHON_TESTS=tests
PYTHON_SCRIPTS=$(PYTHON_TOOLS) $(PYTHON_TESTS)

install:
	@poetry install

update:
	@poetry update

clean:
	@poetry cache clean

lint:
	@$(RUNNER) black $(PYTHON_SCRIPTS) --check

test:
	@$(RUNNER) pytest

coverage:
	@$(RUNNER) pytest --cov=$(PYTHON_TOOLS)

serve-docs:
	@$(RUNNER) pydoc-markdown --server --open

build-docs:
	@$(RUNNER) pydoc-markdown --build --site-dir=docs

deploy-docs: build-docs
	@$(RUNNER) mkdocs gh-deploy