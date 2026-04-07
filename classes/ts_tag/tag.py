"""Representation of a tag with normalization helpers."""

from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Tag:
    """Immutable tag value object.

    Fields:
    - `action`: primary action name
    - `category`: category the action belongs to
    - `subcategory`: optional subcategory
    """
    action: str
    category: str
    subcategory: str | None = None

    def normalize(self) -> tuple[str, str, str | None]:
        """Return a normalized key tuple suitable for dictionary indexing.

        Normalization lowercases and strips surrounding whitespace.
        """
        subcat = self.subcategory
        if subcat:
            subcat = subcat.strip().lower()
        return (
            self.action.strip().lower(),
            self.category.strip().lower(),
            subcat,
        )

    def __hash__(self) -> int:
        return hash(self.action) + hash(self.category) + hash(self.subcategory)