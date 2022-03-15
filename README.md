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
* Google Collab 
* Machine Learning

## Description of the Communication Protocols
####
The team communicates primarily via a Slack Channel. Each member was assigned a role and works on their piece of the project on their individual git branch. When they are ready to push files/updates to the main branch we have opted to use a branch protection rule within Github to make secure and accurate pull requests. 
This rule requires two individuals within the group to review and approve any pull requests that are submitted before the branches can be merged with the added updates.   

## Our Roadmap
####
We collected data sets from the Bureau of Labor Statistics website (BLS) [https://www.bls.gov/data/], a national organization that provides data on labor market activity, working conditions, proice changes, and productivity in the US economy. Additionally, we examined datasets from The Federal Reserve Bank of St. Louis' Federal Reserve Economic Database (FRED) [https://fred.stlouisfed.org/], which is one of the nation's leading trusted sources for economic data. The CSV files we retrieved contain 20+ years (2000-2021) of information which we feel is a sufficient historical view that can be leveraged in order to predict a future outcome. Some of the data columns that we are reviewing include data on educational levels, race, and gender. The plan is to utilize a Linear Regression model in order to quantify future unemployment rates and predict what the US national unemployment rate will be in general, as well as for each of the different variables, by December 2022.

For the data exploration phase, we used an API key to scrape data from the St. Louis FRED website. We selected a few reports that are related to the US unemployment rate and mapped it into a DataFrame using the reduce() method, then saved the results into a CSV file. We filtered and cleaned the data with Python to get rid of duplicate or null rows/columns of data, as then combined related categories into a single CSV (i.e. Male and Female data combined into one CSV [gender.csv]). 

Next, once all the CSVs were sorted and cleaned to only include relevant data, we created an AWS RDS cloud database and linked it to Postgres/pgAdmin4.

![aws](Graphs/aws.png)

From pgAdmin4, the SQL queries were written and executed to create the necessary tables to store the data in pgAdmin4. A table was created for each compiled CSV and their respective CSV was imported into each table. We also wrote a query to join multiple tables, strictly using the database language.

![postgresquery](Graphs/postgresquery.png)

Since this database was created a linked by one member, the other memebrs of the group are able to access the database and contents by executing the following code:

![rds_code](Graphs/rds.png)

Next, once all the CSVs have been sorted and cleaned to only include relevant data, we created an AWS RDS cloud database and linked it to Postgres/pgAdmin4. From pgAdmin4, the necessary SQL queries were written and ran to create the necessary tables to store the data in PgAdmin4. A table was created for each compiled CSV and their respective CSV was imported into each table. We also wrote a query to join two tables, using strictly the database language.

## Machine Learning Model
####
The analysis phase of this project is done through our machine learning models. Our data is primarily continuous rather than categorical. Therefore, we will not be predicting a binary outcome, but rather a numerical outcome. The prediction we are trying to make is what the unemployment rate will be at the end of December 2022 or even in the next month.

One of the machine learning models we will be implementing is the K-Nearest Neighbor (KNN) algorithm. KNN can be used for either linear regression or classification. For our analysis, we intend to use additional data (job openings for various industries and consumer prices for meats) and split them into a training and testing set. The data on job openings and meat prices will be used as the features (X) and the unemployment rate will be used as the target (Y). To confirm that this model is accurate and a good fit, we decided it will be best to use only 1 year's worth of data (Year 2001) and try to predict the next year's worth of data (Year 2002). A graph will then be generated to visualize the results. Before this though, we practiced by using the API to pull other sorts of data to see if it would work. Please refer to the <in>KNN-ML.py</in> file for reference. The code seemed to run successfully, and a graph was generated. See below for the results. We intend to revamp the code to run for the aforementioned releveant datasets next.

![KNN](Graphs/KNN.png)

We are also exploring the AutoRegressive Integrated Moving Average (ARIMA) machine learning model. This is a type of time series forecasting model. Forecasting is a popular ML method to use when you want to predict the future values the series is going to take. Depending on the frequency, a time series can be of yearly (ex: annual budget), quarterly (ex: expenses), monthly (ex: air traffic), weekly (ex: sales qty), daily (ex: weather), hourly (ex: stocks price), minutes (ex: inbound calls in a call canter) and even seconds wise (ex: web traffic). This fits our analysis since we are trying to determine the unemployment rate either at the end of this year in December 2022 or even at the end of next month, as the lowest frequency unit for unemployment rate data is typically released monthly. Please refer to the <in>arimatest.ipynb</in> file for reference. In this file, we were able to test the model out and generate a result. However, the current result was simply a trial run to confirm that the model will execute succesfully so it does not reflect what will be the final product. 

## Dashboard
####
To fully visualize the results of our analysis, we used JavaScript along with HTML and CSS to create an interactive web page that houses all the resulting graphs. 

![dashboard](Graphs/dashboard.png)
