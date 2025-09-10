codex/add-badges-and-ci-configuration
"""Recursive Agency core package."""

from .r2d2_core import Capsule, R2D2Solver
from .agency_engine import AgencyEngine

__all__ = ["Capsule", "R2D2Solver", "AgencyEngine"]

"""Recursive Agency package."""

from .agency_engine import AgencyEngine
from .r2d2_core import Capsule, R2D2Solver

__all__ = ["AgencyEngine", "Capsule", "R2D2Solver"]
        main
