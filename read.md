1 тест(базовый) add_new_book_add_two_books проверяет добавление 2 новых книг в словарь без указания жанра
2 тест test_add_new_book__len_more_than_40_failed проверяет, что в словарь не добавляются книги, название которых более 40 символов
3 тест test_add_book_in_favorites_sucсess проверяет успешное добавление книги в избранное
4 тест test_add_book_in_favorites_two_equal_books_failed проверяет, что повторно одна и та же книга в избранное не добавляется
5 тест test_delete_book_from_favorites_success проверяет удаление книги из избранного
6 тест test_set_book_genre_in_list_success проверяет корректность присвоения методом жанра книги и возврат установленного жанра 
7 тест test_set_book_genre_assign_genre_not_inlist_failed проверяет, что метод не присваевает книге невалидный жанр
8 тест test_get_book_genre_by_name_success проверяет вывод жанра книги по ее названию 
9 тест test_get_books_with_specific_genre_success проверяет список книг с определённым жанром
10 тест test_get_books_for_children_success  проверяет книги, которые подходят детям(у которых не установлен специальный рейтинг
11 тест test_get_list_of_favorites_books_success проверяет, что после добавления книги в избранное, книга добавляется в избранное
12 тест test_get_book_genre_success проверяет, что метод выводит ожидаемый результат из добавленных книг и их жанров 
