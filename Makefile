.PHONY: docs

test:
	pipenv run py.test

flake8:
	pipenv run flake8 stocks_correlation

docs:
	cd docs && pipenv run make html
