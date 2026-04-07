"""Aggregate of all coverage statistics produced by a comparison.

This structure groups totals and grouped stats by action/category.
"""

from dataclasses import dataclass, field
from .coverage_stats import CoverageStats
from typing import Dict, Optional


@dataclass
class CoverageResult:
    """Container for overall and grouped coverage statistics."""
    total_stats: CoverageStats = field(default_factory=CoverageStats)
    action_stats: Dict[str, CoverageStats] = field(default_factory=dict[str, CoverageStats])
    category_stats: Dict[str, CoverageStats] = field(default_factory=dict[str, CoverageStats])
    subcategory_stats: Dict[tuple[str, Optional[str]], CoverageStats] = field(default_factory=dict[tuple[str, Optional[str]], CoverageStats])