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


# Checking if the Driver's License is available
drivers_license = False

if drivers_license == True:
    print("Great! You're all set to explore the Greek islands by car.")
else:
    print("You need a valid driver's license to rent a car.")
# TODO: Declare a Boolean "passport" and check whether it is True. If so, print "You are eligible to travel." 
# Otherwise, print "You cannot travel without a passport."
passport = True

if passport == True:
    print("You are eligible to travel.")
    
else: 
    print("You cannot travel without a passport.")

age = 20  # Example age

if age < 18:
    print("You are eligible for the children's travel package.")
elif age < 60:
    print("You are eligible for the adult's travel package.")
else:
    print("You are eligible for the senior citizen's travel package.")

age = 15  # Example age

# Determine the travel package eligibility based on age
if age < 18 :
    print("You are eligible for the children's travel package.")
else:
    print("You are eligible for the adult's travel package.")

# TODO: Check age and assign a travel package accordingly
# Example age
age = 20

# TODO: Use an if statement to check if the age is less than 18
if age < 18:
    print("Childrens Travel Package")
# TODO: Use an elif statement to check if the age is less than 60
elif age < 60:
    print("Adults Travel Package")
# TODO: Use an else statement for individuals 60 and older
else:
    print("Senior Citizen Travel Package")

# Controlling travel according to age and budget
age = 23
budget = 1500

if age > 18:
    if budget > 1000:
        print("You are eligible for the international travel package.")
    else:
        print("You are eligible for the local travel package.")
else:
    print("You are eligible for the children's travel package.")
    
  # Controlling travel according to age and budget creating a budget between 500 and 1000 for a special deal without using {range}
age = 27
budget = 800

if age > 18:
    if budget >= 1000:
        print("You are eligible for the international travel package.")
    elif budget  >= 500:   # Add the correct condition here
        print("You are eligible for a special deal on the local travel package.")
    else:
        print("You are eligible for the local travel package.")
else:
    print("You are eligible for the children's travel package.")  

# Controlling travel according to age and budget
age = 23
budget = 900

if age > 18:
    if budget >= 1000:
        print("You are eligible for the international travel package.")
    elif budget >= 500:
        print(" You are eligible for a special travel package.")    
    else:
        print("You are eligible for the local travel package.")
else:
    print("You are eligible for the children's travel package.")

# Controlling travel according to age and budget
age = 23
budget = 1500

if age > 18:
    if budget > 1000:
        print("You are eligible for the international travel package.")
    elif budget < 1000:
        print("You are eligible for the local travel package.")
else:
    print("You are eligible for the children's travel package.")

# TODO: Declare variables 'age' and 'budget' with appropriate values
age = 18
budget = 1000
# TODO: Write an 'if' statement to determine if the traveler is over 18
if age >= 18:
    if budget  > 1000:
    # TODO: Inside the 'if' block, write another 'if' statement to check if the budget is more than 1000
        # TODO: Print "You are eligible for the international travel package." for budgets over 1000
        print("You are eligible for th international travel package.")
    # TODO: Else block for budgets 1000 or less
    else:
        print("You are eligible for the local travel package.")
        # TODO: Print "You are eligible for the local travel package."
else:
    print("You are eligible for the children's travel package.")
# TODO: Else block for travelers 18 or below
    # TODO: Print "You are eligible for the children's travel package."
travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": True},
    "Spain": {"capital": "Madrid", "visited": False},
}
destination = "France"

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(f"It seems you haven't visited {destination} yet. Get ready for an exciting adventure in {travel_destinations[destination]['capital']}!")
# Dictionaries within dictionaries .. use the dict[outer_key][nested_key] syntax to access the nested values
# Capital of France in our travel_destinations dictionary, we write travel_destinations["France"]["capital"]
# This first retrieves the dictionary associated with "France" and then fetches the value paired with "capital" within that dictionary.
# Let's imagine a traveler who has a dictionary of destinations with some essential travel info
travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": True},
    "Spain": {"capital": "Madrid", "visited": False},
}

# Test if the traveler is planning to visit a new destination this year
destination = "France"

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(f"It seems you haven't visited {destination} yet. Get ready for an exciting adventure in {travel_destinations[destination]['capital']}!")

# Let's imagine a traveler who has a dictionary of destinations with some essential travel info
# TODO: Change visited status for Italy to False
travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": False},
    "Spain": {"capital": "Madrid", "visited": False},
}

# Test if the traveler had to cancel their trip to Italy
destination = "Italy"

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(f"It seems you had to cancel your trip to {destination}. Hopefully, you can visit {travel_destinations[destination]['capital']} soon!")
# Let's imagine a traveler who has a dictionary of destinations with some essential travel info
travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": True},
    "Spain": {"capital": "Madrid", "visited": False},
}

