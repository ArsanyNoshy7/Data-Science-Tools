# Data-Science-Tools-Project
Bayut Real Estate Price Prediction Project

Project Overview

This project involves scraping real estate data from the Bayut website, cleaning and preprocessing the data, and building a predictive model to estimate house prices. The cleaned data is stored in an SQL Server database, and insightful analysis has been performed to better understand the housing market trends.

Features

Data Scraping: Extracted data from the Bayut website, including:

Property names

Locations

Features (e.g., number of bedrooms, bathrooms, area size)

Prices

Data Cleaning: Processed the raw data to handle missing values, remove duplicates, and standardize formats.

Predictive Modeling: Built a machine learning model to predict house prices based on features such as location, size, and number of rooms.

Database Integration: Stored the cleaned data in an SQL Server database for efficient querying and management.

Data Analysis: Performed exploratory data analysis to uncover trends and patterns in the housing market.

Tech Stack

Programming Language: Python

Libraries:

Web Scraping: BeautifulSoup, requests

Data Processing: pandas, numpy

Machine Learning: scikit-learn

Data Visualization: matplotlib, seaborn

Database: SQL Server

Other Tools: Jupyter Notebook, SQL Server Management Studio (SSMS)

Steps

1. Web Scraping

Scraped data from Bayut's website using BeautifulSoup and requests.

Extracted relevant information such as property descriptions, prices, and features.

2. Data Cleaning

Handled missing and inconsistent data entries.

Converted data into structured formats suitable for analysis and modeling.

3. Predictive Modeling

Split the data into training and testing sets.

Used regression algorithms to predict house prices.

Evaluated the model using metrics such as Mean Absolute Error (MAE) and R-squared.

4. SQL Server Integration

Designed a relational database schema to store the cleaned data.

Inserted data into the database for further analysis and querying.

5. Data Analysis

Visualized key trends such as average house prices by location and price distributions.

Provided insights into the factors affecting house prices.

Repository Structure

|-- data/
|   |-- raw_data.csv         # Raw scraped data
|   |-- cleaned_data.csv     # Cleaned data ready for modeling
|-- notebooks/
|   |-- scraping.ipynb       # Web scraping implementation
|   |-- cleaning.ipynb       # Data cleaning process
|   |-- modeling.ipynb       # Predictive modeling
|-- sql_scripts/
|   |-- schema.sql           # SQL script for database schema
|   |-- insert_data.sql      # SQL script to insert data into SQL Server
|-- analysis/
|   |-- visualizations.ipynb # Exploratory data analysis and insights
|-- README.md                # Project description

Installation and Usage

Prerequisites

Python 3.x installed on your system.

Required Python libraries: Install using:

pip install -r requirements.txt

SQL Server setup to store and manage the data.

Steps to Run

Scrape the data:

Run the scraping.ipynb notebook to collect data from Bayut's website.

Clean the data:

Execute the cleaning.ipynb notebook to preprocess the data.

Store the data:

Use schema.sql to create the database schema in SQL Server.

Run insert_data.sql to insert the cleaned data into the database.

Build and evaluate the model:

Use modeling.ipynb to train and evaluate the predictive model.

Analyze the data:

Execute visualizations.ipynb to generate charts and insights.

Results

Predictive Model: Achieved a high accuracy in predicting house prices.

Insights:

Identified the most influential factors affecting house prices.

Discovered price variations by location and property features.
