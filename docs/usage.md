# R2D2Solver Usage

This document outlines how to use the `R2D2Solver` for recursive problem solving.

## Basic Run

Provide domain-specific hooks for decomposition, hypothesis generation, testing, and aggregation, then call `solve` with an initial problem.

```python
from recursive_agency import R2D2Solver

solver = R2D2Solver(
    is_atomic=is_atomic,
    decompose=decompose,
    hypothesize=hypothesize,
    mutate=mutate,
    test=test,
    score=score,
    aggregate=aggregate,
    compress=compress,
)

result = solver.solve(initial_problem)
print(result.insight)
```

## Iterative Self‑Improvement

`R2D2Solver` supports iterative workflows where the outcome of one run informs the next. Reuse the `memory` list or the returned capsule to refine prompts or settings and call `solve` again.

```python
from recursive_agency import Capsule

memory: list[Capsule] = []

first_pass = solver.solve("Initial problem", memory=memory)

refined_problem = f"Refine solution based on: {first_pass.insight}"
second_pass = solver.solve(refined_problem, memory=memory)
```

By keeping shared state in `memory`, each iteration learns from prior passes, enabling self‑improving problem solving.
