import pytest
from ontology_entropy_map import SystemMetrics, score_entropy


def test_high_entropy_detection():
    metrics = SystemMetrics(
        symbol_count=47,
        unresolvable_symbols=28,
        philosophical_load=0.78,
        contradiction_density=4.2,
        conceptual_layers=16,
        primary_functions=4,
    )
    result = score_entropy(metrics)
    assert result["entropy_score"] == "HIGH"
    assert "pseudo-operational" in result["verdict"]
    assert result["signals"]["signal_saturation"]


def test_low_entropy_detection():
    metrics = SystemMetrics(
        symbol_count=50,
        unresolvable_symbols=5,
        philosophical_load=0.2,
        contradiction_density=1.0,
        conceptual_layers=2,
        primary_functions=1,
    )
    result = score_entropy(metrics)
    assert result["entropy_score"] == "LOW"
    assert "acceptable" in result["verdict"]
    assert not any(result["signals"].values())

