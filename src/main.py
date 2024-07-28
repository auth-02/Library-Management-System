from manager.book_management import BookManager
from manager.user_management import UserManager
from manager.checkout_management import CheckoutManager
from utility.logging_util import setup_logger

logger = setup_logger('main', 'logs/main.log')

def main_menu():
    print("\nLibrary Management System", end="\n\n")

    print("\n##  BOOKS:  ##", end="\n\n")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Books")
    print("4. Update Book")
    print("5. Delete Book")
    
    print("\n##  USERS:  ##", end="\n\n")
    print("6. Add User")
    print("7. List Users")
    print("8. Search Users")
    print("9. Update User")
    print("10. Delete User")
    
    print("\n##  CHECKOUTS:  ##", end="\n\n")
    print("11. Checkout Book")
    print("12. Return Book")
    print("13. List Checkouts")
    
    print("14. Exit", end="\n\n")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    while True:
        choice = main_menu()
        try:
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_manager.add_book(title, author, isbn)
                print("Book added.")
            elif choice == '2':
                book_manager.list_books()
            elif choice == '3':
                attribute = input("Enter attribute to search (title, author, isbn): ")
                value = input("Enter value: ")
                results = book_manager.search_books(attribute, value)
                for book in results:
                    print(book.to_dict())
            elif choice == '4':
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (Skip): ")
                author = input("Enter new author (Skip): ")
                book_manager.update_book(isbn, title, author)
                print("Book updated.")
            elif choice == '5':
                isbn = input("Enter ISBN of the book to delete: ")
                book_manager.delete_book(isbn)
                print("Book deleted.")
            elif choice == '6':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == '7':
                user_manager.list_users()
            elif choice == '8':
                attribute = input("Enter attribute to search (name, user_id): ")
                value = input("Enter value: ")
                results = user_manager.search_users(attribute, value)
                for user in results:
                    print(user.to_dict())
            elif choice == '9':
                user_id = input("Enter user ID of the user to update: ")
                name = input("Enter new name (Skip): ")
                user_manager.update_user(user_id, name)
                print("User updated.")
            elif choice == '10':
                user_id = input("Enter user ID of the user to delete: ")
                user_manager.delete_user(user_id)
                print("User deleted.")
            elif choice == '11':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                checkout_manager.checkout_book(user_id, isbn, book_manager, user_manager)
            elif choice == '12':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to return: ")
                checkout_manager.return_book(user_id, isbn, book_manager)
            elif choice == '13':
                checkout_manager.list_checkouts()
            elif choice == '14':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
            logger.info(f"User choice: {choice} processed")
        except Exception as e:
            print(f"An error occurred: {e}")
            logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
