# US Unemployment Analysis

## Introduction
####
Our team decided to analyze US unemployment data and focus on the data from the years 2000 - 2021. 

## Why was this topic selected? 
####
We selected this topic because we are interested in the impact that major events can have on the unemployment rate fluctuation. We would like to put our data science skills to the test in order to see how the different variables influence the rate.

## Technologies In Use
####
In this project we will be using the following: 
* PostgreSQL 
* Pandas 
* VSCode 
* Jupyter Notebook 
* PGAdmin 
* MongoDB 
* Python 
* AWS 
* Google Colab
* PySpark 
* Machine Learning

## Our Roadmap
####
We collected data sets from the Bureau of Labor Statistics website (BLS) [https://www.bls.gov/data/], a national organization that provides data on labor market activity, working conditions, price changes, and productivity in the US economy. Additionally, we examined datasets from The Federal Reserve Bank of St. Louis' Federal Reserve Economic Database (FRED) [https://fred.stlouisfed.org/], which is one of the nation's leading trusted sources for economic data. The CSV files we retrieved contain 20+ years (2000-2021) of information which we feel is a sufficient historical view that can be leveraged in order to predict a future outcome. Some of the data columns that we are reviewing include data on educational levels, race, and gender. 

For the data exploration phase, we used an API key to scrape data from the St. Louis FRED website. We selected a few reports that are related to the US unemployment rate and mapped it into a DataFrame using the reduce() method, then saved the results into a CSV file. We filtered and cleaned the data with Python to get rid of duplicate or null rows/columns of data, as then combined related categories into a single CSV (i.e. separate CSV datasets for Male and Female data combined into one CSV [gender.csv]). 

Next, once all the CSVs were sorted and cleaned to only include relevant data, we created an AWS RDS cloud database and linked it to Postgres/pgAdmin4 using a connection string.

![aws](Graphs/aws.png)

In AWS, an S3 bucket was created where the cleaned CSVs were uploaded to house our data in the cloud. We were able to access/read these CSVs from Google Colab/PySpark. 

![pysparkS3bucket](Graphs/pysparkS3bucket.png)

From pgAdmin4, SQL queries were written and executed to create the necessary tables to store the data in Postgres/pgAdmin4. A table was created for each compiled CSV and their respective CSV was imported/written into each table via Google Colab/PySpark.

![pysparkwrite](Graphs/pysparkwrite.png)

We also wrote a query to join multiple tables, strictly using the database language.

![postgresquery](Graphs/postgresquery.png)

Though the datasets are housed in the cloud and linked to the database, the database was initially created by one member on their local machine. However, the other members of the group are easily able to access the database and contents by executing the following code:

![rds_code](Graphs/rds.png)


### Machine Learning Model
####
The analysis phase of this project is implemented through our machine learning models. Our data is primarily continuous rather than categorical. Therefore, we will not be predicting a binary outcome, but rather a numerical outcome. The prediction we are trying to make is what the unemployment rate will be at the end of December 2022 or even in the next month.

One of the machine learning models we will be implementing is the K-Nearest Neighbor (KNN) algorithm. KNN can be used for either linear regression or classification. For our analysis, we intend to use additional data (job openings for various industries and consumer prices for meats) that were pulled from the API call and split them into training and testing sets. The data on job openings and meat prices will be used as the features (X) and the unemployment rate will be used as the target (Y). To confirm that this model is accurate and a good fit, we decided it will be best to use only 1 year's worth of data (Year 2001) and try to predict the next year's worth of data (Year 2002). A graph will then be generated to visualize the results. Before this though, we practiced by using the API to pull other sorts of data to see if it would work. Please refer to the KNN-ML.py file for reference. The code seemed to run successfully, and a graph was generated. See below for the results. We intend to revamp the code to run for the aforementioned releveant datasets next.

![KNN](Graphs/KNN.png)

We are also exploring the AutoRegressive Integrated Moving Average (ARIMA) machine learning model, a type of time series forecasting model. Forecasting is a popular ML method to use when predicting the future values the series is going to take. Depending on the frequency, a time series can be of yearly (ex: annual budget), quarterly (ex: expenses), monthly (ex: air traffic), weekly (ex: sales qty), daily (ex: weather), hourly (ex: stocks price), minutes (ex: inbound calls in a call canter) and even seconds wise (ex: web traffic). This fits our analysis since unemployment rate data is typically released monthly/yearly and our intention is to predict possible values for the unemployment rate at either the end of the year in December 2022 or even at the end of next month. Please refer to the arimatest.ipynb file for reference. In this file, we were able to test the model out and generate a result. However, the current result was simply a trial run to confirm that the model will execute succesfully so it does not reflect what will be the final product. We plan to use a Time Series model to quantify future unemployment rates using singular dataset CSVs each time to predict what the US national unemployment rate will be in general, as well as for each of the different variables, by December 2022.

### Dashboard
####
To fully visualize the results of our analysis, we used JavaScript along with HTML and CSS to create an interactive web page that houses all the resulting graphs. 

![dashboard](Graphs/dashboard.png)
