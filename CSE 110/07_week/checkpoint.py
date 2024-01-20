"""
Author: Collin Nunnally
File: checkpoint.py


"""
number = 0

number = int(input("Please give me a positive number: "))

while number <= 0:
    print("Sorry, that is a negative number. Try again.")
    number = int(input("Please give me a positive number: "))

print(f"The number is: {number}.")

candy = "no"

candy = input("May I have a piece of candy? ")

while candy == "no":
    candy = input("May I have a piece of candy? ")

print("Thank you.")