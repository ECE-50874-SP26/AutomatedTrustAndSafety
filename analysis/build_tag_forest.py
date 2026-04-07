"""Build a TagForest by traversing extracted functions.

This module walks the call graph in `ExtractionState` and collects all
tags found on reachable functions into a `TagForest` structure.
"""

from typing import Set
from classes.extraction.extraction_state import ExtractionState
from classes.ts_tag.function_info import FunctionInfo
from classes.forests.tag_forest import TagForest


def search_functions(state: ExtractionState, forest: TagForest, func: FunctionInfo, visited: Set[str]) -> None:
    """Recursively visit `func` and its callees, adding tags to `forest`.

    `visited` prevents infinite recursion on cycles.
    """
    if func.id in visited:
        return

    visited.add(func.id)

    for tag in func.tags:
        forest.add_tag(tag)

    for callee_id in func.calls.keys():
        callee = state.functions.get(callee_id)
        if callee:
            search_functions(state, forest, callee, visited)


def build_tag_forest(state: ExtractionState) -> TagForest:
    """Return a `TagForest` containing all tags reachable from `state`.

    The traversal starts at every discovered function to ensure disconnected
    components are included.
    """
    forest = TagForest()
    visited: Set[str] = set()

    for func in state.functions.values():
        search_functions(state, forest, func, visited)

    return forest
