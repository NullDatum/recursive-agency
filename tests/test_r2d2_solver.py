import sys
from pathlib import Path

# Add core architecture path for import
sys.path.append(str(Path(__file__).resolve().parents[1] / '03_CORE_ARCHITECTURE'))

from r2d2_core import R2D2Solver, Capsule


def make_solver(call_history=None):
    """Create a solver with simple numeric hooks.

    If ``call_history`` is provided, records calls to ``decompose`` and
    ``hypothesize``.
    """
    def is_atomic(x):
        return isinstance(x, int)

    def decompose(x):
        if call_history is not None:
            call_history.setdefault('decompose', []).append(x)
        return x

    def hypothesize(x, memory):
        if call_history is not None:
            call_history.setdefault('hypothesize', []).append(x)
        return [x]

    def mutate(h):
        return [h]

    def test_fn(c):
        return c

    def score(o):
        return o

    def aggregate(parts):
        return sum(parts)

    def compress(insight, memory):
        # Score is unused in these tests
        return Capsule(insight, 0.0)

    return R2D2Solver(
        is_atomic=is_atomic,
        decompose=decompose,
        hypothesize=hypothesize,
        mutate=mutate,
        test=test_fn,
        score=score,
        aggregate=aggregate,
        compress=compress,
    )


def test_atomic_vs_non_atomic_paths():
    calls = {}
    solver = make_solver(calls)

    # Atomic problem should bypass decomposition and go straight to hypothesize
    solver.solve(1)
    assert calls.get('decompose') is None
    assert calls.get('hypothesize') == [1]

    # Non-atomic problem triggers decomposition; hypothesize only for leaves
    calls.clear()
    solver.solve([1, 2])
    assert calls.get('decompose') == [[1, 2]]
    assert calls.get('hypothesize') == [1, 2]


def test_memory_growth_across_nested_calls():
    solver = make_solver()
    memory = []
    solver.solve([[1], [2]], memory)
    # Two leaves + two intermediate nodes + top level = 5 capsules
    assert len(memory) == 5


def test_empty_hypothesize_or_mutate():
    # Case where hypothesize returns an empty list
    def hypo_empty(problem, memory):
        return []

    solver = R2D2Solver(
        is_atomic=lambda p: True,
        decompose=lambda p: [],
        hypothesize=hypo_empty,
        mutate=lambda h: [h],
        test=lambda c: c,
        score=lambda o: 0.0,
        aggregate=lambda parts: parts,
        compress=lambda insight, memory: Capsule(insight, 0.0),
    )
    memory = []
    capsule = solver.solve('problem', memory)
    assert capsule.insight is None
    assert len(memory) == 1

    # Case where mutate returns an empty list
    def mutate_empty(h):
        return []

    solver2 = R2D2Solver(
        is_atomic=lambda p: True,
        decompose=lambda p: [],
        hypothesize=lambda p, m: ['seed'],
        mutate=mutate_empty,
        test=lambda c: c,
        score=lambda o: 0.0,
        aggregate=lambda parts: parts,
        compress=lambda insight, memory: Capsule(insight, 0.0),
    )
    memory2 = []
    capsule2 = solver2.solve('problem', memory2)
    assert capsule2.insight is None
    assert len(memory2) == 1