# Check if the traveler is planning to visit Spain this year
destination = "Spain"

if travel_destinations[destination]["visited"]:
    print(f"You have already visited {destination}!")
else:
    print(f"It seems you haven't visited {destination} yet. Get ready for an exciting adventure in {travel_destinations[destination]['capital']}!")

travel_destinations = {
    "France": {"capital": "Paris", "visited": False},
    "Italy": {"capital": "Rome", "visited": True},
    "Spain": {"capital": "Madrid", "visited": False},
}

# TODO: Set 'destination' to "Italy".
destination = "Italy"

# TODO: Use an if statement to check if 'destination' has been visited.
if travel_destinations[destination]['visited']:
    print(f"You have already visited {destination}!")
else:
    print(f"It seems you had to cancel your trip to {destination}. Hopefully, you can visit {travel_destinations[destinations]['capital']}soon!")
# Print a message according to the visited status.

# This effectively combines if, and, not statements in Python, providing us with a clear, comprehensive check of travel requirements.
# The and operator allows us to check if two conditions are True at the same time.
# The not operator inversely evaluates the condition, turning True into False, and vice versa.
# And last but not least another common one, the or operator checks if at least one of two conditions is True.

travel_profile = {
    "passport": True, 
    "visa": {"required": True, "available": False}, 
    "tickets": True,
}
if travel_profile['passport'] and travel_profile['tickets']:
    if travel_profile['visa']['required'] and not travel_profile['visa']['available']:
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.")
else:
    print("General travel advice: Make sure you have your passport and tickets ready for hassle-free travel.")

# Travel profile has necessary details of the traveller, including insurance now
travel_profile = {
    "passport": True, 
    "visa": {"required": True, "available": True}, 
    "tickets": True,
    "insurance": False,
}

# Check if all required documents for travel are available
# TODO: Insurance check missing
if travel_profile['passport'] and travel_profile['tickets'] and travel_profile['insurance']:
    if travel_profile['visa']['required'] and not travel_profile['visa']['available']:
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.") 
else:
    print("General travel advice: Make sure you have your passport and tickets and insurance ready for hassle-free travel.")  # Mention of insurance is missing

# Travel profile has necessary details of the traveler
travel_profile = {
    "passport": True, 
    "tickets": True,
}

# Check if the basic requirement for travel are met (passport and tickets)
if travel_profile['passport'] and travel_profile['tickets']:
    print("You are ready for the initial phase of travel preparation.")
else:
    print("Please ensure you have both your passport and tickets.")

# Travel profile has necessary details of the traveller
travel_profile = {
    "passport": True, 
    "visa": {"required": True, "available": False}, 
    "tickets": True,
}

# Check if all required documents for travel are available
if travel_profile['passport'] and travel_profile['tickets']:
    if travel_profile['visa']['required'] and not travel_profile['visa']['available']:  # This line contains a bug
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.")
else:
    print("General travel advice: Make sure you have your passport, visa (if required), and tickets ready for hassle-free travel.")
    
# Travel profile has necessary details of the traveller
travel_profile = {
    "passport": True, 
    "visa": {"required": True, "available": True}, 
    "tickets": True,
}

# TODO: Implement nested if statements to check if all required documents for travel are available
# Use the pattern: if <condition>: ... else: ...
# Inside the first if block, add another if statement to check visa requirements
if travel_profile['passport'] and travel_profile['tickets']:
    if travel_profile['visa']['required'] and not travel_profile['visa']['available']:
        print("You need to apply for a visa.")
    else:
        print("You are ready to travel.") 
else:
    print("General travel advice: Make sure you have your passport and your ticket ready for a hassel-free travel experience.")   

# for loop allows us to execute a block of code a known number of times, or for each item in a sequence. 
# It's incredibly useful for handling repetitive tasks without manually programming each repetition.

trip_countries = ["France", "Italy", "Spain", "Japan"]

for country in trip_countries:
    print(f"Considering {country} for the trip.")
# In Python, break and continue are powerful loop controls. The break statement can stop the loop even if the loop condition hasn't been met. 
# On the other hand, the continue statement allows the loop to skip the remainder of the code and move to the next iteration.
packing_list = ["passport", "tickets", "camera", "clothes"]
packed_items = ["passport", "camera", "clothes"]

for item in packing_list:
    if item not in packed_items:
        print(f"Forgot to pack {item}")
        break
        

packing_list = ["passport", "tickets", "camera", "clothes", "snacks"]
packed_items = ["passport", "camera", "clothes"]

