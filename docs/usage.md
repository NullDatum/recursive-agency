# Usage

This snippet demonstrates how to configure and invoke `R2D2Solver`.

```python
from recursive_agency import Capsule, R2D2Solver


def is_atomic(problem):
    return isinstance(problem, int)


def decompose(problem):
    return problem  # assume ``problem`` is a list


def hypothesize(problem, memory):
    memory_insights = [c.insight for c in memory]
    return [problem] + memory_insights


def mutate(candidate):
    return [candidate]


def test(candidate):
    return candidate


def score(observation):
    return float(observation)


def aggregate(parts):
    return max(parts)


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

problem = [3, [1, 4]]
first = solver.solve(problem)
second = solver.solve(problem, memory=[first])

print(first)
print(second)
```
