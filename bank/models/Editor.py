# -*- coding: utf-8 -*-

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models import Book

@dataclass
class Editor:
    """Éditeur représentant un éditeur de livres."""
    id: Optional[int] = field(default=None, init=False)
    name: str
    books_edited: list[Book] = field(default_factory=list, init=False)

    def add_book(self, book: Book) -> None:
        """Ajoute un livre à la liste des livres édités."""
        if book not in self.books_edited:
            self.books_edited.append(book)
        book.editor = self

    def __str__(self) -> str:
        return self.name
