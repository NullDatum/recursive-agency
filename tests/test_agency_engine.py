import pathlib
import sys
from typing import List, Tuple

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "03_CORE_ARCHITECTURE"))

from agency_engine import AgencyEngine


def test_generate_response_logs_history():
    engine = AgencyEngine()
    response = engine.generate_response("hello")
    assert response == "Echo: hello"
    assert engine.history == [("response", "Echo: hello")]


def test_forge_transforms_text_and_logs():
    engine = AgencyEngine()
    forged = engine.forge("artifact")
    assert forged == "ARTIFACT"
    assert engine.history == [("forge", "ARTIFACT")]


def test_reflect_summarizes_actions_and_tracks_history():
    engine = AgencyEngine()
    engine.generate_response("hi")
    engine.forge("test")
    reflection = engine.reflect()
    assert reflection == "Performed actions: response, forge."
    expected_history: List[Tuple[str, str]] = [
        ("response", "Echo: hi"),
        ("forge", "TEST"),
        ("reflect", "Performed actions: response, forge."),
    ]
    assert engine.history == expected_history
