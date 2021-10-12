'''
Made by - Aditya mangal
Purpose - Python mini project
Date  - 18 october 2020
'''
from termcolor import cprint,colored
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)
available=print(colored('Available languages >> \nbengali, chinese, english, french, german, hebrew, hindi, indonesian, italian,japanese, korean, marathi,\n oriya, persian, portuguese, russian, spanish, swedish, telugu, thai, traditionalchinese, turkish',"yellow"))
language=input("\n\nIn which language do you want to start the conversation ? >> ").lower()
trainer.train(f'chatterbot.corpus.{language}')


if __name__ == "__main__":
    cprint("#" * 50, "magenta")
    cprint((f"A Chatot ").center(50), "yellow")
    cprint("#" * 50, "magenta")

    print('You can exit by type exit\n')
    name=input("Enter your name:")
    cprint((f"Start Chatting").center(20), "yellow")
    print()
    while True:
        query = input(colored(f"{name}>> ",'red'))
        if 'exit' in query.lower() or 'bye' in query.lower():
            print(colored("Bot>> Bye :) See you soon.....",'green'))
            exit()
        else:
            print(colored(f"Bot>> {chatbot.get_response(query)}",'green'))
