"""Tests that a simple recursive function halts at its base case."""

def countdown(n: int) -> str:
    """Count down recursively until reaching zero.

    >>> countdown(0)
    'done'
    """
    if n <= 0:
        return "done"
    return countdown(n - 1)


def test_countdown_halts():
    """Ensure the recursive countdown stops at the base case."""
    assert countdown(3) == "done"
