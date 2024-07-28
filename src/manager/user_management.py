from models.models import User
from database.storage import Storage
from utility.logging_util import setup_logger

# Initialize logger for user management
logger = setup_logger('user_management', 'logs/user_management.log')

class UserManager:

    """
    Manages the operations related to users, such as adding, listing, searching,
    updating, and deleting users. It also checks if a user exists.
    """

    def __init__(self, storage_file='data/users.json'):

        """
        Initializes the UserManager with a storage file for users.
        """

        self.storage = Storage(storage_file)
        self.users = [User.from_dict(user) for user in self.storage.load_data()]
        logger.info("UserManager initialized")

    def add_user(self, name, user_id):

        """
        Adds a new user to the system.
        """

        new_user = User(name, user_id)
        self.users.append(new_user)
        self.save_users()
        logger.info(f"User added: {name}, {user_id}")

    def list_users(self):

        """
        Lists all users in the system.
        """

        for user in self.users:
            print(user.to_dict())
        logger.info("Users listed")

    def search_users(self, attribute, value):

        """
        Searches for users based on a given attribute and value.
        """

        results = [user for user in self.users if getattr(user, attribute, None) == value]
        logger.info(f"Users searched by {attribute}: {value}")
        return results

    def update_user(self, user_id, name=None):

        """
        Updates the name of a user.
        """

        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                self.save_users()
                logger.info(f"User updated: {user_id}, {name}")
                return user
        logger.warning(f"User not found for update: {user_id}")
        return None

    def delete_user(self, user_id):

        """
        Deletes a user from the system.
        """

        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_users()
        logger.info(f"User deleted: {user_id}")

    def save_users(self):

        """
        Saves the current list of users to the storage file.
        """

        self.storage.save_data([user.to_dict() for user in self.users])
        logger.info("Users saved")

    def user_exists(self, user_id):

        """
        Checks if a user exists in the system.
        """

        exists = any(user.user_id == user_id for user in self.users)
        logger.info(f"User existence checked: {user_id} - Exists: {exists}")
        return exists
