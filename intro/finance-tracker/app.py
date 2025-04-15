import os
import datetime


DATA_FILE = "my_finances.txt"


def add_transaction():
    print("\n💰 ADD TRANSACTION 💰")

    while True:
        transaction_type = input("➕ Income or ➖ Expense? (i/e): ").lower()
        if transaction_type in ["i", "e"]:
            break
        print("❌ Please enter 'i' or 'e' ")

    amount = input("💵 Enter amount: $")
    category = input("🏷️ Enter category: ")
    description = input("📝 Enter description: ")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    symbol = "+" if transaction_type == "i" else "-"

    # This opens the file in "append mode" ('a').The "append mode" means new data will be added to the end of the file without deleting existing content
    # The with statement is a clean way to handle files that automatically closes them when you're done

    with open(DATA_FILE, "a") as file:
        file.write(f"{today}|{symbol}{amount}|{category}|{description}\n")

    print("✅ Transaction added successfully!")


def view_transactions():
    if not os.path.exists(DATA_FILE):
        print("No transactions found.")
        return

    print("\n📋 TRANSACTIONS 📋")
    print("-" * 60)

    print("DATE          AMOUNT     CATEGORY        DESCRIPTION")
    print("-" * 60)

    with open(DATA_FILE, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            date = parts[0]
            amount = parts[1]
            category = parts[2]
            description = parts[3]
            emoji = "💰" if amount.startswith('+') else "💸"

            print(f"{date}    {emoji} {amount}    {category}    {description}")


def get_summary():
    if not os.path.exists(DATA_FILE):
        print("\n📭 No transactions found")
        return

    total_income = 0
    total_expense = 0

    with open(DATA_FILE, "r") as file:
        for line in file:
            parts = line.strip().split("|")
            amount = parts[1]

            if amount.startswith("+"):
                total_income += float(amount[1:])
            else:
                total_expense += float(amount[1:])

    balance = total_income - total_expense

    print("\n📊 FINANCIAL SUMMARY 📊")
    print(f"💰 Total Income:  ${total_income:.2f}")
    print(f"💸 Total Expense: ${total_expense:.2f}")
    print(f"💵 Balance:      ${balance:.2f}")


def main():
    while True:
        print("\n" + "=" * 30)
        print("💰 FINANCE TRACKER 💰")
        print("="*30)
        print("1. 📝 Add Transaction")
        print("2. 📋 View Transactions")
        print("3. 📊 Summary")
        print("4. 🚪 Exit")

        choice = input("\n🔤 Choice (1-4): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            get_summary()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please go with (1-4)")


main()
