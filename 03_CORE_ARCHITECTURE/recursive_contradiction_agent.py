"""Demonstrate recursive self-mutation driven by contradiction.

This agent attempts to discover an unknown numeric target. Each wrong
guess is treated as a contradiction that mutates the guess and
reinvokes the solver recursively until the contradiction is negligible.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class RecursiveContradictionAgent:
    """Recursive agent that adjusts guesses using contradiction feedback."""

    target: float
    tolerance: float = 1e-6
    guesses: List[float] = field(default_factory=list)

    def run(self, guess: float) -> float:
        """Recursively refine ``guess`` toward ``target``.

        Each step records the guess and mutates it toward the target by
        half of the remaining error. The process stops when the error
        is within ``tolerance`` and returns the final guess.
        """
        self.guesses.append(guess)
        error = self.target - guess
        if abs(error) <= self.tolerance:
            return guess
        return self.run(guess + error / 2)

    def contradictions(self) -> List[float]:
        """Return the signed differences between target and recorded guesses."""
        return [self.target - g for g in self.guesses]


if __name__ == "__main__":
    agent = RecursiveContradictionAgent(target=42.0)
    result = agent.run(0.0)
    print(f"Converged to {result} in {len(agent.guesses)} steps.")
