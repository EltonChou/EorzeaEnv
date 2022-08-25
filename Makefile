.PHONY: help
.SILENT:

help: # Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: # Install requirements of project.
	poetry install

cov-test: # Run the tests.
	coverage run -m pytest

cov-report: # Show the coverage of tests.
	coverage run -m pytest && coverage report -m

freeze: # Export the requirements.txt file.
	poetry export --dev --without-hashes -f requirements.txt --output requirements.txt

lint: # Lint the code.
	flake8

print-changelog: # Print changelog of current version.
	@awk -v ver=$$(poetry version --short) '/^#+ \[/ { if (p) { exit }; if ($$2 == "["ver"]") { p=1; next } } p && NF' CHANGELOG.md
