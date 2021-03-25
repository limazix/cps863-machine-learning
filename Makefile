SHELL:=/bin/bash

install:
	@poetry install

update:
	@poetry update

clean:
	@poetry cache clean

test:
	@poetry run pytest

coverage:
	@poetry run pytest --cov=tools