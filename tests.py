import pytest

books = [
    ['Понедельник начинается в субботу', 'Фантастика'],
    ['2001: Космическая одиссея', 'Фантастика'],
    ['Кладбище домашних животных', 'Ужасы'],
    ['Сияние', 'Ужасы'],
    ['Убийство в восточном экспрессе', 'Детективы'],
    ['Маугли', 'Мультфильмы'],
    ['Трое в лодке, не считая собаки', 'Комедии'],
    ['Приключения бравого солдата Швейка', 'Комедии']
]


# Класс TestBooksCollector объединяет набор тестов, которыми покрывается приложение BooksCollector
class TestBooksCollector:

    # Тесты метода _init_

    def test_genres_are_same_as_in_init(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_are_same_as_in_init(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Тесты остальных методов класса

    def test_add_new_book_add_two_books(self, collector):
        # Добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # Проверяем, что добавилось именно две
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name, genre', books)
    def test_set_book_genre_to_added_book(self, name, genre, collector):
        # Добавляем книгу из глобальной переменной books
        # Напрямую в коллекцию books_genre, без использования метода add_new_book для исключения его влияния на тест
        collector.books_genre[name] = ''
        # Устанавливаем книге жанр с помощью тестируемого метода set_book_genre
        collector.set_book_genre(name, genre)
        # Проверяем, что книге установился именно этот жанр
        # Без использования метода get_book_genre для исключения его влияния на тест
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize('name, genre', books)
    def test_get_book_genre_for_every_in_books(self, name, genre, collector):
        # Добавляем книгу в коллекцию books_genre из глобальной переменной books и устанавливаем ей жанр
        # Без использования методов add_new_book и set_book_genre для исключения их влияния на тест
        collector.books_genre[name] = genre
        # Проверяем, что можно получить жанр по названию книги с помощью тестируемого метода get_book_genre
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_comedy(self, collector):
        genre = 'Комедии'
        names = list()
        # Наполняем коллекцию books_genre данными из глобальной переменной books
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
            # Собираем все книги выбранного жанра в список names
            if books[i][1] == genre:
                names.append(books[i][0])
        # Проверяем, что по выбранному жанру возвращается список книг
        assert collector.get_books_with_specific_genre(genre) == names

    def test_get_books_genre_return_collection(self, collector):
        # Наполняем коллекцию books_genre данными из глобальной переменной books
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
        # Проверяем, что длина возвращаемой коллекции не равна 0
        assert len(collector.get_books_genre()) != 0

    def test_get_books_for_children(self, collector):
        books_for_kids = list()
        # Наполняем коллекцию books_genre данными из глобальной переменной books
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
            # Собираем все книги, подходящие детям, в список books_for_kids
            if books[i][1] not in collector.genre_age_rating:
                books_for_kids.append(books[i][0])
        # Проверяем, что метод возвращает книги из books_for_kids
        assert collector.get_books_for_children() == books_for_kids

    @pytest.mark.parametrize('name', ['Понедельник начинается в субботу', 'Убийство в восточном экспрессе'])
    def test_add_book_in_favorites(self, name, collector):
        # Наполняем коллекцию books_genre данными из глобальной переменной books
        for i in range(len(books)):
            collector.books_genre[books[i][0]] = books[i][1]
        # Добавляем книгу в Избранное
        collector.add_book_in_favorites(name)
        # Проверяем имя книги в Избранном
        assert collector.favorites[0] == name

    def test_delete_book_from_favorites(self, collector):
        deleted_book = '10 негритят'
        collector.favorites = ['Убийство в восточном экспрессе', '10 негритят', 'Смерть на Ниле']
        collector.delete_book_from_favorites(deleted_book)
        # Проверяем, что удаленной книги нет в Избранном
        assert deleted_book not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ['Убийство в восточном экспрессе', '10 негритят', 'Смерть на Ниле']
        assert collector.get_list_of_favorites_books() == ['Убийство в восточном экспрессе', '10 негритят',
                                                           'Смерть на Ниле']
