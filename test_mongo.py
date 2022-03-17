from fredapi import Fred
from pymongo import MongoClient
import pandas as pd
from config import fred_key, mongo_user, mongo_password
from functools import reduce
fred = Fred(api_key=fred_key)
import matplotlib.pyplot as plt
import plotly
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import seaborn as sb


my_pass = mongo_password
user_name = mongo_user
connection_string = "mongodb+srv://" + user_name + ":" + my_pass + "@project1.q26cg.mongodb.net/project1?retryWrites=true&w=majority"

### connect to mongo 
try:
    print("connecting to mongo")
    client = MongoClient(connection_string)
    print("connected to mongo")
except Exception as e:
    print("error: " + str(e))

db = client.project1
# print(db)
collection = db.project1

### clear the collection 
collection.remove({})
for record in collection.find().limit(1):
    print(record)
print("loading df")

### load dataframes from fred API 
fred_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","INTDSRUSM193N","T10YIEM","TB3MS", "CPALTT01USM657N",
"CIVPART","PSAVERT","MPRIME", "LNS14000006"]

dataframes = []
for ind in fred_indexes:
    df = pd.DataFrame(fred.get_series(ind, observation_start='1990  -1-1'))
    df.index.names = ['date']
    dataframes.append(df)

combined = reduce(lambda x, y: pd.merge(x, y, on='date', how = 'outer'), dataframes)
combined.columns = fred_indexes
combined.reset_index(inplace = True, drop = False)
# print(combined.head(3))

### load dataframes into mongo 
collection.insert_many(combined.to_dict('records'))

### read one back 
cursor = collection.find()
# for record in cursor.limit(1):
#     print(record)

### load another collection into mongo into a different collection 
collection2 = db.project2
### clear the collection 
collection2.remove({})

fred_more = ["EMRATIO","UNEMPLOY", 'JTSJOL', 'JTS3000JOL', 'JTS6000JOL','JTU5100JOL','JTU5200JOL']
dataframes = []
for ind in fred_more:
    df1 = pd.DataFrame(fred.get_series(ind, observation_start='1990-1-1'))
    df1.index.names = ['date']
    dataframes.append(df1)

addition = reduce(lambda x, y: pd.merge(x, y, on='date', how = 'outer'), dataframes)
addition.columns = fred_more
addition.reset_index(inplace = True, drop = False)
# print(addition.head(3))

### load dataframes into mongo 
collection2.insert_many(addition.to_dict('records'))
### read one back 
cursor2=collection2.find()
# for record in cursor2.limit(1):
#     print(record)

