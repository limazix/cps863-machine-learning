SHELL:=/bin/bash

install:
	@poetry install

clean:
	@poetry cache clean

test:
	@poetry run pytest