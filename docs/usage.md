# Usage

This example shows how to configure and run a minimal `R2D2Solver` solving the maximum number in a nested list.

```python
from recursive_agency import Capsule, R2D2Solver


def is_atomic(problem):
    return isinstance(problem, int)


def decompose(problem):
    return problem


def hypothesize(problem, memory):
    guesses = [problem]
    guesses.extend(m.insight for m in memory)
    return guesses


def mutate(hypothesis):
    return [hypothesis]


def test(candidate):
    return candidate


def score(observation):
    return float(observation)


def aggregate(partials):
    return max(partials)


def compress(solution, memory):
    return Capsule(insight=solution, score=float(solution))


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

problem = [2, [5, 1], 3]

capsule1 = solver.solve(problem)
print("First pass:", capsule1)

capsule2 = solver.solve(problem, memory=[capsule1])
print("Second pass:", capsule2)
```
