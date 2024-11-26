from book_manager import (
    add_book, remove_book, search_books,
    display_books, change_status
)
from storage import load_data, save_data
from constants import MENU, CHOICE_PROMPT, MSG_EXIT, MSG_INVALID_CHOICE


def main() -> None:
    """
    Основная функция для управления библиотекой.
    """
    books = load_data()
    actions = {
        "1": add_book,
        "2": remove_book,
        "3": search_books,
        "4": display_books,
        "5": change_status
    }

    while True:
        print(MENU)
        choice = input(CHOICE_PROMPT).strip()

        if choice == "6":
            save_data(books)
            print(MSG_EXIT)
            break
        elif choice in actions:
            actions[choice](books)
        else:
            print(MSG_INVALID_CHOICE)


if __name__ == "__main__":
    main()
