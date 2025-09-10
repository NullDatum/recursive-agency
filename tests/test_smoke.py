def test_smoke():
    assert True

def test_air_principle_exists():
    from pathlib import Path
    assert (Path(__file__).parents[1] / "LICENSE_AIR.md").exists()
