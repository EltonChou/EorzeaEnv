.PHONY: help
.SILENT:

help: # Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: # Install requirements of project.
	poetry install

cov-test: # Run the tests.
	coverage run -m pytest

cov-report: cov-test # Show the coverage of tests.
	coverage report -m

freeze: # Export the requirements.txt file.
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	poetry export --with dev --without-hashes -f requirements.txt --output requirements-dev.txt
	poetry export --with test --without-hashes -f requirements.txt --output requirements-test.txt
	poetry export --with dev --without-hashes -f constraints.txt --output constraints.txt

lint: # Lint the code.
	flake8

type-check: # Check the type.
	mypy

format: # Format the code.
	black .

update-version: # Sync package file version.
# 	sed -i -E "s/[0-9]+\.[0-9]+\.[0-9]+/$$(poetry version --short)/1" EorzeaEnv/__init__.py
	python utils/sync_version.py

print-changelog: # Print changelog of current version.
	@awk -v ver=$$(poetry version --short) '/^#+ \[/ { if (p) { exit }; if ($$2 == "["ver"]") { p=1; next } } p && NF' CHANGELOG.md
