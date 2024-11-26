import json
import os
from typing import List, Dict

from constants import DATA_FILE

Book = Dict[str, str | int]


def load_data() -> List[Book]:
    """
    Загружает список книг из файла.

    Возвращает список книг, если файл существует,
    или пустой список, если файла нет.
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(books: List[Book]) -> None:
    """
    Сохраняет список книг в файл.

    books: Список книг, которые нужно сохранить.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
