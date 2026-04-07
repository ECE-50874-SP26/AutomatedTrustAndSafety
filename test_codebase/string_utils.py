def to_upper(text):
    return text.upper()


def to_lower(text):
    return text.lower()


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]