import os
import requests
from dotenv import load_dotenv

# Load API credentials
load_dotenv("config/.env")

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("❌ API Key is missing! Check config/.env")

# Set up headers (OAuth-style authentication for Coinbase Retail)
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "CB-VERSION": "2023-01-01"  # Coinbase requires API version
}

# Test connection to Coinbase API
print("🔄 Checking connection to Coinbase API...\n")

try:
    response = requests.get("https://api.coinbase.com/v2/user", headers=headers)

    print(f"HTTP Status Code: {response.status_code}")
    print("Raw Response:", response.text)

    if response.status_code == 200:
        print("✅ Successfully connected to Coinbase API!")
    else:
        print("❌ Failed to connect. Check API credentials and permissions.")

except requests.exceptions.RequestException as e:
    print(f"❌ Connection error: {e}")