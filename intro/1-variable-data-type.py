# print("Hello world!")


# Strings
name = "Alex"
# Integer (Whole numbers)
age = 25
# Float (decimal number)
height = 9.5
# Boolean
is_student = True

# print("Hey my name is " + name)
# print("Hey my name is", name)

# print(name[-1])

# Python is a case-sensitive language, so "Hello" and "hello" are different words.

message = "hello world"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("l", "L"))
print("World" in message)
print(len(message))

greeting1 = "Hello"
greeting2 = "hello"

if greeting1 == greeting2:
    print("They are the same")
else:
    print("They are different")

# Type conversion
age_str = "30"
age_num = int(age_str)
print(type(age_num))
print(type(age_str))

price_float = 29.99
price_int = int(price_float)
