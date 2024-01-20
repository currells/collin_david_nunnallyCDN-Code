"""
Author: Collin Nunnally
File: prepare.py
Description: 
Being able to read a .txt file in python
"""
# Code will open the file, and display the books.txt file in the console, stripping the "\n" characters at the end of each line.
with open("books.txt", "r") as books_file:
    for line in books_file:
        print(line.strip())