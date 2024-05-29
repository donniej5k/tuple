from datetime import datetime

def average_closing_price(stock_data, stock_symbol, start_date, end_date):
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Filter data for the specified stock symbol and date range
    filtered_data = [
        closing_price
        for symbol, date, closing_price in stock_data
        if symbol == stock_symbol and start_date <= datetime.strptime(date, "%Y-%m-%d") <= end_date
    ]

    # Calculate the average closing price
    if filtered_data:
        average_price = sum(filtered_data) / len(filtered_data)
    else:
        average_price = 0  # or return None, or handle as needed for no data case

    return average_price

# Sample Data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

# Example usage
stock_symbol = "AAPL"
start_date = "2021-01-01"
end_date = "2021-01-02"
average_price = average_closing_price(stock_data, stock_symbol, start_date, end_date)
print(f"The average closing price of {stock_symbol} from {start_date} to {end_date} is {average_price}")
