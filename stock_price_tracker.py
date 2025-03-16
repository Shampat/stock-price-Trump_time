import yfinance as yf
from datetime import datetime

# List of stock symbols
stock_symbols = ["VFV.TO", "XSP.TO", "ZSP.TO"]

# Fetch historical data for January 20, 2017 and today
start_date = "2017-01-20"
end_date = datetime.today().strftime('%Y-%m-%d')

# Loop through each stock symbol and get the price data
for symbol in stock_symbols:
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    
    # Get the price on January 20, 2017
    price_on_jan_20 = stock_data.loc["2017-01-20", "Close"] if "2017-01-20" in stock_data.index else None
    
    # Get the current price (most recent data)
    current_price = stock_data["Close"].iloc[-1]
    
    print(f"Stock price of {symbol} on January 20, 2017: {price_on_jan_20}")
    print(f"Stock price of {symbol} as of today: {current_price}")
    print()