for item in packing_list:
    if item in packed_items:
        continue
    print(f"Need to pack {item}")

# A world of possibilities opens up when you understand and apply break and continue in your loops. These loop controls add flexibility 
# to your code, make your loops more efficient, and generally help avoid unnecessary iterations.

# Essential gadgets needed for the conference
essential_gadgets = ["laptop", "charger", "adapter", "USB drive"]
packed_items = ["laptop", "USB drive", "notebooks", "pens"]


for gadget in essential_gadgets:
    for packed in packed_items:
        if packed == gadget:
            break
    else:
        print(f"Missing {gadget} not found")
            # TODO: Found missing gadget, stop searching
    # TODO: Print missing gadget if there is one

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']
attending_days = ['Monday', 'Wednesday', 'Friday']
# TODO: The loop should skip these days instead of stopping
for day in weekdays:
    if day not in attending_days:
        continue
    print(f"Attending {day}")

# The difference ;in the above code is if you break your result will only be Monday, however if you continue you will get Monday, Wednesday and Friday


items = ["shoes", "shirt", "pants", "underwear", "phone", "passport"]
packed_items = ["passport", "pants", "phone"]

# TODO: Find a way around using the `in` operator
# Make sure NOT to use the `in` operator
for item in items:
    for packed_item in packed_items:
        if items == packed_items:# TODO: Iterate through all the packed items
            break
    # TODO: If you find `item` in the packed items stop the inner loop
   
    # TODO: If the inner loop hasn't been stopped, skip outer loop iteration
    else:
        print(f"Need to pack {item}")

# In this example we need to have a  Nested Loop, Which means you will use a loop inside  another loop.

for packed_item in packed_items:
# Then in the code we used the For-Else: The else block runs if the inner loop doesn't encounter a break. This is useful to determine if an item wasn't found in packed_items.
items = ["shoes", "shirt", "pants", "underwear", "phone", "passport"]
packed_items = ["passport", "pants", "phone"]

# TODO: Find a way around using the `in` operator
# Make sure NOT to use the `in` operator
for item in items:
    for packed_item in packed_items:
        if item == packed_item:# TODO: Iterate through all the packed items  ---> Notice Item vs items and packed_items changed to packed_item
            break
    # TODO: If you find `item` in the packed items stop the inner loop
   
    # TODO: If the inner loop hasn't been stopped, skip outer loop iteration
    else:
        print(f"Need to pack {item}")
#--------While Loops-------------------
# Think of while loops as a trusty friend who continues performing a task as long as a condition holds true. It keeps going until the condition fails or a break command halts it. 
# Let's illustrate how it functions with a code snippet related to planning a trip based on the budget for the countries you want to visit
# We have a budget for the trip and each country costs a certain amount
travel_budget = 5000
country_costs = {"France": 1000, "Italy": 800, "Spain": 900, "Japan": 1200}

total_cost = 0
chosen_countries = []

# Let's add countries to our trip until our budget runs out using a while loop
while total_cost < travel_budget and country_costs:
    country, cost = country_costs.popitem()
    if total_cost + cost <= travel_budget:
        total_cost += cost
        chosen_countries.append(country)

print("Countries chosen for the trip:", chosen_countries)
# We commence with a while loop that verifies two conditions — whether our total_cost is less than our travel_budget, 
# and whether there are still countries left in the country_costs dictionary. The loop keeps running, popping items 
# from the dictionary, and adding them to our trip until one of the conditions fails.

#In this specific case, our budget is enough to go to all countries so the loop stops when country_costs is empty and there 
# are no more countries to consider. If you were to adjust the travel_budget to a lower number the loop should stop sooner 
# when the first condition is no longer met (i.e. total_cost < travel_budget).

# The .popitem() method is used with dictionaries in Python. It removes and returns the last key-value pair added to the dictionary. 
# This is particularly useful when you want to process or remove items one by one from a dictionary.
# Understanding Python's Built-In Functions
# As we dive into Python's built-in functions, it's like discovering a set of powerful tools that make coding simpler. 
# Python comes packed with these ready-to-use functions, saving you the time and effort of writing common functionalities 
# from scratch. For beginners, focusing on a few key functions can be incredibly helpful.

# In the example of planning a trip with a while loop, we specifically use two functions: popitem() and append(). 
# You might also come across functions like len(), which tells you how many items are in a list or dictionary, and print(), which shows your results on the screen.

# popitem(): This function is specific to dictionaries. It removes the last added item and returns it, which is helpful for our loop as it 
# allows us to take countries off our planning list one by one.

# append(): Used with lists, this lets you add new items to the end. For us, it means we can keep adding countries to our travel list until we hit our budget limit.

