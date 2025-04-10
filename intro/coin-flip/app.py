import random

print("🎮 COIN FLIP GAME 🎮")
print("Guess heads or tails ✨")


while True:
    guess = input("\nEnter your guess (heads/tails): ").lower()

    if guess != "heads" and guess != "tails":
        print("❌ Please enter 'heads' or 'tails' ❌")
        continue  # what continue does? it goes back to the start of the loop

    flip = random.choice(["heads", "tails"])

    print(f"\n🪙 Coin shows {flip}")

    if guess == flip:
        print("You won! You guessed correctly. 🎉")
    else:
        print("😢 Sorry, wrong guess. Try again! 🍀")

    again = input("\n🔄 Play again? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
        break
