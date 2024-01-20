"""
Author: Collin Nunnally
File: prepare.py

How to go through a .txt file with open()
"""
NAME_INDEX = 0
HEX_INDEX  = 1
DESC_INDEX = 2

with open("colors.txt", "r") as color_file:
    for line in color_file:
        column     = line.split("|")
        color_name = column[NAME_INDEX].strip()
        color_hex  = column[HEX_INDEX].strip()
        color_def  = column[DESC_INDEX].strip()
        print(f"{color_name} ({color_hex})\n{color_def}\n")