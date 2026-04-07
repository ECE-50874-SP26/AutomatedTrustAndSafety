# extraction/code_parser.py
import re
from .tag_parser import extract_tags
from .confidence import compute_call_confidence, compute_function_confidence
from classes.extraction.extraction_state import ExtractionState
from classes.ts_tag.function_info import FunctionInfo
from classes.ts_tag.tag import Tag
from typing import List

FUNC_DEF_KEYWORDS = ["def", "function", "sub", "void", "func"]
FUNC_DEF_REGEX = re.compile(
    r'\b(?:' + "|".join(FUNC_DEF_KEYWORDS) + r')\b\s+([a-zA-Z_][a-zA-Z0-9_]*)', re.IGNORECASE
)

CALL_REGEX = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b')

def remove_comments(line: str) -> str:
    line = re.sub(r'//.*', '', line)
    line = re.sub(r'#.*', '', line)
    return line

def parse_file(path: str, state: ExtractionState) -> None:
    with open(path, "r", errors="ignore") as f:
        lines = f.readlines()

    previous_tags: list[Tag] = []
    buffer_lines: List[str] = []

    for line in lines:
        tags = extract_tags(line)
        if tags:
            previous_tags = tags
            continue

        stripped = remove_comments(line).strip()
        if not stripped:
            continue

        buffer_lines.append(stripped)
        joined_line = " ".join(buffer_lines)

        func_match = FUNC_DEF_REGEX.search(joined_line)
        if func_match:
            func_name = func_match.group(1)
            state.current_function = func_name
            state.call_stack.append(func_name)

            if func_name not in state.functions:
                state.functions[func_name] = FunctionInfo(id=func_name)
            func_info = state.functions[func_name]

            for tag in previous_tags:
                func_info.tags.add(tag)
            previous_tags = []

            func_info.confidence = compute_function_confidence(bool(func_info.tags), func_name)

        if state.current_function:
            caller = state.current_function
            for callee_candidate in CALL_REGEX.findall(joined_line):
                if callee_candidate == caller:
                    continue

                if callee_candidate not in state.functions:
                    state.functions[callee_candidate] = FunctionInfo(id=callee_candidate)

                confidence = compute_call_confidence(caller, callee_candidate, joined_line)
                state.functions[caller].calls[callee_candidate] = confidence