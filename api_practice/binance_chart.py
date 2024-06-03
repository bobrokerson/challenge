from binance import Client
import matplotlib.pyplot as plt

# Initialize the Binance client
binance_client = Client()


def get_exchange(symbol: str):
    # Fetch ticker data for the given symbol
    ticker_data = binance_client.get_ticker(symbol=symbol)
    return float(ticker_data['lastPrice'])


# Define the quantities
btc_value = 0.01
xrp_value = 1000
eth_value = 0.5

# Calculate the exchange values
btc_exchange_value = btc_value * get_exchange('BTCUSDT')
xrp_exchange_value = xrp_value * get_exchange('XRPUSDT')
eth_exchange_value = eth_value * get_exchange('ETHUSDT')

# Calculate the total value and round to 3 decimal places
total_value = round(
    btc_exchange_value + xrp_exchange_value + eth_exchange_value, 3)
print("Total value:", total_value)

# Plotting the values in a pie chart
plt.pie(
    [btc_exchange_value, xrp_exchange_value, eth_exchange_value],
    labels=[
        f'BTC: {btc_exchange_value:.2f}',
        f'XRP: {xrp_exchange_value:.2f}',
        f'ETH: {eth_exchange_value:.2f}'],
    autopct='%1.1f%%'
)

plt.legend(title=f"Total value: {total_value}")
plt.show()
