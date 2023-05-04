import pandas as pd
import yfinance as yf

# Define the sp100 components
sp100_components = [
    'AAPL', 'ABBV', 'ABT', 'ACN', 'ADBE', 'AIG', 'AMD', 'AMGN', 'AMT', 'AMZN',
    'AVGO', 'AXP', 'BA', 'BAC', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK-B', 'C',
    'CAT', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CRM', 'CSCO', 'CVS',
    'CVX', 'DHR', 'DIS', 'DOW', 'DUK', 'EMR', 'EXC', 'F', 'FDX', 'GD',
    'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS', 'HD', 'HON', 'IBM', 'INTC',
    'JNJ', 'JPM', 'KHC', 'KO', 'LIN', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ',
    'MDT', 'MET', 'META', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'NEE', 'NFLX', 'NKE',
    'NVDA', 'ORCL', 'PEP', 'PFE', 'PG', 'PM', 'PYPL', 'QCOM', 'RTX', 'SBUX',
    'SCHW', 'SO', 'SPG', 'T', 'TGT', 'TMO', 'TMUS', 'TSLA', 'TXN', 'UNH', 'UNP',
    'UPS', 'USB', 'V', 'VZ', 'WBA', 'WFC', 'WMT', 'XOM']

len(sp100_components)



# Define the date range for the data you want to fetch
start_date = '2014-01-01'
end_date = '2022-12-31'

# Fetch historical stock data for each Stoxx component
stox_data = {}
for ticker in sp100_components:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        stox_data[ticker] = data

# Combine the data into a single DataFrame
sp_df = pd.concat(stox_data, axis=1)

# Extract the company name and ticker from the column names
company_names = [col.split('.')[0] for col in sp_df.columns]
tickers = [col.split('.')[1] for col in sp_df.columns]

# Rename the columns to include the company name and ticker
sp_df.columns = pd.MultiIndex.from_arrays([company_names, tickers, sp_df.columns.get_level_values(1)])

# Extract the close price for each company
close_df = sp_df.xs('Close', level=1, axis=1)

# Save the data to an Excel file
close_df.to_excel('sp500.xlsx')
