import yfinance as yf

start_date = '2014-01-01'
end_date = '2022-12-31'

# Download EURO STOXX 50 index data
UL = yf.download('UL', start=start_date, end=end_date)

# Save the data to a CSV file
UL.to_csv('UL.csv')
