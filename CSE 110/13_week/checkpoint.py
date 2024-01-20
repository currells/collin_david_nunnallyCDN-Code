"""
Author: Collin Nunnally
File: checkpoint.py
Description:
Make a program using functions that print: how it is, all caps, capitalization, and empty string
"""

def print_statement_regular(statement):
    print(statement)
def print_statement_upper(statement):
    print(statement.upper())
def print_statement_caps(statement):
    print(statement.capitalize())
def print_statement_lower(statement):
    print(statement.lower())
def print_blank(statement):
    print("\n")

statement = input("What is the statement / word? ")

print_statement_regular(statement)
print_statement_upper(statement)
print_statement_caps(statement)
print_statement_lower(statement)
print_blank(statement)