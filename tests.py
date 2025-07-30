from main import BooksCollector
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

class TestBooksCollector:

    def test_add_new_book_add_two__equal_books_failed(self):
        collector = BooksCollector()
        collector.add_new_book('Джейн Эйр')
        collector.add_new_book('Темная башня')
        assert len(collector.get_books_genre()) == 1

class TestBooksCollector:

    def test_add_new_book_add_books_len_more_than_40_failed(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка о царе Салтане, о сыне его славном и могучем богатыре князе Гвидоне Салтановиче и о прекрасной Царевне Лебеди')
        assert len(collector.get_books_genre()) == 0


class TestBooksCollector:

    def test_add_book_in_favorites_sucsess(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')

        assert len(collector.get_books_genre()) == 0