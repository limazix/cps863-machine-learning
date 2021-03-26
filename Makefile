SHELL:=/bin/bash
RUNNER=poetry run

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
ROOT_DIR := $(dir $(MAKEFILE_PATH))

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
	@$(RUNNER) pydoc-markdown --build --site-dir=gh-pages

deploy-docs:
	@mv ./build/docs/gh-pages .
	@git add .
	@git commit -am"it generates github static page"
	@git push origin `git subtree split --prefix gh-pages main`:gh-pages --force
	@git reset --hard HEAD~

jupyter-lab:
	@docker run -it -p 8888:8888 \
		-v $(ROOT_DIR)/notebooks/:/home/jovyan/work \
		-v $(ROOT_DIR)/data/:/home/jovyan/work/data \
		-w /home/jovyan/work \
		elyra/elyra jupyter lab