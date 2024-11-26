import json
import os

# Файл для хранения данных
DATA_FILE = "library.json"

# Загрузка данных из файла
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Сохранение данных в файл
def save_data(books):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

# Генерация уникального ID
def generate_id(books):
    return max((book["id"] for book in books), default=0) + 1

# Добавление книги
def add_book(books):
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    year = input("Введите год издания: ").strip()
    if not year.isdigit():
        print("Год издания должен быть числом.")
        return
    year = int(year)
    new_book = {
        "id": generate_id(books),
        "title": title,
        "author": author,
        "year": year,
        "status": "в наличии"
    }
    books.append(new_book)
    save_data(books)
    print("Книга успешно добавлена!")

# Удаление книги
def remove_book(books):
    try:
        book_id = int(input("Введите ID книги для удаления: ").strip())
    except ValueError:
        print("ID должен быть числом.")
        return
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_data(books)
            print("Книга успешно удалена!")
            return
    print("Книга с таким ID не найдена.")

# Поиск книг
def search_books(books):
    search_term = input("Введите строку для поиска (по названию, автору или году): ").strip()
    results = [
        book for book in books
        if search_term.lower() in book["title"].lower() or
           search_term.lower() in book["author"].lower() or
           search_term.isdigit() and int(search_term) == book["year"]
    ]
    if results:
        print("\nНайденные книги:")
        display_books(results)
    else:
        print("Книги не найдены.")

# Отображение всех книг
def display_books(books):
    if not books:
        print("Библиотека пуста.")
        return
    for book in books:
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")

# Изменение статуса книги
def change_status(books):
    try:
        book_id = int(input("Введите ID книги: ").strip())
    except ValueError:
        print("ID должен быть числом.")
        return
    for book in books:
        if book["id"] == book_id:
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
            if new_status in ["в наличии", "выдана"]:
                book["status"] = new_status
                save_data(books)
                print("Статус успешно обновлен!")
                return
            else:
                print("Некорректный статус.")
                return
    print("Книга с таким ID не найдена.")

# Главное меню
def main():
    books = load_data()
    actions = {
        "1": add_book,
        "2": remove_book,
        "3": search_books,
        "4": display_books,
        "5": change_status
    }

    while True:
        print("\nУправление библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "6":
            print("Выход из программы.")
            break
        elif choice in actions:
            actions[choice](books)
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
