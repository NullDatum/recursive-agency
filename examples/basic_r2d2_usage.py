from __future__ import annotations

"""Minimal example of the R2D2 solver on a toy summation problem."""

from pathlib import Path
import sys
from typing import Any, List

# Add core module to path
sys.path.append(str(Path(__file__).resolve().parents[1] / "03_CORE_ARCHITECTURE"))
from r2d2_core import Capsule, R2D2Solver


def is_atomic(problem: List[int]) -> bool:
    """An atomic problem is a list with a single element."""
    return len(problem) == 1


def decompose(problem: List[int]) -> List[List[int]]:
    """Split the list into two halves."""
    mid = len(problem) // 2
    return [problem[:mid], problem[mid:]]


def hypothesize(problem: List[int], memory: List[Capsule]) -> List[int]:
    """For an atomic list, the hypothesis is the contained value."""
    return [problem[0]]


def mutate(hypothesis: int) -> List[int]:
    """No mutation; return the hypothesis unchanged."""
    return [hypothesis]


def test(candidate: int) -> int:
    """Testing simply returns the candidate."""
    return candidate


def score(observation: int) -> float:
    """Use the value itself as the score."""
    return float(observation)


def aggregate(results: List[int]) -> int:
    """Combine sub-results by summing them."""
    return sum(results)


def compress(insight: Any, memory: List[Capsule]) -> Capsule:
    """Wrap the insight in a capsule and print it."""
    capsule = Capsule(insight=insight, score=float(insight or 0))
    print(f"[Capsule] {capsule}")
    return capsule


def main() -> None:
    numbers = [1, 2, 3, 4]
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
    final = solver.solve(numbers)
    print(f"Final result: {final.insight}")


if __name__ == "__main__":
    main()
