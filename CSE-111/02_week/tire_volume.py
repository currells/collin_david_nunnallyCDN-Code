"""
Name: Collin Nunnally
Class: CSE-111
Comments:
1. Gets the current date from the computer’s operating system.
2. Opens a text file named volumes.txt for appending.
3. Appends to the end of the volumes.txt file one line of text that contains the following five values:
    a. current date
    b. width of the tire
    c. aspect ratio of the tire
    d. diameter of the wheel
    e. volume of the tire

Ex Output:
> python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24.09 liters
"""
import math
from datetime import datetime 
current_date_and_time = datetime.now()


w_width = int(input("What is the width in millimeters? (ex. 205) "))
a_ratio = int(input("What is the aspect ratio of the tire? (ex. 60) "))
d_diameter = int(input("What is the diameter of the wheel? (ex. 15) "))

# def main():
#     p1 =  math.pi * (w_width ** 2) * a_ratio
#     p2 = w_width * a_ratio
#     p3 = 2540 * d_diameter
#     numerator = p1 * (p2 + p3)
#     volume = numerator / 10000000000
#     print(f"The approximate volume is {volume:.2f} liters.")
# main()

p1 =  math.pi * (w_width ** 2) * a_ratio
p2 = w_width * a_ratio
p3 = 2540 * d_diameter
numerator = p1 * (p2 + p3)
volume = numerator / 10000000000
print(f"The approximate volume is {volume:.2f} liters.")

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {w_width}, {a_ratio}, {d_diameter}, {volume}", file=volumes_file)
