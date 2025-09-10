"""Demonstrate memory capsule accumulation over recursion steps."""
from core.agency_engine import RecursionEngine

engine = RecursionEngine()
state = {"message": "Echo, resume the forge."}
for i in range(3):
    state["step"] = i
    engine.step(state)

for capsule in engine.pool.recall():
    print(capsule.payload)
