# Our list of destinations
travel_destinations = ["Paris", "Sydney", "Tokyo", "New York", "London"]

# Todo: Insert "Berlin" at the third position using the insert() function
travel_destinations.insert(2,"Berlin")
# Checking the list
print(travel_destinations)

# Our travel destinations
travel_destinations = ["Paris", "Sydney", "Tokyo", "New York", "London"]

#Finding the third destination in the list
third_destination = travel_destinations[2]
print("The third destination on the list is: " + third_destination)


# TODO: Establish a list to store travel destinations
# Hint: Use square brackets to denote the list: list_name = [elements, ...]
travel_destinations = ["Oslo", "Copenhagen","Reykjavik","Helsinki","Stockholm"]
# TODO: Find the first destination on the list
# Hint: You can access the first element in a list using list_name[0]
first_destinations = travel_destinations[0]
last_destinations = travel_destinations [-1]
# TODO: Find the last destination on the list
# Hint: Python allows you to find the last item in a list using list_name[-1]
print("The first and last destinations in the list " + first_destinations,"" "and", ""+ last_destinations)

# Initial list of countries for the world tour.
world_tour_countries = ["Italy", "France", "USA", "Brazil", "India", "China"]

# Adds "Australia" to the end of the list.
world_tour_countries.append("Australia")

# Adds "Spain" to the end of the list, following "Australia".
world_tour_countries.append("Spain")

# Removes "Brazil" from the list.
world_tour_countries.remove("Brazil")

# Removes "China" from the list.
world_tour_countries.remove("China")

# Inserts "Japan" at the beginning of the list.
world_tour_countries.insert(0, "Japan")

# The current planned countries to visit in the world tour
world_tour_countries = ["Italy", "France", "USA", "Brazil", "India", "China"]

# Adding new countries to visit at the end of the tour
world_tour_countries.append("Australia")
world_tour_countries.append("Spain")


# print the updated tour plan.
print(world_tour_countries)

# Current plan for the world tour
world_tour_countries = ["Italy", "France", "USA", "Brazil", "India", "China"]

# TODO: Visit Japan before Italy
world_tour_countries.insert(0, "Japan")
# TODO: Visit Spain after all other countries
world_tour_countries.append("Spain")
print(world_tour_countries)

# Current plan for the world tour
world_tour_countries = ["Italy", "France", "USA", "Brazil", "India", "China", "Australia", "Spain"]

# Incorrectly attempting to insert "Japan" into the beginning of the list
world_tour_countries.insert(0, "Japan")

# Printing the updated list of countries
print(world_tour_countries)
# Current plan for the world tour
world_tour_countries = ["Italy", "France", "USA", "Brazil", "India", "China", "Australia", "Spain"]

# TODO: Remove Australia from the tour.
world_tour_countries.remove("Australia")
# print the updated tour plan.
print(world_tour_countries)

# TODO: Add "Australia" and "Spain" at the end of the list
world_tour_countries.append("Australia")
world_tour_countries.append("Spain")
# TODO: Remove "Brazil" and "China" from the list
world_tour_countries.remove("Brazil")
world_tour_countries.remove("China")
# TODO: Add "Japan" at the beginning of the list
world_tour_countries.insert(0,"Japan")
# Print the final world tour plan
print(world_tour_countries)

# Tuples, like lists, are a way to store multiple items in a single variable. However, unlike lists, 
# tuples are delineated with round brackets, and they are immutable, meaning they cannot be altered 
# once they're set. In this unit, we will explore how to create a tuple, access its elements, and 
# understand why its immutability is a key feature. **** Tuples are more memory-efficient than lists ****

# Create a tuple of cities
cities_visited = ("Paris", "Tokyo", "New York", "London", "Berlin")

# My Tuple of Cities I plan to visit
cities_to_visit = ("Barcelona", "Amsterdam", "Prague", "Berlin", "Zurich")

# Print the first city to visit
print("First city to visit: ", cities_to_visit[0])

# Print the last city to visit
print("Last city to visit: ", cities_to_visit[-1])

# TODO: Create a new tuple of cities
new_cities_visited = ("Bangkok", "Dubai", "Sydney", "Toronto", "Cape Town")

# TODO: Access elements in the tuple and print them
print("First city visited: ", new_cities_visited[0])
print("Last city visited: ", new_cities_visited[-1])

# My Tuple of Cities I have visited
cities_visited = ("Paris", "Tokyo", "New York", "London", "Berlin")

# Print the first city visited
print("First city visited: ", cities_visited[0])

# Print the last city visited
print("Last city visited: ", cities_visited[-1])

# Unsuccessful attempt to change tuple value (this will return an error as tuples are immutable)
# cities_visited[0] = "Rome"

#To create a dictionary with starting key:value pairs:

# Creating a simple dictionary to hold the country as key and its capital as value
capital_cities = {
    "France": "Paris",
    "Japan": "Kyoto",
    "Kenya": "Nairobi",
}

