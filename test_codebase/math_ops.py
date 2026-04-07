"""Basic math operations used in the example test codebase.

These helpers are intentionally simple implementations for tests.
"""

def add(a, b):
    """Return the sum of `a` and `b`."""
    return a + b


def subtract(a, b):
    """Return the difference `a - b`."""
    return a - b


def multiply(a, b):
    """Return the product of `a` and `b`."""
    return a * b


def divide(a, b):
    """Return `a / b`. Raises `ValueError` if `b` is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def factorial(n):
    """Compute factorial of `n` recursively.

    Raises `ValueError` for negative inputs.
    """
    if n < 0:
        raise ValueError("Negative input")
    if n == 0:
        return 1
    return n * factorial(n - 1)