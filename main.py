from src.bot import TradingBot
from src.backtester import Backtester
from src.utils.config_manager import ConfigManager

if __name__ == "__main__":
    config = ConfigManager()

    # Run the trading bot
    bot = TradingBot(
        api_key=config.get('api_key'),
        api_secret=config.get('api_secret'),
        passphrase=config.get('passphrase')
    )
    bot.run(
        symbol=config.get('symbol'),
        amount=config.get('amount'),
        threshold=config.get('threshold'),
        poll_interval=config.get('poll_interval')
    )

    # Run the backtester
    backtester = Backtester()
    backtester.run(threshold=config.get('threshold'))