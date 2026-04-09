"""Walk a directory tree and parse supported files into an ExtractionState.

This function traverses `root_path`, finds files with supported
extensions and feeds them to `parse_file` for extraction.
"""

import os
from classes.extraction.extraction_state import ExtractionState
from .code_parser import parse_file

SUPPORTED_EXTENSIONS = (
    ".c", ".cpp", ".h", ".java", ".js", ".ts", ".go", ".rs", ".py", ".txt", ".bas", ".rb"
)


def build_function_forest(root_path: str) -> ExtractionState:
    """Return an `ExtractionState` populated by parsing files under `root_path`."""
    state = ExtractionState()
    print("Scanning:", root_path)
    print("Exists?", os.path.exists(root_path))
    print("Is directory?", os.path.isdir(root_path))
    print("Contents:", os.listdir(root_path))
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(SUPPORTED_EXTENSIONS):
                print(f"Parsing file: {os.path.join(dirpath, filename)}")
                file_path = os.path.join(dirpath, filename)
                parse_file(file_path, state)
                print(f"Finished parsing {filename}. Current function count: {len(state.functions)}")
    return state