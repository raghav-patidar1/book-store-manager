
from abc import ABC, abstractmethod


# ------------------ Abstract Class ------------------- 


class AbstractBook(ABC):
    
    @abstractmethod
    def __repr__(self):
        """ Abstract method to represent a book. """
        pass



# ------------------ Book Class -------------------


class Book(AbstractBook):
    """ Represents a book in the book store (inventory). """
        

    required_fields = ["title", "author", "price", "pages", "isbn", "format"]
    VALID_FORMATS = {"ebook", "printed"}
    

    def __init__(self, **kwargs):
        """ Initialize a Book instance with validated attributes. """

        for key,value in kwargs.items():

            if key == "isbn":
                self.__isbn_no = value
            
            elif key == "price":
                self._price = value 

            else:
                setattr(self, key, value)

            
    @staticmethod
    def validate_data(book_dict):
        """  Validates required fields and valid book format before creating an instance of Book. """

        missing_fields = [field for field in Book.required_fields if field not in book_dict]
        if missing_fields:
            raise ValueError(f"Error: Missing fields - {', '.join(missing_fields)}")
        
        if book_dict["format"] not in Book.VALID_FORMATS:
            raise ValueError(f"Error: Invalid Book Format '{book_dict["format"]}'. Must be one of these - {Book.VALID_FORMATS}.")
        
        return Book(**book_dict)        # create an instance of Book
    
    
    @property
    def price(self):
        return self._price

    
    @property  
    def isbn(self):
        return self.__isbn_no
    

    def __repr__(self):
        return f"Book(title={self.title})"
    

    def __str__(self):
        return f"{self.title} by {self.author} | ₹ {self.price} | {self.pages} pages | ISBN: {self.__isbn_no} | Format: {self.format}." 





