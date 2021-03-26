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
	@$(RUNNER) flake8 $(PYTHON_SCRIPTS) --statistics

test:
	@$(RUNNER) pytest

coverage:
	@$(RUNNER) pytest --cov=$(PYTHON_TOOLS)

serve-docs:
	@$(RUNNER) pydoc-markdown --server --open

build-docs:
	@$(RUNNER) pydoc-markdown --build --site-dir=site

deploy-docs:
	@git push origin `git subtree split --prefix build/docs/site main`:gh-pages --force