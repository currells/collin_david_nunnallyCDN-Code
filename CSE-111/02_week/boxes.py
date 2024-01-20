"""
Name: Collin Nunnally
Class: CSE-111
Comments:
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.

Ex Output:
> python boxes.py
Enter the number of items: 8
Enter the number of items per box: 5

For 8 items, packing 5 items in each box, you will need 2 boxes.

> python boxes.py
Enter the number of items: 25
Enter the number of items per box: 4

For 25 items, packing 4 items in each box, you will need 7 boxes.
"""
import math
items = int(input("Enter the number of items: "))
per_box = int(input("Enter the number of items per box: "))

def main():
    box_num = math.ceil(items / per_box)
    
    print(f"For {items} items, packing {per_box} items in each box, you will need {box_num} boxes.")
main()