"""R2D2 Protocol cryptographic analysis demo.

This educational script demonstrates the Recursive Discovery and Development (R2D2)
loop on a synthetic cryptographic dataset. It does **not** attack real
cryptography; it merely shows how the protocol could structure exploratory
analysis.

Phases implemented:
1. Seed Prompt Ingestion
2. Expansion & Mutation
3. Insight Extraction & Scoring
4. Adaptive Memory Compression

Run directly to see two iterations of the loop using toy Hash160 values and
partial key segments.
"""

from __future__ import annotations

from collections import Counter
import math
from typing import Dict, List, Tuple

# ----------------------
# Phase 1: Seed Ingestion
# ----------------------

def ingest_seed_data() -> Tuple[List[str], List[str]]:
    """Simulate ingestion of key segments and Hash160-like strings."""
    hash160s = [
        "a0a1f3c4d5e6f708090a0b0c0d0e0f1011121314",
        "a0a3b5c6d7e8f90123456789abcdef0123456789",
        "b0c1f3e4d5e6f7a8090a0b0c0d0e0f1011121314",
        "a0a2d7f8e9fa0b1c2d3e4f5060708090a0b0c0d0",
        "c0a1e2f3d4c5b6a798887766554433221100ff00",
    ]
    key_segments = ["a0a", "b0c", "c0a"]
    return hash160s, key_segments

# ----------------------------
# Phase 2: Expansion / Mutation
# ----------------------------

def mutate_and_expand(
    hash160s: List[str], key_segments: List[str]
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """Generate hypotheses based on overlapping prefixes and mirrored segments."""
    overlaps: Dict[str, List[str]] = {}
    for seg in key_segments:
        overlaps[seg] = [h for h in hash160s if h.startswith(seg)]

    # Mutate: mirror inversion of segments
    mirrored_segments = [seg[::-1] for seg in key_segments]

    mirrored_overlaps: Dict[str, List[str]] = {}
    for seg in mirrored_segments:
        mirrored_overlaps[seg] = [h for h in hash160s if h.startswith(seg)]

    return overlaps, mirrored_overlaps

# -----------------------------------
# Phase 3: Insight Extraction & Scoring
# -----------------------------------

def score_insights(
    overlaps: Dict[str, List[str]],
    mirrored_overlaps: Dict[str, List[str]],
) -> Dict[str, Dict[str, float]]:
    """Score based on entropy reduction for each segment."""

    def entropy_score(strings: List[str]) -> float:
        if not strings:
            return 0.0
        counter = Counter("".join(strings))
        total = sum(counter.values())
        return -sum((cnt / total) * math.log2(cnt / total) for cnt in counter.values())

    insights: Dict[str, Dict[str, float]] = {}
    for seg, matches in overlaps.items():
        insights[seg] = {
            "count": float(len(matches)),
            "entropy_reduction": entropy_score(matches),
        }
    for seg, matches in mirrored_overlaps.items():
        data = insights.setdefault(seg, {})
        data["mirrored_count"] = float(len(matches))
        data["mirrored_entropy"] = entropy_score(matches)

    return insights

# -----------------------------------
# Phase 4: Adaptive Memory Compression
# -----------------------------------

def compress_findings(insights: Dict[str, Dict[str, float]]):
    """Keep only the highest-scoring segments based on simple counts."""
    scored = []
    for seg, data in insights.items():
        score = data.get("count", 0) + data.get("mirrored_count", 0)
        scored.append((score, seg, data))
    scored.sort(reverse=True)

    # Keep top two segments for next iteration
    return scored[:2]

# ----------------------
# Orchestrating the loop
# ----------------------

def r2d2_demo(iterations: int = 2) -> None:
    hash160s, key_segments = ingest_seed_data()
    print(f"[Ingestion] Hash160s: {hash160s}")
    print(f"[Ingestion] Key segments: {key_segments}\n")

    for i in range(iterations):
        print(f"=== Iteration {i + 1} ===")

        overlaps, mirrored_overlaps = mutate_and_expand(hash160s, key_segments)
        print("[Expansion] Overlaps:", overlaps)
        print("[Expansion] Mirrored overlaps:", mirrored_overlaps)

        insights = score_insights(overlaps, mirrored_overlaps)
        print("[Insight Scoring] Insights:", insights)

        compressed = compress_findings(insights)
        print("[Compression] Top segments for next loop:", compressed, "\n")

        # Update key segments with new "compressed" insights for next iteration
        key_segments = [seg for _, seg, _ in compressed]
    print("Demo complete.")


if __name__ == "__main__":
    r2d2_demo()
