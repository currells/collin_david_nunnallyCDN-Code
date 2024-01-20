"""
Author: Collin Nunnally
File: prepare_03.py

Creating a program that:

Prompt the user for their age. Convert it to a number, 
add one to it, and tell them how old they will be on 
their next birthday.

Prompt the user for the number of egg cartons they have. 
Assume each carton holds 12 eggs, multiply their number by 12, 
and display the total number of eggs.

Prompt the user for a number of cookies and a number 
of people. Then, divide the number of cookies by the number 
of people to determine how many cookies each person gets.
"""

"""
Wanted to add colors to show the values of the function
Red shows the change, gray is revert color back
"""
gray = "\033[39m"
red = "\033[0;31m"
green = "\003[0;32m"

age = input("\nHow old are you? ")
age = int(age)

print(f"\nOn your next birthday, you will be {red}{age + 1}{gray}.c")

carton = input("\nHow many egg cartons do you have? ")
carton = int(carton)

print(f"\nYou have {red}{carton * 12}{gray} eggs.")

cookie = input("\nHow many cookies do you have? ")
people = input("\nHow many people do you have? ")
cookie = int(cookie)
people = int(people)

print(f"\nEach person can have {red}{cookie / people}{gray} cookies.")