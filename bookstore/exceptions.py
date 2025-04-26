# ------------------ Custom Exceptions -------------------

class DuplicateBookError(Exception):
    """ Raised when attempting to add a duplicate book to the BookStore (inventory). """
    pass

class BookNotFoundError(Exception):
    """ Raised when book not found in BookStore (inventory). """
    pass
