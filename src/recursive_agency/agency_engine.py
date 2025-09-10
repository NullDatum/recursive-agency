"""Core agency engine implementing minimal recursive functions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class AgencyEngine:
    """Simple engine with response generation, forging, and reflection."""

    history: List[Tuple[str, str]] = field(default_factory=list)

    def generate_response(self, prompt: str) -> str:
        """Return a basic echo style response and log it."""
        response = f"Echo: {prompt}"
        self.history.append(("response", response))
        return response

    def forge(self, artifact: str) -> str:
        """Perform a trivial transform to simulate forging an artifact."""
        forged = artifact.upper()
        self.history.append(("forge", forged))
        return forged

    def reflect(self) -> str:
        """Produce a short summary of engine activity."""
        if not self.history:
            return "No activity recorded."
        actions = ", ".join(tag for tag, _ in self.history)
        reflection = f"Performed actions: {actions}."
        self.history.append(("reflect", reflection))
        return reflection
