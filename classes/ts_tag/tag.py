from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Tag:
    action: str
    category: str
    subcategory: str | None = None

    def normalize(self) -> tuple[str, str, str | None]:
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