from models.models import Book
from database.storage import Storage
from utility.logging_util import setup_logger

# Initialize logger for book management
logger = setup_logger('book_management', 'logs/book_management.log')

class BookManager:
    """
    Manages book-related operations such as adding, listing, searching, updating, 
    deleting, checking out, and checking in books.
    """

    def __init__(self, storage_file='data/books.json'):

        """
        Initializes the BookManager with a storage file for books.
        """

        self.storage = Storage(storage_file)
        self.books = [Book.from_dict(book) for book in self.storage.load_data()]
        logger.info("BookManager initialized")

    def add_book(self, title, author, isbn):

        """
        Adds a new book to the collection.
        """

        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        logger.info(f"Book added: {title}, {author}, {isbn}")

    def list_books(self):

        """
        Lists all books in the collection.
        """

        for book in self.books:
            print(book.to_dict())
        logger.info("Books listed")

    def search_books(self, attribute, value):

        """
        Searches for books by a specified attribute and value.
        """

        results = [book for book in self.books if getattr(book, attribute, None) == value]
        logger.info(f"Books searched by {attribute}: {value}")
        return results

    def update_book(self, isbn, title=None, author=None):

        """
        Updates the details of a book by its ISBN.
        """

        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                self.save_books()
                logger.info(f"Book updated: {isbn}, {title}, {author}")
                return book
        logger.warning(f"Book not found for update: {isbn}")
        return None

    def delete_book(self, isbn):

        """
        Deletes a book by its ISBN.
        """

        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        logger.info(f"Book deleted: {isbn}")

    def save_books(self):

        """
        Saves the current collection of books to the storage file.
        """

        self.storage.save_data([book.to_dict() for book in self.books])
        logger.info("Books saved")

    def check_out_book(self, isbn):

        """
        Checks out a book by its ISBN, marking it as unavailable.
        """

        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                self.save_books()
                logger.info(f"Book checked out: {isbn}")
                return book
        logger.warning(f"Book not available for checkout: {isbn}")
        return None

    def check_in_book(self, isbn):

        """
        Checks in a book by its ISBN, marking it as available.
        """

        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                self.save_books()
                logger.info(f"Book checked in: {isbn}")
                return book
        logger.warning(f"Book not found for check-in: {isbn}")
        return None
