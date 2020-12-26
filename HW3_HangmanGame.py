#Turkish Ai Hub Introduction to Python Programming course
#Homework 3
#Hangman Game
#Student Name: Mete Çeşmeci
import random

player_name = input("Enter your name: ")
print("Welcome", player_name)
print("Your aim is finding the word.")
print("The word's length is varied between 6 and 12 characters.")

word_library = [
    "homemade",
    "introduce",
    "classical",
    "python",
    "javascript",
    "cplusplus",
    "csharp",
    "objectpascal",
    "function",
]

word = random.choice(word_library)

print("\nGuess the characters.")
guessed = ""

turns_remaining = 11
print("You have", +turns_remaining, "turns.")

while turns_remaining > 0:

    fail_char = 0

    for character in word:
        if character in guessed:
            print(character, end="")
        else:
            print("_", end="")
            fail_char += 1

    if fail_char == 0:
        print("\n\nCongratulations!")
        print("\nThe word is: ", word)
        break

    guess = input("\n\nGuess the character: ")

    guessed += guess
            
    if guess not in word:
        print("\nThere is no", guess ,"character in the word.")
        
    turns_remaining -= 1

    if turns_remaining == 0:
        print("\n\nGame Over")
    else:
        print("\n", +turns_remaining, "turns are remaining")
