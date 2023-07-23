Код класса BooksCollector в описании финального проекта в тренажере отличается от кода этого класса в файле main.py репозитория, который предлагается клонировать для выполнения задания.
Я писала тесты на методы класса, как они описаны в тренажере.
В связи с этим, чтобы тесты запустились, заменяю код в файле main.py на код из тренажера.

Экземпляры класса BooksCollector создаются с помощью фикстуры collector перед каждым тестом.

Для параметризации используется глобальная переменная books, являющаяся списком списков.

В тестах избегается использование других методов класса, кроме проверяемого, чтобы избежать их влияния на результат теста.

2 теста на метод init:
1. Проверяем, что при создании экземпляра класса жанры класса соответствуют установленным
2. Проверяем, что жанры возрастного ограничения соответствуют установленным

9 тестов на другие методы класса:
1. Тест метода add_new_book. Добавление двух книг и проверка длины возвращаемой коллекции
2. Тест метода set_book_genre. Добавление книги, установка ей жанра и проверка, что книге установился именно этот жанр
3. Тест метода get_book_genre. Добавление книги, установка ей жанра и проверка, что жанр возвращается по названию книги
4. Тест метода get_books_with_specific_genre. Заполнение коллекции с помощью глобальной переменной books, отбор книг жанра Комедия и проверка, что по жанру возвращается верный список книг
5. Тест метода get_books_genre. Заполнение коллекции с помощью глобальной переменной books, проверка длины коллекции
6. Тест метода get_books_for_children. Заполнение коллекции с помощью глобальной переменной books, проверка, что метод возращает только книги определенного рейтинга
7. Тест метода add_book_in_favorites. Заполнение коллекции с помощью глобальной переменной books, добавление книги в Избранные, проверка имени возвращаемой методом книги
8. Тест метода delete_book_from_favorites. Удаление книги, проверка, что удаленной книги нет в списке Избранных
9. Тест метода get_list_of_favorites_books. Проверка возвращаемого списка Избранного