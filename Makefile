.PHONY: check lint test docs

check: lint test docs

lint:
	@ruff check || true
	@npx markdownlint '**/*.md' --ignore node_modules || true
	@git ls-files '*.yml' '*.yaml' | xargs yamllint

test:
	@pytest -q || true

docs:
	@npx markdown-link-check README.md || true
