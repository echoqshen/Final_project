import pandas as pd
from fredapi import Fred
from config import fred_key
from functools import reduce
fred = Fred(api_key=fred_key)

### these are indexes chosen from the fred API which has US financial data 
### these indexes contained monthly data for a reasonable lenght of time 
## we considered them likely to be correlated with unemployment levels 
# fred_indexes = ["EMRATIO","UNEMPLOY", 'JTSJOL', 'JTS3000JOL', 'JTS6000JOL',
# 'JTS9000JOL', 'CUSR0000SAF112','JTU5100JOL','JTU5200JOL']

fred_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","INTDSRUSM193N","T10YIEM","TB3MS", "CPALTT01USM657N",
"CIVPART","PSAVERT","MPRIME", "LNS14000006"]

# fred_indexes = ["UNRATE","FEDFUNDS","CPIAUCSL","GS10","M2SL","M1SL", "CSUSHPINSA",
# "CIVPART","PSAVERT","CES0500000003", "TOTALSA"]

### we used a python library call fred api to query the API endpoint and create dataframes
dataframes = []
### loop thru all the different indexes and create a dataframe for each 
for ind in fred_indexes:
    df = pd.DataFrame(fred.get_series(ind, observation_start='2000-1-1'))
    df.index.names = ['date']
    dataframes.append(df)


counter = 0
for dataframe in dataframes:
    # print(fred_indexes[counter])
    counter = counter + 1

### merge/join the dataframes on the date 
combined = reduce(lambda x, y: pd.merge(x, y, on='date'), dataframes)
combined.columns = fred_indexes
combined.to_csv("Resources/combine.csv")

### KNN REGRESSION 
df = combined
# print(df.head())

# use pandas library to randomly sample data from the dataset
## sklean has "test train split"
## this function randomly samples the data and splits into 2 groups 
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

# import the k nearest neighbors machine learning algorithm "knn" by looking for similar values to the ones we are trying to predict
from sklearn import neighbors

# from sklearn.naive_bayes import GaussianNB

# we plot the mean square error of the machine learnign results to try and pick a number of nearest neighbors that
# will work best. Too low and we overfit the data. Too high we lose predictive ability. 
# we tested and found that a value of 7 looked good there was a local minimum in the plot . 
from sklearn.metrics import mean_squared_error 
from math import sqrt
import matplotlib.pyplot as plt

rmse_val = [] #to store rmse values for different k
for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)
    model.fit(x_train, y_train)  #fit the model
    pred=model.predict(x_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    rmse_val.append(error) #store rmse values
    print('RMSE value for k= ' , K , 'is:', error)

# plotting the rmse values against k values
curve = pd.DataFrame(rmse_val) #elbow curve 
curve.plot()
plt.show()
