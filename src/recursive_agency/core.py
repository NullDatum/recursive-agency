"""Core solver primitives for recursive agency.

This package-level module formalizes the experimental
``03_CORE_ARCHITECTURE/r2d2_core.py`` prototype into a stable package
component.  The original script offered quick iteration but mixed the
algorithm with domain specifics.  By relocating the loop here we trade a
bit of ad-hoc flexibility for a clearer API; callers must now provide hook
implementations explicitly, which increases boilerplate for trivial cases
but yields a predictable interface.

The solver's behaviour is defined entirely by user-supplied hooks, so new
hypothesis generators, scoring schemes, or memory backends can drop in
without touching the recursion itself.  This pluggable design keeps the
core minimal while supporting future extensions.
"""

from .r2d2_core import Capsule, R2D2Solver

__all__ = ["Capsule", "R2D2Solver"]
