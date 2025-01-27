from src.strategies.basic_strategy import should_buy, moving_average_crossover, rsi_strategy

class TradingBot:
    def __init__(self, api_key, api_secret, passphrase):
        self.api = ExchangeAPI(api_key, api_secret, passphrase)
        self.historical_prices = []
        logger.info("Trading bot initialized.")

    def run(self, symbol, amount, threshold, poll_interval):
        logger.info(f"Starting bot for {symbol} with threshold {threshold}.")
        while True:
            try:
                price = self.api.fetch_price(symbol)
                self.historical_prices.append(price)
                if len(self.historical_prices) > 100:  # Keep last 100 prices
                    self.historical_prices.pop(0)

                # Evaluate strategies
                if should_buy(self.historical_prices, threshold):
                    logger.info(f"Price drop strategy: Buying {amount} {symbol}.")
                    # Place buy order here

                if moving_average_crossover(short_window=10, long_window=50, historical_prices=self.historical_prices):
                    logger.info(f"Moving average crossover strategy: Buying {amount} {symbol}.")
                    # Place buy order here

                if rsi_strategy(self.historical_prices, period=14, buy_threshold=30):
                    logger.info(f"RSI strategy: Buying {amount} {symbol}.")
                    # Place buy order here

            except Exception as e:
                logger.error(f"Error in bot execution: {e}")
            time.sleep(poll_interval)