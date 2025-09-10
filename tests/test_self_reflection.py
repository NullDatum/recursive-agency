"""Self-reflection tests ensure recursive loops handle identity hooks."""
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from core.agency_engine import loop, _engine


def test_loop_records_memory():
    _engine.pool._capsules.clear()
    _engine.pool.ghosts.clear()
    loop({"idea": "echo"})
    loop({"idea": "forge"})
    recall = _engine.pool.recall()
    assert recall[-1].payload["state"]["idea"] == "forge"
    assert len(recall) == 2
