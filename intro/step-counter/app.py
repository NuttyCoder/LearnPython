print("🏃 STEP COUNTER 🏃")
daily_goal = int(input("🤷‍♂️ What is your daily step goal? "))
current_steps = int(input("✨ How many steps have you taken today? "))

remaining = daily_goal - current_steps
if remaining > 0:
    print(f"💪 You need {remaining} more steps to reach your goal!")
else:
    print(
        f"🎉 Congratulations! You've exceeded your goal by {-remaining} steps!")
