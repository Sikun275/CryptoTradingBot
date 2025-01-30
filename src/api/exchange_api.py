import os
from dotenv import load_dotenv
from coinbase.wallet.client import Client
import ccxt
import pandas as pd
from src.utils.logger import logger


#for the API key security

# Load .env file from config directory
load_dotenv(dotenv_path="config/.env")

# Retrieve API credentials securely
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
PASSPHRASE = os.getenv("PASSPHRASE")

# Ensure the keys are loaded correctly
if not API_KEY or not API_SECRET or not PASSPHRASE:
    raise ValueError("❌ Missing API credentials. Check config/.env file.")

# Initialize Coinbase API client
client = Client(API_KEY, API_SECRET)

# Test API connection
try:
    user = client.get_current_user()
    print(f"✅ Connected to Coinbase as: {user['name']}")
except Exception as e:
    print(f"❌ Error connecting to API: {e}")

# end of API key security, need to modify the folowing code, such like the 
# 1. name consistancy 
# 2. import the correct and updated library 

class ExchangeAPI:
    def __init__(self, api_key, api_secret, passphrase):
        self.exchange = ccxt.coinbasepro({
            'apiKey': api_key,
            'secret': api_secret,
            'password': passphrase,
        })
        logger.info("Exchange API initialized.")

    def fetch_price(self, symbol):
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker['last']
        except Exception as e:
            logger.error(f"Failed to fetch price for {symbol}: {e}")
            raise

    def fetch_historical_data(self, symbol, timeframe='1h', limit=100):
        try:
            ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            logger.error(f"Failed to fetch historical data for {symbol}: {e}")
            raise