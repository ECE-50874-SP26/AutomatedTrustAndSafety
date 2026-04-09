"""Propagate tag weights along the call graph.

Weights from callee functions are propagated back to callers using a decay
factor and the confidence of the call relationship.
"""

from typing import Set
from classes.extraction.extraction_state import ExtractionState
from classes.ts_tag.function_info import FunctionInfo

DECAY_FACTOR = 0.8


def search_function_calls(state: ExtractionState, func: FunctionInfo, visited: Set[str]) -> None:
    """Recursively propagate tag weights from `func`'s callees back to `func`.

    `visited` prevents revisiting nodes in cyclic graphs.
    """
    if func.id in visited:
        return

    visited.add(func.id)

    # Ensure tags directly on the function are kept at weight 1.0
    for tag in func.tags:
        func.tag_weights[tag] = max(func.tag_weights.get(tag, 0.0), 1.0)

    # Iterate callee id and the call confidence
    for callee_id, call in func.calls.items():
        callee: FunctionInfo | None = state.functions.get(callee_id)

        if not callee:
            continue

        search_function_calls(state, callee, visited)

        for tag, weight in callee.tag_weights.items():
            propagated_weight = weight * call * DECAY_FACTOR

            if propagated_weight <= 0:
                continue

            existing_weight = func.tag_weights.get(tag, 0.0)
            if propagated_weight > existing_weight:
                func.tag_weights[tag] = propagated_weight
                func.tags.add(tag)


def propagate_tags(state: ExtractionState) -> None:
    """Propagate tag weights for all functions in `state`.

    This initializes a traversal from each function; internal `visited`
    tracking prevents redundant work.
    """
    for func in state.functions.values():
        search_function_calls(state, func, set())