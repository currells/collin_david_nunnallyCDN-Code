"""
Name: Collin Nunnally
Class: CSE-111
Comments:
Running through a .txt file and displays the contents
"""

list_provinces = []

with open("provinces.txt", "r") as provinces_file:
    for line in provinces_file:
        if line == "AB":
            pass
        list_provinces.append(line.strip())

print(list_provinces)