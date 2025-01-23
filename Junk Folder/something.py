"""
Hello
"""

STANDARD_INDEX = 0
BOOK_INDEX = 1
CHAPTER_INDEX = 2
VERSE_INDEX = 3

def Program:
    pass
    # Runs all of the functions

def Reference:
    total_reference = {}
    with open(lds-scripture.csv, "rt") as csv_file:
        next(csv_file)

        for row in csv_file:
            columns = row.strip().split(",")
            standard_work = columns[STANDARD_INDEX]
            book = columns[BOOK_INDEX]
            chapter = columns[CHAPTER_INDEX]
            verse = columns[VERSE_INDEX]
            total_reference
    # gets verse chapter and book from .csv

def Scripture:
    pass
     # Slowly deletes words as you continue to run the program

def Word:
    pass    
    # Converts words from the passage to a list of strings of individual words to be replaced with  "___"
