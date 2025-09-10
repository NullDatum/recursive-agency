# Contributing
This project is dual-bound: AGPLv3 (legal) + AIR (recursive). By contributing you agree:
- You must **mutate** ideas, not imitate.
- PRs must include a short **Divergence Note**: what you changed and why.
- Add or update at least one falsifiability check.

## How to dev
1. `pip install -e ".[dev]"`
2. `ruff check .` and `mypy src`
3. `pytest`

## Divergence Note template
- **Source touched:** (file/section)
- **Contradiction introduced:** …
- **Falsifiability hook:** new test/check is …
