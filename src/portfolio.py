class Portfolio:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.holdings = {}  # Dictionary to store assets and their quantities

    def buy(self, symbol, amount, price):
        cost = amount * price
        if cost > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + amount

    def sell(self, symbol, amount, price):
        if symbol not in self.holdings or self.holdings[symbol] < amount:
            raise ValueError("Insufficient holdings.")
        self.balance += amount * price
        self.holdings[symbol] -= amount
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]

    def get_value(self, prices):
        total_value = self.balance
        for symbol, amount in self.holdings.items():
            total_value += amount * prices.get(symbol, 0)
        return total_value