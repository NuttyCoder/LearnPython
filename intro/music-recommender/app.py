import random

print("🎶 MUSIC RECOMMENDER 🎶")

genres = {
    "rock": ["AC/DC", "Queen", "Led Zeppelin"],
    "pop": ["Taylor Swift", "Ed Sheeran", "Ariana Grande"],
    "hip-hop": ["Kendrick Lamar", "Drake", "J. Cole"],
}

choice = input("What genre do you like? (rock/pop/hip-hop): ")

if choice not in genres:
    print("😭 Sorry, I don't know that genre.")
else:
    print(f"Check out {random.choice(genres[choice])}")
