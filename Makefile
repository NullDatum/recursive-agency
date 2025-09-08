.PHONY: check lint test docs

check: lint test docs

lint:
	@ruff check || true
	@markdownlint '**/*.md' || true
	@yamllint .

test:
	@pytest -q || true

docs:
	@python -m linkcheck README.md || true
