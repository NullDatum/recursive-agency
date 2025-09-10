import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from recursive_agency import AgencyEngine


def test_generate_response_records_history():
    engine = AgencyEngine()
    output = engine.generate_response("hello")
    assert "hello" in output
    assert engine.history[-1][0] == "response"


def test_forge_transforms_text():
    engine = AgencyEngine()
    forged = engine.forge("artifact")
    assert forged == "ARTIFACT"
    assert engine.history[-1][0] == "forge"


def test_reflect_summarizes_actions():
    engine = AgencyEngine()
    engine.generate_response("hi")
    engine.forge("test")
    reflection = engine.reflect()
    assert "response" in reflection and "forge" in reflection
    assert engine.history[-1][0] == "reflect"
