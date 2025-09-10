import sys
from pathlib import Path

import pytest

# Load the r2d2_core module from its file path since the directory name is not
# a valid Python package name.
CORE_PATH = Path(__file__).resolve().parents[1] / "03_CORE_ARCHITECTURE"
sys.path.append(str(CORE_PATH))
from r2d2_core import Capsule, R2D2Solver  # type: ignore


def _dummy_compress(combined, memory):
    return Capsule(combined, 0.0)


def test_max_depth_limits_recursion():
    """Solver raises RecursionError when depth limit is exceeded."""
    solver = R2D2Solver(
        is_atomic=lambda p: False,
        decompose=lambda p: [p],
        hypothesize=lambda p, m: [],
        mutate=lambda h: [],
        test=lambda c: 0,
        score=lambda o: 0.0,
        aggregate=lambda parts: None,
        compress=_dummy_compress,
    )

    with pytest.raises(RecursionError):
        solver.solve(problem=0, max_depth=5)


def test_atomic_problem_resolves_with_depth_limit():
    """Atomic problem solves even when max_depth is zero."""
    solver = R2D2Solver(
        is_atomic=lambda p: True,
        decompose=lambda p: [],
        hypothesize=lambda p, m: [],
        mutate=lambda h: [],
        test=lambda c: 0,
        score=lambda o: 0.0,
        aggregate=lambda parts: None,
        compress=_dummy_compress,
    )

    capsule = solver.solve(problem=0, max_depth=0)
    assert isinstance(capsule, Capsule)
