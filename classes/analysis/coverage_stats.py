from dataclasses import dataclass

@dataclass
class CoverageStats:
    total: int = 0
    covered: int = 0
    weighted_coverage: float = 0.0