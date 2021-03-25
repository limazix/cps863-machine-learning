SHELL:=/bin/bash

install:
	@poetry install

update:
	@poetry update

clean:
	@poetry cache clean