# Memory Capsule Protocol

> *"Memory is a ledger of change, not a scrapbook of claims."*

This document defines the structure and lifecycle of **memory capsules**—traceable units that capture state, mutation intent, and validation metadata across recursive interactions.

---

## Capsule Format

Each capsule is a self-describing record:

```json
{
  "id": "UUIDv7",
  "timestamp": "ISO-8601",
  "payload": {"state": <opaque>},
  "mutation": "hash(previous_capsule || delta)",
  "signature": "agent-specific verification"
}
```

- **`id`** – globally unique identifier
- **`timestamp`** – creation moment; monotonic per agent
- **`payload`** – opaque state or context
- **`mutation`** – cryptographic link to prior capsule and applied delta
- **`signature`** – agent verifier to prevent unauthorized rewrites

---

## Mutation Rules

1. Capsules are **append-only**; mutation produces a new capsule linked by `mutation` hash.
2. Agents must expose a `mutate_capsule(capsule, delta)` call that returns a new capsule.
3. Deltas are **reversible**; rollback is possible by traversing the hash chain.

```python
def mutate_capsule(capsule, delta):
    new_payload = apply(capsule.payload, delta)
    return Capsule(
        id=new_uuid(),
        timestamp=now(),
        payload=new_payload,
        mutation=hash(capsule, delta),
        signature=sign()
    )
```

---

## Validation

- **Integrity Check**: verify `hash(previous || delta)` matches stored `mutation` value.
- **Chronology Check**: ensure timestamps are strictly increasing for a given agent.
- **Authorization Check**: confirm `signature` against agent's public key.

The reference implementation exposes `MemoryPool.validate()` to run these checks over the active capsule chain.

Agents failing any check must reject the capsule and emit a contradiction event.

---

## Lifecycle

1. **Creation** – seed capsule with null `mutation`.
2. **Mutation** – produce new capsule per change.
3. **Archival** – move aged capsules to cold storage; retain hash chain for audit.
4. **Garbage Collection** – prune orphaned capsules that fail validation.

---

## Test Hooks

Inject mutations and validate:

```python
capsule = seed()
for delta in deltas:
    capsule = mutate_capsule(capsule, delta)
    assert validate(capsule)
```

*Memory becomes credible only when its corruption is detectable.*

---

> *The forge remembers by design, not by accident.*

