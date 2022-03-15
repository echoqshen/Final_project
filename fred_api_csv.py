import pandas as pd
from fredapi import Fred
from config import fred_key, mongo_user, mongo_password
from functools import reduce
fred = Fred(api_key=fred_key)
from pymongo import MongoClient


# Federal Funds Effective Rate: FEDFUNDS
# Consumer Price Index for All Urban Consumers: All Items in U.S. City Average: CPIAUCSL
# Unemployment Rate: UNRATE
# Interest Rates, Discount Rate for United States: INTDSRUSM193N
# 10-Year Breakeven Inflation Rate: T10YIEM
# 3-Month Treasury Bill Secondary Market Rate: TB3MS
# Consumer Price Index: Total All Items for the United States: CPALTT01USM657N
# Labor Force Participation Rate: CIVPART
# Personal Saving Rate: PSAVERT
# Bank Prime Loan Rate: MPRIME
# Unemployment Rate - Black or African American: LNS14000006

fred_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","INTDSRUSM193N","T10YIEM","TB3MS", "CPALTT01USM657N",
"CIVPART","PSAVERT","MPRIME", "LNS14000006"]

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

# Employment-Population Ratio (EMRATIO)
# Unemployment Level (UNEMPLOY)
# Job Openings: Total Nonfarm (JTSJOL)
# Job Openings: Manufacturing (JTS3000JOL)
# Job Openings: Education and Health Services (JTS6000JOL)
# Job Openings: Government (JTS9000JOL)
# Consumer Price Index for All Urban Consumers: Meats, Poultry, Fish, and Eggs in U.S. City Average (CUSR0000SAF112)
# Job Openings: Information (JTU5100JOL)
# Job Openings: Finance and Insurance (JTU5200JOL)

fred_more = ["EMRATIO","UNEMPLOY", 'JTSJOL', 'JTS3000JOL', 'JTS6000JOL','JTU5100JOL','JTU5200JOL']
dataframes = []
for ind in fred_more:
    df = pd.DataFrame(fred.get_series(ind, observation_start='2000-1-1'))
    df.index.names = ['date']
    dataframes.append(df)

counter = 0
for dataframe in dataframes:
    print(fred_more[counter])
    print(df.head())
    print(df.tail())
    counter = counter + 1

addition = reduce(lambda x, y: pd.merge(x, y, on='date'), dataframes)
addition.columns = fred_more
addition.to_csv("Resources/additional.csv")

