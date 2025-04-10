print("🔤 VOWEL COUNTER 🔤")

# Simple syntax
# while True:
#     text = input("\nEnter some text (or 'quit'): ")

#     if text.lower() == "quit":
#         print("👋 Goodbye!")
#         break

#     vowel_count = 0

#     for letter in text.lower():
#         if letter in ["a", "e", "i", "o", "u"]:
#             vowel_count += 1

#     print(f"That text has {vowel_count} vowels!")


# Advanced syntax

while True:
    text = input("\nEnter some text (or 'quit'): ")

    if text.lower() == "quit":
        print("👋 Goodbye!")
        break

    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"That text has {vowels} vowels!")
