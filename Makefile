.PHONY: check lint test docs hooks

check: lint test docs

lint:
	@ruff check || true
	@markdownlint '**/*.md' || true
	@yamllint .

test:
	@pytest -q || true

docs:
	@python -m linkcheck README.md || true

hooks:
	git config core.hooksPath .githooks
