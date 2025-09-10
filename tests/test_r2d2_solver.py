import pathlib
import sys
from typing import List

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "03_CORE_ARCHITECTURE"))

from r2d2_core import Capsule, R2D2Solver


def make_solver() -> R2D2Solver:
    """Create an R2D2Solver with deterministic toy hooks."""

    def is_atomic(problem: object) -> bool:
        return isinstance(problem, int)

    def decompose(problem: List[int]) -> List[int]:
        return problem

    def hypothesize(problem: int, memory: List[Capsule]) -> List[int]:
        return [problem + 1]

    def mutate(hypothesis: int) -> List[int]:
        return [hypothesis, hypothesis * 2]

    def test(candidate: int) -> int:
        return candidate

    def score(observation: int) -> float:
        return float(observation)

    def aggregate(insights: List[int]) -> int:
        return sum(insights)

    def compress(insight: int | None, memory: List[Capsule]) -> Capsule:
        value = 0 if insight is None else insight
        return Capsule(insight=value, score=float(value))

    return R2D2Solver(
        is_atomic=is_atomic,
        decompose=decompose,
        hypothesize=hypothesize,
        mutate=mutate,
        test=test,
        score=score,
        aggregate=aggregate,
        compress=compress,
    )


def test_solve_atomic_problem():
    solver = make_solver()
    memory: List[Capsule] = []
    capsule = solver.solve(1, memory)
    assert capsule.insight == 4
    assert [c.insight for c in memory] == [4]


def test_solve_composite_problem():
    solver = make_solver()
    memory: List[Capsule] = []
    capsule = solver.solve([1, 2], memory)
    assert capsule.insight == 10
    assert [c.insight for c in memory] == [4, 6, 10]
