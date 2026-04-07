from dataclasses import dataclass, field
from typing import Dict
from node.tag_node import TagNode
from classes.ts_tag.tag import Tag

@dataclass
class TagForest:
    nodes: Dict[tuple[str, str, str | None], TagNode] = field(default_factory=dict[tuple[str, str, str | None], TagNode])

    def add_tag(self, tag: Tag) -> None:
        key = tag.normalize()
        if key not in self.nodes:
            self.nodes[key] = TagNode(tag=tag, count=0)
        self.nodes[key].count += 1