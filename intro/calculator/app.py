def add(x, y):
    return x+y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Divison by zero is not allowed."
    return x / y


def main():
    print("\n==== 🧮 Simple Calculator 🧮 ====")
    print("Select operation:")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")

    while True:
        choice = input("\nEnter choice (1-4):")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid input. Please enter a num between 1 and 4")
        else:
            break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Error! Please enter valid numbers!")
        return

    if choice == "1":
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"\n{num1} - {num2} = {substract(num1, num2)}")
    elif choice == "3":
        print(f"\n{num1} x {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")

    again = input(
        "\nDo you want to perform another calculation? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
        return
    else:
        main()


main()
