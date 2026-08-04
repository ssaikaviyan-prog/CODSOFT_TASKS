from datetime import datetime

# -----------------------------
# Functions
# -----------------------------

def welcome():
    print("=" * 50)
    print("            Welcome to sAI-GPT")
    print("=" * 50)

    now = datetime.now()

    print("Date :", now.strftime("%d-%m-%Y"))
    print("Time :", now.strftime("%H:%M:%S"))
    print()

def help_menu():
    print("\nAvailable Commands")
    print("---------------------------")
    print("hello")
    print("hi")
    print("who are you")
    print("your name")
    print("what is ai")
    print("python")
    print("thank you")
    print("about")
    print("help")
    print("bye")
    print()

def about():
    print("\nProject Details")
    print("---------------------------")
    print("Project Name : sAI-GPT")
    print("Version      : 1.0")
    print("Developer    : Sai Kaviyan")
    print("Language     : Python")
    print("Type         : Rule-Based Chatbot")
    print()

def chatbot():

    welcome()

    name = input("Enter your name: ")

    print(f"\nHello {name}! 👋")
    print("I'm sAI-GPT.")
    print("Type 'help' to see available commands.\n")

    while True:

        message = input("You : ").lower()

        if message == "hello":
            print("Bot : Hello! Nice to meet you.\n")

        elif message == "hi":
            print("Bot : Hi! How can I help you today?\n")

        elif message == "who are you":
            print("Bot : I am a rule-based chatbot created using Python.\n")

        elif message == "your name":
            print("Bot : My name is sAI-GPT.\n")

        elif message == "what is ai":
            print("Bot : Artificial Intelligence enables machines to perform tasks that normally require human intelligence.\n")

        elif message == "python":
            print("Bot : Python is one of the most popular programming languages for AI and Machine Learning.\n")

        elif message == "thank you":
            print("Bot : You're welcome! Happy Learning.\n")

        elif message == "help":
            help_menu()

        elif message == "about":
            about()

        elif message == "bye":
            print("\nBot : Thank you for using sAI-GPT.")
            print("Bot : Goodbye! Have a wonderful day! 👋")
            break

        else:
            print("Bot : Sorry, I don't understand that command.\n")

chatbot()