.PHONY: clean data flake requirements python_environment test check development_environment activate
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

## Set up python interpreter environment
python_environment:
	python -m venv venv
	@echo ">>> New virtualenv created. Activate with cmd: venv\Scripts\activate.bat"
	@echo ">>> or bash: source ./venv/Scripts/activate"

activate:
	source ./venv/Scripts/activate

## Install Python Dependencies
requirements: 
	python -m pip install -U pip setuptools wheel
	python -m pip install -e ".[dev]"

development_environment: 
	activate; \	
	requirements; \
	pre-commit install

## Make Dataset
data: requirements
	python src/data/make_dataset.py data/raw data/processed

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf scikit_lego.egg-info
	rm -rf .ipynb_checkpoints
	rm -rf notebooks/.ipynb_checkpoints

## Lint using flake8
flake:
	flake8 src
	flake8 tests

test:
	pytest --cov=src

check: flake test clean

help:
	@echo: "TODO help file"