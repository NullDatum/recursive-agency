.PHONY: check lint test docs

check: lint test docs

lint:
	@ruff check || true
	@npx markdownlint '**/*.md' --ignore node_modules || true
	@yamllint $(shell git ls-files '*.yml' '*.yaml')

test:
	@pytest -q || true

docs:
	@npx markdown-link-check README.md || true
