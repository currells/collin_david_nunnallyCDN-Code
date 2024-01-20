"""
File: demo.py
Author: Collin Nunnally

Purpose: Display text on the screen.
"""
# This is a single line comment

name = "Collin"

name = input("What is your name? ")
year = input("What year of school are you in? ")
age = input("How old are you? ")

print(f"Hello {name}! You're a {year}! You're an old {year} at {int(age) * 10}!")

