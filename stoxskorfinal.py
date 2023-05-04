import pandas as pd
import yfinance as yf

# Define the sp100 components
stoxx_components = [
    'OR.PA',  # L'Oreal SA
    'DG.PA',  # Vinci SA
    'BBVA.MC',  # Banco Bilbao Vizcaya Argentaria SA
    'SAN.MC',  # Banco Santander SA
    'ASML.AS',  # ASML Holding NV
    'PHIA.AS',  # Koninklijke Philips NV
    'TEF.MC',  # Telefonica SA
    'TTE',  # TOTAL SE
    'AI.PA',  # Air Liquide SA
    'CS.PA',  # AXA SA
    'BNP.PA',  # BNP Paribas SA
    'BN.PA',  # Danone SA
    'VIV.PA',  # Vivendi SA
    'EL.PA',  # EssilorLuxottica SA
    'MC.PA',  # LVMH Moet Hennessy Louis Vuitton SE
    'KER.PA',  # Kering SA
    'AMS.MC',  # Amadeus IT Group SA
    'SAF.PA',  # Safran SA
    'AD.AS',  # Koninklijke Ahold Delhaize NV
    'UNA.AS',  # Unilever NV
    'IBE.MC',  # Iberdrola SA
    'INGA.AS',  # ING Groep NV
    'LIN',  # Linde PLC
    'ITX.MC',  # Industria de Diseno Textil SA
    'ISP.MI',  # Intesa Sanpaolo SpA
    'ENI.MI',  # Eni SpA
    'ENGI.PA',  # Engie SA
    'ORA.PA',  # Orange SA
    'ABI.BR',  # Anheuser-Busch InBev SA/NV
    'SAN.PA',  # Sanofi
    'GLE.PA',  # Societe Generale SA
    'ENEL.MI',  # Enel SpA
    'NOKIA.HE',  # Nokia Oyj
    'SU.PA',  # Schneider Electric SE
    'ALV.DE',  # Allianz SE
    'AIR.PA',  # Airbus SE
    'BAYN.DE',  # Bayer AG
    'BMW.DE',  # Bayerische Motoren Werke AG
    'CRH.L',  # CRH PLC
    'BAS.DE',  # BASF SE
    'SIE.DE',  # Siemens AG
    'VOW3.DE',  # Volkswagen AG
    'MUV2.DE',  # Munich Re
    'FRE.DE',  # Fresenius SE & Co KGaA
    'SAP.DE',  # SAP SE
    'ADS.DE',  # adidas AG
    'DTE.DE',  # Deutsche Telekom AG
    'DPW.DE',  # Deutsche Post AG
    'MBG.DE',  # Daimler AG
    'DB1.DE',  # Deutsche Boerse AG
]


len(stoxx_components)



# Define the date range for the data you want to fetch
start_date = '2014-01-01'
end_date = '2023-05-01'

# Fetch historical stock data for each Stoxx component
stox_data = {}
for ticker in stoxx_components:
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
close_df.to_excel('stox_data123.xlsx')
