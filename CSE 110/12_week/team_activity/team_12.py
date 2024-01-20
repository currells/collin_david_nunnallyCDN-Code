"""
Author: Unathletic Avengers
Teacher: Brother Keers
File: team_12.py
Assignment:
Writing a program to grab select data sets

"""

SCRIPTURE_INDEX = 2
BOOK_INDEX = 0
CHAPTERS_INDEX = 1

# This is the requirements
'''
largest_chapter = 0
largest_scrip = ""
largest_book = ""
# 01: Open the file, read through it line by line, separate the line into the appropriate pieces and display each book in this format: Scripture: Old Testament, Book: Genesis, Chapters: 50
with open("books_and_chapters.txt", "r") as scrip_file:

    for line in scrip_file:
        column = line.strip().split(":")
        scripture_name = column[SCRIPTURE_INDEX]
        book_name = column[BOOK_INDEX]
        chapter_number = int(column[CHAPTERS_INDEX])
        if chapter_number > largest_chapter:
            largest_scrip = scripture_name
            largest_book = book_name
            largest_chapter = chapter_number
        print(f"Scripture: {scripture_name}, Book: {book_name}, Chapters: {chapter_number}")

# 02: Find the largest number of chapters in the scriptures.
# 03: Find the book that has the largest number of chapters in the scriptures.
print(f"\nLargest # of chapters is in the {largest_scrip}, book of {largest_book} with {largest_chapter} chapters.")
'''

learning_scrip = ""
largest_learning_chapter = 0
learning_book = ""

bom_name = ""
bom_chapter = 0

# S03: At the beginning of the program, ask the user which volume of scriptures they would like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price).
print("Scripture: Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price")
learning = input("What volume of scripture would you like to learn about? ")

with open("books_and_chapters.txt", "r") as scrip_file:

    for line in scrip_file:
      
        column = line.strip().split(":")
        scripture_name = column[SCRIPTURE_INDEX]
        book_name = column[BOOK_INDEX]
        chapter_number = int(column[CHAPTERS_INDEX])
      
        if scripture_name == learning:
            if chapter_number > largest_learning_chapter:
                learning_scrip = scripture_name
                learning_book = book_name
                largest_learning_chapter = chapter_number

# S01: Change your program so that it only prints the books in the Book of Mormon.
# S02: Find the book in the Book of Mormon that has the largest number of chapters.
        elif scripture_name == "Book of Mormon":
            if chapter_number > bom_chapter:
                bom_name = book_name
                bom_chapter = chapter_number
            print(f"Scripture: {scripture_name}, Book: {book_name}, Chapters: {chapter_number}")
        else:
            pass
    print(f"\nIn the Book of Mormon, the largest book is {bom_name} with {bom_chapter}")
#S03: Then, find the book in that volume of scripture that has the largest number of chapters.
    print(f"\nIn the scripture you chose, {learning_scrip}, the largest book is {learning_book} with {largest_learning_chapter} chapters.")