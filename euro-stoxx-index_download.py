import yfinance as yf

start_date = '2014-01-01'
end_date = '2023-05-01'

# Download EURO STOXX 50 index data
aaa = yf.download('CRH', start=start_date, end=end_date)

# Save the data to a CSV file
aaa.to_csv('CRH.csv')
