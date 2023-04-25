import yfinance as yf

start_date = '2015-01-01'
end_date = '2022-12-31'

# Download EURO STOXX 50 index data
stoxx50_index = yf.download('^STOXX50E', start=start_date, end=end_date)

# Save the data to a CSV file
stoxx50_index.to_csv('sx5e.csv')