# Both popitem() and append() are simple yet powerful, allowing us to dynamically update our lists and dictionaries.
# Importance of "while" Loops
# Understanding while loops solidifies the ability to automate repetitive tasks and control the iterations fluidly. 
# This understanding opens new avenues for coding efficiency and simplicity. Once mastered, this tool provides incredible flexibility and helps navigate complex tasks with ease.
 # EXAMPLE
# In this task, we're using while loops to pick out attractions for a local tour without going over our budget. 
# This is a cool way to see while loops in action and learn how to change a list as we go with something called popitem().

# Take a look at this line in the code:

attraction, cost = attraction_costs.popitem()

# popitem() takes the last item (like "Historical Site": 30) out of our list of places to visit and their costs. When it does, it gives back this item in a pair called a tuple, which is just a way of grouping things together in Python.
# The magic part is where we say attraction, cost = . 
# This means we take that pair (tuple) and split it, so attraction becomes the name ("Historical Site") 
# and cost becomes how much it costs (30).
# We have a budget for a local tour and each attraction costs a certain amount
local_tour_budget = 150
attraction_costs = {"Museum": 50, "Art Gallery": 40, "Historical Site": 30}

total_spent = 0
selected_attractions = []

# Let's select attractions for our local tour without exceeding our budget
while total_spent < local_tour_budget and attraction_costs:
    attraction, cost = attraction_costs.popitem()
    if total_spent + cost <= local_tour_budget:
        total_spent += cost
        selected_attractions.append(attraction)

print("Attractions selected for the local tour:", selected_attractions)

# while loops can elegantly manage travel budgets and itinerary selections. 
# Let's shift our focus slightly and apply this concept to choosing accommodations for your weekend getaway. 
# By keeping within a set budget, you'll dynamically pick hotels, mirroring the decision-making process for 
# selecting countries within a travel budget. This approach will further solidify your understanding of while 
# loops in budget management and decision-making based on financial constraints.

# Have you been wondering what that += does as we go through this unit? The += operator is a shorthand for 
# adding a value to a variable and then assigning the result back to that variable. So, total_cost += cost is 
# the same as writing total_cost = total_cost + cost. It adds the value of cost to total_cost and updates total_cost 
# with this new value, making our code cleaner and more concise.
# We have a set budget for accommodations over the weekend

# Original Code ------->
accommodation_budget = 300
hotel_costs = {"Hotel A": 90, "Hotel B": 120, "Hotel C": 85}

total_cost = 0
chosen_hotels = []

# TODO: Let's pick hotels for our weekend stay without exceeding our budget
while total_cost < accommodation_budget and hotel_costs:
    hotel, cost = hotel_costs.popitem()
    if total_cost + cost <= accommodation_budget:
        total_cost += cost
        chosen_hotels.append(________)  # Add the hotel to the list of chosen hotels

print("Hotels chosen for the weekend stay:", chosen_hotels)
# Corrected Code --------->

# We have a set budget for accommodations over the weekend
accommodation_budget = 300
hotel_costs = {"Hotel A": 90, "Hotel B": 120, "Hotel C": 85}

total_cost = 0
chosen_hotels = []

# TODO: Let's pick hotels for our weekend stay without exceeding our budget
while total_cost < accommodation_budget and hotel_costs:
    hotel, cost = hotel_costs.popitem()
    if total_cost + cost <= accommodation_budget:
        total_cost += cost
        chosen_hotels.append(hotel)  # Add the hotel to the list of chosen hotels

print("Hotels chosen for the weekend stay:", chosen_hotels)

# The Answer was append(hotel) ----->
# Building on  understanding of while loops for smart budgeting during travel, let's fine-tune the planning process. 
# In this exercise, adapt your code by integrating an additional travel destination along with its cost into the pre-existing dictionary. 
# Specifically, add "Greece" with a cost of 950. This task not only tests the ability to update data structures but also demonstrates 
# the loop's flexibility in accommodating an expanded list of options, further stretching your travel budget's capabilities.

# Orginal Code ------->
# We have a budget for the trip and each country costs a certain amount
travel_budget = 5000
# TODO: Add "Greece" to the country_costs dictionary with a cost and observe how it changes the final output.
country_costs = {"France": 1000, "Italy": 800, "Spain": 900, "Japan": 1200} 

total_cost = 0
chosen_countries = []

# Let's add countries to our trip until our budget runs out using a while loop
while total_cost < travel_budget and country_costs:
    country, cost = country_costs.popitem()
    if total_cost + cost <= travel_budget:
        total_cost += cost
        chosen_countries.append(country)

print("Countries chosen for the trip:", chosen_countries)

