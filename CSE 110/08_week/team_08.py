"""
Author: Unathletic Avengers
File: team_08.py


"""
# Create a string variable to hold the word "Commitment".
keep_playing = "YES"
word = "commitment"


# Write code that loops through the word letter by letter. If the letter is "m", print it as a capital letter. If the letter is anything else, print it out as a lowercase letter.
# Change the print statements so that each letter is not printed on its own line, but rather they are printed out next to each other on the same line.
'''
for letter in word:
    if letter == "m":
        print("M", end="")
    else:
        print(f"{letter}", end="")
'''

# Also, change the program to allow the user to specify the letter (rather than always using "m"). Make sure your program matches the letter in the word, regardless of whether the user entered it as a capital or lowercase, and regardless of whether that letter was a capital or lowercase in the original word.
fav_letter = input("What is your favorite letter? ").lower()
'''
for i, letter in enumerate(word):
    if fav_letter == letter:
        print(f"{fav_letter.upper()}", end="")
    else:
        print(f"{letter}", end="")
'''
# Change the program, so that instead of capitalizing the user's favorite letter, it "hides" it, and replaces it with an underscore in the display.
for i, letter in enumerate(word):
    if fav_letter == letter:
        print("_", end="")
    else:
        print(f"{letter}", end="")



# STRETCH:
# Start a new program that will work similar to one from the core requirements, but use a different string, this time using the following quote from President Nelson: "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
sentence = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
play_again = "YES"

while play_again == "YES":
    num = int(input("What is your favorite number kiddo? "))
    for i, letter in enumerate(sentence):
        if i % num ==0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    play_again = input("\nWould you like to play again? (YES / NO): ").upper()

# Then, instead of your program asking for a favorite letter, have it asks for a number n. Make the program capitalize every n-th letter in the string.


# Add an additional feature to your program so that the user can enter another number and see it's result. To do this, you should ask the user if they would like to enter another number, and continue looping as long as they type yes.
