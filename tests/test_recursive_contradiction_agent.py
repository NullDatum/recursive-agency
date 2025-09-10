import sys
from pathlib import Path

# Add core architecture path for imports
sys.path.append(str(Path(__file__).resolve().parents[1] / "03_CORE_ARCHITECTURE"))

from recursive_contradiction_agent import RecursiveContradictionAgent


def test_converges_to_target():
    agent = RecursiveContradictionAgent(target=5.0, tolerance=1e-6)
    result = agent.run(0.0)
    assert abs(result - 5.0) <= 1e-6
    # ensure contradictions shrink in magnitude
    diffs = agent.contradictions()
    assert all(abs(a) >= abs(b) for a, b in zip(diffs, diffs[1:]))
