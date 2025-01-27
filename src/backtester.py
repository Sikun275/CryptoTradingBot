import pandas as pd
from src.strategies.basic_strategy import should_buy
from src.utils.logger import logger

class Backtester:
    def __init__(self, historical_data_file='data/historical_data.csv'):
        self.historical_data = self._load_data(historical_data_file)
        logger.info("Backtester initialized.")

    def _load_data(self, file):
        try:
            data = pd.read_csv(file)
            data['date'] = pd.to_datetime(data['date'])
            return data
        except Exception as e:
            logger.error(f"Failed to load historical data: {e}")
            raise

    def run(self, threshold=0.05):
        historical_prices = self.historical_data['price'].tolist()
        for i in range(1, len(historical_prices)):
            if should_buy(historical_prices[:i+1], threshold):
                logger.info(f"Buy signal at {self.historical_data.iloc[i]['date']} for price {historical_prices[i]}.")