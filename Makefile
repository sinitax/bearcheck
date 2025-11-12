all: format lint mypy test

fix: format-fix lint-fix

UV = VIRTUAL_ENV=.venv uv

format:
	@$(UV) run ruff format --check

format-fix:
	@$(UV) run ruff format

lint:
	@$(UV) run ruff check

lint-fix:
	@$(UV) run ruff check --fix

mypy:
	@$(UV) run mypy ./src ./tests

test:
	$(UV) run pytest

build:
	@$(UV) build

publish:
	@$(UV) run -m twine upload dist/*

.PHONY: all fix format format-fix lint lint-fix mypy build
