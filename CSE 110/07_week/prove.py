"""
Author: Collin Nunnally
File: prove.py
Creating a wordle program
"""
# Change color of incorrect and correct in code
gray = "\033[39m"
red = "\033[0;31m"
green = "\033[0;32m"

# Have a secret word stored in the program.
print("Welcome to the Great-Value Wordle Game! 💀\n")
secret_word = "bacon"
hint = " "
count_guess = 0
guess = " "



for _ in secret_word:
    hint += "_ "
# Prompt the user for a guess. Continue looping as long as that guess is not correct. 

while secret_word != guess:
    print(f"HINT: {hint}")
    guess = input("Guess the word: ").lower()
    count_guess += 1
    if len(secret_word) != len(guess):
        print("You must guess a word with the same number of letters as the secret word.")
        continue
    for i, s_letter in enumerate(secret_word):
        g_letter = guess[i]
        s_letter = secret_word[i]
        if g_letter in secret_word:
            if g_letter in s_letter:
                hint += g_letter.upper()
            else:
                hint += g_letter.lower()
        else:
            pass
    if secret_word != guess:
        print(f"{red}That is not correct.{gray} Keep trying!\n")
    elif secret_word == guess: # Calculate the number of guesses and display it at the end.
        print(f"{green}You guessed it!{gray}\nYou took {count_guess} tries!")
        break
# You do not need to have any hints at this point.

'''
STRETCH:
# Use a loop to generate the initial hint.
# Make sure to account for the following in your hints:
# Letters that are not present at all in the secret word (underscore _).
# Letters that are present in the secret word, but in a different spot (lowercase).
# Letters that are present in the secret word at that exact spot spot (uppercase).
'''