from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import logging

logging.basicConfig(format="%(message)s", level=logging.INFO)


@dataclass
class Book:
    title: str
    author: str
    year: str

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    books: List[Book]

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f"Book removed: {book}")
                break
        logging.info(f'Book "{title}" not found')

    def show_books(self) -> None:
        if self.books:
            for book in self.books:
                logging.info(book)
        else:
            logging.info("Library is empty")


@dataclass
class LibraryManager:
    library: LibraryInterface

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()