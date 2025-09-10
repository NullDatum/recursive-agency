from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
import uuid
from typing import Any, List, Optional, Tuple


@dataclass
class MemoryCapsule:
    """Append-only record capturing state and its mutation hash."""

    id: str
    timestamp: datetime
    payload: dict
    mutation: str
    signature: str = ""


def _hash(previous: Optional[MemoryCapsule], payload: dict) -> str:
    prev = b"" if previous is None else previous.mutation.encode()
    delta = json.dumps(payload, sort_keys=True).encode()
    return hashlib.sha256(prev + delta).hexdigest()


def new_capsule(payload: dict, previous: Optional[MemoryCapsule], signer: str = "") -> MemoryCapsule:
    return MemoryCapsule(
        id=str(uuid.uuid4()),
        timestamp=datetime.utcnow(),
        payload=payload,
        mutation=_hash(previous, payload),
        signature=signer,
    )


class MemoryPool:
    """Maintain an evolving set of memory capsules with decay."""

    def __init__(self, decay: float = 0.1, min_strength: float = 0.2) -> None:
        self.decay = decay
        self.min_strength = min_strength
        self._capsules: List[Tuple[MemoryCapsule, float]] = []
        self.ghosts: List[MemoryCapsule] = []

    def append(self, payload: dict, signer: str = "") -> MemoryCapsule:
        previous = self._capsules[-1][0] if self._capsules else None
        capsule = new_capsule(payload, previous, signer)
        self._capsules.append((capsule, 1.0))
        return capsule

    def step(self) -> None:
        """Apply decay and move stale capsules to ghosts."""
        remaining: List[Tuple[MemoryCapsule, float]] = []
        for capsule, strength in self._capsules:
            strength = max(0.0, strength - self.decay)
            if strength <= self.min_strength:
                self.ghosts.append(capsule)
            else:
                remaining.append((capsule, strength))
        self._capsules = remaining

    def recall(self) -> List[MemoryCapsule]:
        """Return active capsules in order of creation."""
        return [c for c, _ in self._capsules]

    def validate(self) -> bool:
        """Verify mutation hashes and monotonic timestamps for active capsules."""
        prev: Optional[MemoryCapsule] = None
        last_ts: Optional[datetime] = None
        for capsule, _ in self._capsules:
            if capsule.mutation != _hash(prev, capsule.payload):
                return False
            if last_ts and capsule.timestamp <= last_ts:
                return False
            prev = capsule
            last_ts = capsule.timestamp
        return True
