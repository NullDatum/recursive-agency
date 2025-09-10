import pathlib
import sys
from typing import List

# Ensure the package is importable
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from recursive_agency import Capsule, R2D2Solver


def test_trivial_hooks_return_capsule():
    """Solver with no recursion returns expected capsule."""

    solver = R2D2Solver(
        is_atomic=lambda p: True,
        decompose=lambda p: [],
        hypothesize=lambda p, m: [p],
        mutate=lambda h: [h],
        test=lambda c: c,
        score=lambda o: 1.0,
        aggregate=lambda insights: insights[0] if insights else None,
        compress=lambda insight, mem: Capsule(insight=insight, score=1.0),
    )

    capsule = solver.solve("data")
    assert isinstance(capsule, Capsule)
    assert capsule.insight == "data"
    assert capsule.score == 1.0


def test_memory_reuse_across_recursion():
    """All recursive calls share the same memory list."""

    memory_ids: List[int] = []

    def compress(insight: int, mem: List[Capsule]) -> Capsule:
        memory_ids.append(id(mem))
        return Capsule(insight=insight, score=0.0)

    solver = R2D2Solver(
        is_atomic=lambda p: isinstance(p, int),
        decompose=lambda p: p,  # "p" is a list of ints
        hypothesize=lambda p, m: [p],
        mutate=lambda h: [h],
        test=lambda c: c,
        score=lambda o: float(o),
        aggregate=lambda insights: sum(insights),
        compress=compress,
    )

    memory: List[Capsule] = []
    solver.solve([1, 2], memory)

    assert len(memory) == 3
    assert memory_ids and memory_ids[0] == id(memory)
    assert len(set(memory_ids)) == 1
