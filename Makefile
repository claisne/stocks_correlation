.PHONY: docs

test:
	pipenv run py.test

flake8:
	pipenv run flake8 stocks_correlation

pylint:
	pipenv run pylint stocks_correlation

lint: flake8 pylint

docs:
	cd docs && pipenv run make html
