# Climate Change – Rising Sea Level Analysis

## Introduction
####
Our team decided to focus on Climate Change, specifically the impact rising sea levels will have on coastal US States. 
We want to understand how the ‘StormEvents’ historical data from an enviornmental government website can be leveraged in order to predict which coastal state 
will be submerged underwater via frequent flooding and land erosion events. By focusing on the frequent flooding data measurements of rising water levels and the frequency of incident type (floods) 
we can leverage this data to create a linear regression model in order to predict which state will experience submersion over X-AMOUNT of time.

## Reason why this topic was selected? 
####
The team decided to focus on this topic due to the direct impact this type of event would have on NJ since we are all current residents and want to put our Data Science skills to the test 
in order to see how soon such an event could occur.

## First Steps
####
We collected data sets from the National Centers for Environmental Information Government website (National Centers for Environmental Information (NCEI) [https://www.ncei.noaa.gov/], 
who is the Nation’s leading authority for environmental data, and manage one of the largest archives of atmospheric, coastal, geophysical, and oceanic research in the world. 
The csv files contain 10+ years (2010-2021) of information which we feel is a sufficient historical view that can be leveraged in order to predict a future outcome. 
Some of the columns that we are reviewing are “State”, “IncidentType”, and “IncidentBeginDate”. The plan is to utilize a Linear Regression model in order to quantify the amount of water 
that rose historically and predict how much more water will rise over the next 10 years based upon the frequency of flooding events.

## Technologies In Use
####
PostgreSQL, pandas, VSCode, Jupyter Notebook, PGAdmin, MongoDB, and Machine Learning. 
