"""
Author: Collin Nunnally
File: prepare.py
Description: 
Finding things in a list (youngest person)
"""
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

NAMES_INDEX = 0
AGE_INDEX = 1

#01. Iterate through the list and display each string to the screen.
'''
for individuals in people:
    print(individuals)
'''
#02. Split the string into a name and age and print them to the screen.
'''
for row in people:
    columns = row.strip().split(" ")
    name = columns[NAMES_INDEX]
    age = int(columns[AGE_INDEX])
    print(f"{name:.<10}{age}")
'''

#03. Find the age that is the youngest.
#04. Keep track of the name of the person that is the youngest.

youngest_age = 999
youngest_name= ""

for row in people:
    columns = row.strip().split(" ")
    name = columns[NAMES_INDEX]
    age = int(columns[AGE_INDEX])
    if age < youngest_age:
        youngest_age = age
        youngest_name = name
print(f"The youngest person is {name}, who is {age} years old.")
