import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

# Load API credentials
load_dotenv("config/.env")

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError("❌ API Key or Secret is missing! Check config/.env")

# Coinbase API requires a timestamp in the signature
timestamp = str(int(time.time()))

# Coinbase requires an HMAC-SHA256 signature
message = timestamp + "GET" + "/v2/user"
signature = hmac.new(
    API_SECRET.encode(), message.encode(), hashlib.sha256
).hexdigest()

headers = {
    "CB-ACCESS-KEY": API_KEY,
    "CB-ACCESS-SIGN": signature,
    "CB-ACCESS-TIMESTAMP": timestamp,
    "CB-VERSION": "2023-01-01"
}

# Send authentication request
response = requests.get("https://api.coinbase.com/v2/user", headers=headers)

print("HTTP Status Code:", response.status_code)
print("Raw Response:", response.text)