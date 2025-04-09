# Functions are blocks of code that can be reused, they can take arguments and return values

# def greet_everyone():
#     print("Hello everyone!")


# greet_everyone()


# def greet(name):
#     print("Hello,", name)


# greet("John")
# greet("Jane")
# greet("Kyle")

# An example: without functions
# user1 = "Emma"
# print("Hello,", user1, "Welcome to our app")
# print("We hope you enjoy using our services.")
# print("Let us know if you need any help.")

# user2 = "John"
# print("Hello,", user2, "Welcome to our app")
# print("We hope you enjoy using our services.")
# print("Let us know if you need any help.")

# user3 = "Bob"
# print("Hello,", user3, "Welcome to our app")
# print("We hope you enjoy using our services.")
# print("Let us know if you need any help.")


# With functions
def greet_user(name):
    print("Hello,", name, "Welcome to our app")
    print("We hope you enjoy using our services.")
    print("Let us know if you need any help.")


greet_user("Emma")
greet_user("John")
greet_user("Bob")


def power(base, exponent):
    return base ** exponent


# x = power(2, 5)  # 32
# y = power(8, 2)  # 64
# z = power(3, 3)  # 27

print(power(2, 5))
print(power(8, 2))
print(power(3, 3))
