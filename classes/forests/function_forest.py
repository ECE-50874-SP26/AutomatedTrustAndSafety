"""Container for function nodes and their relationships."""

from node.function_node import FunctionNode
from classes.ts_tag.tag import Tag
from typing import Dict


class FunctionForest:
    """Manage a mapping of function id -> `FunctionNode`.

    Utility methods make it convenient to add calls and attach tags.
    """
    def __init__(self) -> None:
        self.nodes: Dict[str, FunctionNode] = {}

    def get_or_create(self, func_id: str) -> FunctionNode:
        """Return the `FunctionNode` for `func_id`, creating it when missing."""
        if func_id not in self.nodes:
            self.nodes[func_id] = FunctionNode(id=func_id)
        return self.nodes[func_id]

    def add_call(self, caller: str, callee: str, confidence: float) -> None:
        """Record a call edge from `caller` to `callee` with `confidence`."""
        caller_node = self.get_or_create(caller)
        callee_node = self.get_or_create(callee)
        caller_node.add_child(callee_node, confidence)

    def add_tag(self, func_id: str, tag: Tag) -> None:
        """Attach `tag` to the function node identified by `func_id`."""
        node = self.get_or_create(func_id)
        node.add_tag(tag)