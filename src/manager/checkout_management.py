from models.models import Checkout
from database.storage import Storage
from utility.logging_util import setup_logger

# Initialize logger for checkout management
logger = setup_logger('checkout_management', 'logs/checkout_management.log')

class CheckoutManager:

    """
    Manages the checkout and return of books, ensuring that only registered users
    can checkout and return books.
    """

    def __init__(self, storage_file='data/checkouts.json'):

        """
        Initializes the CheckoutManager with a storage file for checkouts.
        """

        self.storage = Storage(storage_file)
        self.checkouts = [Checkout.from_dict(checkout) for checkout in self.storage.load_data()]
        logger.info("CheckoutManager initialized")

    def checkout_book(self, user_id, isbn, book_manager, user_manager):

        """
        Checks out a book for a user if the user exists and the book is available.
        """

        if not user_manager.user_exists(user_id):
            print("User does not exist.")
            logger.warning(f"Checkout failed. User does not exist: {user_id}")
            return

        if any(checkout.user_id == user_id and checkout.isbn == isbn for checkout in self.checkouts):
            print("This book is already checked out by this user.")
            logger.warning(f"Book already checked out by user: {user_id}, ISBN: {isbn}")
            return

        book = book_manager.check_out_book(isbn)
        if book:
            new_checkout = Checkout(user_id, isbn)
            self.checkouts.append(new_checkout)
            self.save_checkouts()
            logger.info(f"Book checked out: {isbn} by User: {user_id}")
            print("Book checked out.")
        else:
            print("Book is not available for checkout.")
            logger.warning(f"Book not available for checkout: {isbn}")

    def return_book(self, user_id, isbn, book_manager):

        """
        Returns a book that was checked out by a user if the user indeed checked out the book.
        """

        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                self.checkouts.remove(checkout)
                book_manager.check_in_book(isbn)
                self.save_checkouts()
                logger.info(f"Book returned: {isbn} by User: {user_id}")
                print("Book returned.")
                return
        print("This user did not check out this book.")
        logger.warning(f"Return failed. User: {user_id} did not check out book: {isbn}")

    def list_checkouts(self):

        """
        Lists all current checkouts.
        """

        for checkout in self.checkouts:
            print(checkout.to_dict())
        logger.info("Checkouts listed")

    def save_checkouts(self):

        """
        Saves the current list of checkouts to the storage file.
        """

        self.storage.save_data([checkout.to_dict() for checkout in self.checkouts])
        logger.info("Checkouts saved")
