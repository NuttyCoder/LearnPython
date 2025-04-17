import time
import random

# Player Stats
player = {
    "name": "",
    "health": 100,
    "gold": 50,
    "items": []
}

# Game locations
locations = {
    "town": {
        "description": "A bustling town with shops and friendly people.",
        "options": ["shop", "forest", "rest"]
    },
    "forest": {
        "description": "A dark forest with strange sounds and hidden treasures.",
        "options": ["explore", "return to town", "camp"]
    },
    "shop": {
        "description": "A small shop with various items for sale.",
        "options": ["buy health potion (20 gold)", "buy sword (50 gold)", "return to town"]
    }
}

# Items with effects
items = {
    "health potion": {"health": 30, "price": 20},
    "sword": {"damage": 10, "price": 50}
}

# Enemies that can be encountered
enemies = [
    {"name": "Goblin", "health": 30, "damage": 5, "gold": 15},
    {"name": "Wolf", "health": 20, "damage": 7, "gold": 10},
    {"name": "Bandit", "health": 40, "damage": 8, "gold": 25}
]


def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)

    print()


def display_stats():
    print("\n" + "=" * 40)
    print(
        f"👤 Name: {player["name"]} | ❤️ Health: {player["health"]} | 💰 Gold: {player['gold']}")

    if player["items"]:
        print(f"🎒 Items: {", ".join(player["items"])}")

    print("=" * 40)


def town():
    slow_print("\n🏠 You are in town.")
    slow_print(locations["town"]["description"])

    while True:
        display_stats()
        print("\nWhat would you like to do?")
        print("1. 🛒 Go to the shop")
        print("2. 🌲 Enter the forest")
        print("3. 🛏️ Rest at the inn (restore health for 10 gold)")
        print("4. 👋 Quit game")

        choice = input("> ").lower()

        if choice == "1" or "shop" in choice:
            shop()
        elif choice == "2" or "forest" in choice:
            forest()
        elif choice == "3" or "rest" in choice:
            rest()
        elif choice == "4" or "quit" in choice:
            slow_print("\n👋 Thanks for playing! Goodbye.")
            exit()
        else:
            print("I don't understand that option. Please try again!")


def shop():
    slow_print("\n🛒 You enter the shop. The shopkeeper greets you.")
    slow_print(locations["shop"]["description"])

    while True:
        display_stats()
        print("\nWhat would you like to do?")
        print("1. 🧪 Buy health potion (20 gold)")
        print("2. ⚔️ Buy sword (50 gold)")
        print("3. 🚶 Return to town")

        choice = input("> ").lower()

        if choice == "1" or "health" in choice:
            buy_item("health potion")
        elif choice == "2" or "sword" in choice:
            buy_item("sword")
        elif choice == "3" or "return" in choice or "town" in choice:
            slow_print("\n🚶 You leave the shop and return to town.")
            return
        else:
            print("❓ I don't understand that. Try again.")


def buy_item(item_name):
    item = items[item_name]

    # if user already bouth the item don't let them to buy again. But they can buy the health poition even if they have it already
    if item_name in player["items"] and item_name != "health potion":
        slow_print(f"\nYou already have a {item_name}")
        return

    if player["gold"] >= item["price"]:
        player["gold"] -= item["price"]

        if item_name not in player["items"]:
            player["items"].append(item_name)

        if "health" in item:
            slow_print(
                f"\n You bought a health potion! You can use it to restore {item["health"]} health!")
        elif 'damage' in item:
            slow_print(
                f"\n✅ You bought a {item_name}! It will help you defeat enemies faster.")
    else:
        slow_print("\n❌ You don't have enough gold to buy that item!")


def forest():
    slow_print("\n🌲 You enter the dark forest...")
    slow_print(locations["forest"]["description"])

    while True:
        display_stats()
        print("\nWhat would you like to do?")
        print("1. 🔍 Explore deeper (chance to find treasure or enemies)")
        print("2. 🏠 Return to town")
        print("3. ⛺ Set up camp (restore 10 health)")

        choice = input("> ").lower()

        if choice == "1" or "explore" in choice:
            explore()
        elif choice == "2" or "return" in choice or "town" in choice:
            slow_print("\n🚶‍♂️ You leave the forest and return to town.")
            return
        elif choice == "3" or "camp" in choice:
            slow_print("\n⛺ You set up camp for a quick rest.")
            player["health"] = min(player["health"] + 10, 100)
            slow_print("😌 You feel a bit better. (+10 health)")
        else:
            print("I don't understand that option! Please try again.")


