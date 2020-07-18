import random

def hangman():
    word=random.choice(["kettle","table","chair","doraemon","pokemon","cricket","covid","lovely","great","kitchen","snake","joint","hyper","shinchan","ragnarok","alaska","penguin","typical"])
    validLetters='qwertyuiopasdfghjklzxcvbnm'
    attempts=10
    guessMade=''

    while len(word) > 0:
        main=""
        missed=0

        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print('You win!')
            break

        print("Guess the word", main)
        guess = input()
        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            attempts = attempts - 1
            if attempts == 9:
                print("9 turns left")
                print("  --------  ")
            if attempts == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if attempts == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if attempts == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if attempts == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if attempts == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if attempts == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if attempts == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if attempts == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if attempts == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

name=input("Enter your name\n")
print("Welcome", name)
print("-----------------------")
print("Please try to guess the word in less than 10 attempts!")
hangman()
