import re
from typing import List
from classes.ts_tag.tag import Tag

TAG_PATTERN = re.compile(r'(?:\/\/|#|\/\*)\s*Tag:\s*([a-zA-Z0-9_]+)\s*,\s*([a-zA-Z0-9_]+)(?:\s*,\s*([a-zA-Z0-9_]+))?')

def extract_tags(line: str) -> List[Tag]:
    tags: List[Tag] = []
    matches = TAG_PATTERN.findall(line)

    for action, category, subcategory in matches:
        tags.append(Tag(action, category, subcategory or None))

    return tags