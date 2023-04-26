import pandas as pd
import yfinance as yf

# Define the FTSE100 components
ftse100_components = [
'III.L', 'ABDN.L', 'ADM.L', 'AAF.L', 'AAL.L', 'ANTO.L', 'AHT.L', 'ABF.L', 'AZN.L', 'AUTO.L',
'AV.L', 'BME.L', 'BA.L', 'BARC.L', 'BDEV.L', 'BEZ.L', 'BKG.L', 'BP.L', 'BATS.L', 'BLND.L',
'BT-A.L', 'BNZL.L', 'BRBY.L', 'CNA.L', 'CCH.L', 'CPG.L', 'CTEC.L', 'CRH.L', 'CRDA.L', 'DCC.L',
'DGE.L', 'EDV.L', 'ENT.L', 'EXPN.L', 'FCIT.L', 'FLTR.L', 'FRAS.L', 'FRES.L', 'GLEN.L', 'GSK.L',
'HLN.L', 'HLMA.L', 'HL.L', 'HSX.L', 'HSBA.L', 'IHG.L', 'IMB.L', 'INF.L', 'IAG.L', 'ITRK.L',
'JD.L', 'JMAT.L', 'KGF.L', 'LAND.L', 'LGEN.L', 'LLOY.L', 'LSEG.L', 'MNG.L', 'MRO.L', 'MNDI.L',
'NG.L', 'NWG.L', 'NXT.L', 'OCDO.L', 'PSON.L', 'PSH.L', 'PSN.L', 'PHNX.L', 'PRU.L', 'RKT.L',
'REL.L', 'RTO.L', 'RMV.L', 'RIO.L', 'RR.L', 'RS1.L', 'SGE.L', 'SBRY.L', 'SDR.L', 'SMT.L',
'SGRO.L', 'SVT.L', 'SHEL.L', 'SMDS.L', 'SMIN.L', 'SN.L', 'SKG.L', 'SPX.L', 'SSE.L', 'STAN.L',
'STJ.L', 'TW.L', 'TSCO.L', 'ULVR.L', 'UU.L', 'UTG.L', 'VOD.L', 'WEIR.L', 'WTB.L', 'WPP.L'
]

# Define the date range for the data you want to fetch
start_date = '2014-01-01'
end_date = '2022-12-31'

# Fetch historical stock data for each Stoxx component
stox_data = {}
for ticker in ftse100_components:
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        stox_data[ticker] = data

# Combine the data into a single DataFrame
ftse_df = pd.concat(stox_data, axis=1)

# Extract the company name and ticker from the column names
company_names = [col.split('.')[0] for col in ftse_df.columns]
tickers = [col.split('.')[1] for col in ftse_df.columns]

# Rename the columns to include the company name and ticker
ftse_df.columns = pd.MultiIndex.from_arrays([company_names, tickers, ftse_df.columns.get_level_values(1)])

# Extract the close price for each company
close_df = ftse_df.xs('Close', level=1, axis=1)

# Save the data to an Excel file
close_df.to_excel('ftse100.xlsx')
