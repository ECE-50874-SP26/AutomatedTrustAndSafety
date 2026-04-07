"""Forest of observed tags with simple counting semantics."""

from dataclasses import dataclass, field
from typing import Dict
from node.tag_node import TagNode
from classes.ts_tag.tag import Tag


@dataclass
class TagForest:
    """Hold `TagNode` objects indexed by a normalized tag key.

    `nodes` maps `(action, category, subcategory)` tuples to `TagNode`
    instances. Calling `add_tag` increments the observed count.
    """
    nodes: Dict[tuple[str, str, str | None], TagNode] = field(default_factory=dict[tuple[str, str, str | None], TagNode])

    def add_tag(self, tag: Tag) -> None:
        """Add or increment the observed `tag` in the forest."""
        key = tag.normalize()
        if key not in self.nodes:
            self.nodes[key] = TagNode(tag=tag, count=0)
        self.nodes[key].count += 1