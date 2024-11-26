from typing import List, Dict

from constants import (
    STATUS_AVAILABLE, STATUS_ISSUED,
    MSG_ENTER_BOOK_TITLE, MSG_ENTER_BOOK_AUTHOR, MSG_ENTER_BOOK_YEAR,
    MSG_BOOK_ADDED, MSG_ID_MUST_BE_NUMBER, MSG_ENTER_BOOK_ID_REMOVE,
    MSG_BOOK_REMOVED, MSG_BOOK_NOT_FOUND, MSG_ENTER_QUERY, MSG_BOOKS_FOUND,
    MSG_NO_BOOKS_FOUND, MSG_NO_BOOKS, MSG_LIST_BOOKS,
    MSG_ENTER_BOOK_ID_STATUS, MSG_ENTER_NEW_STATUS,
    MSG_INVALID_STATUS, MSG_BOOK_STATUS_CHANGED
)

from storage import save_data

Book = Dict[str, str | int]


def add_book(books: List[Book]) -> None:
    """
    Добавляет новую книгу в список.

    books: Список книг, в который будет добавлена новая книга.
    """
    title = input(MSG_ENTER_BOOK_TITLE).strip()
    author = input(MSG_ENTER_BOOK_AUTHOR).strip()
    year = input(MSG_ENTER_BOOK_YEAR).strip()

    try:
        year = int(year)
    except ValueError:
        print("Год издания должен быть числом!")
        return

    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "year": year,
        "status": STATUS_AVAILABLE
    }
    books.append(new_book)
    save_data(books)
    print(MSG_BOOK_ADDED.format(title))


def remove_book(books: List[Book]) -> None:
    """
    Удаляет книгу из списка по её id.

    books: Список книг, из которого нужно удалить книгу.
    """
    book_id = input(MSG_ENTER_BOOK_ID_REMOVE).strip()

    try:
        book_id = int(book_id)
    except ValueError:
        print(MSG_ID_MUST_BE_NUMBER)
        return

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print(MSG_BOOK_REMOVED.format(book_id))
            return

    print(MSG_BOOK_NOT_FOUND.format(book_id))


def search_books(books: List[Book]) -> None:
    """
    Выполняет поиск книг по названию, автору или году.

    books: Список книг, в котором выполняется поиск.
    """
    query = input(MSG_ENTER_QUERY).strip().lower()

    results = [
        book for book in books
        if query in str(book["title"]).lower()
        or query in str(book["author"]).lower()
        or query == str(book["year"])
    ]

    if results:
        print(MSG_BOOKS_FOUND)
        for book in results:
            print(
                f"{book['id']}: {book['title']}\n"
                f"({book['author']}, {book['year']}) - {book['status']}"
            )
    else:
        print(MSG_NO_BOOKS_FOUND)


def display_books(books: List[Book]) -> None:
    """
    Выводит список всех книг.

    books: Список книг, который нужно отобразить.
    """
    if not books:
        print(MSG_NO_BOOKS)
        return

    print(MSG_LIST_BOOKS)
    for book in books:
        print(
            f"{book['id']}: {book['title']}\n"
            f"({book['author']}, {book['year']}) - {book['status']}"
        )


def change_status(books: List[Book]) -> None:
    """
    Изменяет статус книги (в наличии или выдана).

    books: Список книг, в котором изменяется статус.
    """
    book_id = input(MSG_ENTER_BOOK_ID_STATUS).strip()

    try:
        book_id = int(book_id)
    except ValueError:
        print(MSG_ID_MUST_BE_NUMBER)
        return

    for book in books:
        if book["id"] == book_id:
            new_status = input(MSG_ENTER_NEW_STATUS).strip()
            if new_status not in [STATUS_AVAILABLE, STATUS_ISSUED]:
                print(MSG_INVALID_STATUS)
                return

            book["status"] = new_status
            print(MSG_BOOK_STATUS_CHANGED.format(book_id, new_status))
            return

    print(MSG_BOOK_NOT_FOUND.format(book_id))
