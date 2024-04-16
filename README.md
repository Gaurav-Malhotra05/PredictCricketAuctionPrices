# PredictCricketAuctionPrices

## Overview

This repository contains the code used in our research paper that develops a predictive model for the auction prices of players in the Indian Premier League (IPL). Unlike other sports leagues, the IPL has a unique auction system that makes standard prediction models inadequate. Our model leverages machine learning to predict the auction prices based on key quantitative variables, categorizing players into batsmen, bowlers, and all-rounders.

## Data Collection and Processing

The data for this project was meticulously scraped and processed from comprehensive ball-by-ball match details over several years of IPL tournaments. Here's a breakdown of our data processing steps:

1. Data Scraping
Source: Ball-by-ball data was scraped from publicly available IPL match databases.
Scope: Data includes every match played over the past several years, covering thousands of individual performances.
2. Data Cleaning and Preparation
Cleanup: Raw data was cleaned to remove inconsistencies and missing values.
Feature Engineering: Key features were extracted for each player, including total runs, wickets taken, strike rate, economy rate, and more.
3. Data Categorization
Players were classified into three categories: Batsmen, Bowlers, and All-rounders, based on their playing roles and statistics.
Machine Learning Model

Our approach employs several machine learning models to predict auction prices based on historical data and player performance metrics. The models include linear regression techniques. The steps involved include:

## Model Selection: Regression models
Training: Models were trained using historical auction prices as the target variable.
Validation and Testing: The models were rigorously validated and tested to ensure accuracy and reliability.
Predictive Analysis

The final model outputs include:

Predicted Auction Prices: Estimated market value of players based on historical data and performance metrics.
Performance Comparison: Analysis of the predicted prices versus actual auction prices and subsequent player performance in the IPL.
Insights and Implications

This study offers valuable insights into the economic valuation of IPL players, providing a tool for team owners and managers to assess player worth and make informed decisions during auctions. Our model aims to introduce a holistic approach to evaluating player contributions and market value.
