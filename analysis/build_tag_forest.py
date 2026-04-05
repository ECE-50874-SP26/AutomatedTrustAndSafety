from typing import Set
from classes.extraction.extraction_state import ExtractionState
from classes.ts_tag.function_info import FunctionInfo
from classes.forests.tag_forest import TagForest

def search_functions(state: ExtractionState, forest: TagForest, func: FunctionInfo, visited: Set[str]) -> None:
    if func.id in visited:
        return
    
    visited.add(func.id)

    for tag in func.tags:
        forest.add_tag(tag)
    
    for callee_id in func.calls.keys():
        callee = state.functions.get(callee_id)
        if callee:
            search_functions(state, forest, callee, visited)

def build_tag_forest(state: ExtractionState) ->  TagForest:
    forest = TagForest()
    visited: Set[str] = set()

    for func in state.functions.values():
        search_functions(state, forest, func, visited)
    
    return forest
