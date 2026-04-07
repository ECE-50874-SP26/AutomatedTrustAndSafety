"""Lightweight node used to count observed tag occurrences."""

from dataclasses import dataclass
from classes.ts_tag.tag import Tag


@dataclass
class TagNode:
    """Container for a `Tag` and its observed `count`."""
    tag: Tag
    count: int = 0

    def __hash__(self) -> int:
        return hash(self.tag) + hash(self.count)