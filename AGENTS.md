# AGENTS

## Project layout

- `src/recursive_agency/` – core package with `AgencyEngine` and `R2D2Solver`.
- `tests/` – pytest suite covering the package and doctests.
- Numbered spec directories (`01_FOUNDATIONS`..`09_RECURSIVE_AUDIT`)
  hold design docs.
- Support material lives in `docs/`, `specs/`, and `workflows/`.

## Naming conventions

- Python modules and functions use `snake_case`; classes use `CamelCase`.
- Tests sit in `tests/` and start with `test_`.
- Docs use numeric prefixes plus `snake_case`; avoid "god words" per
  `02_DESIGN_PRINCIPLES/no_god_words.md`.

## Linting and testing

Run these checks before committing:

```bash
ruff check
pytest
markdownlint '**/*.md'
python -m linkcheck README.md
yamllint .
```

`make check` executes the full suite.

## Rationale for `recursive_agency`

The package collects reference implementations for the project's recursive
loop. `AgencyEngine` illustrates an echo/forge/reflect cycle.
`R2D2Solver` supplies a generic "divide, recurse, resolve" framework.

## Open questions

API boundaries, docstring style, and extensibility patterns (plugins, async)
remain unsettled. Raise uncertain points in PR discussions.
