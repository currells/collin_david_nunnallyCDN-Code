"""
Name: Collin Nunnally
Class: CSE-111
Comments:
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = π * w**2 * a * (w * a + 2,540 * d) / 10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.

Output Ex:
> python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24.09 liters

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15

The approximate volume is 39.92 liters
"""
import math

w_width = int(input("What is the width in millimeters? (ex. 205) "))
a_ratio = int(input("What is the aspect ratio of the tire? (ex. 60) "))
d_diameter = int(input("What is the diameter of the wheel? (ex. 15) "))

def main():
    p1 =  math.pi * (w_width ** 2) * a_ratio
    p2 = w_width * a_ratio
    p3 = 2540 * d_diameter
    numerator = p1 * (p2 + p3)
    volume = numerator / 10000000000
    print(f"The approximate volume is {volume:.2f} liters.")
main()    