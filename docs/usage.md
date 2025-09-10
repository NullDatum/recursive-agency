# R2D2Solver Usage

This module exposes the `R2D2Solver` class for building recursive problem solvers by
supplying domain-specific hooks. Each call to `solve` returns a `Capsule` object
containing the best insight discovered during that pass.

```python
from recursive_agency.r2d2_core import R2D2Solver, Capsule

# define hooks here ...
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

capsule = solver.solve(problem)
print(capsule.insight)
```

## Iterative refinement

`R2D2Solver` accumulates `Capsule` objects in a shared memory list. Passing the
same memory into subsequent runs allows later iterations to adapt based on earlier
results, enabling self-improving workflows.

```python
memory: list[Capsule] = []
solver = make_solver()

# First pass generates an initial solution and stores a capsule in memory
first_capsule = solver.solve(initial_problem, memory)

# Refine the problem or solver settings using the first result
refined_problem = tweak(initial_problem, first_capsule.insight)

# Second pass builds on prior context stored in ``memory``
second_capsule = solver.solve(refined_problem, memory)
```

This chaining of runs lets the solver iteratively refine its understanding and
improve solutions over time.
