import pandas as pd
from fredapi import Fred
from config import fred_key
from functools import reduce
fred = Fred(api_key=fred_key)
import matplotlib.pyplot as plt

# fred_indexes = ["EMRATIO","UNEMPLOY", 'JTSJOL', 'JTS3000JOL', 'JTS6000JOL',
# 'JTS9000JOL', 'CUSR0000SAF112','JTU5100JOL','JTU5200JOL']

fred_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","GS10","M2SL","M1SL", "CSUSHPINSA",
"CIVPART","PSAVERT","CES0500000003", "TOTALSA"]

### we used a python library call fred api to query the API endpoint and create dataframes
dataframes = []
### loop thru all the different indexes and create a dataframe for each 
for ind in fred_indexes:
    df = pd.DataFrame(fred.get_series(ind, observation_start='2000-1-1'))
    df.index.names = ['date']
    dataframes.append(df)

counter = 0
for dataframe in dataframes:
   counter = counter + 1

### merge/join the dataframes on the date 
combined = reduce(lambda x, y: pd.merge(x, y, on='date'), dataframes)
combined.columns = fred_indexes
combined.to_csv("Resources/combine.csv")

### SVR model
df = combined

# use pandas library to randomly sample data from the dataset
## sklean has "test train split", this function randomly samples the data and splits into 2 groups 
## a treatment group and a control group or a training group for the model and a test group for the model
from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size = 0.3)

# we remove the unemployment because we are trying to predict it 
x_train = train.drop('UNRATE', axis=1)
y_train = train['UNRATE']

x_test = test.drop('UNRATE', axis = 1)
y_test = test['UNRATE']

# scale all the date which is all numerical values (no categorical) to values between zero and one
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

x_train_scaled = scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_train_scaled)

x_test_scaled = scaler.fit_transform(x_test)
x_test = pd.DataFrame(x_test_scaled)


from sklearn.svm import SVR
# most important SVR parameter is Kernel type. 
# It can be #linear,polynomial or gaussian SVR. We have a non-linear condition 
# #so we can select polynomial or gaussian but here we select RBF(a #gaussian type) kernel.

regressor = SVR(kernel='rbf')
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

score=regressor.score(x_train,y_train)
print("model score")
print(score)

# Visualizations
import plotly.graph_objects as go # for data visualization
import plotly.express as px # for data visualization

# # Create a scatter plot
fig = px.scatter(df, x=df['M1SL'], y=df['UNRATE'], 
opacity=0.8, color_discrete_sequence=['black'])

# Change chart background color
fig.update_layout(dict(plot_bgcolor = 'white'))

# Update axes lines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', 
zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', 
showline=True, linewidth=1, linecolor='black')

fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', 
zeroline=True, zerolinewidth=1, zerolinecolor='lightgrey', 
showline=True, linewidth=1, linecolor='black')

# Set figure title
fig.update_layout(title=dict(text="What is related to unemployment", 
font=dict(color='black')))

# Update marker size
fig.update_traces(marker=dict(size=3))

fig.show()
