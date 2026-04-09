"""Compare the model tag forest with observed tags and compute coverage.

The comparison walks the model's tag nodes and checks whether each tag
is present in the observed forest, aggregating counts and computing
weighted coverage statistics.
"""

from classes.forests.tag_forest import TagForest
from classes.analysis.coverage_result import CoverageResult
from classes.analysis.coverage_stats import CoverageStats

DEPTH_WEIGHTS = {"action": 1.0, "category": 2.0, "subcategory": 3.0}

def compute_precision_recall_f1(stats: CoverageStats, observed_total: int) -> None:
    stats.precision = stats.covered / observed_total if observed_total > 0 else 0.0
    stats.recall = stats.covered / stats.total if stats.total > 0 else 0.0
    stats.f1_score = 2 * (stats.precision * stats.recall) / (stats.precision + stats.recall) if (stats.precision + stats.recall) > 0 else 0.0


def compare_forests(model: TagForest, observed: TagForest) -> CoverageResult:
    """Return a `CoverageResult` comparing `model` against `observed`.

    For every tag in `model`, increment totals and, when present in
    `observed`, add coverage counts which are later normalized to
    produce weighted coverage values.
    """
    result = CoverageResult()

    for key, _ in model.nodes.items():
        action, category, subcategory = key
        observed_node = observed.nodes.get(key)

        result.total_stats.total += 1

        if action not in result.action_stats:
            result.action_stats[action] = CoverageStats(total=0, covered=0, weighted_coverage=0.0)
        result.action_stats[action].total += 1

        if category not in result.category_stats:
            result.category_stats[category] = CoverageStats()
        result.category_stats[category].total += 1

        subkey = (category, subcategory)
        if subkey not in result.subcategory_stats:
            result.subcategory_stats[subkey] = CoverageStats()
        result.subcategory_stats[subkey].total += 1

        if observed_node:
            result.total_stats.covered += 1
            result.total_stats.weighted_coverage += observed_node.count

            result.action_stats[action].covered += 1
            result.action_stats[action].weighted_coverage += observed_node.count

            result.category_stats[category].covered += 1
            result.category_stats[category].weighted_coverage += observed_node.count

            result.subcategory_stats[subkey].covered += 1
            result.subcategory_stats[subkey].weighted_coverage += observed_node.count

    # Normalize weighted coverage values by their totals
    if result.total_stats.total > 0:
        result.total_stats.weighted_coverage /= result.total_stats.total
        compute_precision_recall_f1(result.total_stats, result.total_stats.covered)

    for action, stats in result.action_stats.items():
        if stats.total > 0:
            stats.weighted_coverage = (stats.weighted_coverage / stats.total) * DEPTH_WEIGHTS["action"]
        compute_precision_recall_f1(stats, result.action_stats[action].covered)

    for category, stats in result.category_stats.items():
        if stats.total > 0:
            stats.weighted_coverage = (stats.weighted_coverage / stats.total) * DEPTH_WEIGHTS["category"]
        compute_precision_recall_f1(stats, result.category_stats[category].covered)

    for subkey, stats in result.subcategory_stats.items():
        if stats.total > 0:
            stats.weighted_coverage = (stats.weighted_coverage / stats.total) * DEPTH_WEIGHTS["subcategory"]
        compute_precision_recall_f1(stats, result.subcategory_stats[subkey].covered)

    return result