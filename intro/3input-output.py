# name = input("What is your name? ")
# print("Hello", name)

# age = int(input("How old are you? "))
# years_to_100 = 100 - age
# print(f"You will be 100 in {years_to_100} years")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}")


# Working with multiple inputs on one line
# x, y = input("Enter two values seperated by space: ").split()
# print(f"first value: {x}, second value: {y}")


user_choice = input("Choose a color (or press Enter for default): ")
if user_choice == "":
    user_choice = "blue"

print(f"Selected color: {user_choice}")


# possiblities are endless
length = float(input("Enter length in meters: "))
print(f"That's {length * 100} centimeters")
