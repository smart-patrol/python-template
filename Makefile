help:
  @echo "available commands"
  @echo " - install    : installs all requirements"
  @echo " - dev        : installs all development requirements"
  @echo " - test       : run all unit tests"
  @echo " - clean      : cleans up all folders"
  @echo " - flake      : runs flake8 style checks"
  @echo " - black      : runs blake formatting checks"
  
black:
	black clumper tests setup.py --check
flake:
	flake8 clumpter tests setup.py
test:
	pytest

check: black flake test

install:
	pip install rich
	python -m pip install -e .

install-dev: install
		python -m pip install -e ".[dev]"
		pre-commit install

install-test: install
		python -m pip install -e ".[test]]"
		python -m pip install -e ".[all]"

clean:
	rm -rf **/.ipynb_checkpoints **/.pytest_cache **/__pycache__ **/**/__pycache__ .ipynb_checkpoints .pytest_cache
