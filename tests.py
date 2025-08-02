from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two__equal_books_failed(self):
        collector = BooksCollector()
        collector.add_new_book('Джейн Эйр')
        collector.add_new_book('Джейн Эйр')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_len_more_than_40_failed(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче и о прекрасной Царевне Лебеди')
        assert len(collector.get_books_genre()) == 0

    def test_add_book_in_favorites_sucсess(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_two_equal_books_failed(self):
        collector = BooksCollector()
        collector.add_new_book('Виола Тараканова')
        collector.add_book_in_favorites('Виола Тараканова')
        collector.add_book_in_favorites('Виола Тараканова')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка о золотой рыбке')
        collector.add_book_in_favorites('Сказка о золотой рыбке')
        collector.delete_book_from_favorites('Сказка о золотой рыбке')
        assert len(collector.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_in_list_success(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Бегущий по лезвию')
        collector.set_book_genre('Бегущий по лезвию', genre)  
        assert collector.get_book_genre('Бегущий по лезвию') == genre 

    @pytest.mark.parametrize('genre_not_inlist', ['Триллер', 'Мелодрама'])
    def test_set_book_genre_not_inlist_failed(self, genre_not_inlist):
        collector = BooksCollector()
        collector.add_new_book('Поющие в терновнике')
        collector.set_book_genre('Поющие в терновнике', genre_not_inlist)  
        assert collector.get_book_genre('Поющие в терновнике') != genre_not_inlist 

    @pytest.mark.parametrize('name,genre', [
    ['Заживо в темноте', 'Ужасы'],
    ['Золотой теленок', 'Комедии'],
    ['Восточный экспресс', 'Детективы']
]
)
    def test_get_book_genre_by_name_success(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name,genre', [
    ['Заживо в темноте', 'Ужасы'],
    ['Восточный экспресс', 'Детективы']
    ]
    )
    def test_get_books_with_specific_genre_success(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre(genre)
        assert name in books_with_specific_genre

    @pytest.mark.parametrize('name,genre,specific_genre', [
    ['Заживо в темноте', 'Ужасы', True],
    ['Восточный экспресс', 'Детективы', True],
    ['Золотой ключик','Мультфильм', False]
    ]
    )
    def test_get_books_for_children_success(self, name, genre, specific_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre(specific_genre)
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) != books_with_specific_genre

    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        collector.add_new_book('Золотой ключик')
        collector.add_book_in_favorites('Золотой ключик')
        assert len(collector.get_list_of_favorites_books()) == 1