from dataclasses import dataclass, field
from typing import Dict, Set
from .tag import Tag

@dataclass
class FunctionInfo:
    id: str
    confidence: float = 0.0
    calls: Dict[str, float] = field(default_factory=dict[str, float])
    tags: Set[Tag] = field(default_factory=set[Tag])