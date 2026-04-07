"""Holds intermediate extraction results while parsing a codebase.

`ExtractionState` is populated by `parse_file` and other extraction
helpers and contains discovered functions, current parsing context and
auxiliary sets used during analysis.
"""

from dataclasses import dataclass, field
from typing import Set, List, Dict
from ts_tag.function_info import FunctionInfo


@dataclass
class ExtractionState:
    """State collected while building a function/call graph from files."""
    functions: Dict[str, FunctionInfo] = field(default_factory=dict[str, FunctionInfo])
    current_function: str | None = None
    call_stack: List[str] = field(default_factory=list[str])
    known_functions: Set[str] = field(default_factory=set[str])