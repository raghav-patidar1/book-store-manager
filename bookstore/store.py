from .models import Book
from .exceptions import DuplicateBookError, BookNotFoundError
from .utils import log_action


# ------------------ Book Store Iterator -------------------


class BookStoreIterator:
    """ Custom iterator for BookStore. """

    def __init__(self, data):
        """ Initialize BookStoreIterator instance attributes for managing iteration state. """

        self.data = list(data)
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        """ Fetches book from BookStore. """
        
        if self.index >= len(self.data):
            raise StopIteration
        book = self.data[self.index]
        self.index += 1
        return book
    


# ------------------ Book Store  -------------------


class BookStore:
    """ Manages a collection of Books (inventory). """

    def __init__(self):
        """ Initialize Book Store instance attributes. """
        self._inventory = {}

    
    @log_action
    def add_book(self, book_data: dict):
        """ Adds a book to inventory. Raises DuplicateBookError if ISBN exists. """

        book = Book.validate_data(book_data)

        # Check for duplicates

        if book.isbn in self._inventory:
            raise DuplicateBookError(f"Book with ISBN {book.isbn} already exists.")
        
        self._inventory[book.isbn] = book


    @log_action
    def delete_book_by_isbn(self, isbn = None):
        """ Deletes a book by ISBN number. """

        if isbn in self._inventory:
            del self._inventory[isbn]
        else:
            raise BookNotFoundError(f"Book with ISBN {isbn} not found!")


    @log_action
    def delete_book_by_title(self, title = None):
        """ Deletes a book by title. (may delete muliple books if titles match). """

        isbn_to_delete = [isbn for isbn, book in self._inventory.items() if book.title == title]
        if len(isbn_to_delete) > 0:
            for isbn in isbn_to_delete:
                del self._inventory[isbn]
        else:
            raise BookNotFoundError(f"Book with title '{title}' not found!")

        
    def get_all_books(self):
        """ Get all books from the inventory. """

        return self._inventory.values()


    def filter_by_title(self, title):
        """Returns books matching the given title."""

        return [book for book in self.inventory.values() if book.title == title]


    def filter_by_author(self, author):
        """Returns books by the specified author."""

        return [book for book in self.inventory.values() if book.author == author]
    

    def filter_by_price(self, max_price):

        """Returns books that cost less than or equal to the given price."""

        return [book for book in self.inventory.values() if book.price <= max_price]
    

    @property
    def inventory(self):
        return self._inventory
    

    def __str__(self):
        return str(self._inventory)


    def __iter__(self):
        """ Returns BookStoreIterator for inventory. """
        return BookStoreIterator(self._inventory.values())
    






