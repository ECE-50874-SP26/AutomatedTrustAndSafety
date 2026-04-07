from dataclasses import dataclass
from classes.ts_tag.tag import Tag

@dataclass
class TagNode:
    tag: Tag
    count: int = 0

    def __hash__(self) -> int:
        return hash(self.tag) + hash(self.count)