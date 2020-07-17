import random

def hangman():
    word=random.choice(["kettle","table","chair","doraemon","pokemon","cricket","covid","lovely","great","kitchen","snake","joint","hyper","shinchan","ragnarok","alaska","penguin","typical"])
    

name=input("Enter your name\n")
print("Welcome", name)
print("-----------------------")
print("Please try to guess the word in less than 10 attempts!")
hangman()
