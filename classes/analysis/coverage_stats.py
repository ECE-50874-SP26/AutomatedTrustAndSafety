"""Data container for coverage summary statistics."""

from dataclasses import dataclass


@dataclass
class CoverageStats:
    """Hold simple counters and a weighted coverage metric.

    Fields:
    - `total`: number of items in the group
    - `covered`: number of items that were observed/covered
    - `weighted_coverage`: normalized coverage weight (float)
    """
    total: int = 0
    covered: int = 0
    weighted_coverage: float = 0.0