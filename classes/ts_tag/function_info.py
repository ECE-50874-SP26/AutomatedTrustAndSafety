"""Metadata collected for each discovered function during extraction."""

from dataclasses import dataclass, field
from typing import Dict, Set
from .tag import Tag


@dataclass
class FunctionInfo:
    """Store function id, confidence, call map, tags and tag weights."""
    id: str
    confidence: float = 0.0
    calls: Dict[str, float] = field(default_factory=dict[str, float])
    tag_weights: Dict[Tag, float] = field(default_factory=dict[Tag, float])
    tags: Set[Tag] = field(default_factory=set[Tag])