# Contributing to Recursive-Agency

We build by contradiction → reflection → revision. Read this before you open a PR.

## Ground rules
- **License:** Code under **AGPLv3**. Docs under **CC BY-SA 4.0** (unless a file states otherwise).
- **AIR Covenant:** Non-legal community commitment (see `/LICENSE_AIR.md`). We honor it; it does not replace AGPL.
- **Provenance:** Every PR must include a short provenance note: what’s original, what’s adapted, and explicit divergence points.

## Workflow
1. **Issue first.** Describe the contradiction or failure you’re addressing.
2. **Design note.** Add a short `Rationale:` section explaining the mutation.
3. **Tests.** Add or update tests under `/tests`.
4. **PR template.** Fill it. Link the issue. Show deltas and tradeoffs.

## Style
- Code: typed where possible, explicit interfaces, no magic strings.
- Docs: imperative, falsifiable, minimal hype. If it can’t break, it can’t grow.

## Checks
- `make check` must pass locally.
- CI will run lint, unit tests, and linkcheck.
