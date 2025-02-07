import os
import json
from dotenv import load_dotenv
from src.utils.logger import logger

class ConfigManager:
    def __init__(self, config_file='config/config.json'):
        """
        Initialize the ConfigManager.

        :param config_file: Path to the config file (default: 'config/config.json').
        """
        self.config_file = config_file
        self.config = self._load_config()
        load_dotenv()  # Load environment variables from .env file
        self._load_env_vars()
        logger.info("Configuration loaded.")

    def _load_config(self):
        """
        Load configuration from the config file.

        :return: Dictionary containing the configuration.
        """
        try:
            with open(self.config_file) as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            raise

    def _load_env_vars(self):
        """
        Load sensitive information from environment variables.
        """
        self.config['api_key'] = os.getenv("API_KEY", self.config.get('api_key'))
        self.config['api_secret'] = os.getenv("API_SECRET", self.config.get('api_secret'))

    def get(self, key):
        """
        Get a configuration value by key.

        :param key: Key to retrieve from the configuration.
        :return: Value associated with the key, or None if the key doesn't exist.
        """
        return self.config.get(key)