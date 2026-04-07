"""Small string utility helpers used by tests.

This module provides simple convenience functions for string
transformations used in the example test codebase.
"""

def to_upper(text):
    """Return `text` converted to uppercase."""
    return text.upper()


def to_lower(text):
    """Return `text` converted to lowercase."""
    return text.lower()


def capitalize_words(text):
    """Capitalize the first letter of each word in `text`."""
    return " ".join(word.capitalize() for word in text.split())


def reverse_string(text):
    """Return `text` reversed."""
    return text[::-1]


def is_palindrome(text):
    """Return True if `text` is a palindrome (ignoring case and spaces)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]