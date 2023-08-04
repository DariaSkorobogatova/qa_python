import pytest

books = {
    'Понедельник начинается в субботу': 'Фантастика',
    '2001: Космическая одиссея': 'Фантастика',
    'Кладбище домашних животных': 'Ужасы',
    'Сияние': 'Ужасы',
    'Убийство в восточном экспрессе': 'Детективы',
    'Маугли': 'Мультфильмы',
    'Трое в лодке, не считая собаки': 'Комедии',
    'Приключения бравого солдата Швейка': 'Комедии'
}


class TestBooksCollector:

    def test_genres_are_same_as_in_init(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_are_same_as_in_init(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2, f"Длина коллекции должна быть {len(collector.get_books_genre())}"

    @pytest.mark.parametrize('name', ['2001: Космическая одиссея', '', 'Nequeporroquisquamestquidoloremipsumquiad'])
    def test_add_new_book_negative_verifications(self, name, collector):
        collector.add_new_book('2001: Космическая одиссея')
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1, "Книга не добавлена, т.к. она уже существует либо длина названия = 0 либо длина названияя > 40"

    def test_set_book_genre_to_added_book_existent_genre(self, collector):
        name = 'Понедельник начинается в субботу'
        genre = 'Фантастика'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre, f"Жанр должен быть {genre}"

    def test_set_book_genre_to_added_book_nonexistent_genre(self, collector):
        name = 'Дневник памяти'
        genre = 'Роман'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == '', "Жанр не должен был присвоиться, так как его нет в списке допустимых"

    def test_get_books_with_specific_genre_comedy(self, collector):
        name = 'Трое в лодке, не считая собаки'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    @pytest.mark.parametrize('name, genre', [['Сияние', 'Ужасы'], ['Азазель', 'Детективы']])
    def test_get_books_for_children(self, name, genre, collector):
        collector.add_new_book('Маугли')
        collector.set_book_genre('Маугли', 'Мультфильмы')
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == ['Маугли'], "Жанры Ужасы и Детективы не подходят по возрастному рейтингу"

    def test_add_book_in_favorites(self, collector):
        name = 'Понедельник начинается в субботу'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    def test_delete_book_from_favorites(self, collector):
        name = 'Убийство в восточном экспрессе'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()



