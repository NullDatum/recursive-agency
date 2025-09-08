# Recursive Agency — Minimal Spec (v0.1)

**Definition.** A system has recursive agency iff it (a) maintains a self-model, (b) detects contradictions between predicted and observed states, (c) mutates its self-structure to resolve them, and (d) preserves identity continuity across mutations.

## Tests (must pass)
1. **Self-Reference Test (SRT):** The system can describe — in its own schema — how it updates that schema.
2. **Counterfactual Traceability (CT):** For a given mutation M, the system can replay the causal chain that led to M and simulate alternatives.
3. **Provenance Integrity (PI):** The system emits signed change-logs of internal structure mutations.
4. **Falsifiability (FAL):** The system exposes predictions that can be proven wrong by external tests.

A simulator that produces outputs without PI and SRT fails this spec.
