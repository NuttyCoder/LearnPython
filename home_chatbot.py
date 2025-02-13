from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create a new ChatBot instance
chatbot = ChatBot('HomeBot')

# Create a new trainer for the chatbot
corpus_trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the ChatterBot corpus data
corpus_trainer.train("chatterbot.corpus.english")

# Train the chatbot with custom data
custom_trainer = ListTrainer(chatbot)
custom_training_data = [
    "Hi",
    "Hello! How can I assist you today?",
    "What's your favorite color?",
    "I love all colors equally!"
]
custom_trainer.train(custom_training_data)

print("Chatbot is ready to chat!")

# Interactive chat loop
while True:
    try:
        user_input = input("You: ")
        bot_response = chatbot.get_response(user_input)
        print(f"HomeBot: {bot_response}")
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

