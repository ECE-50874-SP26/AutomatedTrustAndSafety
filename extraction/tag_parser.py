"""Utilities to parse inline Tag annotations from source lines.

This module looks for comments like `# Tag: action, category, subcategory`
or `// Tag: ...` and returns `Tag` objects for any matches.
"""

import re
from typing import List
from classes.ts_tag.tag import Tag

TAG_PATTERN = re.compile(r'(?://|#|/\*)\s*Tag:\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)(?:\s*,\s*([a-zA-Z0-9_]+))?')


def extract_tags(line: str) -> List[Tag]:
    """Extract zero or more `Tag` objects from `line`.

    Returns an empty list when no tag annotations are found.
    """
    tags: List[Tag] = []
    matches = TAG_PATTERN.findall(line)

    for action, category, subcategory in matches:
        tags.append(Tag(action, category, subcategory or None))

    return tags