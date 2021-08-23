import unittest

from project.library import Library

class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.library = Library("Name")

    def test_init(self):
        self.assertEqual(self.library.name, "Name")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_name_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_1(self):
        author = "Stephen"
        title = "Shining"
        self.library.add_book(author, title)
        self.assertEqual(self.library.books_by_authors, {author: [title]})

    def test_add_reader_when_not_in(self):
        name = "Ivan"
        self.library.add_reader(name)
        self.assertEqual(self.library.readers, {name: []})

    def test_add_reader_when_in(self):
        name = "Ivan"
        self.library.readers = {name: []}
        actual = self.library.add_reader(name)
        self.assertEqual(actual, f"{name} is already registered in the {self.library.name} library.")

    def test_rent_book_1(self):
        reader_name = "Ivan"
        book_author = "Stephen"
        book_title = "Shining"
        actual = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(actual, f"{reader_name} is not registered in the {self.library.name} Library.")

    def test_rent_book_2(self):

        reader_name = "Ivan"
        book_author = "Stephen"
        book_title = "Shining"
        self.library.readers = {reader_name: []}
        actual = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(actual, f"{self.library.name} Library does not have any {book_author}'s books.")

    def test_rent_book_3(self):
        reader_name = "Ivan"
        book_author = "Stephen"
        book_title = "Shining"
        self.library.readers = {reader_name: []}
        self.library.books_by_authors = {book_author: []}
        actual = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(actual, f"""{self.library.name} Library does not have {book_author}'s "{book_title}".""")

    def test_rent_book_4(self):
        reader_name = "Ivan"
        book_author = "Stephen"
        book_title = "Shining"
        self.library.readers = {reader_name: []}
        self.library.books_by_authors = {book_author: [book_title]}
        self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(self.library.readers, {reader_name: [{book_author: book_title}]})
        self.assertEqual(self.library.books_by_authors, {book_author: []})
