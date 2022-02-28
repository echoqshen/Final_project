
# Climate Change – Rising Sea Level Analysis

## Introduction
####
Our team decided to focus on Climate Change, specifically the impact rising sea levels will have on coastal US States. 

## Reason why this topic was selected? 
####
The team decided to focus on this topic due to the direct impact this type of event would have on NJ since we are all current residents and want to put our Data Science skills to the test in order to see how soon such an event could occur.

## First Steps
####
We collected data sets from the National Centers for Environmental Information Government website (National Centers for Environmental Information (NCEI) [https://www.ncei.noaa.gov/], who is the Nation’s leading authority for environmental data, and manage one of the largest archives of atmospheric, coastal, geophysical, and oceanic research in the world. The csv files contain 10+ years (2010-2021) of information which we feel is a sufficient historical view that can be leveraged in order to predict a future outcome. Some of the columns that we are reviewing are “State”, “IncidentType”, and “IncidentBeginDate”. The plan is to utilize a Linear Regression model in order to quantify the amount of water that rose historically and predict how much more water will rise over the next 10 years based upon the frequency of flooding events.

## Technologies In Use
####
In this project we will be using the following: PostgreSQL, Pandas, VSCode, Jupyter Notebook, PGAdmin, MongoDB, Python, and machine learning. Along with the physical code for the project, we have opted to use a branch protection rule within Github to make secure and accurate pull requests. This rule requires two individuals within the group to approve any pull requests that are submitted before the branches can be merged with the added updates. 

## Our Roadmap
The main question we would like to answer is which coastal state may be the most in danger of being submerged the soonest based on the data collected regarding rising sea levels. Since our data spans almost a decade, we intend to make a prediction into the next decade.

We plan to create an interactive map API to display how an area will be affected by the increase in sea level.

Another question we hope to explore is if sea level change has any correlation to global economic activity. Does a higher increase in sea level affect economic activty across the world in any way? Our intitial hypothesis is that there is NO correlation between them.

## Machine Learning Model
####
Because we have an idea of what we are looking for and what our output should be, we intend to use a Supervised Classification Machine Learning model. The specific machine learning model we plan to use to answer our question is a Logistic Regression model. Despite its name, Logistic Regression is not a regression model, but rather a classification model. In Logistic Regression, the outcome is binary (i.e. Yes or No). Since the question we are trying to answer is whether or not certain coastal US states will be submerged due to natural disasters causing rising sea levels, it fits the binary aspect that this model is used for. Logistic Regression also results in a linear final product. This fits our project because we plan to use data from the previous decade (2010-2021) and predict how when a coastal state may submerge based on the linear increase of rising sea level throughout the years into the next decade.


