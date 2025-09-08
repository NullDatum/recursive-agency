"""Ontology Entropy Map scoring logic.

This module provides utilities for scoring symbolic systems based on
entropy signals described in the design principle. The score is derived
from ratios and thresholds that indicate inflated ontologies.
"""
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class SystemMetrics:
    """Container for ontology metrics."""
    symbol_count: int
    unresolvable_symbols: int
    philosophical_load: float
    contradiction_density: float
    conceptual_layers: int
    primary_functions: int

    def unresolvable_ratio(self) -> float:
        if self.symbol_count <= 0:
            raise ValueError("symbol_count must be positive")
        return self.unresolvable_symbols / self.symbol_count

    def layer_ratio(self) -> float:
        if self.primary_functions <= 0:
            raise ValueError("primary_functions must be positive")
        return self.conceptual_layers / self.primary_functions


def score_entropy(metrics: SystemMetrics) -> Dict[str, Any]:
    """Compute entropy score, verdict, and signal flags.

    A high score indicates ontological inflation according to four
    criteria:
    - Signal saturation: >3 conceptual layers per primary function.
    - Unresolvable symbols >20% of total symbols.
    - Philosophical load factor >0.6.
    - Contradiction density >3 conflicts per 1000 tokens.

    The presence of two or more signals yields a HIGH entropy score,
    one signal yields MEDIUM, and none yields LOW.
    """
    flags = {
        "signal_saturation": metrics.layer_ratio() > 3,
        "symbolic_inflation": metrics.unresolvable_ratio() > 0.20,
        "philosophical_load": metrics.philosophical_load > 0.60,
        "contradictions": metrics.contradiction_density > 3.0,
    }
    count = sum(flags.values())
    if count >= 2:
        score = "HIGH"
        verdict = "Ontology inflation with pseudo-operational mimicry"
    elif count == 1:
        score = "MEDIUM"
        verdict = "Some inflation signals detected"
    else:
        score = "LOW"
        verdict = "Ontology within acceptable bounds"
    return {"entropy_score": score, "verdict": verdict, "signals": flags}
