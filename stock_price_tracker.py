import yfinance as yf
from datetime import datetime

# Define stock symbol
stock_symbol = "VFV.TO"

# Fetch historical data for January 20, 2017 and today
start_date = "2017-01-20"
end_date = datetime.today().strftime('%Y-%m-%d')

# Get stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Get price on January 20, 2017
price_on_jan_20 = stock_data.loc["2017-01-20", "Close"] if "2017-01-20" in stock_data.index else None

# Get the current price (most recent data)
current_price = stock_data["Close"].iloc[-1]

# Print the results
print(f"Stock price of {stock_symbol} on January 20, 2017: {price_on_jan_20}")
print(f"Stock price of {stock_symbol} as of today: {current_price}")
