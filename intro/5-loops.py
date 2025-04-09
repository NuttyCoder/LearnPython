# For loop
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

print("\nReversed counting from 5 to 1:")
for i in range(5, 0, -1):
    print(i)

# While loop
count = 1
print("While loop")
while count <= 5:
    print(count)
    count += 1

# Reversed while loop
count = 5
print("\nReversed While loop")
while count >= 1:
    print(count)
    count -= 1


# Looping thru a list
fruits = ["apple", "banana", "cherry"]
print("My fruits:")
for fruit in fruits:
    print(fruit)

# Reversing a list
print("\nMy fruits in reverse:")
for fruit in reversed(fruits):
    print(fruit)


# Loop with enumerate
print("fruit with indicies:")
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")


# loop with Dictionaries
person = {"name": "John", "age": 30, "city": "NYC"}
print("\nPerson dict")
for key, value in person.items():
    print(f"{key}:{value}")

# List comprehension (compact loop for creating lists)
squares = [x**2 for x in range(1, 6)]
print("Squares from 1 to 5", squares)


# For loop wit zip() - iterate through multiple lists in parallel
colors = ["red", "yellow", "green"]

print("\nFruits and their colors:")
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")


# Break and continue
print("\n Loop with break")
for i in range(1, 10):
    if i > 5:
        break
    print(i)

print("\n Loop with continue")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i)


# Infinite loops with break condition
print("\nControlled infinite loop:")
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
