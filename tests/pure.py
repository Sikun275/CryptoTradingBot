from coinbase.rest import RESTClient
import json
from json import dumps

client = RESTClient(key_file="config/cdp_api_key.json")


accounts = client.get_accounts()
#print(dumps(accounts.to_dict(), indent=2))
'''
# Filter accounts with a non-zero balance
accounts_with_money = [
    account for account in accounts.data if float(account.balance.amount) > 0
]

print(dumps([account.to_dict() for account in accounts_with_money], indent=2))
'''


'''
with open("config/uuid.json", "r") as file:
    data = json.load(file)
uuid = data.get("uuid", "uuid not found")
print(uuid)


pro = client.get_portfolio_breakdown(uuid)
print(dumps(pro.to_dict(), indent=2))

'''


product = client.get_product("BTC-USD")
print(product.price)

product = client.get_product("DOGE-USD")
print(product.price)

product = client.get_product("ADA-USD")
print(product.price)