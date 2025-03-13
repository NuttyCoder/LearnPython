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

