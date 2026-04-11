"""Parse source files to discover functions, tags and call relationships.

This lightweight parser uses regular expressions to locate function
definitions and tentative call sites. It also supports reading tag
annotations from preceding comment lines (via `extract_tags`).
"""

import re
from .tag_parser import extract_tags
from .confidence import compute_call_confidence, compute_function_confidence
from classes.extraction.extraction_state import ExtractionState
from classes.ts_tag.function_info import FunctionInfo
from classes.ts_tag.tag import Tag
from typing import List

# Keywords commonly used to declare functions across multiple languages.
FUNC_DEF_KEYWORDS = ["def", "function", "sub", "void", "func", "fn", "procedure", "method", "public", "private", "protected", "static"]

# Simple regex to capture a following identifier after a function keyword.
FUNC_DEF_REGEX = re.compile(
    r'\b(?:' + "|".join(FUNC_DEF_KEYWORDS) + r')\b'
    r'(?:\s+\w+)*?'
    r'\s+([a-zA-Z_][a-zA-Z0-9_]*)',
    re.IGNORECASE
)

# Find potential identifier tokens which may indicate call candidates.
CALL_REGEX = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b')


def remove_comments(line: str) -> str:
    """Strip common single-line comment markers from `line`.

    Only simple patterns are removed (C/CPP-style `//` and `#`).
    """
    line = re.sub(r'//.*', '', line)
    line = re.sub(r'#.*', '', line)
    return line

def completed_signature(joined_line: str) -> bool:
    """Heuristic to determine if `joined_line` likely contains a complete function signature.

    This is a simple check for balanced parentheses, which may indicate the end of a
    function declaration in many languages. It is not foolproof but can help reduce
    false positives when parsing multi-line signatures.
    """
    open_count = joined_line.count('(')
    if open_count == 0:
        return True  # No parentheses, likely a simple signature
    return joined_line.count(')' ) >= open_count


def parse_file(path: str, state: ExtractionState) -> None:
    """Parse `path`, updating `state` with detected functions and calls.

    The parser reads the file line-by-line, collects tag annotations that
    directly precede a function definition, and heuristically identifies
    call sites to record call confidences in the `ExtractionState`.
    """
    with open(path, "r", errors="ignore") as f:
        lines = f.readlines()

    previous_tags: list[Tag] = []
    signature_buffer: List[str] = []
    in_signature: bool = False

    for line in lines:
        # Collect inline Tag annotations (e.g. "# Tag: action, category")
        tags = extract_tags(line)
        if tags:
            previous_tags.extend(tags)
            continue

        # Remove comments and skip empty lines
        stripped = remove_comments(line).strip()
        if not stripped:
            if not in_signature:
                previous_tags = []
            signature_buffer = []
            in_signature = False
            continue

        signature_buffer.append(stripped)
        joined_line = " ".join(signature_buffer)

        if not in_signature and FUNC_DEF_REGEX.search(joined_line):
            in_signature = True

        if not in_signature:
            # If we are inside a function, look for call candidates
            if state.current_function:
                caller = state.current_function
                for callee_candidate in CALL_REGEX.findall(joined_line):
                    if callee_candidate == caller:
                        continue

                    if callee_candidate not in state.functions:
                        state.functions[callee_candidate] = FunctionInfo(id=callee_candidate)

                    confidence = compute_call_confidence(caller, callee_candidate, joined_line)
                    state.functions[caller].calls[callee_candidate] = confidence
                
                signature_buffer = [stripped]
                continue
        
        if not completed_signature(joined_line):
            continue

        # Detect a function definition in the accumulated buffer
        func_match = FUNC_DEF_REGEX.search(joined_line)
        if func_match:
            func_name = func_match.group(1)
            # Added this line so that tags from different functions with the same name aren't conflated with each other and wrongfully skipped.
            func_name += f" ({path})"  # Append file path for disambiguation
            state.current_function = func_name
            state.call_stack.append(func_name)

            if func_name not in state.functions:
                state.functions[func_name] = FunctionInfo(id=func_name)
            func_info = state.functions[func_name]

            # Attach any tags previously collected to this function
            for tag in previous_tags:
                func_info.tags.add(tag)
                func_info.tag_weights[tag] = 1.0
            previous_tags = []

            func_info.confidence = compute_function_confidence(bool(func_info.tags), func_name)
        
        signature_buffer = []
        in_signature = False

        