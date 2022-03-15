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
from datetime import datetime
import datetime

# # time series plot for multiple columns
start_date = '2000-01-01'
end_date =  '2022-03-09'
dates = pd.date_range(start_date, end_date, freq='MS')
fig = go.FigureWidget()
fig.update_layout(title="Rate Comparison")
graph_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","INTDSRUSM193N","T10YIEM","TB3MS", "CPALTT01USM657N",
"CIVPART","PSAVERT","MPRIME", "LNS14000006"]
for d in graph_indexes:
    # scrape API to dataframe
    df = pd.DataFrame(fred.get_series(d, observation_start='2000-1-1'))
    df.index.names = ['date']

    # convert dataframe to list
    df_list = df.values.tolist()

    # flatten list
    df_list = [item for subl in df_list for item in subl]

    # add index to graph
    fig.add_scatter(x=dates, y= df_list, name = d, selected=None)
    fig.layout.xaxis.tickvals = pd.date_range(start_date, end_date, freq='MS')
    ## make the ticks bold      
    # fig.layout.xaxis.tickformat = '%Y'
    # fig.layout.xaxis.tickvals = ['2000-01-01','2007-01-01', '2007-09-01', '2008-01-01', '2008-09-01', '2009-01-01', '2010-01-01', '2011-01-01',   '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2022-03-09']
    # fig.layout.xaxis.ticktext =  ['2000','2007', 'Financial Crisis Starts', '2008', 'Financial Crisis Ends', '2009', '2010', '2011',  '2012', '2013', '2014', '2015', '2016','2022-03-09']

# dump graph to html
fig.write_html("Event_Impact_new.html")