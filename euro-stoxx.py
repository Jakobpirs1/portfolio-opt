import pandas as pd
import yfinance as yf

# Define the euro50 components
euro50_components = [
'ADS.DE', 'AI.PA', 'AIR.PA', 'ALV.DE', 'AMS.MC', 'ABI.BR', 'ASML.AS', 'CS.PA', 'BBVA.MC', 'SAN.MC',
'BAS.DE', 'BAYN.DE', 'BMW.DE', 'BNP.PA', 'CRH.L', 'MBG.DE', 'BN.PA', 'DB1.DE', 'DPW.DE', 'DTE.DE',
'ENEL.MI', 'ENGI.PA', 'ENI.MI', 'EL.PA', 'FRE.DE', 'IBE.MC', 'ITX.MC', 'INGA.AS', 'ISP.MI', 'KER.PA',
'AD.AS', 'PHIA.AS', 'LIN.DE', 'OR.PA', 'MC.PA', 'MUV2.DE', 'NOKIA.HE', 'ORA.PA', 'SAF.PA', 'SAN.PA',
'SAP.DE', 'SU.PA', 'SIE.DE', 'GLE.PA', 'TEF.MC', 'TTE.PA', 'UNA.AS', 'DG.PA', 'VIV.PA', 'VOW3.DE'
]



# Define the date range for the data you want to fetch
start_date = '2014-01-01'
end_date = '2022-12-31'

# Fetch historical stock data for each Stoxx component
stox_data = {}
for ticker in euro50_components:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        stox_data[ticker] = data

# Combine the data into a single DataFrame
euro_df = pd.concat(stox_data, axis=1)

# Extract the company name and ticker from the column names
company_names = [col.split('.')[0] for col in euro_df.columns]
tickers = [col.split('.')[1] for col in euro_df.columns]

# Rename the columns to include the company name and ticker
euro_df.columns = pd.MultiIndex.from_arrays([company_names, tickers, euro_df.columns.get_level_values(1)])

# Extract the close price for each company
close_df = euro_df.xs('Close', level=1, axis=1)

# Save the data to an Excel file
close_df.to_excel('euro50.xlsx')
