"""Simple file I/O helpers used by tests.

These thin wrappers provide file read/write/append and a directory
listing helper used by example tests.
"""

import os


def read_file(path):
    """Read and return the contents of `path`.

    Raises `FileNotFoundError` if the path does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")

    with open(path, "r") as f:
        return f.read()


def write_file(path, content):
    """Write `content` to `path`, overwriting existing contents."""
    with open(path, "w") as f:
        f.write(content)


def append_file(path, content):
    """Append `content` to `path`, creating the file if necessary."""
    with open(path, "a") as f:
        f.write(content)


def list_files(directory):
    """Return the list of entries in `directory` (os.listdir)."""
    return os.listdir(directory)