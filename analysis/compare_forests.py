from classes.forests.tag_forest import TagForest
from classes.analysis.coverage_result import CoverageResult
from classes.analysis.coverage_stats import CoverageStats

def compare_forests(model: TagForest, observed: TagForest) -> CoverageResult:
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
        
    if result.total_stats.total > 0:
        result.total_stats.weighted_coverage /= result.total_stats.total

    for stats in result.action_stats.values():
        if stats.total > 0:
            stats.weighted_coverage /= stats.total
    
    for stats in result.category_stats.values():
        if stats.total > 0:
            stats.weighted_coverage /= stats.total
    
    for stats in result.subcategory_stats.values():
        if stats.total > 0:
            stats.weighted_coverage /= stats.total
        
    return result



        