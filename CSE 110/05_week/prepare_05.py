"""
Author: Collin Nunnally
File: prepare_05.py

If the first number is greater than the second, 
print "The first number is greater". 
Otherwise, print "The first number is not greater".

If the two numbers are equal print 
"The numbers are equal". 
Otherwise, print "The numbers are not equal".

If the second number is greater than the first, 
print "The second number is greater". 
Otherwise, print "The second number is not greater".

Check to see if the user's favorite animal is the same as 
your favorite animal (meaning you, the programmer). 
If it is, print "That's my favorite animal too!" 
If it's not, print "That one is not my favorite." 
Verify that it works regardless of the capitalization.
"""

first = int(input("First number: "))
second = int(input("Second number: "))

# Determining if the first # is greater
if first > second:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

# Determining if the two numbers are equal
if first == second:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# Determining if the second # is greater
if first < second:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

# Asking favorite animal and then making the input lower case
animal = input("What is your favorite animal? ").lower()

# Testing if their favorite animal is a panda.
if animal == "panda":
    print("That's my favorite animal too!")
else:
    print("That is not my favorite animal.")