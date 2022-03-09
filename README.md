
# US Unemployment Analysis

## Introduction
####
Our team decided to analyze US unemployment data and focus on the data from the years 2000 - 2021. 

## Why was this topic selected? 
####

We selected this topic because we are interested in the impact that major events can have on the unemployment rate fluctuation. We would like to put our data science skills to the test in order to see how the different variables influence the rate.

## Our Roadmap
####
We collected data sets from the Bureau of Labor Statistics website (BLS) [https://www.bls.gov/data/], a national organization that provides data on labor market activity, working conditions, proice changes, and productivity in the US economy. Additionally, we examined datasets from The Federal Reserve Bank of St. Louis' Federal Reserve Economic Database (FRED) [https://fred.stlouisfed.org/], which is one of the nation's leading trusted sources for economic data. The CSV files we retrieved contain 20+ years (2000-2021) of information which we feel is a sufficient historical view that can be leveraged in order to predict a future outcome. Some of the data columns that we are reviewing include data on educational levels, race, and gender. The plan is to utilize a Linear Regression model in order to quantify future unemployment rates and predict what the US national unemployment rate will be at the end of December 2022.

For the data exploration phase, we used an API key to scrape data from the St. Louis FRED website. We selected a few reports that are related to the US unemployment rate and mapped it into a DataFrame using the reduce() method, then saved the results into a CSV file. We filter and clean the data with Python to get rid of any duplicate or null rows/columns of data, as well as combine related categories into a single CSV (i.e. Male and Female data combined into one CSV [gender.csv]). 

Next, once all the CSVs have been sorted and cleaned to only include relevant data, we created the necessary tables to store the data in PgAdmin4. A table was created for each compiled CSV and their respective CSV was imported into each table. We also wrote a query to join two tables, using strictly the database language. 

## Technologies In Use
####
In this project we will be using the following: 
* PostgreSQL, 
* Pandas, 
* VSCode, 
* Jupyter Notebook, 
* PGAdmin, 
* MongoDB, 
* Python, and 
* machine learning.


##Description of the Communication Protocols
####
The team communicates primarily via a Slack Channel. Each member was assigned a role and works on their piece of the project on their individual git branch. When they are ready to push files/updates to the main branch we have opted to use a branch protection rule within Github to make secure and accurate pull requests. 
This rule requires two individuals within the group to approve any pull requests that are submitted before the branches can be merged with the added updates.   

## Machine Learning Model
####
The question we are looking to answer is: what the unemployment rate will be at the end of the end December 2022. Because our prediction is a type of forecasting, the machine learning model that appears to fit our needs is a neural network model. 

The machine learning model we will be implementing is the K-Nearest Neighbor (KNN) algorithm. KNN can be used for either linear regression or classification.



