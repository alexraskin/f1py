.DEFAULT_GOAL := help
.PHONY: coverage deps help lint push test

coverage:  ## Run tests with coverage
	coverage erase
	coverage run --include=formula1py/* -m pytest -ra
	coverage report -m

dev-deps:  ## Install dependencies
	python3 -m pip install pipenv
	pipenv install -dev

lint:  ## Lint and static-check
	flake8 formula1py/formula1.py
	pylint formula1py/formula1.py
	mypy formula1py/formula1.py

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	pytest -ra formula1py/tests/test.py

publish:  ## Publish to PyPi
	python -m flit publish


bind ?= localhost
port ?= 3000
serve:
	python -m http.server dist --bind $(bind) $(port)