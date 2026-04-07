from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Set
from ts_tag.tag import Tag

@dataclass
class FunctionNode:
    id: str = ""
    tags: Set[Tag] = field(default_factory=set[Tag])
    parents: Set["FunctionNode"] = field(default_factory=set["FunctionNode"])
    children: Dict["FunctionNode", float] = field(default_factory=dict["FunctionNode", float])

    def add_child(self, child: "FunctionNode", confidence: float) -> None:
        self.children[child] = confidence
        child.parents.add(self)
    
    def add_tag(self, tag: Tag) -> None:
        self.tags.add(tag)

    def __hash__(self) -> int:
        return hash(self.id)