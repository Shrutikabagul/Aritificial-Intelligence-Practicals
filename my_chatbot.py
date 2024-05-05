from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
customer_service_bot = ChatBot('CustomerServiceBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(customer_service_bot)

# Train the chatbot with the English language corpus
trainer.train('chatterbot.corpus.english')

# Additional training data for specific topics
trainer.train([
    'chatterbot.corpus.english.greetings',
    'chatterbot.corpus.english.conversations',
    'chatterbot.corpus.english.shopping',
    'chatterbot.corpus.english.business'
])

# Start interacting with the user
print("Welcome to Customer Service Bot. How can I assist you today?")
while True:
    # Get user input
    user_input = input("You: ")

    # Exit if user types 'exit'
    if user_input.lower() == 'exit':
        print("Customer Service Bot: Thank you for contacting us. Have a great day!")
        break

    # Get the chatbot's response
    bot_response = customer_service_bot.get_response(user_input)

    # Print the response
    print("Customer Service Bot:", bot_response)