def explore():
    slow_print("\n🔍 You venture deeper into the forest...")
    time.sleep(1)

    # Random encounter: 60% chance on enemy, 30% chance on treasure and 10% on nothing
    encounter = random.choices(
        ["enemy", "treasure", "nothing"], [60, 30, 10])[0]

    if encounter == "enemy":
        enemy_encounter()
    elif encounter == "treasure":
        treasure_encounter()
    else:
        slow_print("🤷 You explore for a while but find nothing interesting.")


def enemy_encounter():
    enemy = random.choice(enemies)
    enemy_health = enemy["health"]

    slow_print(f"\n⚠️ You encounter a {enemy['name']}!")

    while enemy_health > 0 and player["health"] > 0:
        display_stats()
        print(f"\n👹 {enemy['name']} Health: {enemy_health}")
        print("\nWhat will you do?")
        print("1. ⚔️ Attack")
        print("2. 🧪 Use health potion")
        print("3. 🏃 Run away")

        choice = input("> ").lower()

        if choice == "1" or "attack" in choice:
            player_damage = 5
            if "sword" in player["items"]:
                player_damage += items["sword"]["damage"]

            enemy_health -= player_damage
            slow_print(
                f"💥 You attack the {enemy['name']} for {player_damage} damage!")

            if enemy_health <= 0:
                slow_print(f"🎉 You defeated the {enemy['name']}!")
                player['gold'] += enemy['gold']
                slow_print(f"💰 You found {enemy['gold']} gold!")
                return

            player['health'] -= enemy['damage']
            slow_print(
                f"😱 The {enemy['name']} attacks you for {enemy['damage']} damage!")

            if player['health'] <= 0:
                game_over()

        elif choice == "2" or "potion" in choice:
            if "health potion" in player["items"]:
                player['items'].remove("health potion")
                player['health'] = min(
                    player['health'] + items["health potion"]["health"], 100)
                slow_print(
                    f"🧪 You used a health potion and restored {items['health potion']['health']} health!")
            else:
                slow_print("❌ You don't have any health potions!")
                continue

            player['health'] -= enemy['damage']
            slow_print(
                f"😱 The {enemy['name']} attacks you for {enemy['damage']} damage!")

            if player['health'] <= 0:
                game_over()

        elif choice == "3" or "run" in choice:
            # 50% chance to escape
            if random.random() > 0.5:
                slow_print("🏃 You managed to escape!")
                return
            else:
                slow_print("😨 You couldn't escape!")
                player['health'] -= enemy['damage']
                slow_print(
                    f"😱 The {enemy['name']} attacks you for {enemy['damage']} damage!")

                if player['health'] <= 0:
                    game_over()

        else:
            print("❓ I don't understand that. Try again.")


def treasure_encounter():
    gold_found = random.randint(10, 30)
    player["gold"] += gold_found

    # random.random() 0.0 - 0.99
    if random.random() < 0.2 and "health potion" not in player["items"]:
        player["items"].append("health potion")
        slow_print("\n✨ You found a hidden treasure chest!")
        slow_print(f"🎁 Inside was {gold_found} gold and a health potion!")
    else:
        slow_print("\n💰 You found a small pouch with some gold inside!")
        slow_print(f"✨ You gained {gold_found} gold!")


def rest():
    if player['gold'] >= 10:
        player['gold'] -= 10
        player['health'] = 100
        slow_print("\n🛏️ You rest at the inn and fully recover your health.")
        slow_print("😊 It cost you 10 gold, but you feel completely refreshed!")
    else:
        slow_print("\n❌ You don't have enough gold to rest at the inn!")


def game_over():
    slow_print("\n💔 Your health has dropped to 0!")
    slow_print("☠️ GAME OVER!")
    print(f"\n📊 Final stats: {player['gold']} gold collected")

    play_again = input("\n🔄 Would you like to play again? (yes/no): ").lower()

    if play_again.startswith('y'):
        start_game()
    else:
        slow_print("\n👋 Thanks for playing! Goodbye.")
        exit()


def start_game():
    player["health"] = 100
    player["gold"] = 50
    player["items"] = []

    slow_print("\n" + "=" * 60)
    slow_print("🏆 FOREST ADVENTURE 🏆")
    slow_print("="*60)
    slow_print("🎮 Welcome to a simple text adventure game!")

    player["name"] = input("\nWhat is your name, adventurer? ")
    slow_print(
        f"\n🎉Welcome, {player['name']}! Your adveture begins in a small town.")

    town()


start_game()
