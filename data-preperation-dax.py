import yfinance as yf

start_date = '2017-01-01'
end_date = '2022-12-31'

# Download dax index data
dax_index = yf.download('^GDAXI', start=start_date, end=end_date)

# Save the data to a CSV file
dax_index.to_csv('dax.csv')
