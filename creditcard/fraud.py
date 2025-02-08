#Credit Card Fraud
#This dataset consists of credit card transactions in the western United States. It includes information about each transaction including customer details, the merchant and category of purchase, and whether or not the transaction was a fraud.

#Note: You can access the data via the File menu or in the Context Panel at the top right of the screen next to Report, under Files. The data dictionary and filenames can be found at the bottom of this workbook.

#Source: Kaggle
 #The data was partially cleaned and adapted by DataCamp.

#We've added some guiding questions for analyzing this exciting dataset! Feel free to make this workbook yours by adding and removing cells, or editing any of the existing cells.
#Explore this dataset
#Here are some ideas to get your started with your analysis...

#🗺️ Explore: What types of purchases are most likely to be instances of fraud? Consider both product category and the amount of the transaction.
#📊 Visualize: Use a geospatial plot to visualize the fraud rates across different states.
#🔎 Analyze: Are older customers significantly more likely to be victims of credit card fraud?
#🔍 Scenario: Accurately Predict Instances of Credit Card Fraud
#This scenario helps you develop an end-to-end project for your portfolio.

#Background: A new credit card company has just entered the market in the western United States. The company is promoting itself as one of the safest credit cards to use. They have hired you as their data scientist in charge of identifying instances of fraud. The executive who hired you has have provided you with data on credit card transactions, including whether or not each transaction was fraudulent.

#Objective: The executive wants to know how accurately you can predict fraud using this data. She has stressed that the model should err on the side of caution: it is not a big problem to flag transactions as fraudulent when they aren't just to be safe. In your report, you will need to describe how well your model functions and how it adheres to these criteria.

#You will need to prepare a report that is accessible to a broad audience. It will need to outline your motivation, analysis steps, findings, and conclusions.
SELECT * FROM 'credit_card_fraud.csv'
LIMIT 5

import pandas as pd 
ccf = pd.read_csv('credit_card_fraud.csv') 
ccf.head(100)

#Data Dictionary
#transdatetrans_time	Transaction DateTime
#merchant	    Merchant Name
#category	    Category of Merchant
#amt	        Amount of Transaction
#city	        City of Credit Card Holder
#state	      State of Credit Card Holder
#lat	        Latitude Location of Purchase
#long	        Longitude Location of Purchase
#city_pop	    Credit Card Holder's City Population
#job	        Job of Credit Card Holder
#dob	        Date of Birth of Credit Card Holder
#trans_num	  Transaction Number
#merch_lat	  Latitude Location of Merchant
#merch_long	  Longitude Location of Merchant
#is_fraud	    Whether Transaction is Fraud (1) or Not (0)

#   https://www.kaggle.com/datasets/kartik2112/fraud-detection/data
