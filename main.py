import json
from src.bot import TradingBot

# Load config
with open('config/config.json') as f:
    config = json.load(f)

# Initialize and run the bot
bot = TradingBot(config['api_key'], config['api_secret'], config['passphrase'])
bot.run(symbol='BTC/USD', amount=0.001, threshold=0.05, poll_interval=60)