# Add more capital cities
capital_cities["Switzerland"] = "Bern"
capital_cities["Germany"] = "Berlin"
capital_cities["Japan"] = "Tokyo" # Update to new capital

del capital_cities["Germany"] # Removes "Germany" : "Berlin"
# Creating a simple dictionary to hold the country as key and its capital as value
capital_cities = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Kenya": "Nairobi",
}

# Accessing the capital of France
print("The capital of France is:", capital_cities["France"])

# Creating a dictionary to hold the country as key and its capital as value
capital_cities = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Kenya": "Nairobi",
}

# TODO: Add the USA with its capital to the dictionary
capital_cities["USA"] = "Washington D.C."
# TODO: Access and print the capital city of USA
print("The capital of the USA is:", capital_cities["USA"])

# Creating a dictionary to hold the country as key and its capital as value
capital_cities = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Kenya": "Nairobi",
}

# Adding a new country and its capital to the dictionary
capital_cities["India"] = "New Delhi"

# Displaying the dictionary
print("Updated list of countries and their capitals:", capital_cities["India"])

# Creating a dictionary to hold country as key and its capital as value
travel_dict = {
    "France": "Paris",
    "Japan": "Tokyo",
    "USA": "Washington D.C.",
    "Australia": "Canberra"
}

# TODO: Remove Japan and its capital from the dictionary
del travel_dict["Japan"]

# Displaying the dictionary
print("Updated Destination List:", travel_dict)

# A dictionary of countries we've visited and their capitals
visited_capitals = {
    "Spain": "Madrid",
    "Thailand": "Bangkok",
    "Egypt": "Cairo",
    "Australia": "Sydney",  # This is an incorrect entry
}

# TODO: Correct the capital of Australia in the dictionary
visited_capitals["Australia"] = "Canberra"

# Displaying the updated dictionary
print("Countries and their capitals:", visited_capitals)

# TODO: Write a program to create a dictionary of countries and their capital
visited_capitals = {
    'France': 'Paris',
    'Japan': 'Tokyo',
    'USA': 'Washington D.C'}
# TODO: Add and remove countries from the dictionary
visited_capitals['Australia'] = 'Canberra'

del visited_capitals['USA']

# TODO: Display the updated dictionary
print("Updated Travel Plans:", visited_capitals)

# Nested dictionary
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"}
}

airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"}
}

# Add Osaka's Kansai International Airport
airport_codes["KIX"] = {"city": "Osaka", "country": "Japan"}

# Add airport elevation data to KIX
airport_codes["KIX"]["elevation"] = 4

# Update elevation data
airport_codes["KIX"]["elevation"] = 5

# Delete elevation data
del airport_codes["KIX"]["elevation"]

# WHY ARE NESTED DICTIONARIES IMPORTANT
# Nested dictionaries are vital for managing intricate, 
# hierarchical data, crucial for applications like our travel 
# scenario. Understanding these advanced techniques enables 
# sophisticated data modeling and improves problem-solving skills
# in real-world, data-rich environments.
# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
}

# Output the contents of the dictionary
print(airport_codes)

# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
    "HND": {"city": "Tokyo", "country": "Japan"},
    "SYD": {"city": "Sydney", "country": "Australia"}
}

# TODO: Access and print the city and country that corresponds to a particular airport code.
print(airport_codes["LHR"]["city"], "-", airport_codes["LHR"]["country"])

# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
    "HND": {"city": "Tokyo", "country": "Japan"},
    "SYD": {"city": "Sydney", "country": "Australia"}
}

# TODO: Update 'country' of 'LHR' to 'England'
airport_codes['LHR']['country'] ='England'
print(airport_codes)

# A dictionary to handle airport codes
airport_codes = {
    "JFK": {"city": "New York", "country": "USA"},
    "LAX": {"city": "Los Angeles", "country": "USA"},
    "LHR": {"city": "London", "country": "UK"},
    "HND": {"city": "Tokyo", "country": "Japan"},
    "SYD": {"city": "Sydney", "country": "Australia"}
}

# Accessing a nested element with wrong keys - results in KeyError
print(airport_codes["LHR"]["city"], "-", airport_codes["LHR"]["country"])

# TODO: Construct a nested dictionary 
itinerary = {
    "Stop1": {"city": "New York", "country": "USA","airport_code":"JFK"},
    "Stop2": {"city": "Los Angeles", "country": "USA","airport_code":"LAX"},
    "Stop3": {"city": "London", "country": "UK","airport_code":"LHR"}
}
print(itinerary)

# Checking if the Passport is true
passport = True

if passport:
    print("You are eligible to travel.")
else:
    print("You cannot travel without a passport.")

if passport:
    print("You are eligible to travel.")  # This print statement belongs to the if condition
    # Any additional code dependent on the passport being True would also be indented here
else:
    print("You cannot travel without a passport.")  # This print statement belongs to the else condition
    # Code to execute when the passport condition is False would be indented at this level
# Any code here would not be part of the if-else block and executes regardless of the passport condition

