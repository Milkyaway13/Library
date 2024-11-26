# Статусы книг
STATUS_AVAILABLE = "в наличии"
STATUS_ISSUED = "выдана"

# Сообщения
MSG_ENTER_BOOK_TITLE = "Введите название книги: "
MSG_ENTER_BOOK_AUTHOR = "Введите автора книги: "
MSG_ENTER_BOOK_YEAR = "Введите год издания книги: "
MSG_BOOK_ADDED = "Книга '{}' успешно добавлена."
MSG_ENTER_BOOK_ID_REMOVE = "Введите id книги для удаления: "
MSG_BOOK_REMOVED = "Книга с ID {} успешно удалена."
MSG_BOOK_NOT_FOUND = "Книга с ID {} не найдена."
MSG_ENTER_QUERY = "Введите запрос для поиска (название, автор или год): "
MSG_BOOKS_FOUND = "Найденные книги:"
MSG_ID_MUST_BE_NUMBER = "ID должен быть числом."
MSG_NO_BOOKS_FOUND = "Книги по вашему запросу не найдены."
MSG_NO_BOOKS = "В библиотеке пока нет книг."
MSG_LIST_BOOKS = "Список книг:"
MSG_ENTER_BOOK_ID_STATUS = "Введите id книги для изменения статуса: "
MSG_ENTER_NEW_STATUS = "Введите новый статус ('в наличии' или 'выдана'): "
MSG_INVALID_STATUS = "Некорректный статус! Укажите 'в наличии' или 'выдана'."
MSG_BOOK_STATUS_CHANGED = "Статус книги с ID {} успешно изменён на '{}'."

# Файл хранения данных
DATA_FILE = "library.json"

# Строки для меню
MENU = """
Управление библиотекой:
1. Добавить книгу
2. Удалить книгу
3. Искать книги
4. Отобразить все книги
5. Изменить статус книги
6. Выход
"""
CHOICE_PROMPT = "Выберите действие: "
MSG_EXIT = "Выход из программы."
MSG_INVALID_CHOICE = "Некорректный выбор, попробуйте снова."
