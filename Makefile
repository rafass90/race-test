.PHONY: help

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

check-python-import:  ## Check python import
	@cd . && isort --check-only

clean:  ## Clean files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

flake8:  ## Flake8
	@flake8 --show-source .

fix-python-import:  ## Fix python import
	@cd . && isort -rc -y

lint: clean flake8 check-python-import static-check  ## Python lint

test: clean  ## Run all tests
	@py.test -x .

requirements-dev:  ## Install requirements dev
	@pip install -U -r requirements/dev.txt

run:  ## Run job
	@python main.py $(LOG) $(RESULT) $(ARGS)