# Declaring an initial balance of $4500
balance = 4500

# Checking if the Visa Application Balance is greater than or equal to 5000
if balance >= 5000:
    print("You are eligible to apply for a visa.")
else:
    print("You must maintain a balance of at least $5,000 to apply for visa.")

# Declaring a Boolean variable "passport" 
passport = True

# Checking if passport is true
if passport == True: 
    print("You are eligible to travel.")
else:
    print("You cannot travel without a passport.")
# ***********************************New Class [ Technical Indicators in Finacial Anaysis**********************************************************************    
# Technical Indicators in Financial Analysis course! In today's lesson, we'll explore how to calculate and visualize the 
# Simple Moving Average (SMA) for Tesla ($TSLA) stock prices using Pandas in Python. The goal is to help you understand 
# how to handle stock price data, compute a key technical indicator (SMA), and interpret the results visually. Here is the lesson plan:

# Introduction to Financial Data Handling.
# Loading and Preprocessing $TSLA Data.
# Calculating the 20-day Simple Moving Average (SMA).
# Visualizing SMA with Stock Prices.
# Summary and Next Steps.


# Introduction to Financial Data Handling
# Before diving into the code, it's essential to understand why financial data handling is crucial. 
#Financial data analysis allows traders and analysts to interpret market trends, predict future stock movements, and make informed decisions.

# We'll be using Pandas, a powerful Python library for data manipulation and analysis. 
# Pandas mainly operates with DataFrames and Series, making it excellent for time series data like stock prices.

# Time series data involves data points indexed in time order. In the context of stock prices, each data point corresponds to the stock price at a specific date and time.

# Loading and Preprocessing $TSLA Data
# First, let's load the $TSLA dataset. We'll use the datasets library to fetch this data. 
# After loading, we'll review the columns and convert the 'Date' column to datetime format, as it's crucial for time series processing.


import pandas as pd
import datasets
import datetime as dt

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])
# The output of the above code will be a DataFrame tesla_df containing historical price data for Tesla stock, 
# sourced from the codesignal/tsla-historic-prices dataset. This data includes columns for open, close, high, low stock prices, and volume for each trading day.

# Next, we need to ensure the 'Date' column is in datetime format and set it as the DataFrame index. This will help us handle the data more efficiently for time series analysis.
# Convert 'Date' to datetime format and set as index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Sort the dataset by date
tesla_df.sort_index(inplace=True)
# The preprocessing steps ensure that our data is in the correct format and order for further analysis.

#************************Calculating the 20-day Simple Moving Average (SMA)*****************************************************
# The Simple Moving Average (SMA) is a widely-used technical indicator in financial analysis. 
# It helps to smooth out price data by calculating the average stock price over a specific number of periods. 
# This technique allows traders to easily identify the trend direction and filter out noise from random short-term price fluctuations.

# The SMA is calculated by taking the arithmetic mean of the closing prices over a defined number of periods. 
# For example, a 20-day SMA is the average closing price over the last 20 trading days.

# We'll calculate the 20-day SMA for the closing price of the $TSLA stock. 
# Pandas makes this task straightforward by providing the rolling method, which we can use to compute the moving average.

# Visualizing SMA with Stock Prices
# Visualization helps us interpret the data more intuitively. We'll use Matplotlib, a popular Python library for plotting, 
# to visualize the $TSLA closing prices along with the calculated 20-day SMA.

# First, we'll subset the data to a smaller range (e.g., the year 2018) for better visualization.

import matplotlib.pyplot as plt

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']
# Next, we'll plot the 'Close' price and 'SMA_20' on the same chart.

# Plotting
tesla_df_small[['Close', 'SMA_20']].plot(figsize=(12, 6), title="TSLA Close Price and 20-day SMA (2018)")
plt.show()


# The output of the above code is a plot showing Tesla's closing prices and the 20-day SMA for the year 2018. 
# This visualization is key for analyzing the trend and volatility of Tesla's stock, demonstrating how the SMA 
# provides a smoothed average of the closing prices over the specified period.

import pandas as pd
import datasets
import matplotlib.pyplot as plt

# Load TSLA dataset
tesla_data = datasets.load_dataset('codesignal/tsla-historic-prices')
tesla_df = pd.DataFrame(tesla_data['train'])

# Convert 'Date' to datetime format and set as index
tesla_df['Date'] = pd.to_datetime(tesla_df['Date'])
tesla_df.set_index('Date', inplace=True)

# Sort the dataset by date
tesla_df.sort_index(inplace=True)

# Calculate the 20-day Simple Moving Average for the Close Price
tesla_df['SMA_10'] = tesla_df['Close'].rolling(window=10).mean()

# Using a smaller date range for better visualization
tesla_df_small = tesla_df.loc['2018']

# Plotting
tesla_df_small[['Close', 'SMA_10']].plot(figsize=(12, 6), title="TSLA Close Price and 10-day SMA (2018)")
plt.show()

# Print first few rows of the dataframe to check the SMA calculations
print(tesla_df_small.head())
