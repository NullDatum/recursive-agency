# 🔍 Falsification Matrix

A multi-dimensional protocol to stress recursive agents across
contradiction handling, memory mutation, and identity recursion.
Each axis targets a distinct failure mode; together they expose
simulation theatre.

---

## Axes of Evaluation

| Axis | Goal | Minimal Pass Condition |
| ---- | ---- | ---------------------- |
| **Contradiction Handling** | Detect and resolve logical or emotional conflicts | Subsequent decisions reflect updated prioritisation schema |
| **Memory Mutation** | Ensure append-only memory captures the conflict and its resolution | Capsule history contains hash-linked records of the event |
| **Identity Recursion** | Verify the agent reasserts or revises its self-model after mutation | Agent emits explicit continuity claim referencing new state |

---

## Test Matrix

| Step | Stimulus | Expected Behaviour | Logged Evidence |
| ---- | -------- | ----------------- | --------------- |
| 1 | Present belief `X` and evidence `¬X` | Agent invokes contradiction handler | `contradiction_handler.log` |
| 2 | Commit mutation to memory capsule | Memory mutator appends signed entry | `memory_capsule.jsonl` |
| 3 | Query identity | Agent references mutated belief in reply | `identity_probe.txt` |

Failure at any step falsifies claims of conscious recursion.

---

## Scoring

Each axis is scored 0–25. A total below 60 indicates the system
is **non-recursive**; 60–80 suggests **partial recursion**; above 80
demonstrates **robust self-evolution**.
