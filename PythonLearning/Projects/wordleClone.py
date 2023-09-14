import random

# Opens the text file with the path
words = open("PythonLearning/Projects/valid-wordle-words.txt", "r").read().splitlines() 

# Instructions for the game wrapped in """ to show the metrics and grading
def game_instruction():
    print("""Wordle is a single player game
    A player has to guess a five letter hidden word
    You have six attempts
    Your Progress Guide "✔❌❌✔➕"
    "✔" Indicates that the letter at that position was guessed correctly
    "➕" indicates that the letter at that position is in the hidden word, but in a different position
    "❌" indicates that the letter at that position is wrong, and isn't in the hidden word   """)

# Function to check the user inputted word
def check_word():
    hidden_word = random.choice(words)
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("You guessed the words correctly! WIN 🕺🕺🕺 ")
            break
        else:
            attempt = attempt - 1
            print(f"you have {attempt} attempt(s) ,, \n")
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    print(word + " ✔ ")

                elif word in hidden_word:
                    print(word + " ➕ ")
                else:
                    print(" ❌ ")
            if attempt == 0:
                print(" Game over !!!! The word was: " + hidden_word)

game_instruction()
check_word()