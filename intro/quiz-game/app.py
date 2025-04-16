import random
import time


def display_welcome():
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO THE ULTIMATE QUIZ CHALLENGE! 🎮".center(50))
    print("=" * 50)
    print("\n📜 Instructions:")
    print("- Choose a quiz category")
    print("- Answer multiple-choice questions")
    print("- Each correct answer is worth 10 points")
    print("- See your final score at the end")
    print("- Have fun and learn something new!")


def display_categories():
    print("\n🗂️  Quiz Categories:")
    print("1. 🌎 General Knowledge")
    print("2. 🎬 Movies and TV Shows")
    print("3. 🔬 Science and Nature")
    print("4. 🎮 Video Games")
    print("5. 🎲 Random Mix (questions from all categories)")


def get_user_choice():
    while True:
        try:
            choice = int(input("\nSelect a category (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print(f"❌ Please enter a number between 1 and 5")
        except ValueError:
            print("❌ Please enter a valid number")


def load_questions():
    general_knowledge = [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Which of these is not a primary color?",
            "options": ["A. Red", "B. Blue", "C. Green", "D. Yellow"],
            "answer": "C"
        }
    ]

    movies_tv = [
        {
            "question": "Who played Iron Man in the Marvel Cinematic Universe?",
            "options": ["A. Chris Evans", "B. Robert Downey Jr.", "C. Chris Hemsworth", "D. Mark Ruffalo"],
            "answer": "B"
        },
        {
            "question": "Which TV show features a high school chemistry teacher who becomes a drug dealer?",
            "options": ["A. Breaking Bad", "B. The Walking Dead", "C. Game of Thrones", "D. Stranger Things"],
            "answer": "A"
        },
        {
            "question": "What was the first film in the Star Wars original trilogy?",
            "options": ["A. The Empire Strikes Back", "B. Return of the Jedi", "C. A New Hope", "D. The Phantom Menace"],
            "answer": "C"
        },
        {
            "question": "Which actress played Katniss Everdeen in The Hunger Games?",
            "options": ["A. Emma Watson", "B. Jennifer Lawrence", "C. Scarlett Johansson", "D. Emma Stone"],
            "answer": "B"
        },
        {
            "question": "Which animated movie features a snowman named Olaf?",
            "options": ["A. Toy Story", "B. Shrek", "C. Frozen", "D. Finding Nemo"],
            "answer": "C"
        }
    ]

    science_nature = [
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A. Go", "B. Au", "C. Ag", "D. Gd"],
            "answer": "B"
        },
        {
            "question": "Which animal can change its color to match its surroundings?",
            "options": ["A. Chameleon", "B. Elephant", "C. Giraffe", "D. Penguin"],
            "answer": "A"
        },
        {
            "question": "How many elements are in the periodic table?",
            "options": ["A. 92", "B. 100", "C. 118", "D. 120"],
            "answer": "C"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["A. Brain", "B. Liver", "C. Heart", "D. Skin"],
            "answer": "D"
        },
        {
            "question": "Which of these is not a type of cloud?",
            "options": ["A. Cumulus", "B. Stratus", "C. Cirrus", "D. Nucleus"],
            "answer": "D"
        }
    ]

    video_games = [
        {
            "question": "Which video game features a character named Mario?",
            "options": ["A. Call of Duty", "B. Super Mario Bros", "C. Minecraft", "D. Fortnite"],
            "answer": "B"
        },
        {
            "question": "What color is the ghost Inky in Pac-Man?",
            "options": ["A. Red", "B. Pink", "C. Blue", "D. Orange"],
            "answer": "C"
        },
        {
            "question": "Which game features a character named Master Chief?",
            "options": ["A. Halo", "B. God of War", "C. The Last of Us", "D. Uncharted"],
            "answer": "A"
        },
        {
            "question": "In Minecraft, what material is needed to create a torch?",
            "options": ["A. Wood and Iron", "B. Coal and Stick", "C. Stone and Flint", "D. Gold and Wood"],
            "answer": "B"
        },
        {
            "question": "Which of these is not a Pokémon type?",
            "options": ["A. Fire", "B. Water", "C. Earth", "D. Electric"],
            "answer": "C"
        }
    ]

    return {
        1: {"name": "Generalde Knowledge", "questions": general_knowledge},
        2: {"name": "Movies and TV Shows", "questions": movies_tv},
        3: {"name": "Science and Nature", "questions": science_nature},
        4: {"name": "Video Games", "questions": video_games},
        5: {"name": "Random Mix", "questions": general_knowledge + movies_tv+science_nature + video_games},
    }


def run_quiz(category_data):
    category_name = category_data["name"]
    questions = category_data["questions"]

    random.shuffle(questions)

    print(f"\n🎯 Starting the {category_name} quiz! 🎯")
    print("Answer each question by typing the letter of your choice (A,B,C, or D).")

    score = 0
    correct_answers = 0

    for i, q in enumerate(questions):
        print(f"\n-------- Question {i+1}/{len(questions)} ---------")
        print(f"? {q["question"]}")

        for option in q["options"]:
            print(option)

        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").upper()
            if user_answer not in ["A", "B", "C", "D"]:
                print("❌ Please enter A,B,C, or D.")
            else:
                break

        correct = user_answer == q["answer"]

        if correct:
            score += 10
            correct_answers += 1
            print("✅ Correct! +10 points")
        else:
            print(f"❌ Wrong! The correct answer is {q["answer"]}")

        if i < len(questions) - 1:
            print("\nNext question coming up...")
            time.sleep(1.5)

    print("\n" + "="*50)
    print("📊 QUIZ RESULTS 📊".center(50))
    print("="*50)
    print(f"Category: {category_name}")
    print(f"Correct Answers: {correct_answers}/{len(questions)}")
    print(f"Total Score: {score} points")

    percentage = (score / (len(questions)*10)) * 100

    if percentage == 100:
        print("\n🏆 PERFECT SCORE! You're a quiz master! 🏆")
    elif percentage >= 80:
        print("\n🌟 EXCELLENT! You really know your stuff!")
    elif percentage >= 60:
        print("\n😊 GOOD JOB! You've got decent knowledge!")
    elif percentage >= 40:
        print("\n🤔 NOT BAD! There's room for improvement.")
    else:
        print("\n📚 KEEP LEARNING! Practice makes perfect!")

    return score


def main():
    display_welcome()

    total_score = 0
    play_again = True

    while play_again:
        display_categories()

        category_choice = get_user_choice()  # 1

        all_categories = load_questions()
        score = run_quiz(all_categories[category_choice])

        total_score += score

        again = input("\nPlay another round? (yes/no): ").lower()  # hello

        while not (again.startswith("y") or again.startswith("n")):
            print("Please type yes or no.")
            again = input("Play another round? (yes/no): ").lower()

        play_again = again.startswith("y")

    print(
        f"\n🎉 Thanks for playing! Your total score from all rounds: {total_score} points 🎉")


main()
