import time
from src.api.exchange_api import ExchangeAPI
from src.strategies.basic_strategy import (
    should_buy,
    moving_average_crossover,
    rsi_strategy,
)
from src.portfolio import Portfolio
from src.utils.logger import logger


class TradingBot:
    def __init__(self, api_key, api_secret, passphrase, initial_balance=1000):
        """
        Initialize the trading bot.

        :param api_key: API key for the exchange.
        :param api_secret: API secret for the exchange.
        :param passphrase: API passphrase for the exchange.
        :param initial_balance: Initial balance for the portfolio (default: 1000).
        """
        self.api = ExchangeAPI(api_key, api_secret, passphrase)
        self.portfolio = Portfolio(initial_balance)
        self.historical_prices = []
        logger.info("Trading bot initialized.")

    def run(self, symbol, amount, threshold, poll_interval):
        """
        Run the trading bot.

        :param symbol: Trading pair (e.g., 'BTC/USD').
        :param amount: Amount to buy/sell per trade.
        :param threshold: Threshold for price drop strategy (e.g., 0.05 for 5%).
        :param poll_interval: Time interval (in seconds) between price checks.
        """
        logger.info(f"Starting bot for {symbol} with threshold {threshold}.")
        while True:
            try:
                # Fetch the latest price
                price = self.api.fetch_price(symbol)
                self.historical_prices.append(price)

                # Keep only the last 100 prices
                if len(self.historical_prices) > 100:
                    self.historical_prices.pop(0)

                # Evaluate strategies
                self._evaluate_strategies(symbol, amount, price, threshold)

                # Log portfolio value
                portfolio_value = self.portfolio.get_value({symbol: price})
                logger.info(f"Portfolio value: {portfolio_value}")

            except Exception as e:
                logger.error(f"Error in bot execution: {e}")

            # Wait before the next iteration
            time.sleep(poll_interval)

    def _evaluate_strategies(self, symbol, amount, price, threshold):
        """
        Evaluate all trading strategies and execute trades if conditions are met.

        :param symbol: Trading pair (e.g., 'BTC/USD').
        :param amount: Amount to buy/sell per trade.
        :param price: Current price of the asset.
        :param threshold: Threshold for price drop strategy.
        """
        # Strategy 1: Price Drop
        if should_buy(self.historical_prices, threshold):
            logger.info(f"Price drop strategy: Buying {amount} {symbol}.")
            self._execute_trade(symbol, amount, price, "buy")

        # Strategy 2: Moving Average Crossover
        if moving_average_crossover(short_window=10, long_window=50, historical_prices=self.historical_prices):
            logger.info(f"Moving average crossover strategy: Buying {amount} {symbol}.")
            self._execute_trade(symbol, amount, price, "buy")

        # Strategy 3: RSI Strategy
        if rsi_strategy(self.historical_prices, period=14, buy_threshold=30):
            logger.info(f"RSI strategy: Buying {amount} {symbol}.")
            self._execute_trade(symbol, amount, price, "buy")

    def _execute_trade(self, symbol, amount, price, side):
        """
        Execute a trade (buy or sell).

        :param symbol: Trading pair (e.g., 'BTC/USD').
        :param amount: Amount to buy/sell.
        :param price: Current price of the asset.
        :param side: 'buy' or 'sell'.
        """
        try:
            if side == "buy":
                self.portfolio.buy(symbol, amount, price)
            elif side == "sell":
                self.portfolio.sell(symbol, amount, price)
            logger.info(f"Trade executed: {side} {amount} {symbol} at {price}.")
        except Exception as e:
            logger.error(f"Failed to execute trade: {e}")