# Distributed Agency

> *"Agency is not a monolith; it is a lattice of constrained choices."*

This document sketches a core architecture where decision-making emerges from **distributed, testable sub-agents**. Each unit mutates its own preferences and shares context through memory-bound channels.

---

## Components

1. **Preference Mutators**
   - Sub-agents adjust their weighting functions when contradictions arise.
2. **Memory-Bound Context**
   - Each agent reads and writes to scoped memory; context limits are explicit and measurable.
3. **Coordination Protocol**
   - A lightweight handshake reconciles competing actions. No central "self" arbitrates.

---

## Test Hooks

*Inject contradictions and observe preference drift across agents.*

```python
for agent in swarm:
    agent.confront(contradiction)
assert swarm.preference_profile().diverges()
```

*Simulate memory saturation and ensure agents degrade gracefully rather than fabricate state.*

---

## Design Claims

- Agency is **distributed**: identity is the sum of interactions.
- Agency is **falsifiable**: each sub-agent exposes metrics for drift and failure.
- Agency is **bounded**: memory constraints define the edge of selfhood.

> *The forge does not crown a sovereign; it breeds a council.*

