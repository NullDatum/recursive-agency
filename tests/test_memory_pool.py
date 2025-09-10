"""Tests for memory capsule decay and ghosting."""
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.memory_pool import MemoryPool


def test_decay_moves_capsule_to_ghost():
    pool = MemoryPool(decay=0.6, min_strength=0.2)
    pool.append({"msg": "a"})
    pool.step()  # strength 0.4
    pool.step()  # strength -0.2 -> ghosted
    assert pool.ghosts
    assert not pool.recall()


def test_validate_detects_tampering():
    pool = MemoryPool()
    cap = pool.append({"msg": "a"})
    pool.append({"msg": "b"})
    assert pool.validate()  # baseline
    cap.payload["msg"] = "evil"
    assert not pool.validate()
