import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I'm just a chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.) (weather|temperature) (.)",
        ["I'm sorry, I don't have real-time information about the weather.",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", ]
    ],
    [
        r"what's your favorite color?",
        ["I don't have a favorite color. I'm just a computer program.", ]
    ],
    [
        r"who created you?",
        ["I was created by a developer Alvira", ]
    ],
    [
        r"how old are you?",
        ["I don't have an age. I'm just a chatbot.", ]
    ],
    [
        r"how can I contact support?",
        ["For support, please contact Alvira", ]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day.",]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Define a function to interact with the chatbot
def chatbot_response(user_input):
    return chatbot.respond(user_input)

# Main loop for interacting with the chatbot
print("Hello! I'm a simple chatbot. You can type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye! Have a great day.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
