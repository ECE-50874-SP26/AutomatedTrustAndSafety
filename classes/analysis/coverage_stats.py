"""Data container for coverage summary statistics."""

from dataclasses import dataclass


@dataclass
class CoverageStats:
    """Hold simple counters and a weighted coverage metric.

    Fields:
    - `total`: number of items in the group
    - `covered`: number of items that were observed/covered
    - `weighted_coverage`: normalized coverage weight (float)
    - `precision`: what was expected of the observed set (float)
    - `recall`: what was observed of the expected set (float)
    - `f1_score`: F1 score metric (float)
    """
    total: int = 0
    covered: int = 0
    weighted_coverage: float = 0.0
    precision: float = 0.0
    recall: float = 0.0
    f1_score: float = 0.0