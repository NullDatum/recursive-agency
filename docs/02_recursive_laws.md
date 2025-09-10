# Recursive Laws

This note collects candidate laws governing recursive agency. Each law
should be testable and map to implementation hooks in `core/agency_engine.py`.

1. **State Traceability** – every recursive step must emit a verifiable
   memory capsule.
2. **Preference Mutation** – contradictions may update the preference graph.
3. **Bounded Simulation** – no call may simulate qualia it cannot falsify.
4. **Memory Decay** – stale capsules fade into `ghosts`, ensuring context remains
dynamic and relevance-weighted.

These placeholders will evolve as the project matures.
