import requests


def main():
    print("\n✨ Simple Currency Converter ✨")

    print("🔄 Getting exchange rates...")

    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = response.json()["rates"]
        print("✅ Got rates successfully!")
    except:
        print("❌ Error: Couldn't connect to exchange rate API")
        return

    print("\n💼 Popular: USD EUR GBP JPY CAD AUD CNY INR")

    while True:
        print("\n💸 Enter details:")
        from_currency = input("From currency code (e.g. USD): ").upper()
        if from_currency not in rates:
            print(f"❌ Invalid code: {from_currency}")
            continue

        to_currency = input("To currency code (e.g. EUR): ").upper()
        if to_currency not in rates:
            print(f"❌ Invalid code: {from_currency}")
            continue

        try:
            amount = float(input(f"Amount in {from_currency}: "))
        except:
            print("❌ Please enter a valid number")
            continue

        amount_in_usd = amount / rates[from_currency]
        result = amount_in_usd * rates[to_currency]

        print(
            f"\n💰 Result: {amount} {from_currency} = {result:.2f} {to_currency}")
        print(
            f"Rate: 1 {from_currency} = {rates[to_currency]/rates[from_currency]:.4f} {to_currency}")

        if not input("\n Convert again? (y/n): ").lower().startswith("y"):
            print("👋 Thanks for playing!")
            break


main()
