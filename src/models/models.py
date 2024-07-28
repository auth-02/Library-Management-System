class Book:
    
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN number of the book.
        available (bool): The availability status of the book.
    """
    
    def __init__(self, title, author, isbn, available=True):
        
        """
        Initializes a new Book instance.
        """
        
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def to_dict(self):
        
        """
        Converts the Book object to a dictionary.
        """
        
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'available': self.available
        }

    @classmethod
    def from_dict(cls, data):
        
        """
        Creates a Book instance from a dictionary.
        """
        
        return cls(data['title'], data['author'], data['isbn'], data.get('available', True))

class User:
    
    """
    Represents a user in the library system.

    Attributes:
        name (str): The name of the user.
        user_id (str): The user ID of the user.
    """
    
    def __init__(self, name, user_id):
        
        """
        Initializes a new User instance.
        """
        
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        
        """
        Converts the User object to a dictionary.
        """
        
        return {
            'name': self.name,
            'user_id': self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        
        """
        Creates a User instance from a dictionary.
        """
        
        return cls(data['name'], data['user_id'])


class Checkout:
    
    """
    Represents a checkout record in the library system.

    Attributes:
        user_id (str): The user ID of the user who checked out the book.
        isbn (str): The ISBN number of the book that was checked out.
    """

    
    def __init__(self, user_id, isbn):
        
        """
        Initializes a new Checkout instance.
        """
        
        self.user_id = user_id
        self.isbn = isbn

    def to_dict(self):
        
        """
        Converts the Checkout obj to a dictionary.
        """
        
        return {
            'user_id': self.user_id,
            'isbn': self.isbn
        }

    @classmethod
    def from_dict(cls, data):
        
        """
        Creates a Checkout instance from a dictionary.
        """
        
        return cls(data['user_id'], data['isbn'])