# Correct Code ------>
# We have a budget for the trip and each country costs a certain amount
travel_budget = 5000
# TODO: Add "Greece" to the country_costs dictionary with a cost and observe how it changes the final output.
country_costs = {"France": 1000, "Italy": 800, "Spain": 900, "Japan": 1200, "Greece": 950} 

total_cost = 0
chosen_countries = []

# Let's add countries to our trip until our budget runs out using a while loop
while total_cost < travel_budget and country_costs:
    country, cost = country_costs.popitem()
    if total_cost + cost <= travel_budget:
        total_cost += cost
        chosen_countries.append(country)

print("Countries chosen for the trip:", chosen_countries)

# Challenge code ----->

# TODO: Define the budget for the cultural tour
# TODO: Define the cost associated with each city visit

# TODO: Initialize the total amount spent and the list of chosen cities

# TODO: Use a while loop to selectively add cities to the tour list based on the budget
# Inside the loop:
    # TODO: Retrieve a city and its associated cost
    # TODO: Check if adding this city would exceed your budget
        # TODO: If not, update the total spent and add the city to your list

# TODO: Print the list of cities chosen for the cultural tour

travel_budget = 4500
country_costs = {"Germany": 900, "Ireland": 850,"Scotland": 1000, "Greenland": 500}

total_cost = 0
chosen_countries =[]

while total_cost < travel_budget and country_costs:
    country, cost = country_costs.popitem()
    if total_cost + cost <= travel_budget:
        total_cost += cost
        chosen_countries.append(country)
        
print("Countries chosen for the trip:", chosen_countries)


# Nested loops enable us to tackle more complex situations and augment the power of our code.

# Nested loops signify the placement of one loop inside another. These loops prove particularly useful when we need to address scenarios 
# involving more than one sequence, or when the number of iterations depends on the data itself. The set-up could involve a for loop inside 
# another for loop, a for loop inside a while loop, or a combination of for and while loops.

# Consider the following example. Suppose you're planning a trip and desire to list the key sights in the countries you intend to visit.

# We might want to do some sightseeing in each country. For each country, we have a list of sights.
country_sights = {"France": ["Eiffel Tower", "Louvre Museum"],
                  "Italy": ["Colosseum", "Piazza San Marco"],
                  "Spain": ["Park Güell", "The Alhambra"],
                  "Japan": ["Mt. Fuji", "Fushimi Inari Taisha"]}

for country, sights in country_sights.items():
    print(f"***In {country}, I want to see:")
    for sight in sights:
        print(sight)

# In this code snippet, we have a for loop that iterates over all countries, and within that loop, there is another for loop that cycles 
# through all the sights for the current country. There you have it: a nested loop! Here is what you'd get if you run the code above:

***In France, I want to see:
Eiffel Tower
Louvre Museum
***In Italy, I want to see:
Colosseum
Piazza San Marco
***In Spain, I want to see:
Park Güell
The Alhambra
***In Japan, I want to see:
Mt. Fuji
Fushimi Inari Taisha

# Nested loops serve as robust tools in Python. They enable you to manage scenarios with multiple sequences or corresponding data sets and heighten 
# the depth of your code, revealing new potential solutions for complex problems. By using nested loops, you can include an additional layer of complexity 
# in your work while simultaneously making your code more compact and efficient.
# Orgininal Code ------>
# Planning a cultural tour with events for each destination.
destination_events = {
    "France": ["Cannes Film Festival", "Bastille Day Fireworks"],
    "Italy": ["Venice Carnival", "Florence Wine Festival"],
    "Spain": ["La Tomatina", "Running of the Bulls"],
    "Japan": ["Sapporo Snow Festival", "Cherry Blossom Viewing"]
}

for destination, events in destination_events.items():
    print(f"Events to attend in {destination}:")
    for event in events:
        print(f"- {event}")

# Answer to the solution
# We might want to do some sightseeing in each country. For each country, we have a list of sights.
country_sights = {"France": ["Eiffel Tower", "Louvre Museum"],
                  "Italy": ["Colosseum", "Piazza San Marco"],
                  "Spain": ["Park Güell", "The Alhambra"],
                  "Japan": ["Mt. Fuji", "Fushimi Inari Taisha"]}

# There's a bug in the loop structure that prevents the sights from being printed correctly. Fix it.
for country, sights in country_sights.items(): # in this line correct  , sights after country to make the code work~!
    print(f"***In {country}, I want to see:")
    for sight in sights:
        print(sight)


# Corrrect Code ------>

