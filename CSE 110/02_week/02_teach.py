"""
Author: Collin Nunnally
File: 02_teach.py

Write a program to prompt the user for the following:

First name
Last name
Email Address
Phone Number
Job Title
ID Number

To this:
----------------------------------------
[LAST NAME], [first name]
[Job title]
ID: [id number]

[email address]
[phone number]
----------------------------------------
"""
# Questions asked
print("Please, Enter the following information for your ID:\n ")

first = input("Enter your first name. ")
last = input("Enter your last name. ")
email = input("Enter your email. ")
#Trying to format the phone number right by including an Example
print("\nExample: (555) 555-5555")
phone = input("Enter your phone number. ")
job = input("Enter your job title. ")
#Same example with the ID number
print("\nExample: xx-xxxxx")
id = input("Enter your ID number. ")

#Extra credit questions
hair = input("What is your hair color? ")
eyes = input("What is your eye color? ")
month = input("What is your birth month? \n")
print("Enter Yes or No.")
train = input("Have you received training? ")

#Output of the ID badge
print("\n Your ID card is: ")
print(f"{'-' * 50}")

# Last name is caped and first is capitalized 
print(f"{last.upper()}, {first.capitalize()}")
print(f"{job.title()}")
#ID label, including the new line
print(f"ID: {id}\n")

print(f"{email}")
print(f"{phone}\n")

#Formating the Xtra Credit with the spaces and labels in there
print(f"Hair: {hair.title():<16}Eyes: {eyes.title()}")
print(f"Month: {month.capitalize():<15}Training: {train.capitalize()}")
print(f"{'-' * 50}\n")