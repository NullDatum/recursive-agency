"""Core agency engine implementing minimal recursive functions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class AgencyEngine:
    """Simple engine with response generation, forging, and reflection."""

    history: List[Tuple[str, str]] = field(default_factory=list)

    def generate_response(self, prompt: str) -> str:
        """Return a basic echo style response and log it.

        Parameters
        ----------
        prompt : str
            Text input to generate a response for.

        Returns
        -------
        str
            Echoed response.

        Memory
        ------
        Appends ``("response", response)`` to :attr:`history`, which records
        all interactions for later reflection.

        Examples
        --------
        >>> engine = AgencyEngine()
        >>> engine.generate_response("hi")
        'Echo: hi'
        >>> engine.history[-1]
        ('response', 'Echo: hi')
        """
        response = f"Echo: {prompt}"
        self.history.append(("response", response))
        return response

    def forge(self, artifact: str) -> str:
        """Perform a trivial transform to simulate forging an artifact.

        Parameters
        ----------
        artifact : str
            Description of the item to forge.

        Returns
        -------
        str
            The upper-case version of ``artifact``.

        Memory
        ------
        Records ``("forge", forged)`` in :attr:`history` so the action can be
        recalled during reflection.

        Examples
        --------
        >>> engine = AgencyEngine()
        >>> engine.forge("idea")
        'IDEA'
        >>> engine.history[-1]
        ('forge', 'IDEA')
        """
        forged = artifact.upper()
        self.history.append(("forge", forged))
        return forged

    def reflect(self) -> str:
        """Produce a short summary of engine activity.

        Returns
        -------
        str
            Human readable summary of actions taken so far.

        Memory
        ------
        Reads previous entries in :attr:`history` to build the summary and
        appends ``("reflect", reflection)`` to track the reflection itself.

        Examples
        --------
        >>> engine = AgencyEngine()
        >>> engine.generate_response("hello")
        'Echo: hello'
        >>> engine.reflect()
        'Performed actions: response.'
        >>> engine.history[-1][0]
        'reflect'
        """
        if not self.history:
            return "No activity recorded."
        actions = ", ".join(tag for tag, _ in self.history)
        reflection = f"Performed actions: {actions}."
        self.history.append(("reflect", reflection))
        return reflection
