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