# Organizing a photo exhibition of iconic landmarks from around the world.
exhibition_landmarks = {
    "France": ["Louvre Museum", "Mont Saint Michel"],
    "Italy": ["Leaning Tower of Pisa", "Venice Canals"],
    "Spain": ["Sagrada Familia", "Royal Palace of Madrid"],
    "Japan": ["Tokyo Tower", "Kiyomizu-dera"]
}

# TODO: Complete the loop to iterate through the countries and their landmarks
for country, landmarks in exhibition_landmarks.items():
    print(f"Landmarks in {country} to feature:")
    for landmark in landmarks:
        print(landmark)

# Problem to solve ------>
# Organizing a travel guide for museums around the world.
world_museums = {
    "France": ["Louvre Museum", "Orsay Museum"],
    "Italy": ["Uffizi Gallery", "Vatican Museums"],
    "Spain": ["Prado Museum", "Reina Sofia Museum"],
    "Japan": ["Tokyo National Museum", "Kyoto National Museum"]
}

# TODO: Write a nested loop to print each country and its must-see museums in the format:
# In [country], you should visit:
# - [museum 1]
# - [museum 2]
# (Continue for each museum in the country)

# Answer to the problem ------>
# Organizing a travel guide for museums around the world.
world_museums = {
    "France": ["Louvre Museum", "Orsay Museum"],
    "Italy": ["Uffizi Gallery", "Vatican Museums"],
    "Spain": ["Prado Museum", "Reina Sofia Museum"],
    "Japan": ["Tokyo National Museum", "Kyoto National Museum"]
}

# TODO: Write a nested loop to print each country and its must-see museums in the format:
# In [country], you should visit:
# - [museum 1]
# - [museum 2]
# (Continue for each museum in the country)

for country, museums in world_museums.items():
    print(f"In {country}, you should visit:")
    for museum in museums:
        print("-",museum)

# Continuing your impressive journey through Python loops, let's put your learning into action with a practical run-through. 
# Here, we have an example that epitomizes the application of for loops in calculating both total and average costs based on 
# a list and a dictionary — a fundamental skill for data processing tasks.

# This exercise involves iterating over a selection of countries to calculate the total travel cost and then determining the 
# average cost per country. It's a perfect showcase of how loops can automate and simplify operations on collections of data, 
# making tasks like budget planning or financial analysis much more straightforward.

# In this code, the len function is used to calculate the number of countries in the chosen_countries list. It returns the 
# total count of countries, which we then use to divide the total_trip_cost by, in order to find the average cost per country. 
# This function is essential for determining the size of various data types, such as lists, in Python.
# Let's calculate the total and average travel cost for a selection of countries.

chosen_countries = ["France", "Italy", "Spain"]  # This list may be a result of former selection logic

# Predefined costs for each country based on previous examples
country_costs = {"France": 1000, "Italy": 800, "Spain": 900, "Japan": 1200}

total_trip_cost = 0
for country in chosen_countries:
    total_trip_cost += country_costs[country]  # Summing up the cost for each chosen country

average_cost_per_country = total_trip_cost / len(chosen_countries)  # Calculating the average cost

# Display the total cost and the average cost per country
print(f"The total cost of the trip is: ${total_trip_cost}")
print(f"The average cost per country is: ${average_cost_per_country:.2f}") # In this line of code The .2f in the print statement is a format specifier used 
# to display a floating-point number with two decimal places. It ensures that the average cost is shown with exactly two digits after the decimal point, 
# making it look like a typical currency format.
# For example, if the average cost is 850.0, it will be displayed as 850.00.

# Output to the code ------>
The total cost of the trip is: $2700
The average cost per country is: $900.00

# Coding Challenge ------->

# TODO: Define a list named chosen_countries with countries selected for the road trip
chosen_countries = ["UK","Norway","Ireland","Sweden"]
# TODO: Define a dictionary named country_fuel_costs with fuel costs for countries
country_fuel_cost = {"UK":1.46, "Norway": 1.93, "Ireland":1.80, "Sweden": 1.53 }
# TODO: Initialize a variable total_fuel_cost to 0
total_fuel_cost = 0
# TODO: Use a for loop to add up the fuel cost for each chosen country
for country in chosen_countries:
    total_fuel_cost += country_fuel_cost[country]
# TODO: Calculate the average fuel cost per country
average_fuel_cost_per_country = total_fuel_cost / len(chosen_countries)
# TODO: Print the total fuel cost for the road trip
print(f"The total cost of fuel for this road trip is: ${total_fuel_cost}")
# TODO: Print the average fuel cost per country
print(f"The average fuel cost per country is: ${average_fuel_cost_per_country}")

