def compute_function_confidence(has_tag: bool, name: str) -> float:
    score = 0.5

    if has_tag:
        score += 0.4

    if len(name) > 2:
        score += 0.1

    return min(score, 1.0)

def compute_call_confidence(caller: str, callee: str, line: str) -> float:
    score = 0.5

    if callee in line:
        score += 0.2

    if "(" in line and ")" in line:
        score += 0.2

    if caller != callee:
        score += 0.1

    return min(score, 1.0)