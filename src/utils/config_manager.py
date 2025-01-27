import json
from src.utils.logger import logger

class ConfigManager:
    def __init__(self, config_file='config/config.json'):
        self.config_file = config_file
        self.config = self._load_config()
        logger.info("Configuration loaded.")

    def _load_config(self):
        try:
            with open(self.config_file) as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            raise

    def get(self, key):
        return self.config.get(key)