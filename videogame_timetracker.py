import time
import json
from datetime import datetime

# Function to start the timer
def start_timer():
    print("Starting the timer...")
    return time.time()

# Function to stop the timer and calculate elapsed time
def stop_timer(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time played: {elapsed_time / 60:.2f} minutes")
    return elapsed_time

# Function to save game session data
def save_session(game_name, elapsed_time):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session_data = {
        "game_name": game_name,
        "date": date,
        "duration_minutes": elapsed_time / 60
    }

    try:
        with open("game_sessions.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(session_data)

    with open("game_sessions.json
