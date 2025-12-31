# Development Notes

## Repository Layout

The repository is split into numbered modules that mirror the design
sequence:

- `01_FOUNDATIONS/` – falsifiability criteria and baseline assumptions.
- `02_DESIGN_PRINCIPLES/` – naming discipline and architectural rules.
- `03_CORE_ARCHITECTURE/` – high level design docs and executable
  primitives.
- `src/recursive_agency/` – importable package containing the runtime.
- `tests/` – markdown driven test specifications.

Numbered directories are ordered intentionally; keep new material in the
appropriate stage and update references in `README.md` if structure
changes.

## Naming Conventions

- Modules and functions use `snake_case`.
- Classes use `PascalCase`.
- Private helpers are prefixed with a single underscore.
- Tests mirror the package path and use `test_*.py` or markdown doctests.

## R2D2Solver Migration

`R2D2Solver` now lives in `src/recursive_agency/r2d2_core.py`. Migrating it
from a standalone script into the package highlighted several lessons:

1. **Hook-based design** – keeping domain logic injected via callables
   makes the core solver reusable across projects.
2. **Typed dataclasses** – `Capsule` and `R2D2Solver` rely on type hints
   for clarity and static analysis.
3. **Explicit exports** – maintaining `__all__` prevents accidental API
   leakage.

When adding new solvers or extensions, preserve this separation of core
mechanics from domain specifics.

## Linting and Tests

Use the provided `Makefile` targets:

- `make lint` – runs `ruff`, `markdownlint`, and `yamllint`.
- `make test` – executes the `pytest` suite.
- `make check` – runs both lint and test targets plus doc link checks.

### Common Pitfalls

- `markdownlint` enforces an 80 character line limit; break long lines or
  use `<!-- markdownlint-disable-line -->` for justified exceptions.
- Ensure new modules are added to the appropriate directory and exported
  via `__all__` when necessary.

