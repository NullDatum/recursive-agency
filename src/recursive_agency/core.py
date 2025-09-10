"""Core solver interface for recursive problem solving.

This module graduates the experimental prototype located at
``03_CORE_ARCHITECTURE/r2d2_core.py`` into the package namespace.
Wrapping the original R2D2 loop here exposes a stable API while
retaining its hook-based design. Callers provide problem-specific
functions for each stage—decomposition, hypothesis generation,
mutation, testing, scoring, aggregation, and compression—so the solver
remains domain agnostic.

The shift trades the freedom of an ad hoc script for a committed
interface. The lean surface keeps the core simple yet leaves ample
room for future extensions such as alternative search heuristics or
concurrency strategies without breaking existing users.
"""

from .r2d2_core import Capsule, R2D2Solver

__all__ = ["Capsule", "R2D2Solver"]
