"""Command-line entry used to analyze tag coverage across a codebase.

This script wires together the extraction, propagation and analysis
components to compute coverage statistics for a target directory.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "classes"))
sys.path.append(os.path.join(os.path.dirname(__file__), "analysis"))
sys.path.append(os.path.join(os.path.dirname(__file__), "extraction"))

from extraction.build_function_forest import build_function_forest
from analysis.build_tag_forest import build_tag_forest
from analysis.build_model_forest import build_model_forest
from analysis.compare_forests import compare_forests
from extraction.tag_propagation import propagate_tags
from classes.analysis.coverage_result import CoverageResult
from classes.analysis.coverage_stats import CoverageStats
from tabulate import tabulate


def print_summary_table(result: CoverageResult):
    """Print human readable summary tables for `result`.

    The function prints breakdowns by action, category and subcategory.
    """
    action_table: list[list[str | int | float]] = [
        [action, stats.total, stats.covered, round(stats.weighted_coverage, 5), round(stats.precision, 2), round(stats.recall, 2), round(stats.f1_score, 2)]
        for action, stats in result.action_stats.items()
    ]
    print("\n=== Coverage by Action ===")
    print(tabulate(action_table, headers=["Action", "Total", "Covered", "Weighted Coverage", "Precision", "Recall", "F1-Score"]))

    category_table: list[list[str | int | float]] = [
        [category, stats.total, stats.covered, round(stats.weighted_coverage, 5), round(stats.precision, 2), round(stats.recall, 2), round(stats.f1_score, 2)]
        for category, stats in result.category_stats.items()
    ]
    print("\n=== Coverage by Category ===")
    print(tabulate(category_table, headers=["Category", "Total", "Covered", "Weighted Coverage", "Precision", "Recall", "F1-Score"]))

    subcat_table: list[list[str | int | float]] = [
        [f"{cat}/{sub if sub else '-'}", stats.total, stats.covered, round(stats.weighted_coverage, 5), round(stats.precision, 2), round(stats.recall, 2), round(stats.f1_score, 2)]
        for (cat, sub), stats in result.subcategory_stats.items()
    ]
    print("\n=== Coverage by Subcategory ===")
    print(tabulate(subcat_table, headers=["Category/Subcategory", "Total", "Covered", "Weighted Coverage", "Precision", "Recall", "F1-Score"]))


def run_analysis(path: str):
    """Run the full extraction -> propagation -> comparison analysis.

    `path` should be the root of the codebase to scan.
    """
    print(f"Scanning codebase at: {path}\n")

    observed = build_function_forest(path)
    print(f"Discovered {len(observed.functions)} functions.\n")

    # Note: Removed propagation of tags to ensure coverage is based on absolute number of tags rather than inflated counts from propagation.    # propagate_tags(observed)
    # print(f"Propagated tags from caller to callee.")

    observed_tags = build_tag_forest(observed)
    print(f"Consolidated {len(observed_tags.nodes)} unique tags.\n")

    model_tags = build_model_forest()
    print(f"Loaded model forest with {len(model_tags.nodes)} tags.\n")

    result = compare_forests(model_tags, observed_tags)
    print("=== Overall Coverage ===")
    total_stats: CoverageStats = result.total_stats
    print(f"Total Tags: {total_stats.total}, Covered: {total_stats.covered}, "
          f"Weighted Coverage: {total_stats.weighted_coverage:.5f}")

    print_summary_table(result)


if __name__ == "__main__":
    path = input("Enter the path to your codebase: ").strip()
    run_analysis(path)