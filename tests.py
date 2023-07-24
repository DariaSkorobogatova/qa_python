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
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name, genre', [['Понедельник начинается в субботу', 'Фантастика']])
    def test_set_book_genre_to_added_book_existent_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [['Дневник памяти', 'Роман']])
    def test_set_book_genre_to_added_book_nonexistent_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre_comedy(self, collector):
        collector.books_genre = books
        assert collector.get_books_with_specific_genre('Комедии') == ['Трое в лодке, не считая собаки', 'Приключения бравого солдата Швейка']

    def test_get_books_genre_return_collection(self, collector):
        collector.books_genre = books
        assert len(collector.get_books_genre()) == 8

    def test_get_books_for_children(self, collector):
        collector.books_genre = books
        assert collector.get_books_for_children() == ['Понедельник начинается в субботу', '2001: Космическая одиссея', 'Маугли', 'Трое в лодке, не считая собаки', 'Приключения бравого солдата Швейка']

    def test_add_book_in_favorites(self, collector):
        collector.books_genre = books
        collector.add_book_in_favorites('Понедельник начинается в субботу')
        assert collector.get_list_of_favorites_books() == ['Понедельник начинается в субботу']

    def test_delete_book_from_favorites(self, collector):
        deleted_book = '10 негритят'
        collector.favorites = ['Убийство в восточном экспрессе', '10 негритят', 'Смерть на Ниле']
        collector.delete_book_from_favorites(deleted_book)
        assert deleted_book not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.favorites = ['Убийство в восточном экспрессе', '10 негритят', 'Смерть на Ниле']
        assert collector.get_list_of_favorites_books() == ['Убийство в восточном экспрессе', '10 негритят',
                                                           'Смерть на Ниле']
