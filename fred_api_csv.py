import pandas as pd
from fredapi import Fred
from config import fred_key
from functools import reduce
fred = Fred(api_key=fred_key)

# Federal Funds Effective Rate: FEDFUNDS
# Consumer Price Index for All Urban Consumers: All Items in U.S. City Average: CPIAUCSL
# Unemployment Rate: UNRATE
# Market Yield on U.S. Treasury Securities at 10-Year Constant Maturity: GS10
# # M2: M2SL
# M1: M1SL
# S&P/Case-Shiller U.S. National Home Price Index: CSUSHPINSA
# Labor Force Participation Rate: CIVPART
# Personal Saving Rate: PSAVERT
# Average Hourly Earnings of All Employees, Total Private: CES0500000003
# Total Vehicle Sales: TOTALSA

fred_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","GS10","M2SL","M1SL", "CSUSHPINSA",
"CIVPART","PSAVERT","CES0500000003", "TOTALSA"]

dataframes = []
for ind in fred_indexes:
    df = pd.DataFrame(fred.get_series(ind, observation_start='2000-1-1'))
    df.index.names = ['date']
    dataframes.append(df)

counter = 0
for dataframe in dataframes:
    print(fred_indexes[counter])
    print(df.head())
    print(df.tail())
    counter = counter + 1

combined = reduce(lambda x, y: pd.merge(x, y, on='date'), dataframes)
combined.columns = fred_indexes
combined.to_csv("Resources/combine.csv")
