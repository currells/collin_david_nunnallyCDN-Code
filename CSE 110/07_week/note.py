"""
Author: Collin Nunnally
Notes on:
Loops
"""
# from array import array
# letters = array("i") # Look up python typecode and you need one of those where "i" is at

#           0    1    2    3    4
letters = [] #list
dict = {}
"""
print(letters[2]) gives Z

print(letters[0:3]) gives ['P', 'N', 'Z'] (Doesn't include 3rd value)
"""

# for i in range(len(letters)): # makes a hidden list of letters.
#     print(f"{i + 1}) {letters[i]}")

for i in enumerate(letters): 
    print(f"{i + 1}) {val}")

while len(letters) < 5:
    letter = input("Please give me a letter: ").upper()
    letters.append(letter)



import random

user_number = -1

while user_number < 1 or user_number > 100:
    user_number = int(input("Please give me a whole number between 1 and 100: "))

    if user_number < 1 or user_number > 100:
        print("Please enter a number between 1 and 100 only!")

computer_number = -1
guesses = 0

while computer_number != user_number:
    computer_number = random.randint(1, 100)
    guesses += 1
    print(f"The computer is guessing that your number is: {computer_number}")

print(f"It took the computer {guesses} tries to guess your number!")