'''
Strategies include:
    - moving average crossover
    - RSI (Relative Strength Index)

'''


import numpy as np

def should_buy(historical_prices, threshold=0.05):
    if len(historical_prices) < 2:
        return False
    current_price = historical_prices[-1]
    previous_price = historical_prices[-2]
    price_drop = (previous_price - current_price) / previous_price
    return price_drop >= threshold

def moving_average_crossover(short_window, long_window, historical_prices):
    if len(historical_prices) < long_window:
        return False
    short_ma = sum(historical_prices[-short_window:]) / short_window
    long_ma = sum(historical_prices[-long_window:]) / long_window
    return short_ma > long_ma

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    avg_gain = np.mean(gains[:period])
    avg_loss = np.mean(losses[:period])
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def rsi_strategy(historical_prices, period=14, buy_threshold=30, sell_threshold=70):
    if len(historical_prices) < period + 1:
        return False
    rsi = calculate_rsi(historical_prices, period)
    return rsi < buy_threshold