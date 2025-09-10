"""Recursive agency engine managing memory capsules."""
from __future__ import annotations

from typing import Dict, Any, Optional

from .memory_pool import MemoryPool


class RecursionEngine:
    """Coordinate recursion steps and manage a memory pool."""

    def __init__(self, pool: Optional[MemoryPool] = None) -> None:
        self.pool = pool or MemoryPool()

    def step(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Record the state in memory and apply decay."""
        self.pool.append({"state": state})
        self.pool.step()
        return state


_engine = RecursionEngine()


def loop(state: Dict[str, Any]) -> Dict[str, Any]:
    """Compatiblity hook mirroring the original API."""
    return _engine.step(state)
