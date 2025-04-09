# Lists are collections of items that can store different types of data

numbers = [1, 2, 3, 4, 5]
print(numbers[0])
numbers[1] = 22
numbers.append(55)
numbers.remove(3)

print(numbers)
print(len(numbers))

# Slicing lists
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Elements from index 1 to 3
print(numbers[::2])  # Every other element
print(numbers[::-1])  # Reverse the list
print(numbers + [6, 7, 8])  # Concatenate lists
print(numbers * 2)  # Repeat the list


# Dictionaries are collections that store data as key-value pairs.
student = {
    "name": "Emma",
    "age": 22,
    "courses": ["Math", "Computer Science"]
}

print(student["name"])
student["grade"] = "A"
student["age"] += 10
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(f"{key}: {value}")


# Sets are unordered collections of unique items. - No duplicates allowed
unique_colors = {"red", "blue", "green", "green"}
print("unique colors:", unique_colors)

# Tuples are ordered collections that cannot be changed after creation.
coordinates = (10.5, 20.8)
