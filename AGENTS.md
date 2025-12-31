# AGENTS

This repository is organised into three main areas:

- Numbered spec folders (`01_FOUNDATIONS` ... `09_RECURSIVE_AUDIT`) hold
  documentation and design notes.
- `src/recursive_agency` provides the Python package that exposes the core
  runtime and the `R2D2Solver`.
- `tests` contains unit tests and doctest-style specs.

## Naming conventions

- Module files and functions use `snake_case`.
- Classes use `PascalCase`.
- Test modules start with `test_`.
- Exported symbols live in `__all__` and are re-exported in
  `src/recursive_agency/__init__.py`.

## Lessons from migrating `R2D2Solver`

- Solver logic lives in `src/recursive_agency/r2d2_core.py` with hooks that
  accept callables for domain-specific behaviour.
- Simple data containers such as `Capsule` use `@dataclass` for clarity.
- The solver is re-exported from the package root for convenient imports.
- `memory` is optional and threaded through recursive calls, enabling simple
  state sharing.
- Tests rely on deterministic hooks; keep examples pure and reproducible.

## Linting and tests

- Run `make check` to execute linting, tests, and documentation link checks.
- Individual commands:
  - `make lint` (ruff, markdownlint, yamllint)
  - `make test` (pytest)
  - `make docs` (linkcheck)

### Common pitfalls

- `markdownlint` enforces line length (`MD013`). Break long lines or suppress
  with `<!-- markdownlint-disable-next-line MD013 -->`.
- `ruff` flags unused imports and formatting issues; run it before committing.
- Ensure YAML files have consistent indentation to satisfy `yamllint`.
