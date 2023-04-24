import pandas as pd
import yfinance as yf

# Define the Euro Stoxx 50 components
stoxx50_components = ['ABI.BR', 'AD.AS', 'ADS.DE', 'ADYEN.AS', 'AI.PA', 'AIR.PA', 'ALV.DE', 'ASML.AS', 'BAS.DE', 'BAYN.DE', 'BBVA.MC', 'BMW.DE', 'BN.PA', 'BNP.PA', 'CRG.IR', 'CS.PA', 'DB1.DE', 'DG.PA', 'DPW.DE', 'DTE.DE', 'EL.PA', 'ENEL.MI', 'ENI.MI', 'FLTR.IR', 'IBE.MC', 'IFX.DE', 'INGA.AS', 'ISP.MI', 'ITX.MC', 'KER.PA', 'KNEBV.HE', 'LIN.DE', 'MBG.DE', 'MC.PA', 'MUV2.DE', 'OR.PA', 'PHIA.AS', 'PRX.AS', 'RI.PA', 'RMS.PA', 'SAF.PA', 'SAN.MC', 'SAN.PA', 'SAP.DE', 'SIE.DE', 'STLA.MI', 'SU.PA', 'TTE.PA', 'VNA.DE', 'VOW.DE']

# Define the date range for the data you want to fetch
start_date = '2015-01-01'
end_date = '2022-12-31'

# Fetch historical stock data for each Stoxx component
stox_data = {}
for ticker in stoxx50_components:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        stox_data[ticker] = data

# Combine the data into a single DataFrame
stox_df = pd.concat(stox_data, axis=1)

# Extract the company name and ticker from the column names
company_names = [col.split('.')[0] for col in stox_df.columns]
tickers = [col.split('.')[1] for col in stox_df.columns]

# Rename the columns to include the company name and ticker
stox_df.columns = pd.MultiIndex.from_arrays([company_names, tickers, stox_df.columns.get_level_values(1)])

# Extract the close price for each company
close_df = stox_df.xs('Close', level=1, axis=1)

# Save the data to an Excel file
close_df.to_excel('stox_data123.xlsx')
