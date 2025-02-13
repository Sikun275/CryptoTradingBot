import os
import requests
from dotenv import load_dotenv
from coinbase.wallet.client import Client

# Load API keys from .env file
load_dotenv("config/.env")

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


print(f"API_KEY: {API_KEY}")
print(f"API_SECRET: {repr(API_SECRET)}")  # `repr()` shows hidden characters

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "CB-VERSION": "2023-01-01"  # Coinbase requires API version
}

# Send a direct request to check authentication
response = requests.get("https://api.coinbase.com/v2/user", headers=headers)

print("HTTP Status Code:", response.status_code)
print("Raw Response:", response.text)

# Verify API key loading
if not API_KEY or not API_SECRET:
    raise ValueError("❌ API Key or Secret is missing! Check config/.env")

# Initialize Coinbase API Client
client = Client(API_KEY, API_SECRET)

# Test API connection
try:
    user = client.get_current_user()
    print(f"✅ Successfully connected to Coinbase as: {user['name']}")
except Exception as e:
    print(f"❌ Error connecting to Coinbase API: {e}")