# What is a Function and Its Syntax?
# A function is a block of code that performs a specific task independently. We use functions to organize and repurpose code. 
# You can think of a function as a small machine within your sprawling factory of code. Depending on its design, a function receives some input 
# (or none) and returns an output after executing the necessary operations.

# In Python, one defines a function using the def keyword, followed by the function's name and parentheses (). The code block contained in each 
# function is indented and initiates with a colon :. Take a look at the syntax below:
def greet_user():
    print("Hello, traveler!")

# Output ------>
greet_user()  # Outputs: Hello, traveler!


# Define a function to greet the user by name
def greet_user_by_name(name):
    print(f"Hello, {name}!")

# Call the function
greet_user_by_name("Alex")

def my_function(param1, param2):
    #the rest of your function defenition

# Define a function to greet the user by name
def greet_user_by_name(name, city):
    print(f"Hello, {name}! How's the weather in {city}?")

# TODO: Modify the function so it also accepts a second parameter, city, and includes that in the greeting.
# Example of the expected output: "Hello, Alex! How's the weather in Paris?"

# Call the function. You'll need to modify this call too to pass the extra parameter.
greet_user_by_name("Alex", "Paris")


# Coding Challenge--------->

# TODO: Write a function named greet_with_welcome that takes two parameters: name and hometown.
# The function should print a greeting to the user that includes their name and hometown.
def greet_with_welcome(name,hometown):
    print(f'Hello, {name}! What is the population of {hometown}?')    
greet_with_welcome("Jim", "Green Bay")

# Understanding Return Values

# Define a function to calculate the trip cost.
def calculate_trip_cost(countries, country_costs):
    total_cost = 0
    for country in countries:
        total_cost += country_costs[country]
    return total_cost


# Presuming the chosen_countries and their costs
chosen_countries = ['France', 'Italy', 'Spain']
country_costs = {'France': 1200, 'Italy': 950, 'Spain': 800}

# Call the function
trip_cost = calculate_trip_cost(chosen_countries, country_costs)
print(f"The total cost of the trip is: ${trip_cost}")


# Define a function to calculate the trip cost.
def calculate_trip_cost(countries, country_costs):
    total_cost = 0
    for country in countries:
        total_cost += country_costs[country]
    return total_cost

# Presuming the chosen_countries and their costs
chosen_countries = ['France', 'Italy', 'Spain']
country_costs = {'France': 1200, 'Italy': 950, 'Spain': 800}

# Call the function
trip_cost = calculate_trip_cost(chosen_countries, country_costs)
print(f"The total cost of the trip is: ${trip_cost}")


# Coding Challenge ------>

# TODO: Define a function called calculate_souvenir_budget
def calculate_souvenir_budget(countries, souvenir_costs):
# TODO: The function should take two parameters: countries (a list of countries) and souvenir_costs (a dictionary with countries as keys and costs as values)
    total_cost = 0
# TODO: Inside the function, create a variable to hold the total budget and set it to 0
# TODO: Use a for loop to iterate through the list of countries
    for country in countries:
        total_cost += souvenir_costs[country]
    return total_cost    
# TODO: For each country, add the corresponding souvenir cost to the total budget
# TODO: The function should return the total budget

# Assuming the countries you'll visit and the average souvenir costs
countries = ['France', 'Italy', 'Spain']
souvenir_costs = {'France': 150, 'Italy': 100, 'Spain': 75}

# Call the function
total_souvenir_budget = calculate_souvenir_budget(countries, souvenir_costs)
print(f"The total souvenir budget for the trip is: ${total_souvenir_budget}")


# Define a function which tries to modify a global variable
chosen_countries = ["France", "Italy"]

def add_country(country):
    chosen_countries.append(country)  # This modifies the global variable

add_country("Spain")  # Invoke the function
print(chosen_countries)  # ["France", "Italy", "Spain"]

def book_flight():
    destination = "Paris"  # Local variable defined within the function

book_flight()
print(destination)  # Attempt to access the local variable outside its function

# The Importance of Variable Scope
# Understanding variable scope is fundamental for avoiding errors and writing cleaner, 
# more efficient code. If you manage the scope of your variables wisely, you'll have granular control over where and how your data is manipulated.

# Understanding the difference between local and global variables helps prevent unintended side effects in your programs. For instance, 
# imagine that within a large codebase a variable has been unintentionally altered. Sounds bothersome, right? That's just one of the many
# complications that good understanding of variable scope can help you avoid.

# Define a function which tries to modify a global variable
chosen_countries = ["France", "Italy"]

def add_country(country):
    chosen_countries.append(country)  # This modifies the global variable

add_country("Spain")
print(chosen_countries)  # ["France", "Italy", "Spain"]



