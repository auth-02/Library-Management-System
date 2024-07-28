# Library Management System

A simple Library Management System implemented in Python. It includes functionalities to manage books, users, and book checkouts with comprehensive logging and file-based storage.

## File Tree
```markdown
LibraryManagementSystem/
│
├── data/
│   ├── books.json
│   ├── checkouts.json
│   └── users.json
│
├── logs/
│   ├── book_management.log
│   ├── checkout_management.log
│   ├── main.log
│   ├── storage.log
│   └── user_management.log
│
├── src/
│   ├── main.py
│   │
│   ├── database/
│   │   └── storage.py
│   │
│   ├── manager/
│   │   ├── book_management.py
│   │   ├── checkout_management.py
│   │   └── user_management.py
│   │
│   ├── models/
│   │   └── models.py
│   │
│   └── utility/
│       └── logging_util.py
```

## Functionality

### Book Management
- **Add Book**: Adds a new book to the library.
- **List Books**: Lists all books in the library.
- **Search Books**: Searches for books by title, author, or ISBN.
- **Update Book**: Updates the title or author of a book by ISBN.
- **Delete Book**: Deletes a book from the library by ISBN.
- **Check Out Book**: Checks out a book, marking it as unavailable.
- **Check In Book**: Checks in a book, marking it as available.

### User Management
- **Add User**: Adds a new user to the system.
- **List Users**: Lists all users.
- **Search Users**: Searches for users by name or user ID.
- **Update User**: Updates the name of a user by user ID.
- **Delete User**: Deletes a user from the system by user ID.
- **User Exists**: Checks if a user exists in the system.

### Checkout Management
- **Checkout Book**: Allows a user to checkout a book if the user exists and the book is available.
- **Return Book**: Allows a user to return a book if the user had checked it out.
- **List Checkouts**: Lists all current book checkouts.

## Logging

Logging is implemented to record significant events and errors throughout the system. Each module has its own log file:

- **book_management.log**: Logs events related to book management operations.
- **checkout_management.log**: Logs events related to book checkout and return operations.
- **main.log**: Logs events in the main application flow.
- **storage.log**: Logs events related to file storage operations.
- **user_management.log**: Logs events related to user management operations.

The log files are stored in the `logs/` directory.

## File Storage

Data is stored in JSON files within the `data/` directory:

- **books.json**: Stores information about books.
- **checkouts.json**: Stores information about book checkouts.
- **users.json**: Stores information about users.

### Classes and Objects

#### Book
Represents a book in the library.

- **Attributes**: `title`, `author`, `isbn`, `available`

#### User
Represents a user of the library.

- **Attributes**: `name`, `user_id`

#### Checkout
Represents a checkout record for a book.

- **Attributes**: `user_id`, `isbn`

#### Storage
Handles loading and saving data to JSON files.

- **Attributes**: `file_path`

## How to Run

1. **Ensure Python 3.x is installed**.
2. **Navigate to the `src/` directory**.
3. **Run `main.py`**: 
    ```sh
    python main.py
    ```

## Usage

Follow the on-screen/terminal menu to interact with the system. Enter the corresponding number to perform the desired operation.
