
# ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# ChatBot
# database field: database_uri='sqlite:///database.sqlite3'
chatbot = ChatBot(
    'MacChat',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    read_only=True
)

# trainer
trainer = ListTrainer(chatbot)

# existing conversation
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer.train(conversation)

response = chatbot.get_response("Hello!")
print(response)

# gets user input, exists on ctrl + C
while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break