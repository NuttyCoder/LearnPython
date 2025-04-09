import random
import math
import datetime
import os
import sys
import time

# Get a random number
random_number = random.randint(1, 10)  # 1 and 10 is included
print(f"Random number is {random_number}")

# choose a random element from a list
fruits = ["apple", "orange", "cherry", "banana"]
random_fruit = random.choice(fruits)
print(f"Random fruit is {random_fruit}")

# shuffle the list
random.shuffle(fruits)
print(f"Shuffled list: {fruits}")

# Math module
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.8: {math.floor(4.8)}")
print(f"5 raised to power 3: {math.pow(5, 3)}")


# Datetime module
current_time = datetime.datetime.now()
print(f"Current date and time: {current_time}")
print(f"Today's date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().year}")

# OS module
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")
print(f"List of files: {os.listdir('.')}")


# Time module
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done!")

# Sys module
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")  # e.g., 'win32', 'darwin', 'linux'
