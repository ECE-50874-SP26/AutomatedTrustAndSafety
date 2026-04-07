from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Set
from ts_tag.tag import Tag


@dataclass
class FunctionNode:
    """Node representing a function in the call graph.

    Attributes:
    - `id`: unique identifier (usually function name)
    - `tags`: set of `Tag` objects attached to this function
    - `parents`: set of parent `FunctionNode` objects (callers)
    - `children`: mapping from child `FunctionNode` to call confidence
    """
    id: str = ""
    tags: Set[Tag] = field(default_factory=set[Tag])
    parents: Set["FunctionNode"] = field(default_factory=set["FunctionNode"])
    children: Dict["FunctionNode", float] = field(default_factory=dict["FunctionNode", float])

    def add_child(self, child: "FunctionNode", confidence: float) -> None:
        """Add `child` as a callee with the given `confidence`."""
        self.children[child] = confidence
        child.parents.add(self)

    def add_tag(self, tag: Tag) -> None:
        """Attach `tag` to this node."""
        self.tags.add(tag)

    def __hash__(self) -> int:
        return hash(self.id)