# Define a function which tries to modify a global variable
chosen_countries = ["France", "Italy"]

def add_country(country):
    # TODO: Modify the list of chosen_countries to include the new country
    chosen_countries.append(country)
    print("Country added successfully!")  # Feedback confirmation

add_country("Spain")
print(chosen_countries)  # This should print ["France", "Italy", "Spain"] after your modification


# TODO: Declare a global list to keep track of visited landmarks
visited_landmarks = ["Eiffel Tower", "Stonehedge"]
# TODO: Define a function named log_landmark that takes two parameters: landmark and city
def log_landmark(landmark, city):
    # TODO: Add the landmark and its city to the global list in the format "landmark in city"
    entry = f"{landmark} in {city}"
    visited_landmarks.append(entry)
# TODO: Call the log_landmark function with examples e.g., "Eiffel Tower" and "Paris"
log_landmark("Eiffel Tower", "Paris")
log_landmark("Stonehedge", "England")
# TODO: Print the list of visited landmarks
print(visited_landmarks)


# Combining Functions to Solve Complex Problems
travel_budget = 5000
country_costs = {'France': 1200, 'Italy': 1500, 'Spain': 800, 'Germany': 900, 'Greece': 1100}
def choose_countries(budget, costs):
    total_cost = 0
    chosen_countries = []
    for country, cost in costs.items():
        if total_cost + cost > budget:
            break
        total_cost += cost
        chosen_countries.append(country)
    return chosen_countries

chosen_countries = choose_countries(travel_budget, country_costs)
print(chosen_countries) # Prints ['France', 'Italy', 'Spain', 'Germany']

def calculate_cost(countries, costs):
    total_cost = 0
    for country in countries:
        total_cost += costs[country]
    return total_cost

total_cost = calculate_cost(chosen_countries, country_costs)
print(total_cost) # Prints 4400

# TIP
# Focusing on combining functions is vital because, in professional programming scenarios—from web app development to 
# data analysis—you'll often face complex issues that a single function cannot solve. Splitting these challenges into 
# smaller, function-representative tasks not only clarifies your code but also makes it easier to test, debug, and enhance.

# Define multiple functions and use them together to solve a problem.
def choose_countries(budget, costs):
    total_cost = 0
    chosen_countries = []
    for country, cost in costs.items():
        if total_cost + cost > budget:
            break
        total_cost += cost
        chosen_countries.append(country)
    return chosen_countries

def calculate_cost(countries, costs):
    total_cost = 0
    for country in countries:
        total_cost += costs[country]
    return total_cost

# Assuming sample data for budget and costs for demonstration
travel_budget = 5000
country_costs = {'France': 1200, 'Italy': 1500, 'Spain': 800, 'Germany': 900, 'Greece': 1100}

chosen_countries = choose_countries(travel_budget, country_costs)
trip_cost = calculate_cost(chosen_countries, country_costs)

print(f"The countries included in the trip are: {chosen_countries}")
print(f"The total cost of the trip is: ${trip_cost}")


# Partial function to add another country to your trip plan if it fits the budget.
def add_country_if_fits_budget(budget, current_cost, new_country_cost):
    # TODO: Add the missing code to check if you can add the new country without exceeding the budget
    if current_cost + new_country_cost <= budget:
        return True
    else:
        return False

# Assuming sample values for demonstration
current_budget = 5000
current_cost = 3000
new_country_cost = 1200

# Check if adding the new country fits the budget
can_add_country = add_country_if_fits_budget(current_budget, current_cost, new_country_cost)
print(f"Can add new country within budget? {can_add_country}")

# Adjusted function to consider both budget and cost preference.
def choose_countries(budget, cost_threshold, costs):
    total_cost = 0
    chosen_countries = []
    for country, cost in costs.items():
        # TODO: Modify the condition below to also reject countries whose cost exceeds the cost_threshold
        if cost > cost_threshold or total_cost + cost > budget:
            continue
        total_cost += cost
        chosen_countries.append(country)
    return chosen_countries

def calculate_cost(countries, costs):
    total_cost = 0
    for country in countries:
        total_cost += costs[country]
    return total_cost

# Assuming sample data for budget, cost threshold, and costs for demonstration
travel_budget = 5000
cost_threshold = 1000  # New cost preference limit
country_costs = {'France': 1200, 'Italy': 1500, 'Spain': 800, 'Germany': 900, 'Greece': 1100}

chosen_countries = choose_countries(travel_budget, cost_threshold, country_costs)
trip_cost = calculate_cost(chosen_countries, country_costs)

print(f"The countries selected within budget and cost preference are: {chosen_countries}")
print(f"The total cost of the trip is: ${trip_cost}")


