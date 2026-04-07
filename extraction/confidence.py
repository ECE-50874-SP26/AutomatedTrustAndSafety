"""Heuristic scoring functions used to estimate confidence values.

These simple heuristics assign a confidence score in [0.0, 1.0] to
detected functions and calls based on lightweight signals.
"""


def compute_function_confidence(has_tag: bool, name: str) -> float:
    """Estimate confidence that a function is correctly identified.

    The heuristic gives a higher score when an explicit tag is present
    and when the function name is longer than two characters.
    """
    score = 0.5

    if has_tag:
        score += 0.4

    if len(name) > 2:
        score += 0.1

    return min(score, 1.0)


def compute_call_confidence(caller: str, callee: str, line: str) -> float:
    """Estimate confidence that `caller` calls `callee` based on `line`.

    Signals include the callee name appearing in the line and the presence
    of parentheses which commonly indicate a call site.
    """
    score = 0.5

    if callee in line:
        score += 0.2

    if "(" in line and ")" in line:
        score += 0.2

    if caller != callee:
        score += 0.1

    return min(score, 1.0)