"""Generic recursive problem-solving loop (R2D2).

This module implements a framework for the "divide, recurse, resolve" strategy
outlined in `r2d2_core.md`. Domain-specific behaviour is injected through
callable hooks passed to :class:`R2D2Solver`.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, List, Optional, Tuple


@dataclass
class Capsule:
    """Compressed insight returned by each pass of the solver."""
    insight: Any
    score: float


@dataclass
class R2D2Solver:
    """Core recursive problem solver.

    Each parameter is a hook that customises a stage of the loop.
    The solver is domain agnostic; callers define how to decompose
    problems, generate and mutate hypotheses, test them, score
    observations, aggregate partial solutions, and compress results
    into capsules stored in memory.
    """

    is_atomic: Callable[[Any], bool]
    decompose: Callable[[Any], List[Any]]
    hypothesize: Callable[[Any, List[Capsule]], List[Any]]
    mutate: Callable[[Any], List[Any]]
    test: Callable[[Any], Any]
    score: Callable[[Any], float]
    aggregate: Callable[[List[Any]], Any]
    compress: Callable[[Any, List[Capsule]], Capsule]

    def solve(self, problem: Any, memory: Optional[List[Capsule]] = None) -> Capsule:
        """Solve ``problem`` recursively and return a capsule.

        ``memory`` accumulates capsules from previous passes and is reused
        across recursive calls, providing context and feedback.
        """
        if memory is None:
            memory = []
        if self.is_atomic(problem):
            return self._solve_atomic(problem, memory)
        parts = self.decompose(problem)
        solutions = [self.solve(p, memory) for p in parts]
        combined = self.aggregate([s.insight for s in solutions])
        capsule = self.compress(combined, memory)
        memory.append(capsule)
        return capsule

    def _solve_atomic(self, problem: Any, memory: List[Capsule]) -> Capsule:
        """Process an atomic subproblem."""
        hypotheses = self.hypothesize(problem, memory)
        mutated = [m for h in hypotheses for m in self.mutate(h)]
        evaluations: List[Tuple[Any, float]] = []
        for candidate in mutated:
            observation = self.test(candidate)
            evaluations.append((candidate, self.score(observation)))
        if not evaluations:
            capsule = self.compress(None, memory)
            memory.append(capsule)
            return capsule
        best_candidate, best_score = max(evaluations, key=lambda pair: pair[1])
        capsule = self.compress(best_candidate, memory)
        memory.append(capsule)
        return capsule


__all__ = ["Capsule", "R2D2Solver"]
