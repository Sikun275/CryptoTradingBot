import os
import requests
from dotenv import load_dotenv

# Load API credentials
load_dotenv("config/.env")

API_KEY = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "CB-ACCESS-KEY": API_KEY,
    "CB-VERSION": "2023-01-01"
}

# Fetch accounts (Advanced Trade API)
response = requests.get("https://api.coinbase.com/api/v3/brokerage/accounts", headers=headers)

print(f"HTTP Status Code: {response.status_code}")
print("Raw Response:", response.json())