import json
from utility.logging_util import setup_logger

# Set up the logger for this module
logger = setup_logger('storage', 'logs/storage.log')

class Storage:

    """
    Storage class for file storage & retrieval in JSON format.
    
    Attributes:
        file_path (str): JSON file path for storing data.
    """

    def __init__(self, file_path):

        """
        Initialize the Storage object
        """

        self.file_path = file_path
        logger.info(f"Storage initialized with file path: {self.file_path}")

    def load_data(self):

        """
        Load data from the JSON file.
        """

        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                logger.info(f"Data loaded from file: {self.file_path}")
                return data
        except FileNotFoundError:
            logger.error(f"File not found: {self.file_path}")
            return []
        except json.JSONDecodeError:
            logger.error(f"JSON decode error in file: {self.file_path}")
            return []

    def save_data(self, data):

        """
        Save data to JSON file.
        """

        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f"Data saved to file: {self.file_path}")
